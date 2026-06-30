---
name: world-cup-match-predictor
description: Evidence-based workflow for predicting, saving, or backtesting 2026 FIFA World Cup final-tournament match outcomes only, including upcoming fixtures, same-day or tomorrow matches, saved predictions in pred/, group-stage or knockout scenarios, and user requests asking who will win, likely score, draw risk, upset chance, match judgment, or prediction review. Use for 2026 FIFA World Cup final-tournament football/soccer predictions and post-match calibration with current team news, rankings, odds, schedule, injuries, lineups, form, tactics, results, and explicit uncertainty. Do not use for qualifiers, friendlies, club matches, other FIFA events, or generic football predictions.
---

# World Cup Match Predictor

## Overview

Use this skill to produce disciplined 2026 FIFA World Cup final-tournament match predictions and reviews. Treat predictions as probabilistic judgments, not certainties, and ground every major claim in current, cited evidence.

## Skill Maintenance

When optimizing this skill, review both `SKILL.md` and `references/prediction-framework.md` in the same pass. Keep probability bands, scoring rubrics, evidence workflow, persistence requirements, and consistency checks aligned across both files before syncing the installed copy.

## Core Workflow

1. Confirm the fixture.
   - Resolve dates against the user's timezone, then standardize kickoff times and saved filenames to Beijing time (UTC+08:00).
   - Verify competition, venue, kickoff, group/round, standings context, and match state.
   - Use this skill only for the 2026 FIFA World Cup final tournament.
   - For saved predictions in `pred/`, parse the file first; for backtests, verify the final result before scoring.

2. Gather current evidence.
   - Browse before predicting. Do not rely on memory for squads, injuries, standings, lineups, odds, results, or form.
   - Prefer official FIFA pages, federations, match centers, injury/team reports, odds aggregators, and established sports outlets.
   - Use at least two source types when available, usually official/schedule data plus performance, availability, or market data.
   - Within roughly 90 minutes of kickoff, look for confirmed lineups or reliable lineup reports before making a strong pick.
   - For completed matches, use final-score sources plus at least one match report or live text before judging prediction quality.
   - If evidence is unavailable or conflicting, state the limitation and avoid a strong pick.

3. Build an evidence-first case.
   - Establish incentives before team strength, especially qualification status, draw incentives, goal difference, rotation, and whether either side is eliminated. Do not equate eliminated with unmotivated; check pride, young players, coach pressure, and showcase incentives.
   - Compare squad quality, current-tournament form, tactics, coaching/game management, availability, rest/travel/weather, and market movement.
   - Break squad quality into starting XI, first-impact substitutes, bench depth by position, and the main creator, scorer, holding midfielder, center-back, and goalkeeper.
   - Compare coaching through shape, pressing height, buildup, substitution timing, and whether the coach reliably improves games in tournament settings.
   - For tactics, check pressing resistance, set pieces, transition defense, aerial duels, pace, goalkeeper reliability, and whether either side must chase the game.
   - Look specifically for defensive error tendency and control after taking the lead; favorites often fail by conceding during low-control phases.
   - Keep head-to-head secondary unless the current matchup pattern is unusually stable and well supported.
   - Treat current-tournament evidence as stronger than pre-tournament reputation once the tournament has started.
   - Promote material counterarguments into the probability estimate; do not leave rotation, low motivation, draw incentives, or lineup uncertainty only as prose.
   - Build an evidence ledger before assigning probabilities:
     - Factors raising Team A's 90-minute win probability
     - Factors raising the draw probability
     - Factors raising Team B's 90-minute win probability
     - Factors that affect only advancement, not the 90-minute result
   - Translate that ledger into directional probability adjustments. If a rationale point does not move win/draw/loss materially, label it as context rather than a driver.
   - Always include lineup strength / rotation uncertainty: expected starting XI strength relative to best XI, known injuries/suspensions, likely cohesion or firepower impact, and an approximate directional effect on win probability. Put this under `## 首发强度/轮换不确定性`.

4. Estimate outcomes.
   - Working order: evidence ledger -> directional adjustments -> scoring sanity check -> probability ranges -> likely scorelines -> final wording.
   - Give a 90-minute win/draw/loss pick unless the user asks specifically for advancement.
   - Use informative probability ranges, usually 8-12 points wide. If a range exceeds 15 points, explain why; never use a range wider than 20 points.
   - Include one or two likely scorelines and keep them consistent with the probability table.
   - Include category scores unless evidence is too sparse. Default rubric: squad quality 30, recent/tournament performance 20, tactical matchup 25, coaching/game management 15, context/motivation/environment 10.

5. Apply calibration rules.
   - Match prose intensity to probability band: 70%+ favorite requires a weak draw path; 65%-70% supports "clear favorite"; 58%-65% is moderate favorite, not domination; 50%-58% is slight edge/toss-up.
   - If rationale implies a band more than about 5 percentage points away from the table, revise the probabilities or the language.
   - If two outcomes are close enough for wording like "倾向平局", "小优", or "toss-up", make the probability ranges and scoreline order reflect that closeness.
   - For group finales, cap confidence when a stronger team has advanced or has strong rotation incentives. Avoid a clear-favorite probability above 55% without lineup and motivation support.
   - If both teams can benefit from a draw, raise draw probability meaningfully or explain why match dynamics point away from it.

