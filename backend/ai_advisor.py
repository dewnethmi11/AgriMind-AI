from typing import List, Dict, Optional
from datetime import datetime

class AIAdvisor:
    """
    Intelligent farming advisor that provides contextual recommendations
    based on climate, prices, yield, and market conditions.
    """
    
    def __init__(self):
        self.conversation_history = []
        self.farmer_profile = {}
    
    def set_farmer_profile(self, farm_size: float = None, location: str = None, 
                          preferences: List[str] = None, constraints: List[str] = None):
        """Set farmer profile for personalized recommendations."""
        self.farmer_profile = {
            'farm_size': farm_size or 1.0,  # hectares
            'location': location,
            'preferences': preferences or [],
            'constraints': constraints or [],
            'last_updated': datetime.now().isoformat()
        }
    
    def get_advice(self, context: Dict) -> Dict:
        """
        Generate comprehensive farming advice based on context.
        
        Args:
            context: Dict with recommendations, weather, market data
            
        Returns:
            Dict with multi-part advice
        """
        
        advice_parts = []
        
        # Extract data from context
        recommendations = context.get('crop_recommendations', [])
        weather = context.get('weather', {})
        market_data = context.get('market_data', {})
        
        # Generate different advice sections
        crop_advice = self._generate_crop_advice(recommendations)
        timing_advice = self._generate_timing_advice(weather, recommendations)
        risk_advice = self._generate_risk_mitigation(recommendations, weather)
        market_advice = self._generate_market_advice(recommendations, market_data)
        operational_advice = self._generate_operational_advice(weather)
        
        return {
            'summary': self._generate_summary(crop_advice, timing_advice, risk_advice),
            'detailed_advice': {
                'crop_selection': crop_advice,
                'timing_guidance': timing_advice,
                'risk_mitigation': risk_advice,
                'market_strategy': market_advice,
                'operations': operational_advice
            },
            'confidence_score': self._calculate_confidence(context),
            'next_actions': self._suggest_next_actions(recommendations, weather)
        }
    
    def _generate_crop_advice(self, recommendations: List[Dict]) -> Dict:
        """Generate advice on crop selection."""
        if not recommendations:
            return {'recommendation': 'No data available', 'crops': []}
        
        top_crop = recommendations[0]
        top_3_crops = recommendations[:3]
        
        advice = {
            'primary_recommendation': f"Plant {top_crop['crop']} as your primary crop",
            'rationale': f"Strong profitability score of {top_crop['profitability_score']}, "
                        f"yield suitability of {top_crop['yield_suitability']}%, "
                        f"and predicted market price of Rs {top_crop['predicted_price']}",
            'top_alternatives': [
                {
                    'crop': rec['crop'],
                    'profitability': rec['profitability_score'],
                    'reason': rec['reasoning']
                }
                for rec in top_3_crops[1:]
            ],
            'risk_level': self._calculate_crop_risk(top_crop),
            'diversification_suggestion': self._suggest_diversification(top_3_crops)
        }
        
        return advice
    
    def _generate_timing_advice(self, weather: Dict, recommendations: List[Dict]) -> Dict:
        """Generate advice on planting timing."""
        current_temp = weather.get('temperature', 20)
        current_humidity = weather.get('humidity', 60)
        current_rainfall = weather.get('precipitation', 0)
        
        timing_advice = {
            'current_conditions': {
                'temperature': f"{current_temp}°C",
                'humidity': f"{current_humidity}%",
                'rainfall': f"{current_rainfall}mm"
            }
        }
        
        # Generate timing recommendation
        if current_temp < 15:
            timing_advice['recommendation'] = "Wait for warmer conditions before planting"
            timing_advice['reason'] = "Current temperature is too low for optimal germination"
        elif current_temp > 35:
            timing_advice['recommendation'] = "Plant heat-resistant varieties or wait for cooling"
            timing_advice['reason'] = "High temperature may stress seedlings"
        elif current_humidity > 85 and current_rainfall > 10:
            timing_advice['recommendation'] = "Ensure good drainage before planting"
            timing_advice['reason'] = "Wet conditions increase disease risk"
        else:
            timing_advice['recommendation'] = "Conditions are favorable for planting"
            timing_advice['reason'] = "Temperature, humidity, and rainfall are within optimal ranges"
        
        timing_advice['suggested_window'] = self._suggest_planting_window(current_temp)
        
        return timing_advice
    
    def _generate_risk_mitigation(self, recommendations: List[Dict], weather: Dict) -> Dict:
        """Generate risk mitigation strategies."""
        risks = []
        
        # Price volatility risk
        if recommendations:
            top_crop = recommendations[0]
            if top_crop['profitability_score'] > 500:
                risks.append({
                    'type': 'Price Volatility',
                    'severity': 'Medium',
                    'mitigation': 'Lock in prices early through forward contracts with traders'
                })
        
        # Weather risk
        if weather.get('humidity', 0) > 85:
            risks.append({
                'type': 'Fungal Disease',
                'severity': 'High',
                'mitigation': 'Ensure proper spacing, improve drainage, apply preventive fungicides'
            })
        
        if weather.get('temperature', 20) > 35:
            risks.append({
                'type': 'Heat Stress',
                'severity': 'Medium',
                'mitigation': 'Increase irrigation frequency, use mulching, provide shade if possible'
            })
        
        # Yield risk
        risks.append({
            'type': 'Yield Variability',
            'severity': 'Medium',
            'mitigation': 'Plant multiple varieties, practice crop rotation, maintain soil health'
        })
        
        return {
            'identified_risks': risks,
            'overall_risk_assessment': 'Manageable' if len(risks) <= 2 else 'Significant',
            'insurance_recommendation': 'Consider crop insurance for peace of mind'
        }
    
    def _generate_market_advice(self, recommendations: List[Dict], market_data: Dict) -> Dict:
        """Generate market strategy advice."""
        if not recommendations:
            return {'advice': 'No market data available'}
        
        top_crop = recommendations[0]
        
        return {
            'market_opportunity': f"Strong market opportunity for {top_crop['crop']}",
            'expected_price': f"Rs {top_crop['predicted_price']} per kg",
            'market_demand': f"{top_crop['market_demand']}% - {'High' if top_crop['market_demand'] > 80 else 'Moderate'}",
            'expected_revenue': f"Rs {top_crop['revenue_estimate']} per hectare (estimated)",
            'sale_timing': self._suggest_sale_timing(top_crop),
            'buyer_prospects': self._suggest_buyers(top_crop['crop']),
            'quality_premium': 'Organic certification could increase prices by 20-30%'
        }
    
    def _generate_operational_advice(self, weather: Dict) -> Dict:
        """Generate day-to-day operational guidance."""
        current_temp = weather.get('temperature', 20)
        current_humidity = weather.get('humidity', 60)
        current_rainfall = weather.get('precipitation', 0)
        
        operations = {
            'irrigation': self._suggest_irrigation(current_rainfall, current_humidity, current_temp),
            'pest_management': self._suggest_pest_management(current_humidity, current_temp),
            'soil_care': self._suggest_soil_care(current_rainfall),
            'equipment': self._suggest_equipment_needs(weather)
        }
        
        return operations
    
    def _suggest_diversification(self, top_crops: List[Dict]) -> str:
        """Suggest diversification strategy."""
        if len(top_crops) >= 2:
            crop1, crop2 = top_crops[0]['crop'], top_crops[1]['crop']
            return f"Consider planting 70% {crop1} and 30% {crop2} for diversified income"
        return "Focus on single high-profitability crop for this season"
    
    def _calculate_crop_risk(self, crop_data: Dict) -> str:
        """Calculate risk level for a crop."""
        if crop_data['profitability_score'] > 600:
            return "Low - High profitability with stable demand"
        elif crop_data['profitability_score'] > 300:
            return "Medium - Moderate returns with some market volatility"
        else:
            return "High - Lower returns, recommend diversification"
    
    def _suggest_planting_window(self, temp: float) -> str:
        """Suggest planting window based on temperature."""
        if temp < 15:
            return "Wait 1-2 weeks for warming trend"
        elif temp > 35:
            return "Wait for temperature to drop below 32°C"
        else:
            return "Next 3-5 days are optimal for planting"
    
    def _suggest_irrigation(self, rainfall: float, humidity: float, temp: float) -> str:
        """Suggest irrigation schedule."""
        if rainfall > 20:
            return "Reduce irrigation - natural rainfall is sufficient"
        elif humidity > 70:
            return "Light irrigation 2-3 times per week"
        elif temp > 30:
            return "Increase to daily irrigation, water in early morning"
        else:
            return "Standard irrigation 3-4 times per week"
    
    def _suggest_pest_management(self, humidity: float, temp: float) -> str:
        """Suggest pest management approach."""
        if humidity > 80:
            return "Monitor for fungal pests, maintain proper spacing, use neem oil sprays"
        elif temp > 30:
            return "Watch for heat-loving pests, use organic insecticides"
        else:
            return "Standard pest monitoring, preventive measures recommended"
    
    def _suggest_soil_care(self, rainfall: float) -> str:
        """Suggest soil care practices."""
        if rainfall > 50:
            return "Improve drainage, add organic matter to prevent waterlogging"
        else:
            return "Add mulch (5-7cm) to retain moisture, apply compost monthly"
    
    def _suggest_equipment_needs(self, weather: Dict) -> str:
        """Suggest equipment needs based on weather."""
        if weather.get('precipitation', 0) > 20:
            return "Ensure drainage systems are clear, check pump functionality"
        else:
            return "Inspect irrigation systems, ensure water availability"
    
    def _suggest_sale_timing(self, crop_data: Dict) -> str:
        """Suggest when to sell the crop."""
        profitability = crop_data['profitability_score']
        if profitability > 600:
            return "Strong market - sell within 1-2 weeks of harvest"
        elif profitability > 300:
            return "Moderate market - monitor prices, sell at good opportunity"
        else:
            return "Weak market - consider storing for better prices or selling to bulk buyers"
    
    def _suggest_buyers(self, crop: str) -> List[str]:
        """Suggest potential buyers for the crop."""
        buyers = {
            'Tomato': ['Vegetable markets', 'Hotels & restaurants', 'Processors'],
            'Potato': ['Bulk traders', 'Food processors', 'Retail chains'],
            'Carrot': ['Export markets', 'Retail chains', 'Food processors'],
            'Onion': ['Bulk traders', 'Restaurants', 'Spice merchants'],
            'Cabbage': ['Vegetable markets', 'Retail chains', 'Processors'],
            'Lettuce': ['Hotels', 'Restaurants', 'Retail chains'],
            'Broccoli': ['Premium retailers', 'Restaurants', 'Exporters']
        }
        return buyers.get(crop, ['Local vegetable markets'])
    
    def _calculate_confidence(self, context: Dict) -> float:
        """Calculate confidence score of advice."""
        score = 0.5  # Base confidence
        
        if context.get('crop_recommendations'):
            score += 0.2
        if context.get('weather'):
            score += 0.15
        if context.get('market_data'):
            score += 0.15
        
        return min(score, 0.95)
    
    def _generate_summary(self, crop_advice: Dict, timing_advice: Dict, 
                         risk_advice: Dict) -> str:
        """Generate executive summary."""
        return (f"{crop_advice.get('primary_recommendation', 'Consider alternatives')}. "
                f"Current conditions: {timing_advice.get('recommendation', 'Check weather')}. "
                f"Risk level: {risk_advice.get('overall_risk_assessment', 'Moderate')}. "
                f"Ready to proceed when conditions align.")
    
    def _suggest_next_actions(self, recommendations: List[Dict], weather: Dict) -> List[str]:
        """Suggest immediate next steps."""
        actions = []
        
        if recommendations:
            actions.append(f"✓ Prepare land for planting {recommendations[0]['crop']}")
        
        if weather.get('temperature', 20) > 30:
            actions.append("✓ Set up irrigation system")
        
        if weather.get('humidity', 0) > 75:
            actions.append("✓ Improve drainage in field")
        
        actions.append("✓ Procure quality seeds from certified sources")
        actions.append("✓ Arrange manure and fertilizer")
        actions.append("✓ Plan pest management strategy")
        
        return actions[:5]  # Top 5 action items
