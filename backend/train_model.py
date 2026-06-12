import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load dataset
df = pd.read_csv(
    "../dataset/Vegetables_fruit_prices_with_climate_130000_2020_to_2025.csv",
    encoding="latin1",
    low_memory=False
)

# Convert Crop Yield Impact Score to numeric
df["Crop Yield Impact Score"] = pd.to_numeric(
    df["Crop Yield Impact Score"],
    errors="coerce"
)

# Remove rows with invalid values
df = df.dropna()

# Encode Region
region_encoder = LabelEncoder()
df["Region"] = region_encoder.fit_transform(df["Region"])

# Encode Vegetable
veg_encoder = LabelEncoder()
df["vegitable_Commodity"] = veg_encoder.fit_transform(
    df["vegitable_Commodity"]
)

joblib.dump(region_encoder, "region_encoder.pkl")
joblib.dump(veg_encoder, "veg_encoder.pkl")

# Features
X = df[
    [
        "Region",
        "Temperature (°C)",
        "Rainfall (mm)",
        "Humidity (%)",
        "Crop Yield Impact Score",
        "vegitable_Commodity"
    ]
]

# Target
y = df["vegitable_Price per Unit (LKR/kg)"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

print(X.columns)

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nModel Performance")
print("------------------")
print("MAE:", round(mae, 2))
print("R2 Score:", round(r2, 4))

# Save model
joblib.dump(model, "model.pkl")

print("\nModel saved as model.pkl")