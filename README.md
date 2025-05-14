
# Bitcoin Trading Simulation

This project simulates a Bitcoin investment strategy:  
📌 **Buy BTC on a specific weekday using the Open price**  
📌 **Sell all BTC on the same or a later weekday using the Close price**  
The initial investment capital is fixed at **1,000 USD**. The simulation covers the period from **2020-01-01 to 2024-12-31** and visualizes performance and profitability.

---

## Project Structure

```
.
├── main.py                      # Entry point – runs the chart
├── analyze/
│   └── analyze.py               # Investment simulation and best-day analysis
├── data/
│   └── ExtractData.py           # Downloads historical BTC data with weekdays
├── utils/
│   └── find_day.py              # Maps weekday index (0–6) to weekday names
├── visualize/
│   └── trading_chart.py         # Draws chart and shows best buy/sell pair
├── Figure_1.png                 # Output chart image
└── README.md                    # Project documentation
```

---

## Strategy Summary

- **Initial Capital**: 1,000 USD (fixed at the start of the simulation)
- **Data Range**: January 1, 2020 – December 31, 2024
- **Default Buy Day**: Wednesday (weekday index `2`)
- **Default Sell Day**: Friday (weekday index `4`)
- Weekly trading with capital update after each sell

These default days can be changed by modifying the parameters in the `analyze_data(start, end)` function.

---

## Features

- Simulates weekly BTC investment
- Tracks capital growth week-by-week
- Identifies the **most profitable weekday combination**
- Visualizes investment performance in a time-series chart

---

## Best Days Finder

The tool evaluates all 49 weekday combinations (buy on one day, sell on the same or a later day) and reports the one with the **highest return**.

Example output:
> If you bought on **Monday** and sold on **Monday**, your final capital would be **$X,XXX.XX**

This result is annotated on the chart.

---

## Requirements

Install necessary packages:

```bash
pip install yfinance matplotlib pandas
```

---

## How to Run

To run the project, simply execute the `main.py` script:

## Output

The output chart (`Figure_1.png`) displays:
- Investment value trend from 2020 to 2024
- Horizontal line for initial capital ($1,000)
- Final amount and best weekday pair
