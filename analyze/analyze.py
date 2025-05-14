from data.ExtractData import ExtractData
data = ExtractData()


def analyze_data(start=2, end=4):
    amount = 1000
    bitcoin = 0
    trades = []
    for i in range(len(data)):
        row = data.iloc[i]
        if int(row["WeekDay"].item()) == start:
            bitcoin = amount / row["Open"].item()

        elif int(row["WeekDay"].item()) == end and bitcoin > 0:
            amount = bitcoin * row["Close"].item()

            trades.append({
                "date": row["Date"].item(),
                "amount": amount,
                "profit": amount - 1000
            })
            bitcoin = 0

    return trades, amount


def find_best_day():
    best_amount = 0
    best_pair = (0, 0)
    for i in range(7):
        for j in range(7):
            if j >= i:
                _, amount = analyze_data(start=i, end=j)
                if amount > best_amount:
                    best_amount = amount
                    best_pair = (i, j)

    return best_pair, best_amount

