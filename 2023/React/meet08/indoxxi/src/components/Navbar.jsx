import React from "react"
import "./Navbar.css"
import { Link } from "react-router-dom"


export default foction Navbar(){

    return {
        <div className="navbar">
            <div className="logo-navbar">
                img src="https://www.freepnglogos.com/uploads/hogwares-logo.png/hogwarts-logo-shadopro-devianart-0.png" alt="hogwarts logo" />
            </div>
            <ul>
                <li>
                    <Link to=("/")>Home</Link>
                </li>
                <li>
                <Link to=("/")>About</Link>
                </li>
            </ul>
        </div>
    }
}