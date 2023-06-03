import React from 'react';
import { BrowserRouter, Link, Route, Routes } from 'react-router-dom';
import './App.css';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <nav>
          <ul>
            <li>
              <Link to={"/"}>Home</Link>
            </li>
            <li>
              <Link to={"/about"}>About</Link>
            </li>
            <li>
              <Link to={"/project"}>project page</Link>
            </li>
            <li>
              <Link to={"https://google.com"} target="_blank">Google</Link>
            </li>
          </ul>

        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/home" element={<Home />} />
          <Route path="/project" element={<Project />} />
          <Route path="/about" element={<About />} />
        </Routes>
      
      </BrowserRouter>
    </div>
  );
}

function Home() {

  return(

    <h1>Here is your home <span role="img" aria-label="freeze">:thumbsup:</span></h1>

  )
}

function About() {

  return(

    <h1>About page goes here! <span role="img" aria-label="party">:party:</span></h1>

  )

}

function Project() {

  return(

    <h1>About page goes here! <span role="img" aria-label="party">:party:</span></h1>

  )

}


export default App;
