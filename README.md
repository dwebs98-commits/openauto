# OpenAuto 🚗

OpenAuto is a free, open-source, local-first vehicle auction flip analyzer. It helps buyers estimate a maximum auction hammer bid, profit, return on invested cash, and repair-overrun exposure.

## Features (v0.1)
- Editable auction deal assumptions and maximum bid calculation
- Profit and ROI at a proposed bid
- Repair overrun sensitivity
- Session-based watchlist with CSV export
- No login, API key, or auction scraping required

## Quick start

Requires Python 3.10+.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
streamlit run app.py
```

## Formula

`Maximum hammer bid = expected resale - auction fees - repairs - transportation - other costs - target profit`

All inputs are estimates. Include any applicable taxes, title, holding, financing, and selling expenses in the cost fields. Check real auction fee schedules and title/registration rules before bidding. Auction URL is stored as text only; no automatic retrieval is performed.

## Privacy

The watchlist is held only in the current Streamlit session. Export CSV before closing the app. Do not upload confidential third-party case study data.

## Roadmap

- Persistent local SQLite watchlist
- CSV import and vehicle comparison
- Fee schedule configuration
- Comparable-sales data via authorized sources
- Tests and community contribution guide

## License

MIT. See LICENSE.
