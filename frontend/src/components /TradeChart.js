import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import axios from 'axios';

function TradeChart() {
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await axios.get(`${process.env.REACT_APP_API_URL}/trade-data`);
        const data = response.data;

        // Structure data for Chart.js
        const chartConfig = {
          labels: data.dates,
          datasets: [
            {
              label: 'Close Prices',
              data: data.close_prices,
              borderColor: 'rgba(75, 192, 192, 1)',
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              fill: true,
            },
          ],
        };

        setChartData(chartConfig);
      } catch (error) {
        console.error('Error fetching chart data:', error);
      }
    }

    fetchData();
  }, []);

  return (
    <div className="trade-chart">
      <h3>Price Movement</h3>
      {chartData ? (
        <Line data={chartData} />
      ) : (
        <p>Loading chart data...</p>
      )}
    </div>
  );
}

export default TradeChart;
