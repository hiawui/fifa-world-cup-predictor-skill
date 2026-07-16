---
name: world-cup-match-predictor
description: Evidence-based workflow for predicting, saving, or backtesting 2026 FIFA World Cup final-tournament match outcomes only, including upcoming fixtures, same-day or tomorrow matches, saved predictions in pred/, group-stage or knockout scenarios, and user requests asking who will win, likely score, draw risk, upset chance, match judgment, or prediction review. Use for 2026 FIFA World Cup final-tournament football/soccer predictions and post-match calibration with current team news, rankings, odds, schedule, injuries, lineups, form, tactics, results, and explicit uncertainty. Do not use for qualifiers, friendlies, club matches, other FIFA events, or generic football predictions.
---

# World Cup Match Predictor

## Overview

Use this skill to produce disciplined 2026 FIFA World Cup final-tournament match predictions and reviews. Treat predictions as probabilistic judgments, not certainties, and ground every major claim in current, cited evidence.

For deeper, high-stakes, or knockout forecasts, read `references/prediction-framework.md` after this file. For completed-match reviews, read `references/backtesting.md` instead. Load both only when a review also changes the forecasting framework.

## Skill Maintenance

When optimizing this skill, review `SKILL.md`, both reference files, and prediction validation behavior in the same pass. Keep probability bands, scoring rubrics, evidence workflow, persistence requirements, and consistency checks aligned before syncing the installed copy.

## Core Workflow

1. Confirm the fixture.
   - Resolve dates against the user's timezone, then standardize kickoff times and saved filenames to Beijing time (UTC+08:00).
   - Verify competition, venue, kickoff, group/round, standings context, and match state.
   - Use this skill only for the 2026 FIFA World Cup final tournament.
   - For saved predictions in `pred/`, parse the file first; for backtests, verify the final result before scoring.
   - Record forecast creation time, evidence cutoff time, forecast status, lineup status, and whether a later lineup review is needed.
   - Use `赛前初版` when confirmed lineups are unavailable and `确认首发终版` only after the confirmed-lineup repricing gate. A `赛前初版` remains the delivered forecast if no later user request or scheduled update occurs; do not imply that the agent will revisit it autonomously.
   - If a later pre-kickoff review creates a `确认首发终版`, preserve the earlier headline probabilities and scorelines under `## 预测版本记录` before replacing the current headline. Freeze the file once the match kicks off.

2. Gather current evidence.
   - Browse before predicting. Do not rely on memory for squads, injuries, standings, lineups, odds, results, or form.
   - Prefer official FIFA pages, federations, match centers, injury/team reports, odds aggregators, and established sports outlets.
   - Use at least two source types when available, usually official/schedule data plus performance and availability data. Market data, including Polymarket, is a secondary reference layer and must not replace personnel, lineup-strength, tactical, or technical-stat analysis.
   - For current-tournament team performance, use FIFA official team statistics when available before relying on article summaries. Start from `https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/statistics/team-statistics`, then review every visible team-statistics category: Attacking, Distribution, Defending, Discipline, Goalkeeping, Movement, and Physical. Do not base the technical-stat read only on Attacking.
   - FIFA team statistics pages are dynamic; if plain HTML only shows an app shell, use a rendered browser read of visible page text or page requests. Capture the relevant full row for each team across category tabs rather than hand-copying one headline stat.
   - Within roughly 90 minutes of kickoff, look for confirmed lineups or reliable lineup reports before making a strong pick.
   - Once confirmed lineups are available, rerun the confirmed-lineup repricing gate in `references/prediction-framework.md` before finalizing probabilities or scorelines. If lineups remain unconfirmed, make the pick conditional and state which structural choices would move the ranges.
   - For completed matches, use final-score sources plus at least one match report or live text before judging prediction quality.
   - If evidence is unavailable or conflicting, state the limitation and avoid a strong pick.

