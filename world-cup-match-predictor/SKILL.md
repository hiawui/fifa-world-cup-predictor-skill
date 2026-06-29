---
name: world-cup-match-predictor
description: Evidence-based workflow for predicting, saving, or backtesting 2026 FIFA World Cup final-tournament match outcomes only, including upcoming fixtures, same-day or tomorrow matches, saved predictions in pred/, group-stage or knockout scenarios, and user requests asking who will win, likely score, draw risk, upset chance, match judgment, or prediction review. Use for 2026 FIFA World Cup final-tournament football/soccer predictions and post-match calibration with current team news, rankings, odds, schedule, injuries, lineups, form, tactics, results, and explicit uncertainty. Do not use for qualifiers, friendlies, club matches, other FIFA events, or generic football predictions.
---

# World Cup Match Predictor

## Overview

Use this skill to produce disciplined 2026 FIFA World Cup final-tournament match predictions and reviews. Treat predictions as probabilistic judgments, not certainties, and ground every major claim in current, cited evidence.

## Core Workflow

1. Confirm the fixture.
   - Resolve relative dates against the user's timezone and current date.
   - Standardize all kickoff times, saved prediction timestamps, and date references to Beijing time (UTC+08:00), regardless of source timezone. When a source uses local venue time or UTC, convert it to Beijing time and state the conversion when it matters.
   - Verify competition, venue, kickoff time, group/round, standings context, and whether the match is upcoming, live, or complete.
   - Confirm the match belongs to the 2026 FIFA World Cup final tournament; if not, do not use this skill.
   - If the user gives only a local time, state the assumed timezone.
   - For saved predictions in `pred/`, parse the prediction first, then verify the actual result before scoring it.

2. Gather current evidence.
   - Browse for up-to-date sources before predicting.
   - Prefer official FIFA pages, federation/team announcements, reputable match centers, injury reports, odds aggregators, and established sports outlets.
   - Use at least two independent source types when available: official/schedule data plus performance or market data.
   - For matches within roughly 90 minutes of kickoff, look for confirmed lineups or reliable lineup reports before making a strong pick.
   - For completed matches or backtests, use final-score sources and at least one match report or live text before judging why the prediction worked or failed.
   - Do not rely on memory for current squads, injuries, standings, lineups, odds, results, or recent form.
   - If current sources are unavailable, insufficient, or conflicting in a way that cannot be resolved, state the limitation and avoid a strong pick; give only a conditional judgment.

3. Build the case.
   - For group-stage matches, establish incentives before judging team strength: each team's qualification status, whether a draw is enough, goal-difference incentives, rotation incentives, and whether either side is already eliminated.
   - Compare team strength: FIFA ranking/Elo, squad quality, depth, tournament experience, and player availability.
   - Break squad quality into units: starting XI, first-impact substitutes, bench depth by position, and the availability of the main creator, scorer, holding midfielder, center-back, and goalkeeper.
   - Compare coaching profiles: preferred shape, pressing height, build-up style, substitution timing, penalty/extra-time history if relevant, and whether the coach reliably improves games in tournament settings.
   - Use head-to-head history only as a secondary signal; keep it subordinate to present squad strength and tactics unless the matchup pattern is unusually stable and well supported.
   - Compare recent performance: qualifying path, last 5-10 matches where available, group-stage results, goals for/against, chance creation, defensive record, and opponent quality.
   - Separate pre-tournament form from this-tournament form; in World Cup backtests and live predictions, recent matches in the same tournament should carry extra weight because tactics, fatigue, and momentum are already revealed.
   - Evaluate tactical matchup: pressing resistance, set pieces, transition defense, aerial duels, pace, goalkeeper reliability, and whether either side must chase the game.
   - Look specifically for defensive error tendency and control after taking the lead, because these often decide whether a favorite actually converts superiority into a win.
   - Account for context: travel, rest days, venue, weather if relevant, injuries/suspensions, lineup rotation, knockout incentives, goal-difference incentives, and market movement.
   - Promote any major counterargument into the probability estimate. Do not mention rotation, low motivation, or draw incentives only as prose if they materially change the result. Do not equate already eliminated with unmotivated: check whether pride, young creators, coach pressure, or showcase incentives can preserve attacking urgency.
   - **Lineup strength / rotation uncertainty (mandatory):** For every prediction, explicitly state the expected starting-lineup strength for each side relative to their best XI. Estimate whether rotation, rest, or injury degrades a team's cohesion or firepower, and write the directional impact on win probability (e.g., "rotation of 4+ starters in the back line likely costs ~5-8% off their baseline win rate"). If lineup information is unavailable, state the uncertainty and bracket the prediction accordingly. This assessment must appear in the saved markdown file under `## 首发强度/轮换不确定性`.
   - **Knockout-stage dynamics:** When the match is a knockout tie (Round of 32 onward), apply the following additional analysis:
     - The primary prediction remains 90-minute win/draw/loss. A draw at 90 minutes is a real, bettable outcome in knockout matches—do not suppress it just because the tie must eventually produce a winner.
     - The weaker side's rational strategy is often to defend deep and target extra time or penalties. This raises the 90-minute draw probability significantly; in many knockout matches it should be 28%-35% or higher.
     - Assess extra-time and penalty capability as supplementary information: goalkeeper penalty-saving record, designated takers, squad fitness/depth for 120 minutes, and coach substitution patterns in tournament knockouts.
     - Elevate the weight of psychological evidence: how each team performs when trailing, when protecting a lead, and under elimination pressure. Historical knockout exits or comebacks are relevant here.
     - Fatigue accumulation matters more as the bracket progresses; compare rest days, minutes played by key players in prior rounds, and squad rotation capacity.
     - After the main 90-minute prediction, optionally provide "to advance" probabilities as supplementary context, but never let this override or confuse the 90-minute pick.

