import React, { useEffect, useState } from 'react';
import axios from 'axios';

function SignalTable() {
  const [signals, setSignals] = useState([]);

  useEffect(() => {
    async function fetchSignals() {
      try {
        const response = await axios.get(`${process.env.REACT_APP_API_URL}/signals`);
        setSignals(response.data);
      } catch (error) {
        console.error('Error fetching signals:', error);
      }
    }

    fetchSignals();
  }, []);

  return (
    <div className="signal-table">
      <h3>Trading Signals</h3>
      {signals.length > 0 ? (
        <table>
          <thead>
            <tr>
              <th>Date</th>
              <th>Signal</th>
              <th>Confidence</th>
            </tr>
          </thead>
          <tbody>
            {signals.map((signal, index) => (
              <tr key={index}>
                <td>{signal.date}</td>
                <td>{signal.type}</td>
                <td>{signal.confidence}%</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>Loading signals...</p>
      )}
    </div>
  );
}

export default SignalTable;
