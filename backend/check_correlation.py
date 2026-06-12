import pandas as pd

df = pd.read_csv(
    "../dataset/Vegetables_fruit_prices_with_climate_130000_2020_to_2025.csv",
    encoding="latin1",
    low_memory=False
)

print(df.head())
print("\nRows:", len(df))