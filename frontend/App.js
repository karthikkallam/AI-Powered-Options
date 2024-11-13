import React from 'react';
import Dashboard from './components/Dashboard';
import './styles.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>AI Options Trading Dashboard</h1>
      </header>
      <main>
        <Dashboard />
      </main>
    </div>
  );
}

export default App;
