import React from "react"
import "./Meme.css"
function Meme(){

    const [allMemesData, setAllMemesData] = React.useState([]);

    const [state, setState] = React.useState({
        isLoading : true;
        topText : "",
        bottomText : "",
        randomImage : "https://i.imgflip.com/1g8my4.jpg"
    })

    if (state.isLoading)
    return (
        <section className="section--loading--page">
            <h1>Loading...</h1>
        </section>
    )
}