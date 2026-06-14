# AgriMind AI v2.0

An intelligent farming decision assistant that analyzes climate conditions, predicts vegetable prices, recommends profitable crops, integrates weather data, and provides autonomous decision support using machine learning and AI-driven insights.

---

## 🎯 Project Roadmap

### ✅ AgriMind AI v1.0 - Completed
- **Price Prediction System**: ML-based price forecasting for vegetables
- **Interactive Dashboard**: User-friendly interface for predictions

### 🚀 AgriMind AI v2.0 - New Features

#### 1. 🌾 Crop Recommendation Engine ✅
- Analyzes climate conditions (temperature, rainfall, humidity)
- Evaluates multiple crop options simultaneously
- Calculates profitability scores based on yield and market demand
- Provides top 5 ranked recommendations
- Considers region-specific climate suitability

**Features:**
- Multi-crop comparison
- Yield suitability scoring
- Market demand analysis
- Revenue estimation per hectare
- Ranking by profitability

#### 2. 🌦 Weather Integration ✅
- Real-time weather data via OpenMeteo API (free, no API key required)
- 7-day forecast capability
- Historical weather pattern analysis
- Optimal planting window recommendations
- Regional weather data for major Sri Lankan regions:
  - Nuwara Eliya, Kandy, Colombo, Galle, Jaffna, Badulla, Matara, Ratnapura

**Features:**
- Current temperature, humidity, precipitation
- Seasonal weather analysis
- Farming-specific weather insights
- Planting window optimization
- Weather trend analysis

#### 3. 🤖 AI Farming Advisor ✅
- Context-aware intelligent recommendations
- Multi-part farming advice:
  - Crop selection rationale
  - Optimal timing guidance
  - Risk mitigation strategies
  - Market strategy recommendations
  - Operational guidance (irrigation, pest management, soil care)

**Features:**
- Farmer profile customization
- Comprehensive advice generation
- Risk assessment
- Market opportunity analysis
- Equipment recommendations
- Buyer prospect identification

#### 4. 📊 Agent-Based Decision Support ✅
- Autonomous decision-making system
- Scenario analysis (Optimistic, Realistic, Pessimistic)
- Risk-adjusted return calculations
- Sensitivity analysis
- Contingency planning

**Features:**
- Best-case/worst-case/realistic scenarios
- Decision matrix for multiple crops
- Sharpe ratio calculations
- Contingency plans for adverse events
- Profitability forecasting
- ROI calculations

#### 5. 🎯 Comprehensive Farm Analysis ✅
- Integrated analysis combining all v2.0 features
- Single endpoint for complete intelligence dashboard
- Climate data, recommendations, weather, advice, and decisions

---

## 🌟 Key Features

### Crop Recommendation
- **Multi-Crop Analysis**: Compare 7+ vegetable varieties
- **Profitability Scoring**: Data-driven ranking system
- **Yield Suitability**: Climate-based yield potential
- **Market Analysis**: Demand and revenue estimation

### Weather Intelligence
- **Real-Time Data**: Current conditions and forecasts
- **Seasonal Analysis**: Pattern recognition
- **Farming Insights**: Weather-specific recommendations
- **Planting Window**: Optimal sowing schedules

### AI Advisor
- **Smart Recommendations**: Context-aware guidance
- **Risk Mitigation**: Proactive risk identification
- **Market Strategy**: Sales timing and buyer guidance
- **Operational Planning**: Day-to-day farm management

### Decision Support
- **Scenario Analysis**: Multiple outcome planning
- **Sensitivity Analysis**: Variable impact assessment
- **Contingency Plans**: Event-response strategies
- **Financial Forecasting**: Profit predictions

---

## 🏗 Architecture

### Backend (Python/Flask)
```
backend/
├── app.py                 # Main Flask application with all v2.0 endpoints
├── crop_recommender.py    # Crop recommendation engine
├── weather_service.py     # Weather integration service
├── ai_advisor.py          # AI farming advisor
├── decision_agent.py      # Autonomous decision support
├── model.pkl              # Trained ML model
├── region_encoder.pkl     # Region label encoder
├── veg_encoder.pkl        # Vegetable label encoder
└── requirements.txt       # Python dependencies
```

### Frontend (React)
```
frontend/
├── src/
│   ├── App.jsx            # Main app with v2.0 tabs and features
│   ├── App.css            # Enhanced styling for v2.0 UI
│   ├── PriceChart.jsx     # Price visualization component
│   └── main.jsx
├── package.json
└── vite.config.js
```

---

## 🔌 API Endpoints

### V1.0 Endpoints
- `POST /predict` - Price prediction for specific crop

