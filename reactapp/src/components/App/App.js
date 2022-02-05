import React from 'react';
import './App.css';

import Login from '../Login/Login';
import Pokemon from '../Pokemon/Pokemon';

import useToken from './useToken';


function App() {

  const { token, setToken } = useToken();

  if(!token) {
    return <Login setToken={setToken} />
  }

  function logout() {
    console.log(token["access"])
    sessionStorage.clear();
    window.location.reload(false);
  }

  return (
    <div className="wrapper">
      <h1>Pokemon Battle Simulator</h1>
      <button onClick={logout}>logout</button>
      <Pokemon />
    </div>
  );
}

export default App;
  