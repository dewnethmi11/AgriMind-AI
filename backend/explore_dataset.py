import pandas as pd

# Load dataset
df = pd.read_csv(
    "../dataset/Vegetables_fruit_prices_with_climate_130000_2020_to_2025.csv",
    encoding="latin1"
)

print("===================================")
print("DATASET SHAPE")
print("===================================")
print(df.shape)

print("\n===================================")
print("COLUMN NAMES")
print("===================================")
print(df.columns)

print("\n===================================")
print("FIRST 5 ROWS")
print("===================================")
print(df.head())

print("\n===================================")
print("MISSING VALUES")
print("===================================")
print(df.isnull().sum())

print("\n===================================")
print("NUMBER OF REGIONS")
print("===================================")
print(df["Region"].nunique())

print("\n===================================")
print("NUMBER OF VEGETABLES")
print("===================================")
print(df["vegitable_Commodity"].nunique())

print("\n===================================")
print("VEGETABLE LIST")
print("===================================")
print(df["vegitable_Commodity"].unique())