3. Build an evidence-first case.
   - Establish incentives before team strength: qualification status, draw incentives, goal difference, rotation, and whether either side is eliminated. Do not equate eliminated with unmotivated; check pride, young players, coach pressure, and showcase incentives.
   - Compare squad quality, current-tournament form, tactics, coaching/game management, availability, rest/travel/weather, and market movement. Treat personnel configuration and historical/current technical statistics as the main judgment basis; use market movement only as a calibration check or discrepancy flag.
   - Break squad quality into starting XI, first-impact substitutes, bench depth by position, and the main creator, scorer, holding midfielder, center-back, and goalkeeper.
   - Treat "available" and "match-fit starter" as different availability states. Downgrade starting-XI strength when key players are bench-only, minutes-limited, or returning from injury.
   - Use official team statistics as a performance layer, not a replacement for matchup analysis. Weight Attacking, Distribution, Defending, Discipline, Goalkeeping, Movement, and Physical by match relevance.
   - Interpret volume and quality separately. Shot/corner volume can create draw or upset paths, but shots on target, xG, inside-box attempts, possession control, defensive concessions, discipline, goalkeeping, running profile, and physical load determine how strong those paths are.
   - For tactics, check pressing resistance, central-midfield numbers and roles, fullback-winger isolation, set pieces, transition defense, aerial duels, pace, goalkeeper reliability, control after taking the lead, and whether either side must chase the game.
   - For knockout matches and contests between strong teams, build a game-state transition matrix covering 0-0, Team A leading, Team B leading, minutes 60-75, and minutes 75-90. Identify outlet retention, protection tendencies, likely substitution roles, and which state moves probability from draw into either team's win bucket.
   - For favorites, test whether control can become separation: early chance creation, field tilt, opponent ball retention, bench impact, and whether an early goal forces the underdog out of its preferred plan.
   - For underdogs, separate resistance from punch. A team with only blocks and saves mostly raises draw risk; a team with repeatable creator-runner-finisher, set-piece, or counter outlets raises win probability and multi-goal tails, especially against favorites with recent control or defensive-management problems.
   - For host or home-region matches, treat crowd, altitude/climate, referee tempo, cards, penalties, and forced chasing as probability drivers when supported by evidence.
   - Keep head-to-head secondary unless the current matchup pattern is unusually stable and well supported.
   - Treat current-tournament evidence as stronger than pre-tournament reputation once the tournament has started.
   - Promote material counterarguments into the probability estimate; do not leave rotation, low motivation, draw incentives, or lineup uncertainty only as prose.
   - Build an evidence ledger before assigning probabilities:
     - Factors raising Team A's 90-minute win probability
     - Factors raising the draw probability
     - Factors raising Team B's 90-minute win probability
     - Factors that affect only advancement, not the 90-minute result
   - Include a technical-stat interpretation under `## FIFA技术统计权重` for Chinese saved files when official data affects the call. If an older file uses `## 控球/射门数据权重`, make sure it still covers all relevant FIFA categories, not only attacking.
   - Always include lineup strength / rotation uncertainty under `## 首发强度/轮换不确定性`.

4. Estimate outcomes.
   - Working order: evidence ledger -> directional adjustments -> scoring sanity check -> probability ranges -> likely scorelines -> final wording.
   - When strong defensive suppression lowers one side's scoring expectation, decide explicitly how much probability moves into 0-0, a one-goal draw, and opponent clean-sheet wins. Do not place the whole effect in the draw bucket.
   - Give a 90-minute win/draw/loss pick unless the user asks specifically for advancement.
   - Use informative probability ranges, usually 8-12 points wide. If a range exceeds 15 points, explain why; never use a range wider than 20 points.
   - Include one or two likely scorelines and keep them consistent with the probability table.
   - Include category scores unless evidence is too sparse. Default rubric: squad quality 30, recent/tournament performance 20, tactical matchup 25, coaching/game management 15, context/motivation/environment 10.

