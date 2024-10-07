import React, { useState, useContext, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Context } from "../store/appContext";

export const UserPage  = () => {
    const { actions } = useContext(Context);
    const [welcomeMessage, setWelcomeMessage] = useState('');
    const navigate = useNavigate();

    useEffect(() => {
        
        const token = localStorage.getItem('token');
        if (token) {
            setWelcomeMessage('Welcome back to account!');
        } else {
            alert("Login failed, please check your credentials");
        }
    }, []);

    return (
        <div className="container d-flex justify-content-center align-items-center vh-100 bg-light">
            <div className="card p-4 shadow" style={{ maxWidth: '400px', width: '100%' }}>
                
                {welcomeMessage && <div className="alert alert-success text-center">{welcomeMessage}</div>}
                <button>Logout</button>
            </div>
        </div>
    );
};