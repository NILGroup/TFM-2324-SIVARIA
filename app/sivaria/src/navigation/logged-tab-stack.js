import HomeScreen from "../screens/logged-users/home-screen";
import ProfileScreen from "../screens/logged-users/profile-screen";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { AntDesign } from '@expo/vector-icons';
import { Platform, Text } from "react-native";
import stylesSivaria from "../styles/styles-sivaria";
import { useContext } from "react";
import { UserContext } from "../context/user-context";
//import { createAppContainer } from "react-navigation"; 

/*
const TabNavigator = createBottomTabNavigator({
        Home: {
            screen: HomeScreen,
            navigationOptions: {
                tabBarLabel: 'Home',
                tabBarOptions: {
                    activeTintColor: '#006E51',
                },
                tabBarIcon: (tabInfo) => {
                    return ( 
                        <Ionicons 
                          name="md-home"
                          size={24} 
                          color={tabInfo.focused ? "#006E51" : "#8e8e93"} 
                        /> 
                    )
                }

            }
        }
    }
);

export const HomeTabNavigator = createAppContainer(TabNavigator);
*/

const Tab = createBottomTabNavigator();

export const DashboardTabsScreen = ({navigation}) => {
  const userData = useContext(UserContext);
  return (
    <Tab.Navigator 
        screenOptions={({ route }) => ({
          tabBarLabel: ({focused}) => {
            let color = focused ? "white" : "#96bf96";
            //console.log(route.name);
            //console.log(color);
            let routeName = route.name;
            switch(routeName) {
              case 'Home':
                return <Text style={{color: color}}>Home</Text>;
              case 'Profile':
                return <Text style={{color: color}}>Perfil</Text>
            }
          },
          tabBarStyle: {
            backgroundColor: '#006E51',
            paddingBottom: 5,
            paddingTop: 5,
            height: Platform.OS === 'ios' ? 80 : 60,
          },
          tabBarLabelPosition: 'below-icon',
          tabBarIcon: ({ focused }) => {
              let iconName;
              let color = focused ? "white" : "#96bf96";
              let routeName = route.name;
              switch(routeName) {
                case 'Home':
                  iconName = 'home';
                  break;
                case 'Profile':
                  iconName = 'user'
                  break;
              }
              return <AntDesign 
                          name={iconName} 
                          size={24} 
                          color={color} 
                      />;
          },
          headerShown: false,
        })}
      >      
        <Tab.Screen 
            name="Home" 
            component={HomeScreen}
        />
        <Tab.Screen 
            name="Profile" 
            component={ProfileScreen}
        />
    </Tab.Navigator>
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