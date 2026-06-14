import requests
from typing import Dict, Optional
from datetime import datetime, timedelta
import json

class WeatherService:
    """
    Integrates real-time weather data from OpenMeteo API.
    No API key required - uses free tier.
    """
    
    # OpenMeteo coordinates for common Sri Lankan regions
    REGION_COORDINATES = {
        'Nuwara Eliya': {'lat': 6.9271, 'lon': 80.7789, 'elevation': 1868},
        'Kandy': {'lat': 7.2906, 'lon': 80.6337, 'elevation': 465},
        'Colombo': {'lat': 6.9271, 'lon': 79.8612, 'elevation': 7},
        'Galle': {'lat': 6.0535, 'lon': 80.2170, 'elevation': 11},
        'Jaffna': {'lat': 9.6615, 'lon': 80.2855, 'elevation': 8},
        'Badulla': {'lat': 6.9901, 'lon': 81.0555, 'elevation': 680},
        'Matara': {'lat': 5.7482, 'lon': 80.5353, 'elevation': 5},
        'Ratnapura': {'lat': 6.6828, 'lon': 80.4050, 'elevation': 97},
    }
    
    OPENMETEO_BASE_URL = "https://api.open-meteo.com/v1/forecast"
    HISTORICAL_URL = "https://archive-api.open-meteo.com/v1/archive"
    
    @staticmethod
    def get_current_weather(region: str) -> Optional[Dict]:
        """
        Get current weather conditions for a region.
        
        Args:
            region: Region name
            
        Returns:
            Dict with current weather data or None if error
        """
        if region not in WeatherService.REGION_COORDINATES:
            return None
        
        coords = WeatherService.REGION_COORDINATES[region]
        
        try:
            params = {
                'latitude': coords['lat'],
                'longitude': coords['lon'],
                'current': 'temperature_2m,relative_humidity_2m,precipitation,weather_code',
                'timezone': 'Asia/Colombo'
            }
            
            response = requests.get(WeatherService.OPENMETEO_BASE_URL, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            
            current = data.get('current', {})
            
            return {
                'region': region,
                'temperature': current.get('temperature_2m', 0),
                'humidity': current.get('relative_humidity_2m', 0),
                'precipitation': current.get('precipitation', 0),
                'weather_code': current.get('weather_code', 0),
                'timestamp': current.get('time', ''),
                'description': WeatherService._decode_weather_code(current.get('weather_code', 0))
            }
        except Exception as e:
            print(f"Weather API error: {e}")
            return None
    
    @staticmethod
    def get_forecast(region: str, days: int = 7) -> Optional[Dict]:
        """
        Get weather forecast for the next N days.
        
        Args:
            region: Region name
            days: Number of days to forecast (default 7)
            
        Returns:
            Dict with forecast data or None if error
        """
        if region not in WeatherService.REGION_COORDINATES:
            return None
        
        coords = WeatherService.REGION_COORDINATES[region]
        
        try:
            params = {
                'latitude': coords['lat'],
                'longitude': coords['lon'],
                'daily': 'temperature_2m_max,temperature_2m_min,precipitation_sum,relative_humidity_2m_max',
                'forecast_days': min(days, 16),
                'timezone': 'Asia/Colombo'
            }
            
            response = requests.get(WeatherService.OPENMETEO_BASE_URL, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            
            daily = data.get('daily', {})
            dates = daily.get('time', [])
            temps_max = daily.get('temperature_2m_max', [])
            temps_min = daily.get('temperature_2m_min', [])
            precip = daily.get('precipitation_sum', [])
            humidity = daily.get('relative_humidity_2m_max', [])
            
            forecast_list = []
            for i in range(min(len(dates), days)):
                forecast_list.append({
                    'date': dates[i],
                    'temp_max': temps_max[i],
                    'temp_min': temps_min[i],
                    'precipitation': precip[i],
                    'humidity': humidity[i],
                    'avg_temp': (temps_max[i] + temps_min[i]) / 2
                })
            
            return {
                'region': region,
                'forecast': forecast_list,
                'elevation': coords['elevation']
            }
        except Exception as e:
            print(f"Forecast API error: {e}")
            return None
    
    @staticmethod
    def get_seasonal_analysis(region: str) -> Optional[Dict]:
        """
        Get seasonal weather patterns and analysis.
        
        Args:
            region: Region name
            
        Returns:
            Dict with seasonal analysis data
        """
        current = WeatherService.get_current_weather(region)
        forecast = WeatherService.get_forecast(region, days=14)
        
        if not current or not forecast:
            return None
        
        forecast_data = forecast.get('forecast', [])
        
        # Calculate averages and trends
        avg_temp = sum([f['avg_temp'] for f in forecast_data]) / len(forecast_data) if forecast_data else 0
        avg_humidity = sum([f['humidity'] for f in forecast_data]) / len(forecast_data) if forecast_data else 0
        total_rainfall = sum([f['precipitation'] for f in forecast_data]) if forecast_data else 0
        
        return {
            'region': region,
            'current_conditions': {
                'temperature': current['temperature'],
                'humidity': current['humidity'],
                'precipitation': current['precipitation'],
                'description': current['description']
            },
            'forecast_avg': {
                'temperature': round(avg_temp, 2),
                'humidity': round(avg_humidity, 2),
                'expected_rainfall': round(total_rainfall, 2)
            },
            'trend': WeatherService._analyze_trend(forecast_data),
            'farming_insights': WeatherService._generate_farming_insights(
                current['temperature'],
                current['humidity'],
                total_rainfall
            )
        }
    
    @staticmethod
    def _analyze_trend(forecast_data: list) -> str:
        """Analyze weather trend from forecast data."""
        if len(forecast_data) < 2:
            return "Insufficient data"
        
        first_half_avg = sum([f['avg_temp'] for f in forecast_data[:len(forecast_data)//2]]) / (len(forecast_data)//2)
        second_half_avg = sum([f['avg_temp'] for f in forecast_data[len(forecast_data)//2:]]) / (len(forecast_data) - len(forecast_data)//2)
        
        if second_half_avg > first_half_avg + 1:
            return "Warming trend"
        elif second_half_avg < first_half_avg - 1:
            return "Cooling trend"
        else:
            return "Stable conditions"
    
    @staticmethod
    def _generate_farming_insights(temp: float, humidity: float, rainfall: float) -> list:
        """Generate farming-relevant insights from weather data."""
        insights = []
        
        if temp > 30:
            insights.append("High temperature - Increase irrigation for heat-sensitive crops")
        elif temp < 15:
            insights.append("Low temperature - Consider frost-resistant varieties")
        
        if humidity > 85:
            insights.append("High humidity - Watch for fungal diseases, improve drainage")
        elif humidity < 40:
            insights.append("Low humidity - Increase irrigation frequency")
        
        if rainfall > 100:
            insights.append("Heavy rainfall expected - Ensure proper drainage")
        elif rainfall < 20:
            insights.append("Low rainfall - Plan irrigation schedules")
        
        if not insights:
            insights.append("Favorable conditions for most crops")
        
        return insights
    
    @staticmethod
    def _decode_weather_code(code: int) -> str:
        """Decode WMO weather code to human-readable description."""
        codes = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Foggy",
            48: "Depositing rime fog",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            71: "Slight snow",
            73: "Moderate snow",
            75: "Heavy snow",
            77: "Snow grains",
            80: "Slight rain showers",
            81: "Moderate rain showers",
            82: "Violent rain showers",
            85: "Slight snow showers",
            86: "Heavy snow showers",
            95: "Thunderstorm",
            96: "Thunderstorm with slight hail",
            99: "Thunderstorm with heavy hail",
        }
        return codes.get(code, "Unknown")
    
    @staticmethod
    def get_optimal_planting_window(region: str) -> Optional[Dict]:
        """
        Analyze when is the best time to plant based on forecast.
        
        Returns:
            Dict with planting recommendations
        """
        forecast_data = WeatherService.get_forecast(region, days=30)
        if not forecast_data:
            return None
        
        forecast = forecast_data.get('forecast', [])
        optimal_days = []
        
        for i, day in enumerate(forecast[:14]):  # Check next 14 days
            temp = day['avg_temp']
            rainfall = day['precipitation']
            humidity = day['humidity']
            
            # Score optimal conditions: temp 18-25°C, moderate rainfall, good humidity
            score = 0
            if 18 <= temp <= 25:
                score += 40
            if 10 <= rainfall <= 50:
                score += 30
            if 60 <= humidity <= 85:
                score += 30
            
            if score >= 80:
                optimal_days.append({
                    'date': day['date'],
                    'score': score,
                    'conditions': f"Temp: {temp:.1f}°C, Rain: {rainfall:.1f}mm, Humidity: {humidity:.0f}%"
                })
        
        return {
            'region': region,
            'optimal_windows': optimal_days[:5],
            'recommendation': "Ideal planting days in next 2 weeks" if optimal_days else "Consider waiting for better conditions"
        }
