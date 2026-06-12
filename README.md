# AgriMind AI

An intelligent farming decision assistant that analyzes climate conditions, predicts vegetable prices, and recommends profitable crops for cultivation using machine learning and data-driven insights.

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
* Visualizing climate and market trends

Instead of simply predicting a price, AgriMind AI acts as an intelligent assistant that helps farmers choose what to grow based on data-driven recommendations.

---

## Features

### Price Prediction

Predict vegetable prices using:

* Region
* Temperature
* Rainfall
* Humidity
* Crop Yield Impact Score

### Crop Recommendation Engine

Analyze multiple crops and recommend the most profitable cultivation options.

### Climate-Based Analysis

Evaluate climate conditions and their potential impact on crop performance.

### AI Farming Advisor

Provide intelligent recommendations to support farming decisions.

### Analytics Dashboard

Visualize trends and insights through interactive charts and graphs.

---

## Why This Project?

This project was inspired by farming communities in Nuwara Eliya, Sri Lanka, where vegetable cultivation is a major source of income.

Farmers often need to make important decisions without access to reliable data or predictive insights. AgriMind AI aims to bridge this gap by combining machine learning, climate information, and market trends to support better farming decisions.

---

## Technology Stack

### Frontend

* React
* Tailwind CSS
* Chart.js

### Backend

* Flask

### Machine Learning

* Pandas
* Scikit-Learn
* Random Forest Regressor

### Version Control

* Git
* GitHub

---

## Dataset

The project utilizes a dataset containing:

* 130,000 records
* 25 regions
* 20 vegetable categories
* Temperature data
* Rainfall data
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
