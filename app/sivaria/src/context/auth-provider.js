import React from "react";
import { useState } from "react";
import AuthContext from "./auth-context";

function AuthProvider({children}) {
    const [isAuthenticated, setIsAuthenticated] = useState(false);

    return (
        <AuthContext.Provider value={{ isAuthenticated, setIsAuthenticated }}>
            { children }
        </AuthContext.Provider>
    );
}

export default AuthProvider;