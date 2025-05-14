from analyze.analyze import analyze_data
import matplotlib.pyplot as plt
import pandas as pd

results = analyze_data()
df = pd.DataFrame(results)
df = df.sort_values("date")

plt.plot(df["date"], df["amount"], label="Total Amount", color="blue")
plt.axhline(1000, color='gray', linestyle='--', label="Initial Investment")
plt.legend()
plt.show()

