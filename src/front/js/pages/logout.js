import React, { useEffect, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { Context } from "../store/appContext";

const Logout = () => {
    const { actions } = useContext(Context);
    const navigate = useNavigate();

    useEffect(() => {
        actions.logout(); 
        navigate("/home"); 
    }, [actions, navigate]);

    return null;
};

export default Logout;