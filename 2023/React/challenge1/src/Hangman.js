import React, { useState, useEffect } from 'react';

const Hangman = () => {
  const [word, setWord] = useState('');
  const [displayWord, setDisplayWord] = useState('');
  const [guessedLetters, setGuessedLetters] = useState([]);
  const [guessesRemaining, setGuessesRemaining] = useState(6);
  const [gameOver, setGameOver] = useState(false);
  const [gameWon, setGameWon] = useState(false);
  const [hangingMan, setHangingMan] = useState('');

  const words = ['hangman', 'javascript', 'react', 'node', 'css', 'html', 'express' , 'thebaldguy'];

  const selectWord = () => {
    const index = Math.floor(Math.random() * words.length);
    setWord(words[index]);
    setDisplayWord('_'.repeat(words[index].length));
  };

  const handleGuess = (event) => {
    const letter = event.target.value.toLowerCase();
    const updatedLetters = [...guessedLetters, letter];

    if (word.includes(letter)) {
      let updatedDisplayWord = '';
      for (let i = 0; i < word.length; i++) {
        if (word[i] === letter) {
          updatedDisplayWord += letter;
        } else {
          updatedDisplayWord += displayWord[i];
        }
      }
      setDisplayWord(updatedDisplayWord);
    } else {
      setGuessesRemaining(guessesRemaining - 1);
      updateHangingMan();
    }

    setGuessedLetters(updatedLetters);
  };

  const updateHangingMan = () => {
    const stages = [
        '',
        '   O   \n',
        '  /|\\  \n',
        '  / \\  \n',
        '       \n',
        '       \n',
        '       \n'
      ];
      
    const stage = stages[6 - guessesRemaining];
    setHangingMan(stage);
  };

  useEffect(() => {
    if (guessesRemaining === 0) {
      setGameOver(true);
    }
    if (!displayWord.includes('_')) {
      setGameWon(true);
      setGameOver(true);
    }
  }, [guessesRemaining, displayWord]);

  const handleReplay = () => {
    setGameOver(false);
    setGameWon(false);
    setGuessesRemaining(6);
    setGuessedLetters([]);
    setHangingMan('');
    selectWord();
  };

  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  const alphabetButtons = alphabet.split('').map((letter) => (
    <button
      key={letter}
      value={letter}
      onClick={handleGuess}
      disabled={guessedLetters.includes(letter) || gameOver}
    >
      {letter}
    </button>
  ));

  const gameBoard = (
    <div>
      <p>Guess the word:</p>
      <p>{displayWord}</p>
      <p>Guesses remaining: {guessesRemaining}</p>
      <div>{alphabetButtons}</div>
      <pre>{hangingMan}</pre>
    </div>
  );

  const winScreen = (
    <div>
      <p>Congratulations, you won!</p>
      <button onClick={handleReplay}>Play Again</button>
    </div>
  );

  const loseScreen = (
    <div>
      <p>Sorry, you lost. The word was {word}.</p>
      <button onClick={handleReplay}>Play Again</button>
    </div>
  );

  useEffect(() => {
    selectWord();
  }, []);

  return (
    <div>
      <h1>Hangman</h1>
      {gameOver ? (gameWon ? winScreen : loseScreen) : gameBoard}
    </div>
  );
};

export default Hangman;
