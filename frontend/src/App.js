import logo from './logo.svg';
import './App.css';
import React from 'react';
import DataFetcher from './DataFetcher';
import { BrowserRouter as Router } from 'react-router-dom';
function App() {
  return (
    // <div>
    //   <DataFetcher />
    // </div>
    <Router>
      <Navbar />
    </Router>
  );
}

export default App;