5. Apply calibration checks.
   - Match prose intensity to probability band: 70%+ strong favorite, 65%-70% clear favorite, 58%-65% moderate favorite, 50%-58% slight edge/toss-up.
   - If rationale implies a band more than about 5 percentage points away from the table, revise the probabilities or the language.
   - If the likely-score order lists a draw first or co-first and draw probability is near 30%, headline the draw risk rather than presenting a routine win pick.
   - Do not let advancement edge leak into 90-minute probability. Extra-time strength, penalties, and 120-minute squad depth belong in advancement context unless they change regulation tactics.
   - Split favorites into "separation favorites" and "control favorites" before choosing scorelines. Separation favorites can justify 2-0/3-0/3-1 paths; control favorites against compact blocks often fit 1-0/2-0/1-1 better.
   - Score coaching/game management from evidence about the expected plan, role balance, matchup adaptations, substitution behavior, and repeated structural meetings. Do not use reputation alone to overturn a tactical edge already identified elsewhere in the rubric.
   - Do not overprice generic knockout draws when current evidence shows sustained favorite chance creation, weak underdog outlets, defensive-spine absences, or late-game separation.
   - Do not underprice draw/upset paths when the underdog has low-block discipline, strong goalkeeping, set pieces, repeatable counters, or elite single-action attackers.
   - For volatile matches, keep 4+ goal tails visible when cards, penalties, forced chasing, vulnerable fullbacks, aerial mismatches, favorite control failures, or high-conversion attackers support them.
   - For low-event knockout matches with strong defensive results, cautious game states, missing or limited finishers, and no clear chance-volume edge, explicitly test 0-0 alongside 1-1 before ordering scorelines.
   - For group finales, cap confidence when a stronger team has advanced or has strong rotation incentives. Avoid a clear-favorite probability above 55% without lineup and motivation support.
   - Before finalizing any knockout forecast, run the regulation-time separation gate in `references/prediction-framework.md`. Remove extra-time/penalty-only factors and verify that the 90-minute headline still holds; distinguish evidence for separation in minutes 75-90 from depth that matters only after 90; promote a near-30% draw and any repeatable underdog scoring route into the headline and scoreline order.

6. Handle knockout matches.
   - The primary forecast remains 90-minute win/draw/loss; separate it from "to advance".
   - Weaker sides often defend deep and target extra time or penalties, so the 90-minute draw can be 28%-35% or higher when supported by low-block discipline, goalkeeper quality, set pieces, or penalty edge.
   - Keep draws closer to the low/mid 20s when the favorite has sustained territorial control, good counter-press/rest defense, and the underdog lacks reliable outlets.
   - If favorite win is below roughly 50% and draw is 30%+, list a draw scoreline first or co-first unless there is strong evidence the game will open up.
   - Add extra-time/penalty assessment when draw probability exceeds 25%, and include advancement probability only as supplementary context.

7. Explain, persist, and review.
   - Final output may lead with the pick, but the reasoning must be evidence-first.
   - State the key assumption and main failure path.
   - Save every analyzed match to `pred/YYYY-MM-DD_HHMM_TeamA-vs-TeamB.md`, using kickoff time in Beijing time and ASCII-safe team slugs.
   - Saved files must include lifecycle metadata, version history, pick, probability ranges, likely scorelines, scoring table, evidence ledger, FIFA technical-stat weighting when relevant, lineup uncertainty, key assumption, failure path, and source links.
   - For knockout matches and contests between strong teams, also include `## 比赛状态转换` with the required state matrix and its probability implications.
   - For Chinese users, write saved markdown in Chinese.
   - After writing, review the saved file for consistency across headline pick, probability leader, scorelines, scoring table, rationale, key assumption, failure path, and sources.
   - Run `uv run <skill-dir>/scripts/validate_prediction.py --strict <saved-file>` for every newly created or pre-kickoff-updated prediction. Fix every error before responding. Use the non-strict mode only to audit legacy files created before lifecycle metadata existed.
   - Include a narrative-probability check: "If I only read the evidence ledger and rationale, what probability band would I infer?" Fix any material conflict before responding.
   - Use read-only subagents for this review when available; otherwise review manually.

8. Backtest saved predictions when requested.
   - Read and follow `references/backtesting.md`.
   - Treat every file under `pred/` as an immutable pre-match record during review. Never edit, rewrite, append to, rename, or otherwise modify a `pred/` file while backtesting or reviewing it.
   - Return the review in the conversation. Write it elsewhere only when the user explicitly requests a separate output file, and never place that review file under `pred/`.
   - Score the latest pre-kickoff version as the primary forecast. Compare earlier snapshots separately when version history exists.
   - Distinguish outcome hit, likely-score hit, probability quality, and evidence-process quality. Do not call a plausible-probability outcome a calibration failure merely because it occurred.

## Evidence Rules

