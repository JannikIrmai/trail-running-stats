import requests
import pandas as pd
import time

from credentials import EMAIL, PASSWORD


# ---------------------------
# CONFIG
# ---------------------------
RACE_SLUG = "142.hokautmbmont-blancutmb.2025"
OUTPUT_CSV = "UTMB2025.csv"
PAGE_SIZE = 100   # UTMB uses offset-based paging

BASE_URL = f"https://api.utmb.world/races/{RACE_SLUG}/results"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json",
    "Referer": "https://utmb.world/",
    "Origin": "https://utmb.world",
}

offset = 0
all_results = []

while True:
    params = {
        "lang": "en",
        "offset": offset,
        "gender": ""
    }

    r = requests.get(BASE_URL, headers=headers, params=params)
    r.raise_for_status()

    data = r.json()

    # Results are in a list directly
    results = data.get("results", [])
    if not results:
        break

    all_results.extend(results)
    offset += len(results)

    print(f"Fetched {len(results)} (total {len(all_results)})")
    time.sleep(0.3)  # be polite

print(f"\nDownloaded {len(all_results)} total results")

# ---------------------------
# SAVE
# ---------------------------
df = pd.json_normalize(all_results)
df.to_csv(OUTPUT_CSV, index=False)

print(f"Saved to {OUTPUT_CSV}")
