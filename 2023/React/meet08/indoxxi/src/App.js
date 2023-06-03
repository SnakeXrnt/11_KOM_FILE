import  React from 'react';
import {BrowserRouter, Route, Routes } from 'react-router-dom';
import './App.css' ;
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Movie from './pages/Movie';

import logo from './logo.svg';
import './App.css';
import { Nav } from 'react-bootstrap';


function App() {
  return (
    <div className="App">
      <div className='content-section'>
        <BrowserRouter>
        <Navbar />
          <Routes>
            <Route path='/' element{<Home />}/>
            <Route path='movie/:id' element={<Movie />} />
          </Routes>
        </BrowserRouter>
      </div>
      
    </div>
  );
}

export default App;
