# AgriMind AI v2.0 - Setup & Startup Guide

## 🚀 Quick Start (5 Minutes)

### Prerequisites
- Python 3.8+ installed
- Node.js 14+ installed
- Git (for cloning)

### Step 1: Backend Setup (2 min)
```bash
# Navigate to backend directory
cd backend

# Install dependencies
pip install -r requirements.txt

# Start the backend server
python app.py

# Expected output:
# * Running on http://127.0.0.1:5000
# * Debug mode: on
```

### Step 2: Frontend Setup (2 min)
**In a NEW terminal window:**
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev

# Expected output:
# VITE v... ready in ... ms
# ➜  Local: http://localhost:5173/
```

### Step 3: Access the App (1 min)
1. Open browser: `http://localhost:5173`
2. You should see AgriMind AI v2.0 with 6 tabs
3. Start by clicking "Full Analysis" tab
4. Enter sample data and click "Generate Full Analysis"

---

## 📋 Detailed Installation Guide

### Backend Installation

#### 1. Clone or Navigate to Project
```bash
cd AgriMind-AI/backend
```

#### 2. Create Virtual Environment (Optional but Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Verify Installation
```bash
# Run setup verification script
python setup_verify.py

# You should see:
# ✓ Checking Python version...
# ✓ Checking dependencies...
# ✓ Checking ML models...
```

#### 5. Start Backend
```bash
python app.py

# Should see:
# * Running on http://127.0.0.1:5000
# * WARNING: This is a development server...
```

### Frontend Installation

#### 1. Navigate to Frontend
```bash
cd ../frontend
```

#### 2. Install Dependencies
```bash
npm install
```

#### 3. Start Development Server
```bash
npm run dev

# Should see:
# ➜  Local: http://localhost:5173/
# ➜  Press q to quit
```

#### 4. Build for Production (Optional)
```bash
npm run build

# Creates optimized build in dist/
```

---

## 🧪 Testing the Installation

### Test Backend Health
```bash
# In a terminal or browser:
curl http://127.0.0.1:5000/health

# Expected response:
{
  "status": "healthy",
  "service": "AgriMind AI v2.0",
  "timestamp": "2024-06-14T15:30:00Z"
}
```

### Test Crop Recommendations
```bash
curl -X POST http://127.0.0.1:5000/recommend-crops \
  -H "Content-Type: application/json" \
  -d '{
    "Region": "Colombo",
    "Temperature": 28,
    "Rainfall": 100,
    "Humidity": 75,
    "CropYield": 50
  }'

# Should return crop recommendations
```

### Test Weather Data
```bash
curl http://127.0.0.1:5000/weather/Nuwara%20Eliya

# Should return current weather and forecast
```

### Test Frontend
1. Open http://localhost:5173
2. All tabs should load without errors
3. Try clicking "Full Analysis" and entering sample data

---

## 📁 Project Structure

```
AgriMind-AI/
├── backend/                    # Python Flask backend
│   ├── app.py                 # Main Flask application
│   ├── crop_recommender.py    # Crop recommendation engine
│   ├── weather_service.py     # Weather integration
│   ├── ai_advisor.py          # AI advisor module
│   ├── decision_agent.py      # Decision support agent
│   ├── requirements.txt       # Python dependencies
│   ├── setup_verify.py        # Setup verification script
│   ├── model.pkl              # ML model (trained)
│   ├── region_encoder.pkl     # Region encoder
│   └── veg_encoder.pkl        # Vegetable encoder
│
├── frontend/                   # React frontend
│   ├── src/
│   │   ├── App.jsx            # Main app component (v2.0)
│   │   ├── App.css            # Enhanced styling
│   │   ├── PriceChart.jsx     # Chart component
│   │   └── main.jsx
│   ├── package.json
│   ├── vite.config.js
│   └── index.html
│
├── dataset/                    # Training data
├── README.md                   # Project overview
├── V2.0_FEATURES.md           # v2.0 feature documentation
└── SETUP_GUIDE.md             # This file
```

