import { createNativeStackNavigator } from "@react-navigation/native-stack";
import LoginScreen from "../screens/login-screen";
import HomeScreen from "../screens/home-screen";
import RegisterScreen from "../screens/register-screen";
import { Platform } from "react-native";
import { HomeTabsNavigator } from "./logged-tab-stack";
import { useContext } from "react";
import { AuthContext } from "../context/auth-context";

const UserStack = createNativeStackNavigator();

export const UserStackNavigator = () => {
  const { isAuthenticated } = useContext(AuthContext);

  return (
    <UserStack.Navigator screenOptions={ { headerShown: Platform.OS !== 'web' ? true : false } }>
      {isAuthenticated ? ( 
        <UserStack.Screen name="Dashboard">     
        {() => (  
          <HomeTabsNavigator />
        )}
        </UserStack.Screen>
      ) : (
        <>
          <UserStack.Screen name="Login" component={LoginScreen}/>
          <UserStack.Screen name="Register" component={RegisterScreen} />
        </>    
      )}
    </UserStack.Navigator>
  );
}

/*
export const NonLoggedUserStack = () => {
  return (
    <Stack.Navigator screenOptions={{headerShown: false}}>
      <Stack.Screen name="Login" component={LoginScreen} />
      <Stack.Screen name="Register" component={RegisterScreen} />
    </Stack.Navigator>
  );
}


export const LoggedUserStack = () => {
  return (
    <Stack.Navigator screenOptions={{headerShown: false}}>
      <Stack.Screen name="Home" component={HomeScreen} />
    </Stack.Navigator>
  );
};
*/