import React, { useState, useContext } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Context } from '../store/appContext';

export const SignUp = () => {
	const { store, actions } = useContext(Context);
	const [name, setName] = useState('');
	const [email, setEmail] = useState('');
	const [password, setPassword] = useState('');
	const navigate = useNavigate();

	const handleSubmit = async (e) => {
		e.preventDefault();
		
		
		const success = await actions.signUp(name, email, password);
		
		if (success) {
			navigate('/private');
		} else {
			console.log('Error during sign up');
		}
	};

	return (
		<div className="container d-flex justify-content-center align-items-center vh-100">
			<div className="card p-4 shadow" style={{ maxWidth: '400px', width: '100%' }}>
				<h2 className="text-center mb-4">New User Registration</h2>
				<form onSubmit={handleSubmit}>
					<div className="mb-3">
						<label htmlFor="name" className="form-label">Name</label>
						<input
							type="text"
							id="name"
							className="form-control"
							value={name}
							onChange={(e) => setName(e.target.value)}
							placeholder="Enter your name"
							required
						/>
					</div>
					<div className="mb-3">
						<label htmlFor="email" className="form-label">Email</label>
						<input
							type="email"
							id="email"
							className="form-control"
							value={email}
							onChange={(e) => setEmail(e.target.value)}
							placeholder="Enter your email"
							required
						/>
					</div>
					<div className="mb-4">
						<label htmlFor="password" className="form-label">Password</label>
						<input
							type="password"
							id="password"
							className="form-control"
							value={password}
							onChange={(e) => setPassword(e.target.value)}
							placeholder="Enter your password"
							required
						/>
					</div>
					<button type="submit" className="btn btn-primary w-100">Sign Up</button>
				</form>
				<div className="text-center mt-3">
					<Link to="/">
						<button className="btn btn-secondary">Back to Home</button>
					</Link>
				</div>
			</div>
		</div>
	);
};