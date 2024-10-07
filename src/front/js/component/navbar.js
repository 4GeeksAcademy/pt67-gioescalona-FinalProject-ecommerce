import React from 'react';
import { useNavigate, Link } from 'react-router-dom';
import "../../styles/home.css";

export const Navbar = () => {
  const navigate = useNavigate();

  const handleLoginClick = () => {
    navigate('/login'); // Redirige a la página de Login
  };

  const handleCartClick = () => {
    navigate('/cart'); // Redirige a la página del carrito
  };

  return (
    <header>
      <nav className="navbar">
        <div className="navbar-brand">
          <Link to="/">DEER</Link>
        </div>

        <ul className="nav-links">
          <li><Link to="/shirts">Shirts</Link></li>
          <li><Link to="/jeans">Jeans</Link></li>
          <li><Link to="/shoes">Shoes</Link></li>
        </ul>

        <div className="search-bar">
          <input type="text" placeholder="Buscar productos..." />
          <button type="button">Buscar</button>
        </div>

        <button className="user-icon" onClick={handleLoginClick}>
          <i className="fas fa-user"></i> Iniciar Sesión
        </button>

        <div className="cart-icon" onClick={handleCartClick} style={{ cursor: 'pointer' }}>
          <i className="fas fa-shopping-cart"></i>
        </div>
      </nav>
    </header>
  );
};
