import logo from './logo.svg';
import './App.css';
import DataFetcher from './DataFetcher';
import Navbar from './Navbar';
import Home from './components/pages/Home';
import Deals from './components/pages/Deals';
import Products from './components/pages/Products';
import { Component } from 'react';
import Brands from './components/pages/Brands';

function App() {
  switch (window.location.pathname) {
    case '/':
      Component = <Home />
      break
    case '/deals':
      Component = <Deals />
      break
    case '/products':
      Component = <Products />
      break
    case '/brands':
      Component = <Brands />
      break
}
return (
  <>
    <Navbar />
    {Component}
  </>
)} 
export default App;

// function App() {
//   return (
//     <div>
//       <DataFetcher />
//     </div>
//     // <div>
//     //   <Navbar />
//     // </div>
//   );
// }

