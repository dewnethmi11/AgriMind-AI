import pandas as pd
import joblib
from typing import List, Dict
import numpy as np

class CropRecommender:
    """
    Recommends profitable crops based on price predictions and yield data.
    Analyzes climate conditions to suggest the best crop to cultivate.
    """
    
    def __init__(self, model, region_encoder, veg_encoder, crop_data_path=None):
        self.model = model
        self.region_encoder = region_encoder
        self.veg_encoder = veg_encoder
        self.crops = ['Tomato', 'Potato', 'Carrot', 'Onion', 'Cabbage', 'Lettuce', 'Broccoli']
        
        # Sample crop profile data (in production, load from database)
        self.crop_profiles = {
            'Tomato': {'base_yield': 45, 'temp_optimal': 25, 'rainfall_optimal': 600, 'market_demand': 0.9},
            'Potato': {'base_yield': 40, 'temp_optimal': 18, 'rainfall_optimal': 500, 'market_demand': 0.85},
            'Carrot': {'base_yield': 35, 'temp_optimal': 16, 'rainfall_optimal': 400, 'market_demand': 0.8},
            'Onion': {'base_yield': 30, 'temp_optimal': 20, 'rainfall_optimal': 450, 'market_demand': 0.95},
            'Cabbage': {'base_yield': 50, 'temp_optimal': 18, 'rainfall_optimal': 500, 'market_demand': 0.7},
            'Lettuce': {'base_yield': 25, 'temp_optimal': 15, 'rainfall_optimal': 350, 'market_demand': 0.75},
            'Broccoli': {'base_yield': 20, 'temp_optimal': 18, 'rainfall_optimal': 450, 'market_demand': 0.65},
        }
    
    def predict_crop_prices(self, climate_data: Dict) -> Dict[str, float]:
        """
        Predict prices for all crops given climate conditions.
        
        Args:
            climate_data: Dict with Region, Temperature, Rainfall, Humidity, CropYield
            
        Returns:
            Dict with crop names and predicted prices
        """
        prices = {}
        try:
            region_encoded = self.region_encoder.transform([climate_data['Region']])[0]
            
            for crop in self.crops:
                try:
                    veg_encoded = self.veg_encoder.transform([crop])[0]
                    
                    features = pd.DataFrame([{
                        "Region": region_encoded,
                        "Temperature (°C)": climate_data["Temperature"],
                        "Rainfall (mm)": climate_data["Rainfall"],
                        "Humidity (%)": climate_data["Humidity"],
                        "Crop Yield Impact Score": climate_data["CropYield"],
                        "vegitable_Commodity": veg_encoded
                    }])
                    
                    price = float(self.model.predict(features)[0])
                    prices[crop] = max(0, price)  # Ensure non-negative
                except:
                    prices[crop] = 0
        except Exception as e:
            print(f"Error predicting prices: {e}")
        
        return prices
    
    def calculate_yield_score(self, climate_data: Dict, crop: str) -> float:
        """Calculate how suitable climate is for a specific crop."""
        if crop not in self.crop_profiles:
            return 0
        
        profile = self.crop_profiles[crop]
        temp = climate_data["Temperature"]
        rainfall = climate_data["Rainfall"]
        
        # Calculate temperature fit (±5°C is optimal)
        temp_diff = abs(temp - profile['temp_optimal'])
        temp_score = max(0, 100 - (temp_diff * 5))
        
        # Calculate rainfall fit (±100mm is optimal)
        rainfall_diff = abs(rainfall - profile['rainfall_optimal'])
        rainfall_score = max(0, 100 - (rainfall_diff * 0.2))
        
        # Combined score
        yield_score = (temp_score * 0.6 + rainfall_score * 0.4) / 100
        return yield_score
    
    def get_recommendations(self, climate_data: Dict, top_n: int = 5) -> List[Dict]:
        """
        Get top crop recommendations based on climate and market data.
        
        Args:
            climate_data: Dict with climate parameters
            top_n: Number of recommendations to return
            
        Returns:
            List of recommended crops with scores and reasoning
        """
        prices = self.predict_crop_prices(climate_data)
        recommendations = []
        
        for crop in self.crops:
            if crop not in prices:
                continue
            
            price = prices[crop]
            profile = self.crop_profiles.get(crop, {})
            
            # Calculate yield suitability
            yield_score = self.calculate_yield_score(climate_data, crop)
            
            # Calculate profitability (price * yield * demand)
            base_yield = profile.get('base_yield', 30)
            expected_yield = base_yield * yield_score
            market_demand = profile.get('market_demand', 0.8)
            profitability = price * expected_yield * market_demand
            
            recommendation = {
                'crop': crop,
                'predicted_price': round(price, 2),
                'yield_suitability': round(yield_score * 100, 2),
                'expected_yield': round(expected_yield, 2),
                'market_demand': round(market_demand * 100, 2),
                'profitability_score': round(profitability, 2),
                'revenue_estimate': round(profitability * 1000, 2),  # Estimated for 1 hectare
                'reasoning': self._generate_reasoning(crop, price, yield_score, market_demand)
            }
            
            recommendations.append(recommendation)
        
        # Sort by profitability score
        recommendations.sort(key=lambda x: x['profitability_score'], reverse=True)
        return recommendations[:top_n]
    
    def _generate_reasoning(self, crop: str, price: float, yield_score: float, demand: float) -> str:
        """Generate human-readable reasoning for recommendation."""
        reasons = []
        
        if price > 300:
            reasons.append("High market price")
        elif price > 150:
            reasons.append("Good market price")
        else:
            reasons.append("Moderate market price")
        
        if yield_score > 0.8:
            reasons.append("Excellent climate fit")
        elif yield_score > 0.6:
            reasons.append("Good climate suitability")
        else:
            reasons.append("Moderate climate fit")
        
        if demand > 0.9:
            reasons.append("High market demand")
        elif demand > 0.8:
            reasons.append("Strong demand")
        
        return " | ".join(reasons)
