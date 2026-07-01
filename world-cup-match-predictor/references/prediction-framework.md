# Prediction Framework

Use this reference for deeper or high-stakes match calls. `SKILL.md` is the operating workflow; this file is the calibration and checklist layer.

## Evidence Ledger

Build the ledger before probabilities:

1. Factors raising Team A 90-minute win probability.
2. Factors raising the draw probability.
3. Factors raising Team B 90-minute win probability.
4. Factors affecting only advancement, not the 90-minute result.

Then convert each material factor into a directional probability adjustment. If a fact is worth mentioning but does not move win/draw/loss, label it as context.

## Evidence Priority

1. Official match facts: schedule, venue, kickoff, group/round, standings, disciplinary status, final result for backtests.
2. Incentives and match state: must-win, draw-enough, already-qualified, eliminated, goal-difference needs, likely opponent-selection incentives.
3. Availability: confirmed lineups, injuries, suspensions, late fitness news, coach comments, credible rotation reports.
4. Team quality: Elo/SPI-style ratings, FIFA ranking, squad market value, club level of starters, bench depth.
5. Current performance: this-tournament results, opponent-adjusted form, xG if available, goals for/against, clean sheets, set-piece output.
6. Context: rest days, travel, climate, home-region advantage, rotation incentives.
7. Market signal: bookmaker odds or prediction markets, especially liquid markets or sharp late moves.

When the match is a knockout fixture in a host nation's true home venue, split home advantage into concrete pieces: crowd pressure, familiar pitch/stadium, climate or altitude adaptation, travel burden, referee/tempo pressure, and likelihood of a fast start. Treat supported factors as probability drivers, not only narrative context.

## Scoring Rubric

Default 100-point rubric, aligned with `SKILL.md`:

- Squad quality: 30
- Recent/tournament performance: 20
- Tactical matchup: 25
- Coaching/game management: 15
- Context/motivation/environment: 10

Use the score as a sanity check, not a formula. A narrow score edge should usually map to a narrow probability edge. If the score and pick diverge, explain the override.

Optional sub-factors:

- Squad quality: starting XI, first-impact substitutes, positional cover, goalkeeper and center-back reliability.
- Tactical matchup: low-block breaking, chance conversion, set pieces, transition defense, aerial duels, pressing resistance.
- Coaching/game management: default shape, pressing triggers, substitution timing, rotation choices, penalty/extra-time handling.
- Match-state reliability: defensive error tendency, control after scoring first, ability to protect a draw, late-game concentration.

For group-stage finales, make incentives visible in the score. If useful, move 5-10 points of weight from squad/tactics into context/motivation to reflect qualification status, draw incentives, rotation, cards, and minute management.

For host-nation knockout matches, the 10-point context/motivation/environment bucket may understate the effect if the game is genuinely at home. If the host has solid form and near-best lineup, reflect the edge both in the context score and in the probability table. If the opponent has a credible low block or altitude/climate adaptation, offset the adjustment explicitly.

## Probability Calibration

Use these 90-minute probability bands:

- 70%+: strong favorite; explain why the draw path is unusually weak.
- 65%-70%: clear favorite; acknowledge rotation, knockout, or low-block risk if present.
- 58%-65%: moderate favorite; do not write the rationale like domination.
- 50%-58%: slight edge or toss-up; scorelines and language should stay cautious.
- No side above 50%: draw or true toss-up may be a first-order outcome.

Draw guardrails:

- Football draw probability must stay visible even when one side is stronger.
- Do not list a draw as a likely scoreline while assigning it a very low probability unless explicitly explaining it as a secondary path.
- If both teams benefit from a draw, start near 30% and adjust for tactics, defensive reliability, and market signal.
- If both teams can accept a draw and lineups/shapes are conservative, make 0-0 a live scoreline, not just 1-1.

When guardrails point in opposite directions, use the evidence ledger to decide the net effect. For example, true home advantage and opponent defensive absences can lower the draw from the generic knockout range, while elite low-block discipline or a strong goalkeeper can offset those favorite-side factors.

Favorite guardrails:

- Already-qualified favorite with probable rotation versus a motivated opponent: reduce 90-minute win probability by roughly 5-12 points unless confirmed lineups contradict rotation.
- If rotation removes the defensive spine (goalkeeper, center-backs, holding midfielder, fullback pair), downgrade defensive reliability again or widen opponent/draw ranges.
- Already-qualified favorite with strong lineup still needs motivation evidence before exceeding 60% against an opponent with a must-win path and enough attacking quality.
- If prose says "rotation could make this close" or "a draw is natural", the table must reflect that risk.
- Strong favorite scoring ceiling: when a favorite has a major attacking edge and the opponent is missing a defensive-spine player (center-back, holding midfielder, or goalkeeper), test 3-0 or 3-1 as a plausible scoreline. Do not let generic knockout caution force every favorite prediction into 1-goal-margin scores if the evidence points to sustained pressure and weak resistance.
- Strong home host adjustment: in true home knockout conditions with no major host lineup downgrade and at least solid current form, consider adding roughly 3-7 points to the host's 90-minute win probability. Use the lower end for disciplined, low-block opponents; use the higher end when the host has early-pressure weapons and the opponent shows defensive fragility.

