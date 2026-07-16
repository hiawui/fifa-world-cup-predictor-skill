#!/usr/bin/env python3
"""Validate saved World Cup prediction markdown files."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


LIFECYCLE_FIELDS = {
    "预测生成时间": None,
    "信息截止时间": None,
    "预测状态": {"赛前初版", "确认首发终版"},
    "首发状态": {"未公布", "可靠预计", "已确认"},
    "是否需要临场复核": {"是", "否"},
}

REQUIRED_HEADINGS = (
    "## 评分",
    "## 证据账本",
    "## 首发强度/轮换不确定性",
    "## 关键假设",
    "## 预测失效路径",
    "## 来源",
)

KNOCKOUT_MARKERS = (
    "淘汰赛",
    "三十二强",
    "十六强",
    "八强",
    "四分之一决赛",
    "半决赛",
    "季军赛",
    "决赛",
    "Round of 32",
    "Round of 16",
    "Quarterfinal",
    "Semifinal",
    "Third-place",
    "Final",
)


@dataclass
class Report:
    path: Path
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate prediction lifecycle metadata and structural consistency."
    )
    parser.add_argument("paths", nargs="+", type=Path, help="Markdown files or directories")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat missing lifecycle/version/game-state fields as errors for new forecasts.",
    )
    return parser.parse_args()


def markdown_files(paths: list[Path]) -> list[Path]:
    files: set[Path] = set()
    for path in paths:
        if path.is_dir():
            files.update(path.rglob("*.md"))
        elif path.is_file():
            files.add(path)
        else:
            raise FileNotFoundError(path)
    return sorted(files)


def field_value(text: str, label: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(label)}\s*[：:]\s*(.+?)\s*$", text)
    if not match:
        return None
    return match.group(1).strip().strip("[]").replace("**", "").strip()


def add_compat_issue(report: Report, strict: bool, message: str) -> None:
    target = report.errors if strict else report.warnings
    target.append(message)


def probability_midpoints(text: str) -> list[float] | None:
    cleaned = text.replace("**", "")
    for line in cleaned.splitlines():
        if "90" not in line or "概率" not in line:
            continue
        matches = re.findall(
            r"(\d+(?:\.\d+)?)%\s*(?:[-~至]\s*(\d+(?:\.\d+)?)%)?", line
        )
        if len(matches) < 3:
            continue
        midpoints = []
        for low_raw, high_raw in matches[:3]:
            low = float(low_raw)
            high = float(high_raw) if high_raw else low
            if low > high or low < 0 or high > 100:
                return []
            midpoints.append((low + high) / 2)
        return midpoints
    return None


def validate(path: Path, strict: bool) -> Report:
    report = Report(path)
    text = path.read_text(encoding="utf-8")

    if not text.startswith("# "):
        report.errors.append("missing top-level match title")

    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            add_compat_issue(report, strict, f"missing required heading: {heading}")

    values: dict[str, str] = {}
    for label, allowed in LIFECYCLE_FIELDS.items():
        value = field_value(text, label)
        if value is None:
            add_compat_issue(report, strict, f"missing lifecycle field: {label}")
            continue
        values[label] = value
        if allowed is not None and value not in allowed:
            report.errors.append(
                f"invalid {label}: {value!r}; expected one of {sorted(allowed)}"
            )

    if "## 预测版本记录" not in text:
        add_compat_issue(report, strict, "missing heading: ## 预测版本记录")

    if values.get("预测状态") == "确认首发终版":
        if values.get("首发状态") != "已确认":
            report.errors.append("确认首发终版 requires 首发状态: 已确认")
        if values.get("是否需要临场复核") != "否":
            report.errors.append("确认首发终版 requires 是否需要临场复核: 否")

    is_knockout = any(marker.lower() in text.lower() for marker in KNOCKOUT_MARKERS)
    if is_knockout and "## 比赛状态转换" not in text:
        add_compat_issue(report, strict, "knockout forecast missing: ## 比赛状态转换")

    midpoints = probability_midpoints(text)
    if midpoints == []:
        report.errors.append("invalid 90-minute probability range")
    elif midpoints is None:
        add_compat_issue(
            report, strict, "could not find three 90-minute outcome probabilities"
        )
    else:
        total = sum(midpoints)
        if not 90 <= total <= 110:
            report.errors.append(f"probability midpoint sum is {total:.2f}%, expected near 100%")
        elif not 97 <= total <= 103:
            report.warnings.append(f"probability midpoint sum is {total:.2f}%")

    return report


def main() -> int:
    args = parse_args()
    try:
        files = markdown_files(args.paths)
    except FileNotFoundError as exc:
        print(f"ERROR: path not found: {exc.args[0]}", file=sys.stderr)
        return 2

    if not files:
        print("ERROR: no markdown files found", file=sys.stderr)
        return 2

    reports = [validate(path, args.strict) for path in files]
    for report in reports:
        status = "FAIL" if report.errors else "OK"
        print(f"{status} {report.path}")
        for message in report.errors:
            print(f"  ERROR: {message}")
        for message in report.warnings:
            print(f"  WARN: {message}")

    error_count = sum(len(report.errors) for report in reports)
    warning_count = sum(len(report.warnings) for report in reports)
    print(
        f"Checked {len(reports)} file(s): {error_count} error(s), "
        f"{warning_count} warning(s)."
    )
    return 1 if error_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
