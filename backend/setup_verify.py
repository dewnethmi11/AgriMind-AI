#!/usr/bin/env python3
"""
AgriMind AI v2.0 - Quick Setup Guide
This script helps you verify the installation and run the backend server.
"""

import os
import sys
import subprocess

def check_python():
    """Check Python version."""
    print("✓ Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"  Python {version.major}.{version.minor}.{version.micro} ✓")
        return True
    else:
        print(f"  Python {version.major}.{version.minor} is too old. Need 3.8+")
        return False

def check_dependencies():
    """Check if all required packages are installed."""
    print("\n✓ Checking dependencies...")
    required_packages = [
        'flask',
        'flask_cors',
        'pandas',
        'numpy',
        'scikit-learn',
        'joblib',
        'requests'
    ]
    
    missing = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"  {package} ✓")
        except ImportError:
            print(f"  {package} ✗")
            missing.append(package)
    
    return len(missing) == 0, missing

def check_models():
    """Check if ML models are available."""
    print("\n✓ Checking ML models...")
    models = ['model.pkl', 'region_encoder.pkl', 'veg_encoder.pkl']
    missing = []
    
    for model in models:
        if os.path.exists(model):
            print(f"  {model} ✓")
        else:
            print(f"  {model} ✗")
            missing.append(model)
    
    return len(missing) == 0, missing

def print_endpoints():
    """Print available API endpoints."""
    print("\n" + "="*60)
    print("API ENDPOINTS")
    print("="*60)
    
    endpoints = [
        ("POST", "/predict", "Price prediction (v1.0)"),
        ("POST", "/recommend-crops", "Crop recommendations (v2.0)"),
        ("GET", "/weather/<region>", "Weather data (v2.0)"),
        ("POST", "/advisor", "AI advisor (v2.0)"),
        ("POST", "/decision-support", "Decision support (v2.0)"),
        ("POST", "/comprehensive-analysis", "Full analysis (v2.0)"),
        ("GET", "/health", "Health check"),
    ]
    
    print(f"\n{'METHOD':<8} {'ENDPOINT':<30} {'DESCRIPTION':<30}")
    print("-"*60)
    for method, endpoint, desc in endpoints:
        print(f"{method:<8} {endpoint:<30} {desc:<30}")
    
    print("\nSupported Weather Regions:")
    regions = ["Nuwara Eliya", "Kandy", "Colombo", "Galle", "Jaffna", 
               "Badulla", "Matara", "Ratnapura"]
    for i, region in enumerate(regions, 1):
        print(f"  {i}. {region}")

def print_startup_instructions():
    """Print startup instructions."""
    print("\n" + "="*60)
    print("GETTING STARTED")
    print("="*60)
    
    instructions = """
1. BACKEND SETUP:
   - All dependencies should be installed from requirements.txt
   - Run: python app.py
   - Backend will run on http://127.0.0.1:5000

2. FRONTEND SETUP:
   - Navigate to frontend directory
   - Install: npm install
   - Run: npm run dev
   - Frontend will run on http://localhost:5173

3. TESTING THE API:
   - Use /health endpoint to verify backend is running
   - Use comprehensive-analysis endpoint for full system test
   
4. EXAMPLE REQUEST (Crop Recommendation):
   POST http://127.0.0.1:5000/recommend-crops
   {
     "Region": "Colombo",
     "Temperature": 28,
     "Rainfall": 100,
     "Humidity": 75,
     "CropYield": 50
   }

5. EXAMPLE REQUEST (Weather Data):
   GET http://127.0.0.1:5000/weather/Nuwara%20Eliya

6. TROUBLESHOOTING:
   - If models are missing, train them using train_model.py
   - If requests fail, check backend is running on port 5000
   - Ensure CORS is enabled (should be automatic)
   - Weather data requires internet connection (uses free API)
"""
    print(instructions)

def main():
    """Run all checks."""
    print("\n" + "="*60)
    print("AGRIMIND AI v2.0 - SETUP VERIFICATION")
    print("="*60 + "\n")
    
    # Check Python
    if not check_python():
        print("\n❌ Python version check failed!")
        return False
    
    # Check dependencies
    deps_ok, missing_deps = check_dependencies()
    if not deps_ok:
        print(f"\n❌ Missing dependencies: {', '.join(missing_deps)}")
        print("Install with: pip install -r requirements.txt")
        return False
    
    # Check models
    models_ok, missing_models = check_models()
    if not models_ok:
        print(f"\n⚠️  Missing ML models: {', '.join(missing_models)}")
        print("Train models using: python train_model.py")
    
    # Print endpoints
    print_endpoints()
    
    # Print instructions
    print_startup_instructions()
    
    print("\n" + "="*60)
    if deps_ok:
        print("✓ All checks passed! Ready to run AgriMind AI v2.0")
        print("\nStart backend with: python app.py")
        print("="*60 + "\n")
        return True
    else:
        print("❌ Some checks failed. Please resolve the issues above.")
        print("="*60 + "\n")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
