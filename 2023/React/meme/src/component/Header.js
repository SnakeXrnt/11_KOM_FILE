/* eslint-disable jsx-a11y/alt-text */
import React from "react"
 
import "./Header.css"
import TrollImg from "../assets/img/troll.png"
 
function Header(props){
 
    return (
        <header className={`header ${props.darkMode ? "dark--mode" : ""}`}>
            <img className="header--image"
                src={TrollImg}/>
            <h1 className="headder--title">
                Meme Generator
            </h1>
            <h4 className="header--project">
                React Course - Project 3
            </h4>
 
            <div className={`header--toggle--darkmode
                ${ props.darkMode ? "header--toggle--darkmode--clicked" :
                "header--toggle--darkmode--unclicked" }`}>
                <span
                    className={`header--circle--darkmode ${ props.darkMode ?
                    "header--circle--darkmode--clicked" : "header--circle--darkmode--unclicked"}`}
                    onclick={props.toggleDarkMode}></span>
            </div>
        </header>
    )
}
 
export default Header;