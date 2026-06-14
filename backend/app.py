from flask import Flask, request, jsonify
import pandas as pd
import joblib
from flask_cors import CORS
from crop_recommender import CropRecommender
from weather_service import WeatherService
from ai_advisor import AIAdvisor
from decision_agent import DecisionAgent

app = Flask(__name__)
CORS(app)

# Load model and encoders
model = joblib.load("model.pkl")
region_encoder = joblib.load("region_encoder.pkl")
veg_encoder = joblib.load("veg_encoder.pkl")

# Initialize v2.0 components
crop_recommender = CropRecommender(model, region_encoder, veg_encoder)
ai_advisor = AIAdvisor()
decision_agent = DecisionAgent()

# ========================= V1.0 Routes =========================

@app.route("/")
def home():
    return jsonify({
        "message": "AgriMind AI Backend Running!",
        "version": "2.0",
        "features": [
            "Price Prediction (v1.0)",
            "Crop Recommendation (v2.0)",
            "Weather Integration (v2.0)",
            "AI Advisor (v2.0)",
            "Decision Support (v2.0)"
        ]
    })

@app.route("/predict", methods=["POST"])
def predict():
    """V1.0: Price prediction for specific crop"""
    try:
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
            "success": True,
            "crop": data.get("Vegetable"),
            "region": data.get("Region"),
            "predicted_price": round(float(prediction[0]), 2),
            "currency": "Rs"
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


# ========================= V2.0 Routes =========================

@app.route("/recommend-crops", methods=["POST"])
def recommend_crops():
    """V2.0: Get crop recommendations based on climate data"""
    try:
        data = request.json
        
        climate_data = {
            "Region": data.get("Region"),
            "Temperature": data.get("Temperature", 20),
            "Rainfall": data.get("Rainfall", 100),
            "Humidity": data.get("Humidity", 60),
            "CropYield": data.get("CropYield", 50)
        }
        
        recommendations = crop_recommender.get_recommendations(climate_data, top_n=5)
        
        return jsonify({
            "success": True,
            "region": data.get("Region"),
            "recommendations": recommendations
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


@app.route("/weather/<region>", methods=["GET"])
def get_weather(region):
    """V2.0: Get current weather and forecast"""
    try:
        current = WeatherService.get_current_weather(region)
        forecast = WeatherService.get_forecast(region, days=7)
        seasonal = WeatherService.get_seasonal_analysis(region)
        optimal_window = WeatherService.get_optimal_planting_window(region)
        
        if not current:
            return jsonify({
                "success": False, 
                "error": f"Region '{region}' not supported. Available regions: {list(WeatherService.REGION_COORDINATES.keys())}"
            }), 400
        
        return jsonify({
            "success": True,
            "region": region,
            "current_weather": current,
            "forecast": forecast.get("forecast") if forecast else [],
            "seasonal_analysis": seasonal,
            "planting_window": optimal_window
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


@app.route("/advisor", methods=["POST"])
def get_advisor():
    """V2.0: Get AI farming advisor recommendations"""
    try:
        data = request.json
        
        context = {
            "crop_recommendations": data.get("recommendations", []),
            "weather": data.get("weather", {}),
            "market_data": data.get("market_data", {})
        }
        
        # Set farmer profile if provided
        if data.get("farmer_profile"):
            profile = data.get("farmer_profile")
            ai_advisor.set_farmer_profile(
                farm_size=profile.get("farm_size"),
                location=profile.get("location"),
                preferences=profile.get("preferences"),
                constraints=profile.get("constraints")
            )
        
        advice = ai_advisor.get_advice(context)
        
        return jsonify({
            "success": True,
            "advice": advice
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


@app.route("/decision-support", methods=["POST"])
def get_decision_support():
    """V2.0: Get autonomous decision support analysis"""
    try:
        data = request.json
        
        climate_data = {
            "Region": data.get("Region"),
            "Temperature": data.get("Temperature", 20),
            "Rainfall": data.get("Rainfall", 100),
            "Humidity": data.get("Humidity", 60),
            "CropYield": data.get("CropYield", 50)
        }
        
        recommendations = crop_recommender.get_recommendations(climate_data, top_n=5)
        
        weather = {
            "temperature": data.get("Temperature", 20),
            "humidity": data.get("Humidity", 60),
            "precipitation": data.get("Rainfall", 100)
        }
        
        weather_forecast = WeatherService.get_forecast(data.get("Region"), days=7)
        
        analysis = decision_agent.analyze_scenarios(climate_data, recommendations, weather_forecast or {})
        decision_summary = decision_agent.get_decision_summary(
            analysis.get("scenarios", {}),
            recommendations
        )
        
        return jsonify({
            "success": True,
            "analysis": analysis,
            "decision_summary": decision_summary
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


@app.route("/comprehensive-analysis", methods=["POST"])
def comprehensive_analysis():
    """V2.0: Complete analysis combining all features"""
    try:
        data = request.json
        region = data.get("Region")
        
        climate_data = {
            "Region": region,
            "Temperature": data.get("Temperature", 20),
            "Rainfall": data.get("Rainfall", 100),
            "Humidity": data.get("Humidity", 60),
            "CropYield": data.get("CropYield", 50)
        }
        
        # Get recommendations
        recommendations = crop_recommender.get_recommendations(climate_data, top_n=5)
        
        # Get weather data
        weather = WeatherService.get_current_weather(region)
        seasonal = WeatherService.get_seasonal_analysis(region)
        forecast = WeatherService.get_forecast(region, days=7)
        optimal_window = WeatherService.get_optimal_planting_window(region)
        
        weather_data = {
            "temperature": weather.get("temperature") if weather else 20,
            "humidity": weather.get("humidity") if weather else 60,
            "precipitation": weather.get("precipitation") if weather else 0
        }
        
        # Get advisor recommendations
        context = {
            "crop_recommendations": recommendations,
            "weather": weather_data,
            "market_data": {}
        }
        advice = ai_advisor.get_advice(context)
        
        # Get decision support
        analysis = decision_agent.analyze_scenarios(climate_data, recommendations, forecast or {})
        decision_summary = decision_agent.get_decision_summary(
            analysis.get("scenarios", {}),
            recommendations
        )
        
        return jsonify({
            "success": True,
            "region": region,
            "climate_data": climate_data,
            "crop_recommendations": recommendations,
            "weather_data": {
                "current": weather,
                "seasonal": seasonal,
                "forecast": forecast.get("forecast") if forecast else [],
                "planting_window": optimal_window
            },
            "ai_advisor": advice,
            "decision_support": {
                "scenarios": analysis.get("scenarios"),
                "decision_matrix": analysis.get("decision_matrix"),
                "contingency_plans": analysis.get("contingency_plans"),
                "sensitivity_analysis": analysis.get("sensitivity_analysis"),
                "summary": decision_summary
            }
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "AgriMind AI v2.0",
        "timestamp": pd.Timestamp.now().isoformat()
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)