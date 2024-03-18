import React, { useState, useEffect } from 'react';
import axios from 'axios';
import yolk from './yolk.png';
import './App.css';

function App() {
  // State variable to hold the fetched joke
  const [joke, setJoke] = useState('');

  // Function to fetch a random joke from the Dad Joke API
  const fetchRandomJoke = async () => {
    try {
      const response = await axios.get('https://icanhazdadjoke.com/', {
        headers: {
          'Accept': 'application/json'
        }
      });
      // Extract the joke from the response data
      const data = response.data;
      setJoke(data.joke);
    } catch (error) {
      console.error('Error fetching joke:', error);
    }
  };

  // Fetch a random joke when the component mounts
  useEffect(() => {
    // preventDefault();
    fetchRandomJoke();
  }, []); // Empty dependency array means it only runs once when the component mounts

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
