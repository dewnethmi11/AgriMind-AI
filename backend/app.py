from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and encoders
model = joblib.load("model.pkl")
region_encoder = joblib.load("region_encoder.pkl")
veg_encoder = joblib.load("veg_encoder.pkl")

@app.route("/")
def home():
    return "AgriMind AI Backend Running!"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    region = region_encoder.transform([data["Region"]])[0]
    vegetable = veg_encoder.transform([data["Vegetable"]])[0]

    features = pd.DataFrame([{
        "Region": region,
        "Temperature (°C)": data["Temperature"],
        "Rainfall (mm)": data["Rainfall"],
        "Humidity (%)": data["Humidity"],
        "Crop Yield Impact Score": data["CropYield"],
        "vegitable_Commodity": vegetable
    }])

    prediction = model.predict(features)

    return jsonify({
        "predicted_price": round(float(prediction[0]), 2)
    })

if __name__ == "__main__":
    app.run(debug=True)