from analyze.analyze import analyze_data, find_best_day
import matplotlib.pyplot as plt
import pandas as pd

from utils.find_day import find_name_of_day


def draw_chart():
    results, amount = analyze_data()
    df = pd.DataFrame(results)
    df = df.sort_values("date")

    best_pair, best_amount = find_best_day()
    number_buy_day, number_sell_day = best_pair
    buy_day = find_name_of_day(number_buy_day)
    sell_day = find_name_of_day(number_sell_day)

    plt.plot(df["date"], df["amount"], label="Total investment", color="blue")
    plt.axhline(1000, color='gray', linestyle='--', label="Initial investment")

    text = f"Maximum profit: If you buy on {buy_day} (start index={number_buy_day}), sell on {sell_day} (end index={number_sell_day}) → your final investment was: ${best_amount:,.2f}"
    plt.figtext(0.5, 0.01, text, ha="center")

    plt.xlabel("Date")
    plt.ylabel("Investment Value")
    plt.title("Profit and loss chart in Bitcoin")
    plt.legend()
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.show()
