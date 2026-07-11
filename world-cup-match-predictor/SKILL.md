---
name: world-cup-match-predictor
description: Evidence-based workflow for predicting, saving, or backtesting 2026 FIFA World Cup final-tournament match outcomes only, including upcoming fixtures, same-day or tomorrow matches, saved predictions in pred/, group-stage or knockout scenarios, and user requests asking who will win, likely score, draw risk, upset chance, match judgment, or prediction review. Use for 2026 FIFA World Cup final-tournament football/soccer predictions and post-match calibration with current team news, rankings, odds, schedule, injuries, lineups, form, tactics, results, and explicit uncertainty. Do not use for qualifiers, friendlies, club matches, other FIFA events, or generic football predictions.
---

# World Cup Match Predictor

## Overview

Use this skill to produce disciplined 2026 FIFA World Cup final-tournament match predictions and reviews. Treat predictions as probabilistic judgments, not certainties, and ground every major claim in current, cited evidence.

For deeper, high-stakes, knockout, or backtesting work, read `references/prediction-framework.md` after this file. `SKILL.md` is the operating workflow; the reference file is the detailed calibration layer.

## Skill Maintenance

When optimizing this skill, review both `SKILL.md` and `references/prediction-framework.md` in the same pass. Keep probability bands, scoring rubrics, evidence workflow, persistence requirements, and consistency checks aligned before syncing the installed copy.

## Core Workflow

1. Confirm the fixture.
   - Resolve dates against the user's timezone, then standardize kickoff times and saved filenames to Beijing time (UTC+08:00).
   - Verify competition, venue, kickoff, group/round, standings context, and match state.
   - Use this skill only for the 2026 FIFA World Cup final tournament.
   - For saved predictions in `pred/`, parse the file first; for backtests, verify the final result before scoring.

2. Gather current evidence.
   - Browse before predicting. Do not rely on memory for squads, injuries, standings, lineups, odds, results, or form.
   - Prefer official FIFA pages, federations, match centers, injury/team reports, odds aggregators, and established sports outlets.
   - Use at least two source types when available, usually official/schedule data plus performance and availability data. Market data, including Polymarket, is a secondary reference layer and must not replace personnel, lineup-strength, tactical, or technical-stat analysis.
   - For current-tournament team performance, use FIFA official team statistics when available before relying on article summaries. Start from `https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/statistics/team-statistics`, then review every visible team-statistics category: Attacking, Distribution, Defending, Discipline, Goalkeeping, Movement, and Physical. Do not base the technical-stat read only on Attacking.
   - FIFA team statistics pages are dynamic; if plain HTML only shows an app shell, use a rendered browser read of visible page text or page requests. Capture the relevant full row for each team across category tabs rather than hand-copying one headline stat.
   - Within roughly 90 minutes of kickoff, look for confirmed lineups or reliable lineup reports before making a strong pick.
   - For completed matches, use final-score sources plus at least one match report or live text before judging prediction quality.
   - If evidence is unavailable or conflicting, state the limitation and avoid a strong pick.

