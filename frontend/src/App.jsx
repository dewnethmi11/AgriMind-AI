import { useState } from "react";
import axios from "axios";
import "./App.css";
import PriceChart from "./PriceChart";

function App() {
  const regions = [
    "Ampara","Anuradhapura","Badulla","Batticaloa","Colombo","Galle",
    "Gampaha","Hambantota","Jaffna","Kalutara","Kandy","Kegalle",
    "Kilinochchi","Kurunegala","Mannar","Matale","Matara","Monaragala",
    "Mullaitivu","Nuwara Eliya","Polonnaruwa","Puttalam","Ratnapura",
    "Trincomalee","Vavuniya"
  ];

  const supportedRegions = [
    'Nuwara Eliya', 'Kandy', 'Colombo', 'Galle', 'Jaffna', 'Badulla', 'Matara', 'Ratnapura'
  ];

  const vegetables = [
    "Winged Bean","Bitter Melon","Brinjal","Long Purple Eggplant",
    "Asiatic Pennywort","Red Spinach","Pennywort","Leeks","Carrot",
    "Beetroot","Cabbage","Knol-Khol","Pumpkin","Onion","Potato",
    "Drumsticks","Jackfruit","Breadfruit","Taro","Manioc"
  ];

  const [activeTab, setActiveTab] = useState("v1-price");
  
  // V1.0 State
  const [formData, setFormData] = useState({
    Region: "Colombo",
    Temperature: "",
    Rainfall: "",
    Humidity: "",
    CropYield: "",
    Vegetable: "Carrot"
  });

  const [price, setPrice] = useState(null);
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);

  // V2.0 State
  const [v2Region, setV2Region] = useState("Nuwara Eliya");
  const [v2ClimateData, setV2ClimateData] = useState({
    Temperature: 20,
    Rainfall: 100,
    Humidity: 60,
    CropYield: 50
  });
  const [recommendations, setRecommendations] = useState(null);
  const [weatherData, setWeatherData] = useState(null);
  const [adviceData, setAdviceData] = useState(null);
  const [decisionData, setDecisionData] = useState(null);
  const [comprehensiveData, setComprehensiveData] = useState(null);
  const [v2Loading, setV2Loading] = useState(false);

  // V1.0 Functions
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const resetForm = () => {
    setFormData({
      Region: "Colombo",
      Temperature: "",
      Rainfall: "",
      Humidity: "",
      CropYield: "",
      Vegetable: "Carrot"
    });
    setPrice(null);
  };

  const predictPrice = async () => {
    if (
      !formData.Temperature ||
      !formData.Rainfall ||
      !formData.Humidity ||
      !formData.CropYield
    ) {
      alert("Please fill all fields");
      return;
    }

    try {
      setLoading(true);
      const response = await axios.post(
        "http://127.0.0.1:5000/predict",
        formData
      );
      const predicted = response.data.predicted_price;
      setPrice(predicted);
      setHistory((prev) => [
        ...prev,
        {
          vegetable: formData.Vegetable,
          price: predicted
        }
      ]);
    } catch (error) {
      console.error(error);
      alert("Prediction failed: " + error.message);
    } finally {
      setLoading(false);
    }
  };

  // V2.0 Functions
  const handleV2ClimateChange = (e) => {
    setV2ClimateData({
      ...v2ClimateData,
      [e.target.name]: parseFloat(e.target.value)
    });
  };

  const getRecommendations = async () => {
    try {
      setV2Loading(true);
      const response = await axios.post(
        "http://127.0.0.1:5000/recommend-crops",
        {
          Region: v2Region,
          ...v2ClimateData
        }
      );
      setRecommendations(response.data.recommendations);
    } catch (error) {
      console.error(error);
      alert("Failed to get recommendations: " + error.message);
    } finally {
      setV2Loading(false);
    }
  };

  const getWeatherData = async () => {
    try {
      setV2Loading(true);
      const response = await axios.get(
        `http://127.0.0.1:5000/weather/${v2Region}`
      );
      setWeatherData(response.data);
    } catch (error) {
      console.error(error);
      alert("Weather data not available for this region. Available: Nuwara Eliya, Kandy, Colombo, Galle, Jaffna, Badulla, Matara, Ratnapura");
    } finally {
      setV2Loading(false);
    }
  };

  const getAdvice = async () => {
    if (!recommendations) {
      alert("Get recommendations first!");
      return;
    }
    try {
      setV2Loading(true);
      const response = await axios.post(
        "http://127.0.0.1:5000/advisor",
        {
          recommendations: recommendations,
          weather: {
            temperature: v2ClimateData.Temperature,
            humidity: v2ClimateData.Humidity,
            precipitation: v2ClimateData.Rainfall
          }
        }
      );
      setAdviceData(response.data.advice);
    } catch (error) {
      console.error(error);
      alert("Failed to get advice: " + error.message);
    } finally {
      setV2Loading(false);
    }
  };

  const getDecisionSupport = async () => {
    try {
      setV2Loading(true);
      const response = await axios.post(
        "http://127.0.0.1:5000/decision-support",
        {
          Region: v2Region,
          ...v2ClimateData
        }
      );
      setDecisionData(response.data);
    } catch (error) {
      console.error(error);
      alert("Failed to get decision support: " + error.message);
    } finally {
      setV2Loading(false);
    }
  };

  const getComprehensiveAnalysis = async () => {
    try {
      setV2Loading(true);
      const response = await axios.post(
        "http://127.0.0.1:5000/comprehensive-analysis",
        {
          Region: v2Region,
          ...v2ClimateData
        }
      );
      setComprehensiveData(response.data);
    } catch (error) {
      console.error(error);
      alert("Failed to get comprehensive analysis: " + error.message);
    } finally {
      setV2Loading(false);
    }
  };

  return (
    <div className="container">
      <h1>🌱 AgriMind AI</h1>
      <p className="subtitle">
        Intelligent Farming Decision Assistant - v2.0
      </p>

      {/* TAB NAVIGATION */}
      <div className="tabs">
        <button
          className={`tab-btn ${activeTab === "v1-price" ? "active" : ""}`}
          onClick={() => setActiveTab("v1-price")}
        >
          💰 Price Prediction (v1.0)
        </button>
        <button
          className={`tab-btn ${activeTab === "v2-crops" ? "active" : ""}`}
          onClick={() => setActiveTab("v2-crops")}
        >
          🌾 Crop Recommendation (v2.0)
        </button>
        <button
          className={`tab-btn ${activeTab === "v2-weather" ? "active" : ""}`}
          onClick={() => setActiveTab("v2-weather")}
        >
          🌦 Weather (v2.0)
        </button>
        <button
          className={`tab-btn ${activeTab === "v2-advisor" ? "active" : ""}`}
          onClick={() => setActiveTab("v2-advisor")}
        >
          🤖 AI Advisor (v2.0)
        </button>
        <button
          className={`tab-btn ${activeTab === "v2-decision" ? "active" : ""}`}
          onClick={() => setActiveTab("v2-decision")}
        >
          📊 Decision Support (v2.0)
        </button>
        <button
          className={`tab-btn ${activeTab === "v2-comprehensive" ? "active" : ""}`}
          onClick={() => setActiveTab("v2-comprehensive")}
        >
          🎯 Full Analysis (v2.0)
        </button>
      </div>

      {/* ============= V1.0: PRICE PREDICTION ============= */}
      {activeTab === "v1-price" && (
        <div>
          <div className="card">
            <h2>💰 Price Prediction</h2>
            <p className="section-desc">Predict vegetable prices based on climate conditions</p>

            <label>Region</label>
            <select name="Region" value={formData.Region} onChange={handleChange}>
              {regions.map((r) => (
                <option key={r}>{r}</option>
              ))}
            </select>

            <label>Temperature (°C)</label>
            <input type="number" name="Temperature" value={formData.Temperature} onChange={handleChange} />

            <label>Rainfall (mm)</label>
            <input type="number" name="Rainfall" value={formData.Rainfall} onChange={handleChange} />

            <label>Humidity (%)</label>
            <input type="number" name="Humidity" value={formData.Humidity} onChange={handleChange} />

            <label>Crop Yield Score</label>
            <input type="number" step="0.1" name="CropYield" value={formData.CropYield} onChange={handleChange} />

            <label>Vegetable</label>
            <select name="Vegetable" value={formData.Vegetable} onChange={handleChange}>
              {vegetables.map((v) => (
                <option key={v}>{v}</option>
              ))}
            </select>

            <div className="button-group">
              <button className="predict-btn" onClick={predictPrice} disabled={loading}>
                {loading ? "Predicting..." : "Predict Price"}
              </button>
              <button className="reset-btn" onClick={resetForm}>
                Reset
              </button>
            </div>
          </div>

          <div className="weather-card">
            <h3>🌦 Input Summary</h3>
            <p><strong>Region:</strong> {formData.Region}</p>
            <p><strong>Temperature:</strong> {formData.Temperature || "-"} °C</p>
            <p><strong>Rainfall:</strong> {formData.Rainfall || "-"} mm</p>
            <p><strong>Humidity:</strong> {formData.Humidity || "-"} %</p>
          </div>

          {price !== null && (
            <div className="result-card">
              <h2>💰 Prediction Result</h2>
              <h1>Rs {price}</h1>
              <p>Estimated price for <strong>{formData.Vegetable}</strong></p>
            </div>
          )}

          {price !== null && <PriceChart predictedPrice={price} />}

          {history.length > 0 && (
            <div className="history">
              <h2>📊 Prediction History</h2>
              <table>
                <thead>
                  <tr>
                    <th>Vegetable</th>
                    <th>Price (Rs)</th>
                  </tr>
                </thead>
                <tbody>
                  {history.map((item, index) => (
                    <tr key={index}>
                      <td>{item.vegetable}</td>
                      <td>Rs {item.price}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      )}

      {/* ============= V2.0: CROP RECOMMENDATION ============= */}
      {activeTab === "v2-crops" && (
        <div>
          <div className="card">
            <h2>🌾 Crop Recommendation Engine</h2>
            <p className="section-desc">Get AI-powered crop recommendations based on climate and market data</p>

            <label>Region</label>
            <select value={v2Region} onChange={(e) => setV2Region(e.target.value)}>
              {regions.map((r) => (
                <option key={r}>{r}</option>
              ))}
            </select>

            <label>Temperature (°C)</label>
            <input 
              type="number" 
              name="Temperature" 
              value={v2ClimateData.Temperature} 
              onChange={handleV2ClimateChange}
            />

            <label>Rainfall (mm)</label>
            <input 
              type="number" 
              name="Rainfall" 
              value={v2ClimateData.Rainfall} 
              onChange={handleV2ClimateChange}
            />

            <label>Humidity (%)</label>
            <input 
              type="number" 
              name="Humidity" 
              value={v2ClimateData.Humidity} 
              onChange={handleV2ClimateChange}
            />

            <label>Crop Yield Score</label>
            <input 
              type="number" 
              step="0.1"
              name="CropYield" 
              value={v2ClimateData.CropYield} 
              onChange={handleV2ClimateChange}
            />

            <div className="button-group">
              <button className="predict-btn" onClick={getRecommendations} disabled={v2Loading}>
                {v2Loading ? "Analyzing..." : "Get Recommendations"}
              </button>
            </div>
          </div>

          {recommendations && (
            <div className="results-container">
              <h2>🏆 Top Crop Recommendations</h2>
              {recommendations.map((rec, idx) => (
                <div key={idx} className="recommendation-card">
                  <div className="rec-header">
                    <h3>#{idx + 1} - {rec.crop}</h3>
                    <span className="profitability-score">Score: {rec.profitability_score}</span>
                  </div>
                  <div className="rec-details">
                    <p><strong>Predicted Price:</strong> Rs {rec.predicted_price}/kg</p>
                    <p><strong>Yield Suitability:</strong> {rec.yield_suitability}%</p>
                    <p><strong>Expected Yield:</strong> {rec.expected_yield} units</p>
                    <p><strong>Market Demand:</strong> {rec.market_demand}%</p>
                    <p><strong>Revenue Estimate:</strong> Rs {rec.revenue_estimate}</p>
                    <p><strong>Why:</strong> {rec.reasoning}</p>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* ============= V2.0: WEATHER INTEGRATION ============= */}
      {activeTab === "v2-weather" && (
        <div>
          <div className="card">
            <h2>🌦 Weather Integration</h2>
            <p className="section-desc">Get real-time weather and forecast for your region</p>
            <p className="note">Supported regions: Nuwara Eliya, Kandy, Colombo, Galle, Jaffna, Badulla, Matara, Ratnapura</p>

            <label>Region</label>
            <select value={v2Region} onChange={(e) => setV2Region(e.target.value)}>
              {supportedRegions.map((r) => (
                <option key={r}>{r}</option>
              ))}
            </select>

            <div className="button-group">
              <button className="predict-btn" onClick={getWeatherData} disabled={v2Loading}>
                {v2Loading ? "Loading..." : "Get Weather Data"}
              </button>
            </div>
          </div>

          {weatherData && (
            <div className="results-container">
              {weatherData.current_weather && (
                <div className="weather-card">
                  <h3>🌍 Current Weather - {weatherData.region}</h3>
                  <p><strong>Temperature:</strong> {weatherData.current_weather.temperature}°C</p>
                  <p><strong>Humidity:</strong> {weatherData.current_weather.humidity}%</p>
                  <p><strong>Precipitation:</strong> {weatherData.current_weather.precipitation}mm</p>
                  <p><strong>Condition:</strong> {weatherData.current_weather.description}</p>
                </div>
              )}

              {weatherData.seasonal_analysis && (
                <div className="weather-card">
                  <h3>📈 Seasonal Analysis</h3>
                  <p><strong>Avg Temperature:</strong> {weatherData.seasonal_analysis.forecast_avg.temperature}°C</p>
                  <p><strong>Avg Humidity:</strong> {weatherData.seasonal_analysis.forecast_avg.humidity}%</p>
                  <p><strong>Expected Rainfall:</strong> {weatherData.seasonal_analysis.forecast_avg.expected_rainfall}mm</p>
                  <p><strong>Trend:</strong> {weatherData.seasonal_analysis.trend}</p>
                  <h4>Farming Insights:</h4>
                  <ul>
                    {weatherData.seasonal_analysis.farming_insights.map((insight, idx) => (
                      <li key={idx}>{insight}</li>
                    ))}
                  </ul>
                </div>
              )}

              {weatherData.planting_window && (
                <div className="weather-card">
                  <h3>🌱 Optimal Planting Window</h3>
                  <p><strong>Recommendation:</strong> {weatherData.planting_window.recommendation}</p>
                  {weatherData.planting_window.optimal_windows.length > 0 && (
                    <div>
                      <h4>Best Days to Plant:</h4>
                      {weatherData.planting_window.optimal_windows.map((window, idx) => (
                        <p key={idx}><strong>{window.date}</strong> - Score: {window.score}% - {window.conditions}</p>
                      ))}
                    </div>
                  )}
                </div>
              )}
            </div>
          )}
        </div>
      )}

      {/* ============= V2.0: AI ADVISOR ============= */}
      {activeTab === "v2-advisor" && (
        <div>
          <div className="card">
            <h2>🤖 AI Farming Advisor</h2>
            <p className="section-desc">Get intelligent farming advice based on data analysis</p>

            <label>Region</label>
            <select value={v2Region} onChange={(e) => setV2Region(e.target.value)}>
              {regions.map((r) => (
                <option key={r}>{r}</option>
              ))}
            </select>

            <label>Temperature (°C)</label>
            <input 
              type="number" 
              name="Temperature" 
              value={v2ClimateData.Temperature} 
              onChange={handleV2ClimateChange}
            />

            <label>Rainfall (mm)</label>
            <input 
              type="number" 
              name="Rainfall" 
              value={v2ClimateData.Rainfall} 
              onChange={handleV2ClimateChange}
            />

            <label>Humidity (%)</label>
            <input 
              type="number" 
              name="Humidity" 
              value={v2ClimateData.Humidity} 
              onChange={handleV2ClimateChange}
            />

            <label>Crop Yield Score</label>
            <input 
              type="number" 
              step="0.1"
              name="CropYield" 
              value={v2ClimateData.CropYield} 
              onChange={handleV2ClimateChange}
            />

            <div className="button-group">
              <button className="predict-btn" onClick={getRecommendations} disabled={v2Loading}>
                {v2Loading ? "Analyzing..." : "Step 1: Get Recommendations"}
              </button>
              <button className="predict-btn" onClick={getAdvice} disabled={v2Loading || !recommendations}>
                {v2Loading ? "Analyzing..." : "Step 2: Get AI Advice"}
              </button>
            </div>
          </div>

          {adviceData && (
            <div className="results-container">
              <div className="advice-card">
                <h3>💡 AI Advisor Summary</h3>
                <p className="summary-text">{adviceData.summary}</p>
              </div>

              {adviceData.detailed_advice && (
                <>
                  <div className="advice-card">
                    <h3>🌾 Crop Selection</h3>
                    <p><strong>{adviceData.detailed_advice.crop_selection.primary_recommendation}</strong></p>
                    <p>{adviceData.detailed_advice.crop_selection.rationale}</p>
                    <p><strong>Risk Level:</strong> {adviceData.detailed_advice.crop_selection.risk_level}</p>
                  </div>

                  <div className="advice-card">
                    <h3>⏰ Timing Guidance</h3>
                    <p><strong>{adviceData.detailed_advice.timing_guidance.recommendation}</strong></p>
                    <p><strong>Reason:</strong> {adviceData.detailed_advice.timing_guidance.reason}</p>
                    <p><strong>Suggested Window:</strong> {adviceData.detailed_advice.timing_guidance.suggested_window}</p>
                  </div>

                  <div className="advice-card">
                    <h3>⚠️ Risk Mitigation</h3>
                    {adviceData.detailed_advice.risk_mitigation.identified_risks.map((risk, idx) => (
                      <div key={idx} className="risk-item">
                        <p><strong>{risk.type}</strong> (Severity: {risk.severity})</p>
                        <p>Mitigation: {risk.mitigation}</p>
                      </div>
                    ))}
                  </div>

                  <div className="advice-card">
                    <h3>💼 Market Strategy</h3>
                    <p><strong>Opportunity:</strong> {adviceData.detailed_advice.market_strategy.market_opportunity}</p>
                    <p><strong>Expected Price:</strong> {adviceData.detailed_advice.market_strategy.expected_price}</p>
                    <p><strong>Revenue Estimate:</strong> {adviceData.detailed_advice.market_strategy.expected_revenue}</p>
                  </div>

                  <div className="advice-card">
                    <h3>✅ Next Actions</h3>
                    <ol>
                      {adviceData.next_actions.map((action, idx) => (
                        <li key={idx}>{action}</li>
                      ))}
                    </ol>
                  </div>
                </>
              )}
            </div>
          )}
        </div>
      )}

      {/* ============= V2.0: DECISION SUPPORT ============= */}
      {activeTab === "v2-decision" && (
        <div>
          <div className="card">
            <h2>📊 Decision Support System</h2>
            <p className="section-desc">Autonomous decision-making with scenario analysis</p>

            <label>Region</label>
            <select value={v2Region} onChange={(e) => setV2Region(e.target.value)}>
              {regions.map((r) => (
                <option key={r}>{r}</option>
              ))}
            </select>

            <label>Temperature (°C)</label>
            <input 
              type="number" 
              name="Temperature" 
              value={v2ClimateData.Temperature} 
              onChange={handleV2ClimateChange}
            />

            <label>Rainfall (mm)</label>
            <input 
              type="number" 
              name="Rainfall" 
              value={v2ClimateData.Rainfall} 
              onChange={handleV2ClimateChange}
            />

            <label>Humidity (%)</label>
            <input 
              type="number" 
              name="Humidity" 
              value={v2ClimateData.Humidity} 
              onChange={handleV2ClimateChange}
            />

            <label>Crop Yield Score</label>
            <input 
              type="number" 
              step="0.1"
              name="CropYield" 
              value={v2ClimateData.CropYield} 
              onChange={handleV2ClimateChange}
            />

            <div className="button-group">
              <button className="predict-btn" onClick={getDecisionSupport} disabled={v2Loading}>
                {v2Loading ? "Analyzing..." : "Analyze Scenarios"}
              </button>
            </div>
          </div>

          {decisionData && (
            <div className="results-container">
              <div className="decision-card">
                <h3>🎯 Decision Summary</h3>
                <p className="summary-text">{decisionData.decision_summary}</p>
              </div>

              {decisionData.analysis && (
                <>
                  <div className="scenario-container">
                    <div className="scenario optimistic">
                      <h3>📈 Optimistic Scenario (20-25%)</h3>
                      <p><strong>Crop:</strong> {decisionData.analysis.scenarios.optimistic.crop}</p>
                      <p><strong>Price:</strong> Rs {decisionData.analysis.scenarios.optimistic.predicted_price}</p>
                      <p><strong>Revenue:</strong> Rs {decisionData.analysis.scenarios.optimistic.estimated_revenue}</p>
                      <p><strong>Profit:</strong> Rs {decisionData.analysis.scenarios.optimistic.profit_per_hectare}</p>
                    </div>

                    <div className="scenario realistic">
                      <h3>📊 Realistic Scenario (50-60%)</h3>
                      <p><strong>Crop:</strong> {decisionData.analysis.scenarios.realistic.crop}</p>
                      <p><strong>Price:</strong> Rs {decisionData.analysis.scenarios.realistic.predicted_price}</p>
                      <p><strong>Revenue:</strong> Rs {decisionData.analysis.scenarios.realistic.estimated_revenue}</p>
                      <p><strong>Profit:</strong> Rs {decisionData.analysis.scenarios.realistic.profit_per_hectare}</p>
                    </div>

                    <div className="scenario pessimistic">
                      <h3>📉 Pessimistic Scenario (15-20%)</h3>
                      <p><strong>Crop:</strong> {decisionData.analysis.scenarios.pessimistic.crop}</p>
                      <p><strong>Price:</strong> Rs {decisionData.analysis.scenarios.pessimistic.predicted_price}</p>
                      <p><strong>Revenue:</strong> Rs {decisionData.analysis.scenarios.pessimistic.estimated_revenue}</p>
                      <p><strong>Profit:</strong> Rs {decisionData.analysis.scenarios.pessimistic.profit_per_hectare}</p>
                    </div>
                  </div>

                  <div className="decision-card">
                    <h3>💰 Risk-Adjusted Return</h3>
                    <p><strong>Expected Profit:</strong> Rs {decisionData.analysis.risk_adjusted_return.expected_profit}</p>
                    <p><strong>Confidence Range:</strong> {decisionData.analysis.risk_adjusted_return.confidence_interval}</p>
                    <p><strong>Sharpe Ratio:</strong> {decisionData.analysis.risk_adjusted_return.sharpe_ratio}</p>
                  </div>

                  <div className="decision-card">
                    <h3>🏆 Decision Matrix</h3>
                    <table>
                      <thead>
                        <tr>
                          <th>Rank</th>
                          <th>Crop</th>
                          <th>Profitability</th>
                          <th>Yield %</th>
                          <th>Price</th>
                          <th>Risk</th>
                        </tr>
                      </thead>
                      <tbody>
                        {decisionData.analysis.decision_matrix.map((item, idx) => (
                          <tr key={idx}>
                            <td>{item.rank}</td>
                            <td>{item.crop}</td>
                            <td>{item.profitability}</td>
                            <td>{item.yield_suitability}</td>
                            <td>{item.price}</td>
                            <td>{item.risk}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>

                  <div className="decision-card">
                    <h3>⚡ Contingency Plans</h3>
                    {decisionData.analysis.contingency_plans.map((plan, idx) => (
                      <div key={idx} className="contingency-item">
                        <p><strong>Event:</strong> {plan.event} (Probability: {plan.probability})</p>
                        <p><strong>Impact:</strong> {plan.impact}</p>
                        <p><strong>Mitigation:</strong></p>
                        <ul>
                          {plan.mitigation.map((m, i) => (
                            <li key={i}>{m}</li>
                          ))}
                        </ul>
                      </div>
                    ))}
                  </div>
                </>
              )}
            </div>
          )}
        </div>
      )}

      {/* ============= V2.0: COMPREHENSIVE ANALYSIS ============= */}
      {activeTab === "v2-comprehensive" && (
        <div>
          <div className="card">
            <h2>🎯 Complete Farm Analysis</h2>
            <p className="section-desc">Integrated analysis combining all features</p>

            <label>Region</label>
            <select value={v2Region} onChange={(e) => setV2Region(e.target.value)}>
              {regions.map((r) => (
                <option key={r}>{r}</option>
              ))}
            </select>

            <label>Temperature (°C)</label>
            <input 
              type="number" 
              name="Temperature" 
              value={v2ClimateData.Temperature} 
              onChange={handleV2ClimateChange}
            />

            <label>Rainfall (mm)</label>
            <input 
              type="number" 
              name="Rainfall" 
              value={v2ClimateData.Rainfall} 
              onChange={handleV2ClimateChange}
            />

            <label>Humidity (%)</label>
            <input 
              type="number" 
              name="Humidity" 
              value={v2ClimateData.Humidity} 
              onChange={handleV2ClimateChange}
            />

            <label>Crop Yield Score</label>
            <input 
              type="number" 
              step="0.1"
              name="CropYield" 
              value={v2ClimateData.CropYield} 
              onChange={handleV2ClimateChange}
            />

            <div className="button-group">
              <button className="predict-btn" onClick={getComprehensiveAnalysis} disabled={v2Loading}>
                {v2Loading ? "Analyzing..." : "Generate Full Analysis"}
              </button>
            </div>
          </div>

          {comprehensiveData && (
            <div className="results-container">
              <div className="comprehensive-summary">
                <h2>📋 Analysis for {comprehensiveData.region}</h2>
                <p className="section-desc">Complete farming intelligence dashboard</p>
              </div>

              {comprehensiveData.crop_recommendations && (
                <div>
                  <h3>🌾 Top Crop Recommendations</h3>
                  {comprehensiveData.crop_recommendations.slice(0, 3).map((rec, idx) => (
                    <div key={idx} className="recommendation-card compact">
                      <p><strong>#{idx + 1} {rec.crop}</strong> - Score: {rec.profitability_score}</p>
                      <p>Price: Rs {rec.predicted_price} | Yield: {rec.yield_suitability}% | Revenue: Rs {rec.revenue_estimate}</p>
                    </div>
                  ))}
                </div>
              )}

              {comprehensiveData.weather_data && comprehensiveData.weather_data.current && (
                <div className="weather-card">
                  <h3>🌦 Current Weather</h3>
                  <p><strong>Temperature:</strong> {comprehensiveData.weather_data.current.temperature}°C</p>
                  <p><strong>Humidity:</strong> {comprehensiveData.weather_data.current.humidity}%</p>
                  <p><strong>Condition:</strong> {comprehensiveData.weather_data.current.description}</p>
                </div>
              )}

              {comprehensiveData.decision_support && (
                <div className="decision-card">
                  <h3>🎯 Decision Summary</h3>
                  <p className="summary-text">{comprehensiveData.decision_support.summary}</p>
                </div>
              )}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default App;