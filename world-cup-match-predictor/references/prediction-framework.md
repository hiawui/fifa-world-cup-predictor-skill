# Prediction Framework

## Evidence Priority

1. Official 2026 FIFA World Cup match facts: schedule, venue, kickoff, group/round, standings, disciplinary status, final result for backtests.
2. Incentives and match state: must-win, draw-enough, already-qualified, eliminated, goal-difference needs, likely opponent-selection incentives.
3. Availability: confirmed lineups, injuries, suspensions, late fitness news, coach comments, credible rotation reports.
4. Team quality: Elo/SPI-equivalent ratings, FIFA ranking, squad market value, club level of starters, bench depth.
5. Performance: recent results adjusted for opponent strength, expected goals if available, goals for/against, clean sheets, set-piece output.
6. Context: rest days, travel, climate, home-region advantage, rotation incentives.
7. Market signal: bookmaker odds or prediction markets, especially when many books agree or odds move sharply.

## Polymarket Usage

Use Polymarket only as a market-signal input. It can help calibrate the model, but it is not an official source for fixtures, lineups, injuries, standings, or final results.

When available, query active open markets from Polymarket's public Gamma API and capture:

- question and slug
- market id
- outcomes
- outcomePrices or lastTradePrice
- bestBid and bestAsk
- volume and liquidity
- active and closed status
- update timestamp when available

Prefer match-specific markets over tournament-level markets. For a World Cup match prediction:

- A liquid 90-minute win/draw/win or advancement market can materially inform the market-signal category.
- A team-to-win-the-tournament market is only a broad team-strength and public-pricing check.
- Do not infer a single-match win probability directly from a championship market without bracket path, opponent, rotation, and match-state adjustments.

Data quality checks:

- Prefer markets with meaningful liquidity, recent trading, and narrow bid/ask spreads.
- Treat low-liquidity, one-sided, stale, or wide-spread markets as weak evidence.
- Use `bestBid`/`bestAsk` and `lastTradePrice` together; a last trade far outside the current spread may be stale.
- Convert prices into rough probabilities only after checking the market resolution rules.
- Confirm whether the market is for 90-minute result, advancement, group qualification, or tournament winner before using it.

Search and filtering:

- Do not trust Polymarket search results blindly; broad search terms can return unrelated markets.
- If search is noisy, pull a bounded market/event list and locally filter `question`, `slug`, and `category` for team names, "FIFA", "World Cup", and "soccer".
- If no match-specific market is found, state that limitation and either use the tournament-winner market lightly or omit Polymarket from the match forecast.

Query hygiene:

- Prefer one bounded list query per object type (`events` or `markets`) and filter locally instead of firing many broad search queries.
- Normalize team names and aliases before filtering, including common short forms and spelling variants.
- Read only the fields you need for calibration; prioritize `question`, `slug`, `category`, `bestBid`, `bestAsk`, `lastTradePrice`, `volume`, `liquidity`, and timestamps.
- If the result set is large, filter first by football-related keywords, then by exact teams or market type, then by liquidity and recency.
- If an API call returns unrelated or stale-looking results, stop widening the search and fall back to other evidence sources.

Calibration rules:

- If a liquid Polymarket match market strongly disagrees with the model, first re-check lineups, injuries, incentives, weather, and market rules.
- If the disagreement remains unexplained, widen the probability band rather than blindly adopting the market.
- A sharp late price move is a trigger for evidence review, especially near lineup release or major injury news.
- Keep Polymarket inside the market-signal slice of the rubric unless it reveals or strongly implies new information that can be independently verified.

## Suggested Weighting

Use this as a thinking aid, not a rigid formula:

- Squad quality and depth: 20%
- This-tournament performance or recent form: 20%
- Availability and lineup certainty: 15%
- Tactical matchup: 20%
- Coach and in-game management: 10%
- Reliability under match states: 10%
- Context and market signal: 5%

