import logo from './logo.svg';
import './App.css';
import React from 'react';
import DataFetcher from './DataFetcher';
import Navbar from './components/Navbar';
import { BrowserRouter as Router } from 'react-router-dom';

function App() {
  return (
    <div>
      <DataFetcher />
    </div>
    // <div>
    //   <Navbar />
    // </div>
  );
}

export default App;