4. Estimate outcomes.
   - Give a clear pick for 90-minute result unless the user asks for qualification/advancement.
   - Include uncertainty with approximate probability ranges for win/draw/loss.
   - Keep probability range widths informative: typical interval width should be 8-12 percentage points (e.g., "35%-45%"). If an interval exceeds 15 points, explicitly state why evidence is insufficient to narrow it. Never use intervals wider than 20 points—if uncertainty is that high, state the limitation and make the pick conditional rather than hiding it in a vague range.
   - For knockout matches, always separate "90-minute result" from "to advance" probabilities. The 90-minute result (including draw) is the primary prediction for betting purposes. Provide "to advance" only as supplementary context. Include an explicit extra-time/penalty edge assessment when 90-minute draw probability exceeds 25%.
   - Include one or two likely scorelines.
   - Keep likely scorelines consistent with the probability table. If a draw is listed as a likely score, draw probability should usually be close to the top outcome unless you explain why it is only a secondary path.
   - Cross-check the headline pick, probability ranges, likely scorelines, scoring table, rationale, key assumption, and failure path before finalizing. They must tell the same story. If the highest probability outcome is not the stated pick, either revise the pick or revise the probabilities and scorelines.
   - If two outcomes are close enough that the prose says "倾向平局", "小优", "toss-up", or similar, make the probability ranges reflect that closeness and order likely scorelines accordingly.
   - In group finales, cap confidence when a stronger team has already advanced or has strong rotation incentives. Avoid a clear-favorite probability above 55% without confirmed lineup and motivation evidence. If the favorite has already qualified and rotates most of its defensive spine or midfield screen, treat defensive coordination as a first-order risk and usually keep its win probability in the slight-favorite or toss-up band unless confirmed attacking urgency offsets it.
   - If both teams can benefit from a draw, raise draw probability meaningfully or explain why match dynamics still point away from it. If both teams can accept a draw and both lineups or shapes are conservative, make 0-0 a live scoreline rather than defaulting to 1-1.
   - Include category scores and a total score comparison for both teams in every prediction, unless evidence is too sparse to score responsibly; if scoring is withheld, state why.
   - Use a clear 100-point rubric by default: squad quality 30, recent/tournament performance 20, tactical matchup 25, coaching/game management 15, and context/motivation/environment 10.

5. Explain the judgment.
   - Lead with the prediction.
   - Make the first-line judgment match the probability table: the named winner should normally have the highest win probability, and a stated draw lean should normally have draw as the highest or co-highest outcome.
   - Present the strongest evidence first.
   - Explicitly mention the main way the prediction could fail.
   - Avoid overclaiming from one metric or one match.
   - State the key assumption that would most change the pick, such as confirmed rotation, late injury news, or one team's must-win interpretation.

6. Persist the prediction.
   - Write the final prediction to `pred/` as a markdown file for every match you analyze.
   - Use a filename shaped like `pred/YYYY-MM-DD_HHMM_TeamA-vs-TeamB.md`.
   - Base the timestamp on the match kickoff time converted to Beijing time; otherwise use the best-supported date/time you have and state the timezone uncertainty.
   - Normalize team names into ASCII-safe slugs for the filename.
   - Put the same structured prediction you would give the user into the file, including pick, probability ranges, likely scorelines, category scores, total scores, key assumptions, failure path, and source links.
   - If the user is Chinese or asks in Chinese, write the saved markdown content in Chinese, including headings, labels, rationale, assumptions, and scoring table. Keep filenames ASCII-safe even when the markdown content is Chinese.

7. Run post-prediction consistency review.
   - After writing prediction markdown files, use subagents when available to review the saved files for internal consistency before giving the final answer.
   - Split reviews into small independent batches, usually one or two match files per subagent, and make each subagent read-only. Ask it to check whether the headline pick, probability leader, likely scoreline order, scoring table totals, rationale, key assumption, and failure path agree.
   - Ask each subagent to report "consistent" or "inconsistent", cite the exact conflicting lines or phrases, and suggest the smallest safe correction. Do not ask subagents to edit prediction files unless you explicitly assign a disjoint write scope.
   - While subagents run, do non-overlapping work such as checking skill sync or source diffs. When results return, integrate only the corrections that improve consistency and re-check the edited files.
   - If subagents are unavailable, do the same consistency review manually before responding. Do not skip this step.

8. Backtest saved predictions when requested.
   - For each completed match, compare the primary 90-minute pick, predicted probability, likely scorelines, and actual result.
   - Track three levels separately: primary outcome hit, likely-score hit, and calibration quality.
   - Do not count live or unfinished matches as wins or losses.
   - Explain misses by linking them to evidence gaps or weighting errors, not by treating the result as proof that every premise was wrong.
   - Convert repeated misses into concrete skill updates, especially for group-stage incentives, lineup uncertainty, draw pricing, or overreliance on squad reputation.

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
