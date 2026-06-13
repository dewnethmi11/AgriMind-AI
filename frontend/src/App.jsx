import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {

  const regions = [
    "Ampara",
    "Anuradhapura",
    "Badulla",
    "Batticaloa",
    "Colombo",
    "Galle",
    "Gampaha",
    "Hambantota",
    "Jaffna",
    "Kalutara",
    "Kandy",
    "Kegalle",
    "Kilinochchi",
    "Kurunegala",
    "Mannar",
    "Matale",
    "Matara",
    "Monaragala",
    "Mullaitivu",
    "Nuwara Eliya",
    "Polonnaruwa",
    "Puttalam",
    "Ratnapura",
    "Trincomalee",
    "Vavuniya"
  ];

  const vegetables = [
    "Winged Bean",
    "Bitter Melon",
    "Brinjal",
    "Long Purple Eggplant",
    "Asiatic Pennywort",
    "Red Spinach",
    "Pennywort",
    "Leeks",
    "Carrot",
    "Beetroot",
    "Cabbage",
    "Knol-Khol",
    "Pumpkin",
    "Onion",
    "Potato",
    "Drumsticks",
    "Jackfruit",
    "Breadfruit",
    "Taro",
    "Manioc"
  ];

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

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
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

      setPrice(response.data.predicted_price);

    } catch (error) {

      console.error(error);
      alert("Prediction failed");

    } finally {

      setLoading(false);

    }
  };

  return (
    <div className="container">

      <h1>🌱 AgriMind AI</h1>

      <p>
        AI-Powered Vegetable Price Prediction System
      </p>

      <div className="card">

        <label>Region</label>
        <select
          name="Region"
          value={formData.Region}
          onChange={handleChange}
        >
          {regions.map(region => (
            <option key={region}>{region}</option>
          ))}
        </select>

        <label>Temperature (°C)</label>
        <input
          type="number"
          name="Temperature"
          value={formData.Temperature}
          onChange={handleChange}
        />

        <label>Rainfall (mm)</label>
        <input
          type="number"
          name="Rainfall"
          value={formData.Rainfall}
          onChange={handleChange}
        />

        <label>Humidity (%)</label>
        <input
          type="number"
          name="Humidity"
          value={formData.Humidity}
          onChange={handleChange}
        />

        <label>Crop Yield Score</label>
        <input
          type="number"
          step="0.1"
          name="CropYield"
          value={formData.CropYield}
          onChange={handleChange}
        />

        <label>Vegetable</label>
        <select
          name="Vegetable"
          value={formData.Vegetable}
          onChange={handleChange}
        >
          {vegetables.map(veg => (
            <option key={veg}>{veg}</option>
          ))}
        </select>

        <button onClick={predictPrice}>
          {loading ? "Predicting..." : "Predict Price"}
        </button>

        {price !== null && (
          <div className="result">
            Predicted Price: Rs. {price}
          </div>
        )}

      </div>

    </div>
  );
}

export default App;