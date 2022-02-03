import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import './App.css';

import Dashboard from '../Dashboard/Dashboard';
import Login from '../Login/Login';
import Register from '../Login/Register';

import useToken from './useToken';



function App() {

  const { token, setToken } = useToken();

  if(!token) {
    return <Login setToken={setToken} />
  }

  function logout() {
    sessionStorage.clear();
    window.location.reload(false);
  }

  return (
    <div className="wrapper">
      <h1>Application</h1>
      <button onClick={logout}>logout</button>
      <Router>
        <Routes>
          <Route exact path="/dashboard" element={<Dashboard />}/>
          <Route exact path="/register" element={<Register />}/>
          <Route exact path="/login" component={<Login/>}/>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
  