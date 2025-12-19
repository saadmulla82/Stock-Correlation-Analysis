# Stock Price Correlation — Saad's Mac (macOS)

This README is tailored specifically for running this project on Saad's Mac (macOS). Commands assume zsh and that Homebrew and Python 3.11+ are available.

## Quick Start (Saad's Mac)

1. Install or verify Homebrew and Python:

```bash
# Install Homebrew (if needed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3
brew install python
```

2. Create and activate a virtual environment from the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Run the main script from the project directory:

```bash
python stock_correlation_main.py
```

## What this does (concise)

- Loads historical daily closing prices from a CSV in the project root
- Calculates pairwise Pearson correlations
- Lists strongly correlated pairs (threshold default: 0.7)
- Saves the correlation matrix to `correlation_matrix.json`
- Shows a heatmap and a dual-line plot for a correlated pair

## Data expectations

- Input file: `stock_prices.csv`
- First column: `Date` (YYYY-MM-DD)
- Remaining columns: one stock symbol per column with daily closing prices

Example row:

```csv
Date,AAPL,MSFT,GOOGL
2024-01-01,150.25,320.50,125.75
```

## macOS-specific notes for Saad

- If matplotlib raises a display or backend error, ensure Xcode command-line tools are installed:

```bash
xcode-select --install
```

- If permissions or GUI issues occur, run inside the logged-in GUI session (not a headless SSH session).

- Use the included `.venv` for consistent dependencies; avoid installing packages globally.

## Troubleshooting

- Missing packages: `pip install -r requirements.txt`
- CSV formatting issues: ensure the `Date` column exists and price columns are numeric
- If the heatmap or plots do not show, try adding `matplotlib.use('TkAgg')` before imports or run in a GUI-enabled session

## Output

- `correlation_matrix.json` will be generated in the project root after a successful run

---

This file is intentionally minimal and specific to Saad's Mac environment. No personal names or external file paths are included.
