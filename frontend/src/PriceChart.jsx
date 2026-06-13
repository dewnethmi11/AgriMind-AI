import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer
} from "recharts";

import "./PriceChart.css";

function PriceChart({ predictedPrice }) {

  const data = [
    { month: "Jan", price: predictedPrice - 40 },
    { month: "Feb", price: predictedPrice - 20 },
    { month: "Mar", price: predictedPrice - 10 },
    { month: "Apr", price: predictedPrice },
    { month: "May", price: predictedPrice + 15 },
    { month: "Jun", price: predictedPrice + 25 }
  ];

  return (
    <div className="chart-card">

      <h2>📈 Price Trend</h2>

      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="month" />
          <YAxis />
          <Tooltip />
          <Line
            type="monotone"
            dataKey="price"
          />
        </LineChart>
      </ResponsiveContainer>

    </div>
  );
}

export default PriceChart;