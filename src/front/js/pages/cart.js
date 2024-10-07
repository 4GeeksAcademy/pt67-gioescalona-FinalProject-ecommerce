import React, { useContext } from 'react';
import { Context } from '../store/appContext';
import "../../styles/home.css";

export const Cart = () => {
    const { store, removeFromCart } = useContext(Context);

    const handlePayment = () => {
        alert("Procediendo al pago...");
    };

    return (
        <div className="cart-container">
            <h1>Carrito de Compras</h1>
            {store.cart && store.cart.length > 0 ? (
                <div className="cart-items">
                    {store.cart.map((item, index) => (
                        <div key={index} className="cart-item">
                            <img src={item.image} alt={item.title} />
                            <div className="item-details">
                                <h2>{item.title}</h2>
                                <p>${item.price}</p>
                                <button className="remove-button" onClick={() => removeFromCart(index)}>
                                    Eliminar
                                </button>
                            </div>
                        </div>
                    ))}
                </div>
            ) : (
                <div className="empty-cart">
                    <p>No hay productos en tu carrito.</p>
                </div>
            )}
            {store.cart && store.cart.length > 0 && (
                <button className="pay-button" onClick={handlePayment}>
                    Pagar
                </button>
            )}
        </div>
    );
};