---

## ⚙️ Environment Configuration

### Backend Configuration
The backend runs on:
- **Host**: 127.0.0.1
- **Port**: 5000
- **Debug Mode**: ON (for development)

To change:
Edit `app.py` last line:
```python
if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Modify port here
```

### Frontend Configuration
The frontend runs on:
- **Host**: localhost
- **Port**: 5173

To change:
Edit `frontend/vite.config.js`:
```javascript
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173  // Change here
  }
})
```

### API Base URL
Frontend API calls to `http://127.0.0.1:5000/`

To change:
Search in `App.jsx` for `http://127.0.0.1:5000/` and update URLs

---

## 🛠️ Common Issues & Fixes

### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution**: Install requirements
```bash
pip install -r requirements.txt
```

### Issue: "Port 5000 already in use"
**Solution**: Either:
1. Kill process using port 5000:
   - Windows: `netstat -ano | findstr :5000` then `taskkill /PID <PID> /F`
   - macOS/Linux: `lsof -i :5000` then `kill -9 <PID>`
2. Change port in app.py (line at bottom)

### Issue: "Port 5173 already in use"
**Solution**: Vite will auto-increment to 5174, 5175, etc.
Or kill the process and restart.

### Issue: Frontend shows "Cannot GET /"
**Solution**: Make sure you're accessing:
- `http://localhost:5173/` (not 5000)
- Development server is running with `npm run dev`

### Issue: CORS error when calling API
**Solution**:
1. Verify backend is running on port 5000
2. Check CORS headers are enabled (they are by default)
3. Verify frontend is on port 5173

### Issue: Weather data not loading
**Solution**:
1. Check internet connection (uses free API)
2. Use supported region (Nuwara Eliya, Kandy, Colombo, etc.)
3. Check console errors in browser DevTools

### Issue: ML Models Missing (model.pkl not found)
**Solution**: Train the model
```bash
cd backend
python train_model.py
```

### Issue: "Cannot find module 'axios'" in frontend
**Solution**: Reinstall npm packages
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

---

## 🔍 Verification Checklist

After installation, verify:

- [ ] Backend runs without errors: `python app.py`
- [ ] Frontend runs without errors: `npm run dev`
- [ ] Health endpoint responds: `curl http://127.0.0.1:5000/health`
- [ ] Frontend loads: `http://localhost:5173`
- [ ] Can switch between tabs
- [ ] Can enter climate data
- [ ] "Full Analysis" works and returns data
- [ ] Weather tab works for supported regions
- [ ] No console errors in browser DevTools
- [ ] No errors in terminal output

---

## 📊 Sample Test Data

### Test Input 1: Nuwara Eliya (Highland Region)
```json
{
  "Region": "Nuwara Eliya",
  "Temperature": 18,
  "Rainfall": 200,
  "Humidity": 85,
  "CropYield": 75
}
```

### Test Input 2: Colombo (Coastal Region)
```json
{
  "Region": "Colombo",
  "Temperature": 28,
  "Rainfall": 100,
  "Humidity": 70,
  "CropYield": 50
}
```

### Test Input 3: Badulla (Middle Region)
```json
{
  "Region": "Badulla",
  "Temperature": 25,
  "Rainfall": 150,
  "Humidity": 75,
  "CropYield": 60
}
```

Try these inputs in the "Full Analysis" tab to see how the system responds.

---

## 🚀 Next Steps

### After Getting It Running
1. **Explore Features**: Try each tab to understand functionality
2. **Read Documentation**: Check `V2.0_FEATURES.md` for detailed feature info
3. **Test APIs**: Use cURL or Postman to test endpoints
4. **Customize**: Modify climate data to see how recommendations change
5. **Deploy**: See deployment guide below

### Production Deployment
For production deployment:

**Backend (Heroku Example)**:
```bash
# Create Procfile in backend/
web: gunicorn app:app

# Deploy
git push heroku main
```