### V2.0 Endpoints
- `POST /recommend-crops` - Get top 5 crop recommendations
- `GET /weather/<region>` - Current weather and forecast
- `POST /advisor` - AI farming advisor recommendations
- `POST /decision-support` - Scenario analysis and decision support
- `POST /comprehensive-analysis` - Complete farm intelligence
- `GET /health` - Health check endpoint

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js 14+
- pip, npm

### Installation

#### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python app.py
```

#### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### Environment Variables
No API keys required! Uses free OpenMeteo weather API.

---

## 💡 How to Use

### 1. Price Prediction (v1.0)
1. Go to "Price Prediction" tab
2. Select region and climate parameters
3. Choose vegetable
4. Click "Predict Price"
5. View historical predictions

### 2. Crop Recommendations (v2.0)
1. Go to "Crop Recommendation" tab
2. Enter region and climate data
3. Click "Get Recommendations"
4. View top 5 crops ranked by profitability

### 3. Weather Analysis (v2.0)
1. Go to "Weather" tab
2. Select supported region
3. Click "Get Weather Data"
4. View current conditions, forecast, and planting windows

### 4. AI Advisor (v2.0)
1. Go to "AI Advisor" tab
2. Enter climate parameters
3. Click "Step 1: Get Recommendations"
4. Click "Step 2: Get AI Advice"
5. View comprehensive farming guidance

### 5. Decision Support (v2.0)
1. Go to "Decision Support" tab
2. Enter climate parameters
3. Click "Analyze Scenarios"
4. View scenario analysis and contingency plans

### 6. Full Analysis (v2.0)
1. Go to "Full Analysis" tab
2. Enter climate parameters
3. Click "Generate Full Analysis"
4. View integrated intelligence dashboard

---

## 🤖 AI/ML Components

### Crop Recommender
- **Inputs**: Region, Temperature, Rainfall, Humidity, Crop Yield
- **Process**: 
  - Price prediction for all crops
  - Yield suitability scoring
  - Profitability calculation
  - Ranking by profitability
- **Outputs**: Top-N recommendations with reasoning

### Weather Service
- **Data Source**: OpenMeteo API (free)
- **Process**:
  - Fetch current weather
  - Analyze 7-14 day forecast
  - Generate farming insights
  - Identify optimal planting windows
- **Outputs**: Weather data, trends, recommendations

### AI Advisor
- **Inputs**: Recommendations, weather, market data
- **Process**:
  - Analyze crop selection options
  - Assess timing based on weather
  - Identify and mitigate risks
  - Generate market strategy
  - Provide operational guidance
- **Outputs**: Comprehensive advice with next actions

### Decision Agent
- **Inputs**: Climate data, recommendations, forecasts
- **Process**:
  - Build optimistic scenario
  - Build realistic scenario
  - Build pessimistic scenario
  - Calculate risk-adjusted returns
  - Generate decision matrix
  - Create contingency plans
- **Outputs**: Scenario analysis, decision support

---

## 📊 Supported Regions

### Price Prediction (v1.0)
All 25 Sri Lankan districts:
Ampara, Anuradhapura, Badulla, Batticaloa, Colombo, Galle, Gampaha, Hambantota, Jaffna, Kalutara, Kandy, Kegalle, Kilinochchi, Kurunegala, Mannar, Matale, Matara, Monaragala, Mullaitivu, Nuwara Eliya, Polonnaruwa, Puttalam, Ratnapura, Trincomalee, Vavuniya

### Weather Data (v2.0)
- Nuwara Eliya (1868m elevation)
- Kandy (465m elevation)
- Colombo (7m elevation)
- Galle (11m elevation)
- Jaffna (8m elevation)
- Badulla (680m elevation)
- Matara (5m elevation)
- Ratnapura (97m elevation)

---

## 📈 Crop Varieties Analyzed

Primary crops in recommendations:
- Tomato
- Potato
- Carrot
- Onion
- Cabbage
- Lettuce
- Broccoli

Price prediction covers 20+ vegetable varieties including:
Winged Bean, Bitter Melon, Brinjal, Eggplant, Pennywort, Red Spinach, Leeks, Beetroot, Knol-Khol, Pumpkin, Drumsticks, Jackfruit, Breadfruit, Taro, Manioc, and more.

---

## 🔧 Technology Stack

### Frontend
- **React 18**: Modern UI framework
- **Axios**: HTTP client for API calls
- **Chart.js**: Data visualization
- **Vite**: Fast build tool
- **CSS3**: Advanced styling with gradients and animations

### Backend
- **Flask**: Lightweight web framework
- **Flask-CORS**: Cross-origin resource sharing
- **Pandas**: Data manipulation
- **Scikit-Learn**: Machine learning
- **Joblib**: Model serialization
- **Requests**: HTTP library for OpenMeteo API

### Data & ML
- **Random Forest Regressor**: Price prediction model
- **Label Encoders**: Category encoding
- **Scikit-Learn Preprocessing**: Data normalization

### External APIs
- **OpenMeteo**: Free weather data (no API key required)

---

## 📚 Data Sources

### Training Data (v1.0)
- 130,000 historical records
- 25 regions across Sri Lanka
- 20 vegetable varieties
- Climate parameters (temperature, rainfall, humidity)
- Crop yield impact scores
- 5 years of data (2020-2025)

### Weather Data (v2.0)
- OpenMeteo free API
- Real-time observations
- 16-day forecasts
- Historical weather patterns

---

## 🎓 Use Cases

### For Farmers
- Decide which crops to plant based on current conditions
- Understand optimal planting timing
- Identify risk factors and mitigations
- Plan market strategy and sales timing
- Manage daily farm operations

### For Agricultural Advisors
- Support farmers with data-driven recommendations
- Explain decisions through scenario analysis
- Identify farming opportunities
- Provide contingency planning

### For Policymakers
- Understand regional farming trends
- Plan agricultural interventions
- Monitor crop profitability
- Support farmer decision-making

---

## 🔒 Privacy & Data

- No user data collection
- No personal information stored
- Open-source weather data
- Local ML model predictions
- Secure API communication

---

## 📝 License

This project is open-source and available for agricultural development and educational purposes.

---

## 🤝 Contributing

Contributions welcome! Areas for enhancement:
- Additional crop varieties
- More weather data sources
- Mobile app development
- Multi-language support
- Integration with farmers' cooperatives
- Real market data integration

---

## 📧 Support

For issues, questions, or suggestions:
- Review the API documentation
- Check the comprehensive analysis tab
- Test with sample data
- Verify region support

---

## 🌍 About

AgriMind AI was created to empower farming communities with intelligent decision support tools, particularly benefiting farmers in regions like Nuwara Eliya, Sri Lanka, where vegetable cultivation is a vital income source.

**Version**: 2.0  
**Status**: Production Ready  
**Last Updated**: 2026-06-14

---

## Problem

Farmers often face uncertainty due to changing climate conditions and fluctuating vegetable prices. This makes it difficult to decide which crops to cultivate and when to grow them, potentially reducing profitability and increasing financial risk.

Many farmers rely on experience and intuition rather than data-driven decision-making. As climate patterns become increasingly unpredictable, there is a growing need for intelligent tools that can support cultivation planning and crop selection.

---

## Solution

AgriMind AI is an AI-powered farming decision assistant that helps farmers make informed cultivation decisions by:

* Predicting future vegetable prices using climate and regional data
* Comparing multiple crop options
* Recommending the most profitable crops for cultivation
* Providing AI-powered farming insights and decision support
* Integrating real-time weather data
* Analyzing multiple scenarios for risk management
* Visualizing climate and market trends

Instead of simply predicting a price, AgriMind AI acts as an intelligent assistant that helps farmers choose what to grow based on data-driven recommendations.

---

## Why This Project?

This project was inspired by farming communities in Nuwara Eliya, Sri Lanka, where vegetable cultivation is a major source of income.

Farmers often need to make important decisions without access to reliable data or predictive insights. AgriMind AI aims to bridge this gap by combining machine learning, climate information, and market trends to support better farming decisions.

---
* Humidity data
* Crop Yield Impact Scores
* Historical vegetable prices

---

## Machine Learning Model

Current model:

* Random Forest Regressor

Input Features:

* Region
* Temperature (°C)
* Rainfall (mm)
* Humidity (%)
* Crop Yield Impact Score
* Vegetable Commodity

Output:

* Predicted Vegetable Price (LKR/kg)

---

## Project Structure

AgriMind-AI

├── backend

│ ├── train_model.py

│ ├── explore_dataset.py

│ ├── model.pkl

│ └── venv/

│

├── frontend/

│

├── dataset/

│ └── Vegetables_fruit_prices_with_climate_130000_2020_to_2025.csv

│

├── diagrams/

│

├── .gitignore

└── README.md

---

## Future Enhancements

* Real-time weather integration
* Real-time market price integration
* Sinhala language support
* Tamil language support
* AI chatbot for farming assistance
* Mobile application for farmers
* Advanced crop yield prediction
* Personalized farming recommendations

---

## Current Status

🚧 Under Development

AgriMind AI is currently being developed as part of the Microsoft Agents League Hackathon.

Current Progress:

* Project setup completed
* Dataset exploration completed
* Data preprocessing completed
* Machine learning model trained
* Model persistence implemented

Upcoming:

* Flask API development
* Crop recommendation engine
* React frontend
* Dashboard implementation
* AI advisor integration

---

## License

This project is developed for educational and hackathon purposes.
