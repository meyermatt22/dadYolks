import React, { useState, useEffect } from 'react';
import axios from 'axios';
// import yolk from './yolk.png';
import './App.css';
import Footer from './Footer';
import Header from './Header';

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
      <Header/>
      <header className="App-header">

        <button onClick={handleNewJokeClick} className='joke'>{joke}</button>

      </header>
      <Footer/>
    </div>
  );
}

export default App;
