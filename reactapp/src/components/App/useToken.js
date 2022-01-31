import {useState} from 'react';

export default function useToken() {
    const getToken = () => {
        const tokenString = sessionStorage.getItem('token');
        const useToken = JSON.parse(tokenString);
        return useToken?.token.access
    };

    const [token, setToken] = useState(getToken);

    const saveToken = useToken => {
        sessionStorage.setItem('token', JSON.stringify(useToken));
        setToken(useToken.token.access);
    };

    return {
        setToken: saveToken,
        token
    }
}