# Vehicle comparison: proposed first feature

## Scope
Compare 2–5 manually entered auction scenarios from the existing session watchlist. Preserve the current single-vehicle analyzer and CSV export. No account, scraping, external API, or persistent storage in the first version.

## Experience
1. Add scenarios using the existing inputs and watchlist button.
2. Select 2–5 scenarios using unique session IDs, so duplicate year/make/model entries remain distinct.
3. Show vehicle, mileage, title status and listing URL next to bid, resale, fees, repairs, transport, other costs and target profit.
4. Compare maximum bid, total invested cash, estimated profit, ROI, room under maximum bid and profit after a shared repair overrun.
5. Let the user sort by profit, ROI, or maximum bid; show title differences as context without inventing numerical risk scores.
6. Export selected scenarios and calculated metrics to CSV. Explain that the watchlist is session-only.

## Implementation
Reuse Deal for all calculations. Extend scenario records with stable IDs and calculate comparison metrics from stored assumptions. Keep ranking and metric helpers separate from Streamlit. Handle zero investment, negative maximum bids, ties, duplicate labels, fewer than two selections and deletion/clearing without stale selections. Clearly label all values as user estimates.

## Acceptance checks
- The existing example still returns $6,100 maximum bid, $2,700 profit and 39.7% ROI at $4,900.
- Two scenarios with different costs produce the same results as independent Deal calculations.
- Repair overrun lowers profit by the entered amount and changes invested cash consistently if stress ROI is displayed.
- Selecting, sorting, clearing and CSV export work; empty and single-scenario states offer clear guidance.
- Existing analyzer and watchlist behavior remains intact.

## Later
CSV import with validation, then optional local SQLite persistence. Authorized comparable-sales sources can be evaluated separately.
