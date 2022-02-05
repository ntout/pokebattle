import React, {useState} from "react";
import propTypes from 'prop-types';
import './Login.css';

const loginUrl = 'http://127.0.0.1:8000/user/token/obtain/'
const createUrl = 'http://127.0.0.1:8000/user/create/'

async function loginUser(credentials) {
    return fetch(loginUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(credentials)
    })
    .then(response => {
        if(!response.ok)
            throw new Error(response.status);
        else return response.json()
    })
}

async function createUser(credentials) {
    return fetch(createUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(credentials)
    })
    .then(response => {
        if(!response.ok)
            throw new Error(response.status);
        else return response.json()
    })
}

export default function Login({setToken}) {
    const [username, setUserName] = useState();
    const [password, setPassword] = useState();
    const [isLogin, setIsLogin] = useState(true);


    const handleSubmit = async e => {
        if (!isLogin) {
            await createUser({
                username,
                password
            });
        }
        e.preventDefault();
        const token = await loginUser({
            username,
            password
        });
        if(!token['access'])
            console.log("no token")
        else
            setToken(token);
    }    

    function handleCreatAccount() {
        setIsLogin(false);
    }

    function handleLogInOption(){
        setIsLogin(true);
    }
    

    return(
        <div className="login-wrapper">
            <>
                {isLogin ? <h1>Please Log in</h1> : <h1>Register for new account</h1>}
            </>
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
                    <>
                        {isLogin ? <button type="submit">Login</button> : <button type="submit">Save</button>}
                    </>
                </div>
            </form>
            <>
                {isLogin ? <a onClick={handleCreatAccount}>Create a new account.</a>
                     : <a onClick={handleLogInOption}>Already an existing user?</a>}
            </>

        </div>
    )
}

Login.propTypes = {
    setToken: propTypes.func.isRequired
}