3. Build an evidence-first case.
   - Establish incentives before team strength: qualification status, draw incentives, goal difference, rotation, and whether either side is eliminated. Do not equate eliminated with unmotivated; check pride, young players, coach pressure, and showcase incentives.
   - Compare squad quality, current-tournament form, tactics, coaching/game management, availability, rest/travel/weather, and market movement. Treat personnel configuration and historical/current technical statistics as the main judgment basis; use market movement only as a calibration check or discrepancy flag.
   - Break squad quality into starting XI, first-impact substitutes, bench depth by position, and the main creator, scorer, holding midfielder, center-back, and goalkeeper.
   - Treat "available" and "match-fit starter" as different availability states. Downgrade starting-XI strength when key players are bench-only, minutes-limited, or returning from injury.
   - Use official team statistics as a performance layer, not a replacement for matchup analysis. Weight Attacking, Distribution, Defending, Discipline, Goalkeeping, Movement, and Physical by match relevance.
   - Interpret volume and quality separately. Shot/corner volume can create draw or upset paths, but shots on target, xG, inside-box attempts, possession control, defensive concessions, discipline, goalkeeping, running profile, and physical load determine how strong those paths are.
   - For tactics, check pressing resistance, set pieces, transition defense, aerial duels, pace, goalkeeper reliability, control after taking the lead, and whether either side must chase the game.
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
   - Do not overprice generic knockout draws when current evidence shows sustained favorite chance creation, weak underdog outlets, defensive-spine absences, or late-game separation.
   - Do not underprice draw/upset paths when the underdog has low-block discipline, strong goalkeeping, set pieces, repeatable counters, or elite single-action attackers.
   - For volatile matches, keep 4+ goal tails visible when cards, penalties, forced chasing, vulnerable fullbacks, aerial mismatches, favorite control failures, or high-conversion attackers support them.
   - For low-event knockout matches with strong defensive results, cautious game states, missing or limited finishers, and no clear chance-volume edge, explicitly test 0-0 alongside 1-1 before ordering scorelines.
   - For group finales, cap confidence when a stronger team has advanced or has strong rotation incentives. Avoid a clear-favorite probability above 55% without lineup and motivation support.

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
   - Saved files must include pick, probability ranges, likely scorelines, scoring table, evidence ledger, FIFA technical-stat weighting when relevant, lineup uncertainty, key assumption, failure path, and source links.
   - For Chinese users, write saved markdown in Chinese.
   - After writing, review the saved file for consistency across headline pick, probability leader, scorelines, scoring table, rationale, key assumption, failure path, and sources.
   - Include a narrative-probability check: "If I only read the evidence ledger and rationale, what probability band would I infer?" Fix any material conflict before responding.
   - Use read-only subagents for this review when available; otherwise review manually.

8. Backtest saved predictions when requested.
   - Treat every file under `pred/` as an immutable pre-match record during review. Never edit, rewrite, append to, rename, or otherwise modify a `pred/` file while backtesting or reviewing it.
   - Return the review in the conversation. Write it elsewhere only when the user explicitly requests a separate output file, and never place that review file under `pred/`.
   - Compare primary 90-minute pick, predicted probability, likely scorelines, and actual result.
   - Track primary outcome hit, likely-score hit, and calibration quality separately.
   - Do not score live or unfinished matches.
   - Explain misses through evidence gaps or weighting errors, not hindsight certainty.
   - If advancement was right but the 90-minute result missed, audit whether advancement strength leaked into the regulation-time headline.
   - If a likely scoreline hit but the headline pick missed, classify it as a headline/probability calibration error rather than a full model miss.
   - If the result class was right but goal total was wrong, audit overused both-teams-to-score, underweighted 0-0 conditions, or underweighted punch-underdog/high-event volatility.
   - Convert repeated misses into explicit future probability adjustments, especially for incentives, lineup uncertainty, draw pricing, overreliance on reputation, underdog outlets, and knockout draw/penalty paths.

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
- [A队]：[主力程度描述]，对胜率影响 [方向和幅度]
- [B队]：[同上]
- 信息确定度：[已确认首发 / 可靠报道 / 纯推测]

依据：
1. [最强证据]
2. [第二证据]
3. [主力/替补/教练证据]
4. [战术/赛程/对位证据]
5. [爆冷或平局风险]

关键假设：[最影响预测的一条前提]
结论：[一句话总结 pick，并说明最大不确定性。]
```

For knockout matches, optionally append supplementary context after the main block:

```text
淘汰赛附加（补充信息，非主预测）：
- 90 分钟平局概率：xx%
- 加时/点球优势方：[球队]，理由：[门将扑点/体力/教练经验]
- 晋级概率：[A队] xx%，[B队] xx%
```

When writing files into `pred/`, keep the content concise and structured so each file is easy to scan later. For Chinese predictions, use Chinese markdown headings such as `## 评分`, `## 首发强度/轮换不确定性`, `## FIFA技术统计权重`, `## 依据`, `## 关键假设`, `## 预测失效路径`, `## 来源`, and for knockout matches also `## 淘汰赛附加`.
