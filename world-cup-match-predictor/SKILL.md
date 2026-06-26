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
   - Promote any major counterargument into the probability estimate. Do not mention rotation, low motivation, or draw incentives only as prose if they materially change the result.

4. Estimate outcomes.
   - Give a clear pick for 90-minute result unless the user asks for qualification/advancement.
   - Include uncertainty with approximate probability ranges for win/draw/loss.
   - For knockout matches, separate "90-minute result" from "to advance" if relevant.
   - Include one or two likely scorelines.
   - Keep likely scorelines consistent with the probability table. If a draw is listed as a likely score, draw probability should usually be close to the top outcome unless you explain why it is only a secondary path.
   - In group finales, cap confidence when a stronger team has already advanced or has strong rotation incentives. Avoid a clear-favorite probability above 55% without confirmed lineup and motivation evidence.
   - If both teams can benefit from a draw, raise draw probability meaningfully or explain why match dynamics still point away from it.
   - Include category scores and a total score comparison for both teams when the evidence supports it or the user asks for technical analysis.

5. Explain the judgment.
   - Lead with the prediction.
   - Present the strongest evidence first.
   - Explicitly mention the main way the prediction could fail.
   - Avoid overclaiming from one metric or one match.
   - State the key assumption that would most change the pick, such as confirmed rotation, late injury news, or one team's must-win interpretation.

6. Persist the prediction.
   - Write the final prediction to `pred/` as a markdown file for every match you analyze.
   - Use a filename shaped like `pred/YYYY-MM-DD_HHMM_TeamA-vs-TeamB.md`.
   - Base the timestamp on the match kickoff time in the relevant local timezone when available; otherwise use the best-supported date/time you have.
   - Normalize team names into ASCII-safe slugs for the filename.
   - Put the same structured prediction you would give the user into the file, including score, probability ranges, rubric scores when used, key assumptions, failure path, and source links.

7. Backtest saved predictions when requested.
   - For each completed match, compare the primary 90-minute pick, predicted probability, likely scorelines, and actual result.
   - Track three levels separately: primary outcome hit, likely-score hit, and calibration quality.
   - Do not count live or unfinished matches as wins or losses.
   - Explain misses by linking them to evidence gaps or weighting errors, not by treating the result as proof that every premise was wrong.
   - Convert repeated misses into concrete skill updates, especially for group-stage incentives, lineup uncertainty, draw pricing, or overreliance on squad reputation.

## Evidence Rules

- Cite sources with links in the final answer.
- If sources disagree, state the discrepancy and use the more authoritative or newer source.
- Treat betting odds as a market signal, not proof.
- Treat FIFA ranking as a baseline only; adjust for current form, injuries, matchup, and tournament context.
- Treat coach quality, lineup construction, and bench usage as first-class evidence, not afterthoughts.
- Treat this-tournament performance as stronger evidence than pre-tournament reputation when both exist.
- Treat confirmed lineups, group standings, and qualification incentives as hard constraints on probability calibration.
- Do not present a forecast as guaranteed or as gambling advice.

## Output Shape

For Chinese users, answer in Chinese unless asked otherwise. Use this compact structure:

```text
我判断：[球队] 更可能赢，倾向比分 [x-y] 或 [x-y]。
90 分钟粗略概率：[A胜] xx%-xx%，平局 xx%-xx%，[B胜] xx%-xx%。

如证据足够或用户要求技术分析，加入评分对比：
1. [项目A]：[A队] x/x， [B队] x/x
2. [项目B]：[A队] x/x， [B队] x/x
3. [项目C]：[A队] x/x， [B队] x/x
4. [项目D]：[A队] x/x， [B队] x/x
总分：[A队] xx/100， [B队] xx/100

依据：
1. [最强证据]
2. [第二证据]
3. [主力/替补/教练证据]
4. [战术/赛程/对位证据]
5. [爆冷或平局风险]

关键假设：[最影响预测的一条前提，例如首发强度、轮换幅度、战意或伤停]
结论：[一句话总结 pick，并说明最大不确定性。]
```

For deeper requests, read `references/prediction-framework.md`.

When writing files into `pred/`, keep the content concise and structured so each file is easy to scan later.
