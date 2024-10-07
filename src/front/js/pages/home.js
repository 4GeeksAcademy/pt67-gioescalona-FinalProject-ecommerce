import React from 'react';
import { Link } from 'react-router-dom';
import "../../styles/home.css";

export const Home = () => {
  return (
    <div className="home-container">
      {/* Banner principal con una imagen destacada */}
      <div className="main-banner">
        <img src="https://masterbundles.com/wp-content/uploads/2022/12/1-592.jpg" alt="Main Banner" />
        <div className="banner-text">
          <h1>Descubre la nueva colección</h1>
        </div>
      </div>

      {/* Sección de categorías */}
      <div className="category-section">
        <div className="category-item">
          <Link to="/shirts">
            <img src="https://img.abercrombie.com/is/image/anf/KIC_123-4002-0119-303_prod2.jpg?policy=product-large" alt="Camisetas" />
            <h2>Shirts</h2>
          </Link>
        </div>
        <div className="category-item">
          <Link to="/jeans">
            <img src="https://img.abercrombie.com/is/image/anf/KIC_155-3577-0040-278_prod1?policy=product-large" alt="Vaqueros" />
            <h2>Jeans</h2>
          </Link>
        </div>
        <div className="category-item">
          <Link to="/shoes">
            <img src="https://img.abercrombie.com/is/image/anf/KIC_112-3145-0045-900_prod1?policy=product-large" alt="Zapatos" />
            <h2>Shoes</h2>
          </Link>
        </div>
      </div>

      {/* Sección de productos destacados */}
      <div className="featured-products-section">
        <h2>Productos Destacados</h2>
        <div className="featured-products">
          <div className="product-item">
            <img src="https://img.abercrombie.com/is/image/anf/KIC_224-4093-0067-012_prod1?policy=product-large" alt="Producto 1" />
            <h3>Camiseta gris casual</h3>
            <p>50.00€</p>
          </div>
          <div className="product-item">
            <img src="https://img.abercrombie.com/is/image/anf/KIC_131-4962-00163-975_prod1.jpg?policy=product-large" alt="Producto 2" />
            <h3>Vaquero estandar origin</h3>
            <p>60.00€</p>
          </div>
          <div className="product-item">
            <img src="https://img.abercrombie.com/is/image/anf/KIC_112-4034-0049-320_prod2.jpg?policy=product-large" alt="Producto 3" />
            <h3>Sueco piel birken</h3>
            <p>70.00€</p>
          </div>
        </div>
      </div>
    </div>
  );
};
