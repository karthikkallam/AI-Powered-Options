import React from 'react';
import TradeChart from './TradeChart';
import SignalTable from './SignalTable';
import RiskMetrics from './RiskMetrics';
import ControlPanel from './ControlPanel';

function Dashboard() {
  return (
    <div className="dashboard">
      <h2>Trading Overview</h2>
      <div className="dashboard-section">
        <TradeChart />
      </div>
      <div className="dashboard-section">
        <SignalTable />
      </div>
      <div className="dashboard-section">
        <RiskMetrics />
      </div>
      <div className="dashboard-section">
        <ControlPanel />
      </div>
    </div>
  );
}

export default Dashboard;
