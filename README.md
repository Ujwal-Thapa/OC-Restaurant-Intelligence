# OC Restaurant Intelligence

> An AI-powered market entry analytics tool for first-time restaurant operators in Orange County, California.

**Status:** 🚧 In Progress (Week 1 of 8)  
**Timeline:** April 27 – June 15, 2026  
**Author:** Ujwal Thapa, DBA Candidate in Business Intelligence & Data Analytics

---

## The Question

> *For a first-time restaurant operator in Orange County, which cuisine categories show the strongest growth signals over the past 24 months, and which underserved zip codes represent the best market entry opportunity?*

This project answers that question by integrating four public data sources into a MySQL database, applying R-based statistical forecasting, and embedding six Claude API use cases throughout the analytical pipeline.

---

## Why This Project Exists

Restaurants in California fail at some of the highest rates in the United States. Many of those failures trace back to decisions made before the restaurant ever opened — the wrong cuisine in the wrong neighborhood, underestimated competition, or demographic mismatch.

Professional consulting engagements to answer these questions typically cost $10,000–$15,000. This project builds the same class of analysis using public data, open-source tooling, and a single AI integration partner — accessible to any first-time operator.

---

## Key Features

- **Clean cuisine taxonomy** — Claude standardizes Yelp's messy category system into 15 clear cuisines
- **Natural-language-to-SQL chatbot** — Ask questions in plain English, get database answers
- **Review sentiment analysis** — 5,000 Yelp reviews scored across 5 dimensions (food, service, price, ambiance, value)
- **Time series forecasting** — R-based ARIMA models project category growth over 12 months
- **AI-generated executive summaries** — Auto-written market summaries for any zip + cuisine combo
- **Excel operator dashboard** — Interactive scenario modeling with filters

---

## Tech Stack

| Layer | Tool |
|---|---|
| Data extraction | Python (Pandas, Requests) |
| Database | MySQL |
| Statistical analysis | R (forecast, tseries) |
| AI layer | Claude API (Sonnet 4.6) |
| Delivery | Excel dashboard |
| Version control | Git, GitHub |

---

## Data Sources

| Source | Provides | Access |
|---|---|---|
| Yelp Fusion API | Restaurants, categories, ratings, reviews | Free API key |
| BLS QCEW | County-level food service employment | Free API key |
| US Census ACS | Demographics by zip code | Free API key |
| CA Open Data Portal | Health inspection records | Free CSV download |

---

## Project Structure
```
Claude Project/
├── data/
│   ├── raw/          # Original API pulls (untouched)
│   └── processed/    # Cleaned datasets
├── scripts/
│   ├── python/       # API calls, Claude integrations
│   └── r/            # Statistical analysis, forecasting
├── sql/              # Database schema and queries
├── output/           # Final dashboards and charts
├── docs/             # Methodology, write-ups, prompt archive
├── notebooks/        # Exploratory analysis
└── README.md
```

---

## Roadmap

- [x] **Week 1: Setup & Scope** — APIs, environment, repo, first test calls
- [ ] **Week 2: Data Collection + Cuisine Classification** — Pull OC restaurants, Claude classifies cuisines
- [ ] **Week 3: Cleaning + Address Normalization** — Build MySQL schema, Claude normalizes addresses
- [ ] **Week 4: SQL Exploration + NL→SQL Chatbot** — Competitive analysis, build natural-language query tool
- [ ] **Week 5: Statistical Analysis + Sentiment** — R forecasting, review sentiment scoring
- [ ] **Week 6: Dashboard + Auto Summaries** — Excel dashboard with AI-generated summaries
- [ ] **Week 7: Write-up + Methodology** — Final report, AI methodology documentation
- [ ] **Week 8: Polish + Publish** — GitHub cleanup, LinkedIn post, video walkthrough

---

## AI Integration

This project uses Claude (Anthropic's Sonnet 4.6) for six distinct use cases:

1. **Cuisine classification** — Mapping Yelp's messy taxonomy to a clean 15-category taxonomy
2. **Address normalization** — Structured JSON extraction from inconsistent address formats
3. **Natural-language-to-SQL** — Plain-English questions converted to database queries
4. **Review sentiment analysis** — Multi-dimensional scoring of customer reviews
5. **Executive summary generation** — Auto-written market summaries per zip + cuisine
6. **Methodology documentation** — Transparent write-up of prompts, iterations, and limitations

Full prompt archive and methodology documented in `/docs`.

---

## About the Author

**Ujwal Thapa** is a DBA candidate at Westcliff University specializing in Business Intelligence and Data Analytics. Previously analyzed digital transaction data across POS, QR, and mobile banking channels at NIC Asia Bank in Kathmandu, Nepal, building executive dashboards that informed decisions on payment infrastructure, workforce efficiency, and product performance.

- **LinkedIn:** [linkedin.com/in/ujwalthapa97](https://linkedin.com/in/ujwalthapa97)
- **Email:** ujwal.thapa97@gmail.com
- **GitHub:** [github.com/Ujwal-Thapa](https://github.com/Ujwal-Thapa)

---

## License

MIT License — see LICENSE file for details.