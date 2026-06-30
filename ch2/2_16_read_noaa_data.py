import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/thomasnield/"
      "training-data-repository/refs/heads/main/TORNADO_TRX.csv")

print(df.info())
