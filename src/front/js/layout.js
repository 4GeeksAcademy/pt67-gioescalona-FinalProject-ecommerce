import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";
import { BackendURL } from "./component/backendURL";

import { Home } from "./pages/home";
import { Demo } from "./pages/demo";
import { Single } from "./pages/single";
import { Cart } from "./pages/cart"; 
import { Shirts } from "./pages/shirts";  
import { Jeans } from "./pages/jeans";    
import { Shoes } from "./pages/shoes";    
import injectContext from "./store/appContext";

import { Navbar } from "./component/navbar";
import { Login } from "./component/login";

//create your first component
const Layout = () => {
    const basename = process.env.BASENAME || "";

    if (!process.env.BACKEND_URL || process.env.BACKEND_URL === "") return <BackendURL />;

    return (
        <div>
            <BrowserRouter basename={basename}>
                <ScrollToTop>
                    <Navbar />
                    <Routes>
                        <Route element={<Home />} path="/" />
                        <Route element={<Demo />} path="/demo" />
                        <Route element={<Single />} path="/single/:theid" />
                        <Route element={<Cart />} path="/cart" />
                        <Route element={<Shirts />} path="/shirts" />  
                        <Route element={<Jeans />} path="/jeans" />   
                        <Route element={<Shoes />} path="/shoes" />  
                        <Route element={<Login />} path="/login" /> 
                        <Route element={<h1>Not found!</h1>} />
                    </Routes>
    
                </ScrollToTop>
            </BrowserRouter>
        </div>
    );
};

export default injectContext(Layout);
