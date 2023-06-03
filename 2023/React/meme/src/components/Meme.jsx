import React, { useState, useEffect } from "react";
import "./Meme.css";

function Meme() {
  const [state, setState] = useState({
    isLoading: true,
    topText: "",
    bottomText: "",
    image: "",
  });
  const [allMemeData, setAllMemeData] = useState([]);

  useEffect(() => {
    fetch("https://api.imgflip.com/get_memes")
      .then((res) => res.json())
      .then((data) => {
        setAllMemeData(data.data.memes);
        setState({
          ...state,
          isLoading: false,
          image: getRandomMemeImage(data.data.memes),
        });
      })
      .catch((err) => console.log(err));
  }, []);

  function getRandomMemeImage(memeArr) {
    const randomIndex = Math.floor(Math.random() * memeArr.length);
    const imageUrl = memeArr[randomIndex].url;
    return imageUrl;
  }

  function getMemeImage(event) {
    event.preventDefault();
    setState((state) => ({
      ...state,
      image: getRandomMemeImage(allMemeData),
    }));
  }

  function handleChange(event) {
    const { name, value } = event.target;
    setState((state) => ({
      ...state,
      [name]: value,
    }));
  }

  return (
    <section className="section--meme">
      <form className="meme--form" onSubmit={getMemeImage}>
        <input
          type="text"
          name="topText"
          placeholder="Top Text"
          className="meme--form--input"
          value={state.topText}
          onChange={handleChange}
          id=""
        />
        <input
          type="text"
          name="bottomText"
          placeholder="Bottom Text"
          className="meme--form--input"
          value={state.bottomText}
          onChange={handleChange}
          id=""
        />
        <input
          type="submit"
          value="Get new image"
          className="meme--form--button"
        />
      </form>

      <div className="meme--content">
        {state.isLoading ? (
          <p>Loading...</p>
        ) : (
          <>
            <img src={state.image} className="meme-image" alt="" />
            <h2 className="meme--top--text">{state.topText}</h2>
            <h2 className="meme--bottom--text">{state.bottomText}</h2>
          </>
        )}
      </div>
    </section>
  );
}

export default Meme;
