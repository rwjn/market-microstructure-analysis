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

### Task 3 — Block Order Detection & Market Impact Analysis

**Block order identification** follows Church & Cliff (2019): an order qualifies as a block if both sides of the book have quantity > 1, one side is at least 10× the counterparty quantity, and the order is larger than the previous order on the same side. The relative rather than absolute size criterion reflects that market impact depends on order size relative to available liquidity, not raw quantity.

**Market impact timing** uses the divergence between mid price `(best_bid + best_ask) / 2` and micro price (quantity-weighted best bid/ask) to define the impact window. A block order creates a quantity imbalance that pulls the micro price away from the mid price; the window closes when the mid/micro spread returns to its pre-block level, avoiding an arbitrary fixed time horizon.

**Regression analysis** estimates the relationship between block order size and the magnitude of subsequent price changes:
- **OLS** — baseline model with standard and clustered (by day) standard errors. Block order size is significant at the 99% level; a one-unit increase in quantity is associated with a 0.30 increase in subsequent price change
- **Log-log OLS** — a 1% increase in block size leads to a ~1.7% increase in price change magnitude, suggesting an elastic response
- **Extended OLS** — adding LOB liquidity (best bid/ask spread, following Schroeter 2014) and time-to-equilibrium improves R² to 0.176; both variables significant at the 99% level
- **Quantile regression** — addresses non-normal residuals; reveals the block size–price impact relationship varies significantly across the distribution, with coefficients and R² differing notably across quantiles

**Robustness checks**: White test (homoskedastic — robust SE not required), Durbin-Watson test (no significant autocorrelation), Jarque-Bera test (non-normal residuals across all models — motivating the quantile regression approach). Clustered standard errors increase slightly from 0.025 to 0.035 but leave coefficients and significance unchanged.

**Key finding**: block order size is a statistically significant predictor of price impact, but explanatory power remains low (adjusted R² ~0.03–0.18), consistent with Abergel et al. (2015) who find LOB regression coefficients are unstable over time. The causal interpretation is limited without information on trader behaviour.

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

Open `analysis/EwPY2473787.ipynb` in Jupyter and run the cells in order.

## Dependencies

| Library | Purpose |
|---------|---------|
| `pandas` | Data processing |
| `numpy` | Numerical operations |
| `regex` | LOB string parsing |
| `matplotlib` | Static and animated charts |
| `statsmodels` / `patsy` | Regression and statistical analysis |
