import matplotlib.ticker as ticker
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("UTMB2025.csv")

df["time"] = pd.to_timedelta(df["time"])
df = df.loc[~df["time"].isna()]
print(df)

def hhmmss_formatter(x, pos):
    # x is in nanoseconds because matplotlib converts timedelta to float
    total_seconds = x / 1e9  # convert nanoseconds → seconds
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


fig, ax = plt.subplots(1, 3, figsize=(20, 10))
ax[0].plot(df["rank"], df["time"])
ax[0].yaxis.set_major_formatter(ticker.FuncFormatter(hhmmss_formatter))

ax[1].hist(df["time"].astype("int64"), bins=np.linspace(10**9*3600*18, 10**9*3600*46, 29))
ax[1].xaxis.set_major_formatter(ticker.FuncFormatter(hhmmss_formatter))

ax[2].scatter(df["time"].astype("int64"), df["index"])
ax[2].xaxis.set_major_formatter(ticker.FuncFormatter(hhmmss_formatter))

x = np.linspace(df["time"].astype("int64").min(), df["time"].astype("int64").max(), 100)
scale = (df["index"][0] * df["time"].astype("int64")[0])
print(1 / 1000 * scale)
y = 1 / x * scale

ax[2].plot(x, y, color="black")

plt.show()
