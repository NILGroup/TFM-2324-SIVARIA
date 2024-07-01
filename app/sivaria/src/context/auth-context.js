// src/context/AuthContext.js
import React, { createContext, useState, useEffect } from 'react';
import { getItemLocalStorage, setItemLocalStorage } from '../utils/general-local-storage';

export const AuthContext = createContext();

const initialState = {
    isLoading: true,
    isSignout: false, 
    userToken: null
};

const authReducer = (state, action) => {
    switch(action.type) {
        case 'RESTORE_TOKEN':
            break;
        case 'LOGIN':
            break;
        case 'LOGOUT':
    }
}

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true);

  const checkTokenAndRoute = async () => {
    const token = await getItemLocalStorage('userToken');
    if (token) {
      setIsAuthenticated(true);
    }
    setLoading(false);
  };

  useEffect(() => {
    checkTokenAndRoute();
  }, []);

  const login = async (token) => {
    await setItemLocalStorage('userToken', token);
    setIsAuthenticated(true);
  };

  const logout = async () => {
    await setItemLocalStorage('userToken', '');
    setIsAuthenticated(false);
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
