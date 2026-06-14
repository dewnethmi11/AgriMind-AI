from typing import List, Dict, Optional
import json
from datetime import datetime, timedelta

class DecisionAgent:
    """
    Autonomous agent that makes farming decisions based on
    comprehensive analysis of market, weather, and yield data.
    Provides scenario analysis and strategic recommendations.
    """
    
    def __init__(self):
        self.scenarios = {}
        self.decision_log = []
    
    def analyze_scenarios(self, climate_data: Dict, recommendations: List[Dict], 
                         weather_forecast: Dict) -> Dict:
        """
        Analyze best-case, worst-case, and realistic scenarios.
        
        Args:
            climate_data: Current climate parameters
            recommendations: Crop recommendations with predictions
            weather_forecast: Weather forecast data
            
        Returns:
            Dict with scenario analysis results
        """
        
        scenarios = {
            'optimistic': self._build_optimistic_scenario(recommendations, weather_forecast),
            'realistic': self._build_realistic_scenario(recommendations, weather_forecast),
            'pessimistic': self._build_pessimistic_scenario(recommendations, weather_forecast),
        }
        
        return {
            'scenarios': scenarios,
            'recommended_strategy': self._recommend_strategy(scenarios),
            'risk_adjusted_return': self._calculate_risk_adjusted_return(scenarios),
            'decision_matrix': self._build_decision_matrix(recommendations),
            'contingency_plans': self._generate_contingency_plans(scenarios),
            'sensitivity_analysis': self._perform_sensitivity_analysis(recommendations)
        }
    
    def _build_optimistic_scenario(self, recommendations: List[Dict], 
                                   weather_forecast: Dict) -> Dict:
        """Build best-case scenario analysis."""
        if not recommendations:
            return {}
        
        top_crop = recommendations[0]
        
        # Optimistic: Prices 20% higher, Yield 15% higher
        optimistic_price = top_crop['predicted_price'] * 1.2
        optimistic_yield = top_crop['expected_yield'] * 1.15
        optimistic_revenue = optimistic_price * optimistic_yield * 1000  # per hectare
        
        return {
            'crop': top_crop['crop'],
            'assumptions': [
                'Prices increase due to high demand',
                'Yield exceeds expectations due to favorable weather',
                'No significant pest or disease outbreaks',
                'Good market access and fair prices'
            ],
            'predicted_price': round(optimistic_price, 2),
            'predicted_yield': round(optimistic_yield, 2),
            'estimated_revenue': round(optimistic_revenue, 2),
            'profit_per_hectare': round(optimistic_revenue * 0.6, 2),  # Assuming 40% input costs
            'probability': '20-25%',
            'timeline': f"If weather remains favorable and markets are strong"
        }
    
    def _build_realistic_scenario(self, recommendations: List[Dict], 
                                  weather_forecast: Dict) -> Dict:
        """Build realistic/most likely scenario."""
        if not recommendations:
            return {}
        
        top_crop = recommendations[0]
        
        # Realistic: Use predicted values as-is
        realistic_revenue = top_crop['revenue_estimate']
        
        return {
            'crop': top_crop['crop'],
            'assumptions': [
                'Market prices align with predictions',
                'Yield meets expectations',
                'Normal pest/disease management required',
                'Reasonable market access'
            ],
            'predicted_price': round(top_crop['predicted_price'], 2),
            'predicted_yield': round(top_crop['expected_yield'], 2),
            'estimated_revenue': round(realistic_revenue, 2),
            'profit_per_hectare': round(realistic_revenue * 0.6, 2),
            'probability': '50-60%',
            'timeline': 'Most likely outcome based on current trends'
        }
    
    def _build_pessimistic_scenario(self, recommendations: List[Dict], 
                                    weather_forecast: Dict) -> Dict:
        """Build worst-case scenario analysis."""
        if not recommendations:
            return {}
        
        top_crop = recommendations[0]
        
        # Pessimistic: Prices 25% lower, Yield 20% lower
        pessimistic_price = top_crop['predicted_price'] * 0.75
        pessimistic_yield = top_crop['expected_yield'] * 0.8
        pessimistic_revenue = pessimistic_price * pessimistic_yield * 1000
        
        return {
            'crop': top_crop['crop'],
            'assumptions': [
                'Market prices drop due to oversupply',
                'Yield lower due to unfavorable weather',
                'Significant pest or disease issues',
                'Limited market access or buyer options'
            ],
            'predicted_price': round(pessimistic_price, 2),
            'predicted_yield': round(pessimistic_yield, 2),
            'estimated_revenue': round(pessimistic_revenue, 2),
            'profit_per_hectare': round(max(0, pessimistic_revenue * 0.6 - 5000), 2),
            'probability': '15-20%',
            'timeline': 'If major adverse events occur'
        }
    
    def _recommend_strategy(self, scenarios: Dict) -> Dict:
        """Recommend farming strategy based on scenario analysis."""
        realistic = scenarios.get('realistic', {})
        optimistic = scenarios.get('optimistic', {})
        pessimistic = scenarios.get('pessimistic', {})
        
        realistic_profit = realistic.get('profit_per_hectare', 0)
        pessimistic_profit = pessimistic.get('profit_per_hectare', 0)
        
        # Calculate risk-reward ratio
        profit_range = realistic_profit - pessimistic_profit
        
        if profit_range < 10000:
            strategy_type = 'CONSERVATIVE'
            explanation = 'Low variance - Stable returns. Safe option for financial planning.'
        elif profit_range < 30000:
            strategy_type = 'MODERATE'
            explanation = 'Moderate variance - Balanced risk and return. Recommended.'
        else:
            strategy_type = 'AGGRESSIVE'
            explanation = 'High variance - Higher potential but greater risk. Suitable for risk-takers.'
        
        return {
            'strategy_type': strategy_type,
            'explanation': explanation,
            'recommended_crop': realistic.get('crop', 'N/A'),
            'expected_roi': self._calculate_roi(realistic_profit),
            'risk_level': self._assess_risk_level(scenarios),
            'diversification_needed': profit_range > 25000
        }
    
    def _calculate_roi(self, profit_per_hectare: float) -> str:
        """Calculate return on investment percentage."""
        # Assuming input cost of ~25000 per hectare
        input_cost = 25000
        roi = (profit_per_hectare / input_cost) * 100 if input_cost > 0 else 0
        return f"{roi:.1f}%"
    
    def _assess_risk_level(self, scenarios: Dict) -> str:
        """Assess overall risk level."""
        realistic = scenarios.get('realistic', {}).get('profit_per_hectare', 0)
        pessimistic = scenarios.get('pessimistic', {}).get('profit_per_hectare', 0)
        
        downside = realistic - pessimistic
        
        if downside < 5000:
            return "LOW RISK"
        elif downside < 20000:
            return "MODERATE RISK"
        else:
            return "HIGH RISK"
    
    def _calculate_risk_adjusted_return(self, scenarios: Dict) -> Dict:
        """Calculate risk-adjusted returns."""
        optimistic = scenarios.get('optimistic', {}).get('profit_per_hectare', 0)
        realistic = scenarios.get('realistic', {}).get('profit_per_hectare', 0)
        pessimistic = scenarios.get('pessimistic', {}).get('profit_per_hectare', 0)
        
        # Weighted average: 20% optimistic, 60% realistic, 20% pessimistic
        expected_value = (optimistic * 0.20) + (realistic * 0.60) + (pessimistic * 0.20)
        
        # Standard deviation as measure of risk
        variance = ((optimistic - expected_value)**2 * 0.20 + 
                   (realistic - expected_value)**2 * 0.60 + 
                   (pessimistic - expected_value)**2 * 0.20)
        std_dev = variance ** 0.5
        
        return {
            'expected_profit': round(expected_value, 2),
            'profit_std_deviation': round(std_dev, 2),
            'sharpe_ratio': round(expected_value / std_dev, 2) if std_dev > 0 else 0,
            'confidence_interval': f"Rs {round(expected_value - std_dev, 2)} to Rs {round(expected_value + std_dev, 2)}"
        }
    
    def _build_decision_matrix(self, recommendations: List[Dict]) -> List[Dict]:
        """Build decision matrix for multiple crop options."""
        decision_matrix = []
        
        for i, rec in enumerate(recommendations[:5]):
            decision_matrix.append({
                'rank': i + 1,
                'crop': rec['crop'],
                'profitability': rec['profitability_score'],
                'yield_suitability': f"{rec['yield_suitability']}%",
                'price': f"Rs {rec['predicted_price']}",
                'revenue': f"Rs {rec['revenue_estimate']}",
                'risk': 'Low' if rec['profitability_score'] > 400 else 'Medium' if rec['profitability_score'] > 200 else 'High',
                'recommendation': 'PLANT' if i == 0 else ('CONSIDER' if i < 3 else 'BACKUP')
            })
        
        return decision_matrix
    
    def _generate_contingency_plans(self, scenarios: Dict) -> List[Dict]:
        """Generate contingency plans for different events."""
        plans = [
            {
                'event': 'Crop Price Drops Below Expected',
                'probability': 'Medium',
                'impact': 'Reduced profit by 20-30%',
                'mitigation': [
                    'Sell directly to wholesalers to reduce middleman costs',
                    'Process crop (e.g., tomato puree) for value addition',
                    'Store in appropriate conditions and sell when prices recover',
                    'Diversify to alternative crops if situation worsens'
                ]
            },
            {
                'event': 'Pest or Disease Outbreak',
                'probability': 'Medium',
                'impact': 'Yield reduction of 15-40%',
                'mitigation': [
                    'Implement integrated pest management immediately',
                    'Use biological controls and organic pesticides',
                    'Increase monitoring frequency',
                    'Isolate affected areas, practice crop rotation'
                ]
            },
            {
                'event': 'Adverse Weather (Excess Rain/Drought)',
                'probability': 'Medium',
                'impact': 'Yield loss of 20-50%',
                'mitigation': [
                    'Excess rain: Improve drainage, reduce irrigation',
                    'Drought: Increase irrigation, use drought-resistant varieties',
                    'Apply protective mulch or shade in extreme conditions',
                    'Have backup water source or crop insurance'
                ]
            },
            {
                'event': 'Market Supply Glut',
                'probability': 'Low-Medium',
                'impact': 'Difficulty finding buyers, price collapse',
                'mitigation': [
                    'Pre-arrange sales contracts before planting',
                    'Develop relationships with bulk buyers',
                    'Consider value-added products',
                    'Participate in farmer cooperatives for bulk sales'
                ]
            },
            {
                'event': 'Input Cost Inflation',
                'probability': 'Medium',
                'impact': 'Profit margin reduction',
                'mitigation': [
                    'Buy inputs in advance when prices are low',
                    'Use organic/alternative inputs to reduce costs',
                    'Practice efficient resource management',
                    'Join farmer groups for bulk input purchases'
                ]
            }
        ]
        
        return plans
    
    def _perform_sensitivity_analysis(self, recommendations: List[Dict]) -> Dict:
        """Perform sensitivity analysis on key variables."""
        if not recommendations:
            return {}
        
        top_crop = recommendations[0]
        base_revenue = top_crop['revenue_estimate']
        base_profit = base_revenue * 0.6  # Assuming 60% net margin
        
        return {
            'base_profit': round(base_profit, 2),
            'sensitivity_factors': [
                {
                    'factor': 'Price Change (+/- 10%)',
                    'impact_profit': f"Rs {round(base_profit * 0.1, 2)}",
                    'interpretation': 'Each 10% price change affects profit by ± Rs amount shown'
                },
                {
                    'factor': 'Yield Change (+/- 10%)',
                    'impact_profit': f"Rs {round(base_revenue * 0.6 * 0.1, 2)}",
                    'interpretation': 'Each 10% yield change affects profit by ± Rs amount shown'
                },
                {
                    'factor': 'Input Cost Change (+/- 10%)',
                    'impact_profit': f"Rs {round(base_revenue * 0.4 * 0.1, 2)}",
                    'interpretation': 'Each 10% input cost change affects profit by ∓ Rs amount shown'
                }
            ],
            'most_sensitive_to': 'Price fluctuations (highest impact)',
            'recommendation': 'Lock in prices early through forward contracts'
        }
    
    def log_decision(self, decision_data: Dict):
        """Log decision for future reference and learning."""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'decision': decision_data,
            'outcome': None,
            'status': 'pending'
        }
        self.decision_log.append(log_entry)
    
    def get_decision_summary(self, scenarios: Dict, recommendations: List[Dict]) -> str:
        """Generate executive decision summary."""
        if not recommendations:
            return "Insufficient data for decision making."
        
        top_crop = recommendations[0]
        strategy = self._recommend_strategy(scenarios)
        risk_adjusted = self._calculate_risk_adjusted_return(scenarios)
        
        summary = (
            f"DECISION SUMMARY:\\n\\n"
            f"Recommended Crop: {top_crop['crop']}\\n"
            f"Strategy: {strategy['strategy_type']} - {strategy['explanation']}\\n"
            f"Expected Profit: Rs {risk_adjusted['expected_profit']} per hectare\n"
            f"Confidence Range: {risk_adjusted['confidence_interval']}\\n"
            f"Risk Level: {self._assess_risk_level(scenarios)}\\n"
            f"\\nKey Success Factors:\\n"
            f"• Maintain optimal irrigation based on weather\\n"
            f"• Implement proactive pest management\\n"
            f"• Lock in prices through advance sales contracts\\n"
            f"• Monitor market trends for best sales timing"
        )
        
        return summary