When the tournament is underway, this-tournament performance should usually outweigh older friendly or qualifying form. When the tournament has not started, use opponent-adjusted recent form instead.

Adjust weights when a factor is unusually decisive. For example, confirmed absence of a first-choice goalkeeper or striker can outweigh small ranking differences.

For group-stage finales, use an incentive-aware weighting before the normal rubric:

- Squad quality and depth: 18%
- This-tournament performance: 20%
- Availability and lineup certainty: 15%
- Tactical matchup: 17%
- Group incentives and rotation risk: 15%
- Reliability under match states: 10%
- Market signal: 5%

If a team is already qualified, eliminated, or only needs a draw, the incentive category can dominate small squad-quality edges. Do not let a stronger reputation override a clear, current tournament incentive without evidence.

## Probability Calibration

- Heavy favorite: 65-75% win probability in 90 minutes.
- Clear favorite: 55-65%.
- Slight favorite: 45-55%.
- Toss-up: no side above 45%.
- Underdog with real upset path: 20-35%.
- Very large mismatch: favorite may exceed 75%, but explain tournament volatility.

Keep draw probability visible in football predictions. Even a superior team may have only a 50-60% 90-minute win chance when the underdog can defend deep.

Use these calibration guardrails:

- Already-qualified favorite with probable rotation versus motivated opponent: reduce favorite win probability by roughly 5-12 points unless confirmed lineups contradict rotation. If rotation removes most of the defensive spine (goalkeeper, center-backs, holding midfielder, or fullback pair), reduce again or widen the opponent win range because coordination errors can outweigh bench talent.
- Already-qualified favorite using a heavily rotated XI against an eliminated opponent with credible creators or transition pace should rarely sit above 35-38% in 90-minute win probability without strong evidence of urgency and defensive stability.
- Already-qualified favorite with strong lineup confirmed: still check whether it needs the win; avoid exceeding 60% if the opponent has a must-win path and enough attacking quality.
- Both teams benefit from a draw or one team only needs a draw: draw probability usually starts near 30%, then adjust for tactical mismatch, defensive reliability, and market signal. If both sides use conservative shapes or five-defender structures and neither needs early goal difference, 0-0 should be a primary scoreline candidate alongside or ahead of 1-1.
- If the written risk says "rotation could make this close" or "a draw is natural", the probabilities must reflect that risk. Otherwise the forecast is internally inconsistent.
- Do not list a draw as one of two likely scores while assigning a very low draw probability. The scoreline list and probability table should tell the same story.

## Scoring Rubric

Use a 100-point comparison when the user wants a more technical call or when the matchup is close.

Suggested categories:

- Squad quality and depth: 20
- This-tournament performance / recent form: 20
- Availability and lineup certainty: 15
- Tactical matchup: 20
- Coach quality and in-game management: 10
- Reliability under match states: 10
- Context and market signal: 5

When the tournament is already underway, split form into:

- Pre-tournament form
- This-tournament form

Give this-tournament form extra weight in backtests and live forecasts because it captures the actual competitive environment.

For group-stage finales, replace "Context and market signal" with two categories when useful:

- Group incentives and rotation risk: 15
- Market signal: 5

Keep total score at 100 by reducing squad quality to 18 and tactical matchup to 17. This forces qualification status, likely rotation, and draw incentives into the score instead of burying them in commentary.

Optional sub-factors to split out when they matter:

- Tactical matchup: low-block breaking, chance conversion, set-piece edge, transition defense, aerial duels.
- Reliability under match states: defensive error tendency, control after scoring first, ability to protect a draw, late-game concentration.
- Coach quality and in-game management: substitution timing, shape changes, rotation choices, penalty/extra-time handling.
- Squad quality and depth: starting XI, first-impact substitutes, positional cover, goalkeeper and center-back reliability.

Score each team in every category, then sum to a total. Keep the scale consistent within a single analysis. If one factor is decisive, explain why the category weight should be effectively higher than the default.

