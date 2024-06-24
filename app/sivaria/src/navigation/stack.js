import { createNativeStackNavigator } from "@react-navigation/native-stack";
import LoginScreen from "../screens/login-screen";
import DashboardScreen from "../screens/dashboard-screen";
import RegisterScreen from "../screens/register-screen";

const Stack = createNativeStackNavigator();

export const HomeStack = () => {
    return (
      <Stack.Navigator screenOptions={{headerShown: false}}>
        <Stack.Screen name="Login" component={LoginScreen} />
        <Stack.Screen name="Dashboard" component={DashboardScreen} />
        <Stack.Screen name="Register" component={RegisterScreen} />
      </Stack.Navigator>
    );
  }
