import React, { useState, useEffect } from 'react';
import axios from 'axios';
// import yolk from './yolk.png';
import './App.css';

function App() {

  const [joke, setJoke] = useState('');

  const fetchRandomJoke = async () => {
    try {
      const response = await axios.get('https://icanhazdadjoke.com/', {
        headers: {
          'Accept': 'application/json'
        }
      });

      const data = response.data;
      setJoke(data.joke);
    } catch (error) {
      console.error('Error fetching joke:', error);
    }
  };


  useEffect(() => {
    
    fetchRandomJoke();
  }, []);

  const handleNewJokeClick = () => {
    fetchRandomJoke();
  }

  return (
    <div className="App">
      <header className="App-header">
        {/* <h1>press to scramble yolk</h1> */}
        {/* <img src={yolk} className='App-yolk' alt="yolk"/> */}
        <button onClick={handleNewJokeClick} className='joke'>{joke}</button>
        {/* <a href="#" onClick={handleNewJokeClick}>
          <img src={yolk} className='App-yolk' alt="yolk"/>
        </a> */}
        {/* <p className='joke'>{joke}</p> */}
      </header>
    </div>
  );
}

export default App;
