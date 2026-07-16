# Backtesting Framework

Use this reference for completed-match reviews of saved predictions. Read `SKILL.md` first. Load `prediction-framework.md` only when the review also changes forecasting rules.

## Contents

- Prediction snapshot and evidence integrity
- Result verification
- Outcome, scoreline, and probability scoring
- Diagnostic attribution
- Repeated-error threshold
- Review output checklist

## Prediction Snapshot

Treat every file under `pred/` as an immutable pre-match ledger during review. Never edit, rewrite, append to, rename, or create review artifacts in that directory.

1. Read the saved file before checking the result.
2. Record forecast creation time, evidence cutoff, forecast status, lineup status, and version history.
3. Score the latest version created before kickoff as the primary forecast. If a confirmed-lineup final exists, compare the initial snapshot separately to measure the value of late information.
4. If only a `赛前初版` exists and no later user request or scheduled update occurred, treat it as the delivered forecast. Do not call the absence of a confirmed-lineup final an execution violation.
5. If confirmed lineups were already public before the recorded evidence cutoff but the file treated them as unknown, classify that as stale evidence. If they appeared only later, classify the forecast as conditional or snapshot-limited instead.
6. Legacy files without lifecycle metadata remain valid pre-match records. Infer timing only from explicit text and file history; state uncertainty rather than inventing a final status.

## Result Verification

- Review only completed matches.
- Verify the final score and whether it is a 90-minute, extra-time, or shootout result from an official source or established match center.
- Read at least one match report or complete live-text source before attributing causes.
- Capture the goal timeline, red cards, penalties, material injuries, confirmed formations, substitution timing, shots, shots on target, possession, corners, and xG when reliable.
- Keep 90-minute result and advancement separate throughout the review.

## Scoring Layers

Report these independently:

1. **Primary 90-minute outcome:** hit or miss based on the headline probability leader or explicit draw-first call.
2. **Likely scoreline:** hit only if the actual score was one of the one or two headline scorelines. A score listed only in a long distribution or failure path is a recognized secondary route, not a likely-score hit.
3. **Advancement:** score separately for knockout matches.
4. **Goal-shape:** compare both-teams-to-score, clean-sheet, total-goal core range, and high-event tail.
5. **Probability quality:** use normalized midpoint probabilities, Brier score, log loss, and market comparison when available.
6. **Evidence process:** judge only information available by the recorded cutoff.

An outcome miss is not automatically a probability failure. A result assigned 25%-35% is a normal realized branch unless repeated comparable forecasts show systematic underpricing or the evidence named a route that the table failed to represent.

## Quantitative Scoring

Convert each 90-minute probability range to its midpoint. Normalize the three midpoints to sum to 1:

`p_i = midpoint_i / sum(midpoints)`

For actual outcome indicators `y_i` in `{0, 1}`:

- Three-way Brier score: `sum((p_i - y_i)^2)`. Lower is better; 0 is perfect.
- Log loss: `-ln(p_actual)`. Lower is better. Never replace a zero probability with certainty; flag the forecast as structurally invalid and use a small documented floor only for aggregate computation.
- Market comparison: when a liquid pre-match 90-minute market was saved, normalize its implied probabilities and compute the same scores. Compare model and market on the same result definition and timestamp class.

For one match, report the numbers descriptively. Do not label calibration good or bad from one observation. For aggregates, report mean Brier, mean log loss, outcome hit rate, likely-score hit rate, and results by probability band.

## Diagnostic Attribution

Choose the smallest supported set of causes; do not explain every miss with every available category.

- **Forecast lifecycle:** stale evidence, unresolved conditional branch, or no later final snapshot.
- **Lineup translation:** confirmed central overload, wide isolation, starter fitness, or defensive-spine change did not reach the probability table.
- **Game-state transition:** the model missed protection behavior, outlet removal, comeback substitutions, sustained late pressure, or post-concession volatility.
- **Evidence-to-probability:** the actual winning route was named but left mainly in prose, the draw bucket, or a low tail.
- **Chance-quality error:** territorial control or shot volume was mistaken for big-chance creation, or low volume hid elite finishing quality.
- **Event variance:** finishing, goalkeeper errors, deflections, isolated set pieces, penalties, or cards not supported as recurring pre-match risks.
- **Advancement leakage:** extra-time depth, penalty quality, or goalkeeper shootout reputation inflated a 90-minute win call.

Use these specific review rules:

- If a likely scoreline hits but the headline outcome misses, classify a headline/probability-ordering error rather than a full match-shape miss.
- If the exact score appears only in a failure path or long score distribution, credit route recognition but keep the likely-score result as a miss.
- If advancement is right after a 90-minute draw, audit low-block discipline, goalkeeper quality, and whether advancement strength leaked into regulation time.
- If a favorite wins narrowly despite territorial dominance, audit control versus chance volume and move future score ordering toward 1-0/2-0 where supported.
- If a team loses after leading, compare the saved game-state matrix with actual outlet retention, protective substitutions, opponent attacking changes, and minutes 75-90 pressure.
- If total goals exceed the core range, audit cards, penalties, forced chasing, high-conversion attackers, and punch-underdog routes before changing the primary outcome model.

## Repeated-Error Threshold

Do not create a permanent numerical adjustment from one match.

Promote a lesson into the forecasting framework only when at least one condition holds:

1. The same directional error appears in at least three genuinely comparable matches.
2. An aggregate of at least ten completed forecasts is materially worse than the saved market baseline on mean Brier or log loss.
3. A deterministic process failure is independently reproducible, such as using lineups published before the evidence cutoff as if they were unavailable.

Before adding a fixed adjustment, define the comparison class, avoid overlapping causes, and backtest the proposed rule against earlier saved predictions. Prefer a new checklist gate over a fixed percentage when the evidence is tactical and context-dependent.

## Review Output

Return the review in the conversation unless the user explicitly requests a separate file outside `pred/`.

Include:

- Actual 90-minute result and advancement result
- Forecast version and information cutoff
- Primary outcome, likely-score, advancement, and goal-shape results
- Normalized probabilities, Brier score, and log loss
- Market comparison when the saved file contains a comparable market snapshot
- What the forecast got right
- The one to three strongest causes of error
- Whether the issue is single-match variance, a conditional snapshot limitation, or a repeated pattern
- A future adjustment only when the repeated-error threshold is met; otherwise record a hypothesis to monitor

