# Market Decision Policy

Use this policy after probabilities are fitted and before publishing any pick. Evidence quality and directional edge are separate questions: clean, fresh data can still describe a close match with no usable selection.

## Market-Level Abstention

Keep all diagnostic probabilities, but publish a market pick only when both the top-probability floor and the gap to the runner-up pass:

| Market | Minimum top probability | Minimum gap |
| --- | ---: | ---: |
| 90-minute 1X2 | 45% | 6 percentage points |
| Qualification | 60% | 20 percentage points |
| Totals | 56% | 12 percentage points |
| BTTS | 56% | 12 percentage points |
| Asian handicap | 56% | 12 percentage points |

These are conservative publication gates, not fitted model weights. They reduce forced selections in near-even matches without altering the underlying probability distribution. Change them only after grouped chronological validation on archived, replayable forecasts.

Use these stable reason ids:

- `low_top_probability`: the most likely selection is below the market floor.
- `narrow_probability_gap`: the two leading selections are too close.
- `insufficient_market_edge`: no supported market passes its publication gate.

## Response Rules

- Say `观望` or `no forecast edge` for each rejected market.
- Continue to show its probabilities as diagnostics, clearly labeled non-actionable.
- Never restore a rejected pick through narrative judgment, team reputation, public betting share, or a guessed bookmaker motive.
- A score ladder is a scenario distribution, not an exact-score recommendation.
- If one market is rejected, other independently assessed markets may remain actionable.
- If every supported market is rejected, the whole forecast is non-actionable even when source confidence is high.

## Historical And Legacy Reviews

Chat-only predictions without the original structured input, timestamped quotes, event id, and input fingerprint are audit-only. They may reveal workflow mistakes and justify stricter structural safeguards, but they must not enter calibration or evolution data and must not change model weights.

