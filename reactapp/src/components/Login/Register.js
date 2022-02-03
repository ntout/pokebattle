import React, {useState} from "react";
import propTypes from 'prop-types';
import './Login.css';
import { useNavigate } from "react-router-dom";

async function registerUser(credentials) {
    return fetch('http://127.0.0.1:8000/user/create/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(credentials)
        })
          .then(data => data.json())
}

export default function Register({setToken}) {
    const [username, setUserName] = useState();
    const [password, setPassword] = useState();

    const handleSubmit = async e => {
        e.preventDefault();
        const token = await registerUser({
            username,
            password
        });
        setToken(token);
    }

    return(
        <div className="register-wrapper">
            <h1> Create Account </h1>
            <form onSubmit={handleSubmit}>
                <label>
                    <p>Username</p>
                    <input type="text" onChange={e => setUserName(e.target.value)} />
                </label>
                <label>
                    <p>Password</p>
                    <input type="password" onChange={e => setPassword(e.target.value)}/>
                </label>
                <div>
                    <button type="submit">Save</button>
                </div>
            </form>
        </div>
    )
}

Register.propTypes = {
    setToken: propTypes.func.isRequired
}