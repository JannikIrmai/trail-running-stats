import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker


def main():
    df = pd.read_csv("utmb-index-races.csv")

    df["Winner Time"] = pd.to_timedelta(df["Winner Time"])
    perfect_time = df["Winner Time"] * df["Winner Index"] / 1000
    perfect_pace = perfect_time / df["Distance"]

    fig, ax = plt.subplots()
    sc = ax.scatter(df["Distance"], df["Elevation Gain"], c=perfect_pace)
    cbar = plt.colorbar(sc)

    def format_mmss(x, pos):
        x = x * 1e-9
        total_seconds = int(x)
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

    cbar.ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_mmss))
    cbar.set_label("Pace per KM (MM:SS)")

    plt.show()

if __name__ == "__main__":
    main()