**Frontend (Netlify/Vercel)**:
```bash
# Build
npm run build

# Deploy dist/ folder
# On Netlify: Drag and drop dist/
# On Vercel: Connect GitHub repo
```

---

## 📞 Getting Help

### Troubleshooting Resources
1. Check console output (terminal and browser DevTools)
2. Read error messages carefully
3. Verify all dependencies installed
4. Try restarting servers
5. Check firewall isn't blocking ports

### Documentation Files
- `README.md` - Project overview
- `V2.0_FEATURES.md` - Feature documentation
- `SETUP_GUIDE.md` - This file
- Backend code comments - Detailed explanations

---

## 🎓 Understanding the System

### Data Flow
```
User Input (Climate Data)
    ↓
Backend API Endpoint
    ↓
ML Model + Business Logic
    ↓
AI Analysis (Recommendations, Weather, Advice, Decisions)
    ↓
JSON Response
    ↓
Frontend Display
    ↓
User Views Results
```

### Key Modules
1. **Crop Recommender**: ML-based price + yield analysis
2. **Weather Service**: Real-time data via OpenMeteo API
3. **AI Advisor**: Rule-based contextual guidance
4. **Decision Agent**: Scenario analysis and planning

### Technologies
- **Backend**: Python 3, Flask
- **Frontend**: React 19, Vite
- **Database**: Not required (stateless)
- **ML**: Scikit-Learn, Joblib
- **API**: RESTful JSON endpoints
- **Weather**: OpenMeteo (free, no key)

---

## 🔐 Security Notes

- **No Authentication**: System is open-access (add if needed for production)
- **No Database**: All processing is stateless
- **Free Weather API**: No sensitive API keys stored
- **CORS Enabled**: Allows frontend to call backend
- **Input Validation**: Basic validation on inputs

For production, consider:
- Adding authentication/authorization
- Rate limiting
- Input validation/sanitization
- HTTPS/SSL
- Environment variables for config
- Error logging and monitoring

---

## 📈 Performance Optimization

### Backend Performance
- Response time: < 500ms per request
- Concurrent requests: Handled by Flask
- ML model: Pre-loaded for fast inference
- Weather API: Cached responses (configurable)

### Frontend Performance
- Vite: Fast development server
- React: Optimized rendering
- CSS: Modern styling with minimal overhead
- Responsive: Works on mobile/tablet/desktop

### Scaling Considerations
For production scaling:
- Use Gunicorn + Nginx for backend
- Implement caching (Redis)
- Database for user data (PostgreSQL)
- Load balancing
- CDN for static files

---

## 🎯 Quick Commands Reference

```bash
# Backend
cd backend
pip install -r requirements.txt     # Install
python app.py                       # Run
python setup_verify.py              # Verify setup
python train_model.py              # Train ML model (if needed)

# Frontend
cd frontend
npm install                         # Install
npm run dev                         # Run dev server
npm run build                       # Build for production
npm run preview                     # Preview production build
```

---

## 📚 Learning Path

### For Beginners
1. Install and run both servers
2. Explore frontend tabs
3. Try sample data
4. Read feature documentation
5. Experiment with different inputs

### For Developers
1. Review architecture
2. Understand ML models
3. Check API endpoints
4. Modify/enhance code
5. Deploy to production

### For Farmers/Users
1. Run the application
2. Enter your region and climate data
3. Review recommendations
4. Follow AI advisor guidance
5. Use decision support for planning

---

## ✅ Installation Complete!

You're now ready to use AgriMind AI v2.0!

### Quick Access
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:5000
- **Health Check**: http://localhost:5000/health

### Next: 
1. Open the app in your browser
2. Select "Full Analysis" tab
3. Enter climate data
4. Click "Generate Full Analysis"
5. Review the comprehensive results!

---

**Happy Farming! 🌾🌱**

For questions or issues, refer to:
- V2.0_FEATURES.md (detailed feature docs)
- Backend code comments
- Frontend component documentation

**Last Updated**: 2026-06-14  
**Version**: v2.0.0  
**Status**: Ready for Use
