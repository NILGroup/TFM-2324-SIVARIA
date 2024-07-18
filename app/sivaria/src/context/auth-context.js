// src/context/AuthContext.js
import React, { useRef, createContext, useState, useEffect, useReducer, useMemo } from 'react';
import { getItemLocalStorage, removeItemLocalStorage, setItemLocalStorage } from '../utils/general-local-storage';
import axios from 'axios';
// NOT USED (NOT NOW)
export const AuthContext = createContext();

export const AuthProvider = ({children}) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const isAuthenticatedRef = useRef(false);
  isAuthenticatedRef.current = isAuthenticated;

  // Each time a page is loaded, it is checked if the user is authenticatd or not.
  useEffect(() => {
    const checkToken = async() => {
      const token = await getItemLocalStorage('userToken');
      if(token) {
        console.log('AUTENTICADO EN EL CONTEXTO');
        setIsAuthenticated(true);
      }
      //setLoading(false);
    }

    checkToken();
  }, []);

  const login = () => {
      setIsAuthenticated(true)
  };
  
  const logout = () => {
      setIsAuthenticated(false)
  };

  return (
      <AuthContext.Provider value={{ isAuthenticatedRef, login, logout }}>
          { children }
      </AuthContext.Provider>
  );
}

const initialState = {
    isLoading: true,
    isLoggedIn: false, 
    userToken: null
};

const authReducer = (state, action) => {

    switch(action.type) {
      case 'LOGIN':
        return{
          ...state,
          isLoggedIn: true,
          userToken: action.token
        };
      case 'LOGOUT':
        return {
          ...state,
          isLoggedIn: false,
          userToken: null,
        };
      case 'REGISTER':
        return {
          ...state,
          isLoggedIn: false,
          userToken: null,
        };
      case 'RESTORE_TOKEN':
        return {
          ...state,
          isLoading: false,
          userToken: action.token,
        };
    }
}

const prueba = ({children}) => {
  const [state, dispatch] = useReducer(authReducer, initialState);

  useEffect(() => {
    // Fetch the token from storage then navigate to our appropriate place
    const searchToken = async () => {
      let userToken;

      userToken = await getItemLocalStorage('userToken');
      

      // After restoring token, we may need to validate it in production apps

      // This will switch to the App screen or Auth screen and this loading
      // screen will be unmounted and thrown away.
      dispatch({ type: 'RESTORE_TOKEN', token: userToken });
    };

    searchToken();
  }, []);

  useEffect(() => {
    const saveCurrentRoute = () => {
      const currentRoute = (navigationRef !== null) ? navigationRef.current.getCurrentRoute().name : null;
      //console.log('Current Route');
      //console.log(currentRoute);
      if (currentRoute) {
        setItemLocalStorage('currentRoute', currentRoute);
      }
    };

    if (Platform.OS !== 'web') {
      const handleAppStateChange = (nextAppState) => {
        if (nextAppState === 'background') {
          saveCurrentRoute();
        }
      };

      const subscription = AppState.addEventListener('change', handleAppStateChange);

      return () => {
        subscription.remove();
      };

    } else {
      window.addEventListener('beforeunload', saveCurrentRoute);

      return () => {
        window.removeEventListener('beforeunload', saveCurrentRoute);
      };
    }
  }, []);

  const authContext = useMemo(
    () => ({
      login: async (data) => {
        // login logic
        /*
        const data = {
          email:data.email,
          password:password,
        }

        if (Platform.OS !== 'web') {
            data['expo_token'] = expoPushToken.data
        }*/

        await axiosInstance.post('/sivaria/v1/user/login', data)
        .then(async function (response) {
          userData = response.data.data;
          setItemLocalStorage('userToken', response.data.token);
          setItemLocalStorage('email', userData.email);
          setIsAuthenticated(true);
        })
        .catch(function (error) {
            const message = 'Ha habido un error durante el proceso de login.\n' + error.response.data.data;
            setVisibleModal(ModalType.Error, ModalTitle.ErrorTitle, message)
        }); 
        dispatch({type: 'LOGIN', token: token})
      },
      logout: async (data) => {
        // logout logic
        dispatch({type: 'LOGOUT', token: token})
      },
      register: async (data) => {
        // register logic
        await axiosInstance.post('/sivaria/v1/user/register', data)
        .then(function (response) {
            navigation.navigate('Login');
        })
        .catch(function (error) {
            const message = 'Ha habido un error durante el proceso de registro del usuario. ' + error.response.data.data;
            setVisibleModal(ModalType.Error, ModalTitle.ErrorTitle, message)
        });
        dispatch({type: 'REGISTER', token: token})
      }

  }), []);

  return (
    <AuthContext.Provider value={authContext}>
      {children}
    </AuthContext.Provider>
  );
}
/*
export const AuthProvider = ({ children }) => {
  //const [state, dispatch] = useReducer(authReducer, initialState);

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
    // Perform login logic and set user and isAuthenticated
    await setItemLocalStorage('userToken', token);
    await setItemLocalStorage('email', email);
    setIsAuthenticated(true);
  };

  const logout = async () => {
    // Perform logout logic and reset user and isAuthenticated
    await removeItemLocalStorage('userToken');
    await removeItemLocalStorage('email');
    setIsAuthenticated(false);
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
*/
