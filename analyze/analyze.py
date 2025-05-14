from data.ExtractData import ExtractData

data = ExtractData()


def analyze_data():
    amount = 1000
    bitcoin = 0
    trades = []
    for i in range(len(data)):
        row = data.iloc[i]
        if int(row["WeekDay"].item()) == 2:
            bitcoin = amount / row["Open"].item()

        elif int(row["WeekDay"].item()) == 4:
            amount = bitcoin * row["Close"].item()
            trades.append({
                "date": row["Date"].item(),
                "amount": amount
            })
            bitcoin = 0

    return trades