## Knockout Calibration

Keep 90-minute result separate from advancement.

- Weaker sides often rationally defend deep and target extra time/penalties.
- Raise 90-minute draw into the 28%-35% range when the underdog has credible low-block discipline, strong goalkeeper, set-piece threat, or penalty edge.
- Keep draw closer to 24%-29% when the favorite creates early chances, the underdog has repeated defensive errors, both sides play high-transition football, or the underdog must attack.
- Do not mechanically overprice the draw against a strong favorite when the underdog's defensive spine is weakened. In that case, keep the draw visible but allow the favorite's multi-goal path to take more probability.
- If favorite win is below roughly 50% and draw is 30%+, list a draw scoreline first or co-first unless there is strong evidence the game will open.
- Add advancement context only after the 90-minute table. Mention goalkeeper penalty record, designated takers, rest days, prior minutes, and squad depth for 120 minutes when relevant.

## Matchup Checklists

Favorite vs underdog:

- Can the favorite break a low block without overcommitting?
- Does the underdog have counter pace, set-piece threat, or aerial advantage?
- Are the favorite's fullbacks vulnerable behind the line?
- How important is the first goal? Can the underdog keep 0-0 deep?
- Can the favorite's bench change the game after 60 minutes?
- Does the underdog have more than one viable game state?

Two strong teams:

- Separate midfield control from chance creation.
- Compare goalkeeper and center-back error risk.
- Check whether either coach is likely to rotate or protect players.
- Treat extra time and penalties separately from 90-minute superiority.

Group-stage finale:

- State current points, goal difference, and qualification route.
- Identify who needs a win, who can accept a draw, who is already through, and who is eliminated.
- Check rotation, card protection, minute management, and injury avoidance.
- If a weaker team must open up, raise both its upset path and the favorite's transition path.
- Do not downgrade eliminated teams automatically; assess pride, young-player incentives, coach pressure, and set-piece/transition weapons.
- If final lineups are not confirmed, widen ranges and make the pick conditional.

## Polymarket Usage

Use Polymarket only as market signal. It is not a source for fixtures, lineups, injuries, standings, or final results.

When available, capture:

- question, slug, market id, outcomes
- bestBid, bestAsk, lastTradePrice or outcomePrices
- volume, liquidity, active/closed status, update timestamp when available

Use hierarchy:

1. Liquid match-specific 90-minute markets.
2. Liquid advancement markets, only for "to advance" context.
3. Tournament-winner markets, only as broad strength/public-pricing checks.

Data quality checks:

- Prefer meaningful liquidity, recent trading, and narrow spreads.
- Treat low-liquidity, stale, wide-spread, or one-sided markets as weak evidence.
- Check market resolution rules before converting prices into probabilities.
- If a liquid market strongly disagrees with the model, re-check lineups, injuries, incentives, weather, and rules first. If still unexplained, widen the probability band rather than blindly adopting the market.

Search hygiene:

- If search is noisy, pull a bounded market/event list and locally filter `question`, `slug`, and `category`.
- Filter first by football keywords, then exact team names/aliases, then market type, liquidity, and recency.
- If no match-specific market exists, state that limitation or omit Polymarket.

## Red Flags

- Predicting from FIFA ranking alone.
- Ignoring group/knockout format, standings, incentives, or rotation.
- Treating one blowout as full proof of team level.
- Using stale injury or lineup information.
- Making confirmed-lineup-dependent claims before lineups are available.
- Giving exact-looking probabilities when evidence supports only ranges.
- Pick, probability leader, scoreline order, scoring table, rationale, key assumption, or failure path contradict each other.
- Equal or near-equal total scores paired with confident one-sided language without an override.
- Major draw/rotation risk appears in prose but not in probabilities.
- Mixing "win in 90 minutes" with "advance".
- Presenting gambling certainty or staking advice.

## Backtesting

For saved predictions in `pred/`:

- Count only completed matches.
- Verify final score from official/match-center sources and read at least one match report or live text.
- Track primary 90-minute outcome, likely-score hit, and calibration quality separately.
- A 53% favorite losing is not automatically a bad forecast; repeated misses from the same hidden factor are the problem.
- Attribute misses to the most likely weighting error: incentives, lineup uncertainty, tactical matchup, finishing variance, set pieces, red cards, stale evidence, or knockout draw/penalty path.
- Convert repeated errors into explicit future probability adjustments.

## Final Consistency Check

Before saving or answering:

- Date/time are absolute and Beijing time is clear where needed.
- Prediction says whether it is 90-minute result or advancement.
- Probability ranges, scorelines, scoring table, evidence ledger, rationale, key assumption, and failure path tell the same story.
- If the headline says "draw lean", draw is top or co-top.
- If a team has the highest probability, the headline names it as slight/clear/strong favorite according to the band.
- Sources support schedule, availability, standings, and key claims.
- Re-read the saved markdown after writing; run read-only subagent consistency review when available.
