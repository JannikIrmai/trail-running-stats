import matplotlib.ticker as ticker
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("utmb_race_results.csv")

df["time"] = pd.to_timedelta(df["time"])

print(df["time"])

def hhmmss_formatter(x, pos):
    # x is in nanoseconds because matplotlib converts timedelta to float
    total_seconds = x / 1e9  # convert nanoseconds → seconds
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


fig, ax = plt.subplots(1, 2)
ax[0].plot(df["rank"], df["time"])
ax[0].yaxis.set_major_formatter(ticker.FuncFormatter(hhmmss_formatter))

times = df["time"].dropna().view("int64")
ax[1].hist(times, bins=np.linspace(10**9*3600*20, 10**9*3600*46, 27))
ax[1].xaxis.set_major_formatter(ticker.FuncFormatter(hhmmss_formatter))

plt.show()
