import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("py-technologies.csv")
df = pd.DataFrame(data).sort_values("Value", ascending=False)

colors = ["red" if value > df["Value"].mean() else "blue" for value in df["Value"]]

plt.figure(figsize=(10, 6))
plt.bar(df["Technology"], df["Value"], color=colors, width=0.4)
plt.xticks(rotation=90)
plt.show()