- Cite sources with links in the final answer.
- If sources disagree, state the discrepancy and use the more authoritative or newer source.
- Treat betting odds and Polymarket as market signals, not proof. Prefer liquid, active, match-specific markets; discount thin, stale, wide-spread, or noisy markets.
- For Polymarket World Cup pages, start with `https://polymarket.com/sports/world-cup` when a direct match market may exist. Capture the visible match card or linked match page first, especially 90-minute moneyline/reg-time prices, volume, spread/handicap, total-goals, and any relevant player-prop context. Use Gamma/API filtering as fallback or cross-check, not as the only discovery path.
- For 2026 World Cup use, prefer match-specific markets when they exist. If only tournament winner markets are available, use them as a broad strength check, not a substitute for match-level evidence.
- Do not overweight markets over confirmed lineups, standings, injuries, rotation reports, squad construction, tactical matchup, or historical/current technical statistics. A sharp price move should trigger a re-check of those inputs, not replace them.
- Treat FIFA ranking as a baseline only; adjust for current form, injuries, matchup, and tournament context.
- Treat FIFA official team statistics as preferred current-tournament performance evidence. Use the full row and ratios across Attacking, Distribution, Defending, Discipline, Goalkeeping, Movement, and Physical, not a single sorted column or only the Attacking tab.
- Treat coach quality, lineup construction, and bench usage as first-class evidence, not afterthoughts.
- Treat confirmed lineups, group standings, and qualification incentives as hard constraints on probability calibration.
- Do not present a forecast as guaranteed or as gambling advice.
- Do not output staking sizes, Kelly fractions, or bet instructions unless the user explicitly asks for them. Even then, label them as a mathematical exercise rather than a recommendation, and keep the match prediction separate from betting execution.

## Output Shape

For Chinese users, answer in Chinese unless asked otherwise. Saved markdown files for Chinese predictions must also be written in Chinese. Use this compact structure:

```text
预测生成时间：[YYYY-MM-DD HH:MM BJT]
信息截止时间：[YYYY-MM-DD HH:MM BJT]
预测状态：[赛前初版 / 确认首发终版]
首发状态：[未公布 / 可靠预计 / 已确认]
是否需要临场复核：[是 / 否]

## 预测版本记录

- [时间] [赛前初版 / 确认首发终版]：[90分钟概率、主要比分和变更理由；初版也记录当前快照]

我判断：[球队] 更可能赢，倾向比分 [x-y] 或 [x-y]。
90 分钟粗略概率：[A胜] xx%-xx%，平局 xx%-xx%，[B胜] xx%-xx%。

## 评分

1. 阵容实力：[A队] x/30，[B队] x/30
2. 近期/赛事表现：[A队] x/20，[B队] x/20
3. 战术对位：[A队] x/25，[B队] x/25
4. 教练与比赛管理：[A队] x/15，[B队] x/15
5. 赛程/战意/环境：[A队] x/10，[B队] x/10
综合评分：[A队] xx/100，[B队] xx/100

## 证据账本

- 推高[A队]胜率：[要点]
- 推高平局概率：[要点]
- 推高[B队]胜率：[要点]
- 只影响晋级而非90分钟：[要点，如加时/点球深度]

## 首发强度/轮换不确定性

- [A队]：[主力程度描述]，对胜率影响 [方向和幅度]
- [B队]：[同上]
- 信息确定度：[已确认首发 / 可靠报道 / 纯推测]

## 比赛状态转换（淘汰赛或强强对话）

- 0-0：[控制、机会与换人倾向]
- A队领先：[守领先能力、反击出口、对手追分结构]
- B队领先：[同上]
- 60-75分钟：[预计换人角色及概率方向]
- 75-90分钟：[常规时间分离路线，不混入加时因素]

## 依据

1. [最强证据]
2. [第二证据]
3. [主力/替补/教练证据]
4. [战术/赛程/对位证据]
5. [爆冷或平局风险]

## 关键假设

[最影响预测的一条前提]

## 预测失效路径

- [最可能令主预测失效的具体比分与比赛路线]

## 来源

- [支持赛程、首发、数据和关键判断的链接]

## 结论

[一句话总结 pick，并说明最大不确定性。]
```

For knockout matches, optionally append supplementary context after the main block:

```text
淘汰赛附加（补充信息，非主预测）：
- 90 分钟平局概率：xx%
- 加时/点球优势方：[球队]，理由：[门将扑点/体力/教练经验]
- 晋级概率：[A队] xx%，[B队] xx%
```

When writing files into `pred/`, keep the content concise and structured so each file is easy to scan later. For Chinese predictions, use Chinese markdown headings such as `## 评分`, `## 首发强度/轮换不确定性`, `## FIFA技术统计权重`, `## 依据`, `## 关键假设`, `## 预测失效路径`, `## 来源`, and for knockout matches also `## 淘汰赛附加`.
