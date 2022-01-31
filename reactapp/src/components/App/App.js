import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import Dashboard from '../Dashboard/Dashboard';
import Login from '../Login/Login';
import useToken from './useToken';



function App() {

  const { token, setToken } = useToken();
  console.log(token)
  console.log(setToken)
  if(!token) {
    return <Login setToken={setToken} />
  }

  return (
    <div className="App">
      <h1>Application</h1>
      <Router>
        <Routes>
          <Route exact path="/dashboard" element={<Dashboard />}>dfg
          </Route>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
  