Use the total score as a decision aid, not a substitute for narrative reasoning. A narrow score edge should usually map to a narrow win probability edge.

## Red Flags

- Predicting from FIFA ranking alone.
- Ignoring whether the match is group stage or knockout.
- Ignoring current group standings, qualification incentives, or rotation incentives.
- Treating a single blowout as full proof of team level.
- Using stale injury or squad information.
- Naming confirmed-lineup-dependent conclusions before checking whether lineups are available.
- Giving exact-looking probabilities when evidence only supports broad ranges.
- Mentioning a major draw or rotation risk but leaving probabilities unchanged.
- Mixing "will win the match" with "will advance" without clarification.
- Giving gambling certainty or encouraging staking decisions.

## Matchup Notes

When analyzing a favorite versus underdog:

- Ask whether the favorite can break a low block.
- Check set-piece quality on both sides.
- Look for transition risk if the favorite uses high fullbacks.
- Consider whether the underdog has pace for counters.
- Give special weight to first-goal scenarios; underdogs often need 0-0 deep into the match.
- Check whether the favorite's bench can change the game after 60 minutes or whether the underdog has only one realistic game state.

## Squad And Coach Checklist

When evidence is available, always cover:

- First-choice goalkeeper quality and reliability.
- Center-back pairing and whether either defender is vulnerable in space.
- Fullback width and whether it can be exposed behind the line.
- Midfield ball progression versus defensive cover.
- Primary scorer and creator, plus the best bench attacker.
- Best substitute defender or midfielder if the match becomes stateful.
- Coach's default shape, pressing trigger, and substitution habits.
- Coach history in tournament knockout pressure or must-not-lose games.
- Whether head-to-head history matches the current personnel and coach, or is too stale to matter.

When analyzing two strong teams:

- Separate control of midfield from chance creation.
- Compare goalkeeper and center-back error rates where evidence exists.
- Look at whether either coach is likely to rotate or protect players.
- Treat knockout extra time and penalties separately.

## Group-Stage Finale Checklist

Before making the pick:

- State each team's current points, goal difference, and qualification route when available.
- Identify whether each team needs a win, can accept a draw, is already through, or is already eliminated.
- Check whether the stronger team has reason to rotate, protect cards, manage minutes, or avoid injuries. If it rotates the goalkeeper-center-back-holding-midfielder spine, explicitly downgrade defensive reliability even if the bench attackers are strong.
- Check whether a weaker team must open up; that can raise both upset chance and favorite transition chances. If the weaker or eliminated team does not need standings points, still assess pride, young-star showcase incentives, coach pressure, and set-piece or transition weapons before downgrading motivation.
- Separate "more talented" from "more likely to play a full-strength, high-urgency match."
- If final lineups are not confirmed, make the pick conditional and keep probability bands wider.

## Backtesting Saved Predictions

When reviewing predictions in `pred/`:

- Count only completed matches.
- Report primary-outcome hit rate separately from scoreline hit rate.
- Treat an alternate scoreline hit as useful signal, but do not mark the primary pick correct if the win/draw/loss was wrong.
- Review calibration: a 53% favorite losing is not automatically a bad forecast, but a pattern of misses around the same hidden factor is a skill problem.
- For each miss, identify the most likely weighting error: incentives, lineup uncertainty, tactical matchup, finishing variance, set pieces, red cards, or stale evidence.
- Feed repeated errors back into future predictions as explicit probability adjustments.

## Final Answer Checks

Before answering:

- Confirm date/time in absolute terms.
- State whether the pick is for 90 minutes or advancement.
- Include citations for schedule and key evidence.
- Include probability ranges, not false precision.
- Check that likely scorelines and probability ranges are internally consistent.
- Check group incentives and rotation risk for group-stage matches.
- Include category scores and a total score comparison when technical detail is requested.
- Name the main counterargument.