6. Handle knockout matches.
   - The primary forecast remains 90-minute win/draw/loss; separate it from "to advance".
   - Weaker sides often defend deep and target extra time or penalties, so the 90-minute draw can be 28%-35% or higher when supported by low-block discipline, goalkeeper quality, set pieces, or penalty edge.
   - Do not force high draws mechanically. Keep draws closer to 24%-29% when the favorite has early-chance creation, the underdog has defensive errors, both teams are high-transition, or game state forces the underdog to attack.
   - If favorite win is below roughly 50% and draw is 30%+, list a draw scoreline first or co-first unless there is strong evidence the game will open up.
   - Add extra-time/penalty assessment when draw probability exceeds 25%, and include advancement probability only as supplementary context.
   - Account for elimination-pressure psychology, prior minutes played, rest days, squad depth for 120 minutes, goalkeeper penalty record, and designated takers.

7. Explain, persist, and review.
   - Final output may lead with the pick, but the reasoning must be evidence-first.
   - State the key assumption and main failure path.
   - Save every analyzed match to `pred/YYYY-MM-DD_HHMM_TeamA-vs-TeamB.md`, using kickoff time in Beijing time and ASCII-safe team slugs.
   - Saved files must include pick, probability ranges, likely scorelines, scoring table, evidence ledger, lineup uncertainty, key assumption, failure path, and source links.
   - For Chinese users, write saved markdown in Chinese.
   - After writing, review the saved file for consistency across headline pick, probability leader, scorelines, scoring table, rationale, key assumption, failure path, and sources.
   - Include a narrative-probability check: "If I only read the evidence ledger and rationale, what probability band would I infer?" Fix any material conflict before responding.
   - Use read-only subagents for this review when available; otherwise review manually.

8. Backtest saved predictions when requested.
   - Compare primary 90-minute pick, predicted probability, likely scorelines, and actual result.
   - Track primary outcome hit, likely-score hit, and calibration quality separately.
   - Do not score live or unfinished matches.
   - Explain misses through evidence gaps or weighting errors, not hindsight certainty.
   - Convert repeated misses into skill updates, especially for incentives, lineup uncertainty, draw pricing, overreliance on reputation, and knockout draw/penalty paths.

## Evidence Rules

- Cite sources with links in the final answer.
- If sources disagree, state the discrepancy and use the more authoritative or newer source.
- Treat betting odds as a market signal, not proof.
- If Polymarket data is available, treat it as a market signal with the same caution: prefer liquid, actively traded markets; use `bestBid`, `bestAsk`, `lastTradePrice`, `volume`, and `liquidity` over a raw midpoint; and discount thin or stale books.
- For 2026 World Cup use, prefer match-specific markets when they exist. If only tournament winner markets are available, use them as a broad strength check, not a substitute for match-level evidence.
- If a Polymarket search endpoint returns noisy results, filter the returned market list locally by question, slug, and category instead of trusting search alone.
- Do not overweight Polymarket over confirmed lineups, standings, injuries, or rotation reports. A sharp price move should trigger a re-check of those inputs, not replace them.
- Treat FIFA ranking as a baseline only; adjust for current form, injuries, matchup, and tournament context.
- Treat coach quality, lineup construction, and bench usage as first-class evidence, not afterthoughts.
- Treat this-tournament performance as stronger evidence than pre-tournament reputation when both exist.
- Treat confirmed lineups, group standings, and qualification incentives as hard constraints on probability calibration.
- Do not present a forecast as guaranteed or as gambling advice.

## Output Shape

For Chinese users, answer in Chinese unless asked otherwise. Saved markdown files for Chinese predictions must also be written in Chinese. Use this compact structure:

```text
我判断：[球队] 更可能赢，倾向比分 [x-y] 或 [x-y]。
90 分钟粗略概率：[A胜] xx%-xx%，平局 xx%-xx%，[B胜] xx%-xx%。

评分对比：
1. 阵容实力：[A队] x/30，[B队] x/30
2. 近期/赛事表现：[A队] x/20，[B队] x/20
3. 战术对位：[A队] x/25，[B队] x/25
4. 教练与比赛管理：[A队] x/15，[B队] x/15
5. 赛程/战意/环境：[A队] x/10，[B队] x/10
综合评分：[A队] xx/100，[B队] xx/100

证据账本：
- 推高[A队]胜率：[要点]
- 推高平局概率：[要点]
- 推高[B队]胜率：[要点]
- 只影响晋级而非90分钟：[要点，如加时/点球深度]

首发强度/轮换不确定性：
- [A队]：[主力程度描述，如"预计最强阵/轮换2-3人/半替补阵"]，对胜率影响 [方向和幅度]
- [B队]：[同上]
- 信息确定度：[已确认首发 / 可靠报道 / 纯推测]

依据：
1. [最强证据]
2. [第二证据]
3. [主力/替补/教练证据]
4. [战术/赛程/对位证据]
5. [爆冷或平局风险]

关键假设：[最影响预测的一条前提，例如首发强度、轮换幅度、战意或伤停]
结论：[一句话总结 pick，并说明最大不确定性。]
```

For knockout matches, optionally append supplementary context after the main block:

```text
淘汰赛附加（补充信息，非主预测）：
- 90 分钟平局概率：xx%
- 加时/点球优势方：[球队]，理由：[门将扑点/体力/教练经验]
- 晋级概率：[A队] xx%，[B队] xx%
```

For deeper requests, read `references/prediction-framework.md`.

When writing files into `pred/`, keep the content concise and structured so each file is easy to scan later. For Chinese predictions, use Chinese markdown headings such as `## 评分`, `## 首发强度/轮换不确定性`, `## 依据`, `## 关键假设`, `## 预测失效路径`, `## 来源`, and for knockout matches also `## 淘汰赛附加`.
