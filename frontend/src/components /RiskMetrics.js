import React, { useEffect, useState } from 'react';
import axios from 'axios';

function RiskMetrics() {
  const [metrics, setMetrics] = useState(null);

  useEffect(() => {
    async function fetchMetrics() {
      try {
        const response = await axios.get(`${process.env.REACT_APP_API_URL}/risk-metrics`);
        setMetrics(response.data);
      } catch (error) {
        console.error('Error fetching risk metrics:', error);
      }
    }

    fetchMetrics();
  }, []);

  return (
    <div className="risk-metrics">
      <h3>Risk Metrics</h3>
      {metrics ? (
        <ul>
          <li><strong>Max Drawdown:</strong> {metrics.max_drawdown}%</li>
          <li><strong>Sharpe Ratio:</strong> {metrics.sharpe_ratio}</li>
          <li><strong>Sortino Ratio:</strong> {metrics.sortino_ratio}</li>
          <li><strong>Volatility:</strong> {metrics.volatility}%</li>
        </ul>
      ) : (
        <p>Loading risk metrics...</p>
      )}
    </div>
  );
}

export default RiskMetrics;
