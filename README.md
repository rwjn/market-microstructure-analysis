# Market Microstructure Analysis

This project was completed as part of coursework for the Economics with Data Science MSc. The project received a distinction.

The analysis processes 6 months of intraday market activity using Python, covering data extraction and filtering, market depth visualisation, and block order detection with econometric analysis of market impact — drawing on financial market microstructure theory including price discovery, liquidity measurement, and the relationship between order flow and price formation.

## Project Structure

```
├── analysis/             # Source code
│   ├── EwPY2473787.ipynb # Master Jupyter notebook
│   ├── t1_*.py           # Task 1: Data extraction & summarisation
│   ├── t2_*.py           # Task 2: Market depth visualisation
│   └── t3_*.py           # Task 3: Block order detection & analysis
└── Outputs/              # Directory for exported results
```

## Tasks

### Task 1 — Data Extraction & Summarisation
- Filters trade tape and LOB data by user-specified date and time ranges
- Outputs summary or verbatim views of trade records
- Optionally exports results to CSV

### Task 2 — Market Depth Visualisation
- **Chart 1**: Static snapshot of the order book at a chosen time — plots bid/ask depth curves with mid and micro price overlays
- **Chart 2**: Animated evolution of market depth over a time range using `matplotlib.animation`
- Computes:
  - **Mid price**: `(best_bid + best_ask) / 2`
  - **Micro price**: volume-weighted price using best bid/ask quantities

### Task 3 — Block Order Detection
- Identifies block orders meeting all of:
  - Both sides of the book have quantity > 1
  - One side is at least 10× the counterparty quantity
  - The order is larger than the previous order on the same side
- Calculates pre/post-block spread, mid price, micro price, and counterparty response time
- Visualises block order impact on price discovery

## Data

The analysis uses two CSV file types per trading day:

| Type | Naming Pattern | Description |
|------|---------------|-------------|
| Tapes | `UoB_Set01_YYYY-MM-DDtapes.csv` | Trade/cancellation events (`TRADE`, `CAN`) with time, order ID, direction, price, quantity |
| LOBs | `UoB_Set01_YYYY-MM-DDLOBs.csv` | Limit order book snapshots with nested bid/ask price-quantity pairs |

Data files are not included in this repository (~800 MB across ~250 CSV files). Place them in a `DataSet01/` directory at the project root.

## Setup

```bash
# Install dependencies
pip install pandas numpy regex matplotlib statsmodels patsy
```

Open `EWPY2473787/EwPY2473787.ipynb` in Jupyter and run the cells in order.

## Dependencies

| Library | Purpose |
|---------|---------|
| `pandas` | Data processing |
| `numpy` | Numerical operations |
| `regex` | LOB string parsing |
| `matplotlib` | Static and animated charts |
| `statsmodels` / `patsy` | Regression and statistical analysis |
