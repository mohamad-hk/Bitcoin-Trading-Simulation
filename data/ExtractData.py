import yfinance as yf


def ExtractData():
    data = yf.download("BTC-USD", start="2020-01-01", end="2024-12-31")
    data["Date"] = data.index
    data["WeekDay"] = data["Date"].dt.weekday
    return data
