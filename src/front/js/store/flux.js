const getState = ({ getStore, getActions, setStore }) => {
    return {
        store: {
            auth: false,
            message: null,
            demo: [
                {
                    title: "FIRST",
                    background: "white",
                    initial: "white"
                },
                {
                    title: "SECOND",
                    background: "white",
                    initial: "white"
                }
            ]
        },
        actions: {
            // Función ejemplo para cambiar color
            exampleFunction: () => {
                getActions().changeColor(0, "green");
            },

            // Función para registrar un nuevo usuario (sign up)
            signUp: async (name, email, password) => {
                try {
                    const response = await fetch("https://upgraded-rotary-phone-5gg67p7g9vxgcv96q-3001.app.github.dev/api/signup", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            name: name,
                            email: email,
                            password: password
                        })
                    });

                    if (response.ok) {
                        const data = await response.json();
                        // Guarda el token en localStorage
                        localStorage.setItem("token", data.access_token);
                        // Actualiza el estado de autenticación
                        setStore({ auth: true });
                        return true;
                    } else {
                        console.log("Error during sign up");
                        return false;
                    }
                } catch (error) {
                    console.error("There was an error with the sign up:", error);
                    return false;
                }
            },
            
            // Función de login
            login: async (name, email, password) => {
                try {
                    const response = await fetch("https://upgraded-rotary-phone-5gg67p7g9vxgcv96q-3001.app.github.dev/api/login", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            name: name, 
                            email: email, 
                            password: password
                        })
                    });

                    if (response.ok) {
                        const data = await response.json();
                        // Guarda el token en localStorage
                        localStorage.setItem("token", data.access_token);
                        // Actualiza el estado de autenticación
                        setStore({ auth: true });
                        console.log('Token:', data.access_token);
                        return true; // Indica que el login fue exitoso
                    } else {
                        console.log('Login failed');
                        return false; // Indica que el login falló
                    }
                } catch (error) {
                    console.error("There was an error during login:", error);
                    return false; // Indica que hubo un error durante el login
                }
            },

            // Función para cerrar sesión (logout)
            logout: () => {
                localStorage.removeItem("token");
                setStore({ auth: false });
                console.log("User logged out");
            },

            // Función para obtener mensajes
            getMessage: async () => {
                try {
                    const response = await fetch(process.env.BACKEND_URL + "/api/hello");
                    const data = await response.json();
                    setStore({ message: data.message });
                    return data;
                } catch (error) {
                    console.log("Error loading message from backend", error);
                }
            },

            // Función para cambiar color
            changeColor: (index, color) => {
                const store = getStore();
                const demo = store.demo.map((elm, i) => {
                    if (i === index) elm.background = color;
                    return elm;
                });
                setStore({ demo: demo });
            }
        }
    };
};

export default getState;