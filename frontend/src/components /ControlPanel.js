import React, { useState } from 'react';
import axios from 'axios';

function ControlPanel() {
  const [statusMessage, setStatusMessage] = useState('');

  const handleStartTrading = async () => {
    try {
      const response = await axios.post(`${process.env.REACT_APP_API_URL}/start-trading`);
      setStatusMessage(response.data.message);
    } catch (error) {
      console.error('Error starting trading:', error);
      setStatusMessage('Failed to start trading.');
    }
  };

  const handleStopTrading = async () => {
    try {
      const response = await axios.post(`${process.env.REACT_APP_API_URL}/stop-trading`);
      setStatusMessage(response.data.message);
    } catch (error) {
      console.error('Error stopping trading:', error);
      setStatusMessage('Failed to stop trading.');
    }
  };

  return (
    <div className="control-panel">
      <h3>Control Panel</h3>
      <button onClick={handleStartTrading}>Start Trading</button>
      <button onClick={handleStopTrading}>Stop Trading</button>
      {statusMessage && <p>{statusMessage}</p>}
    </div>
  );
}

export default ControlPanel;
