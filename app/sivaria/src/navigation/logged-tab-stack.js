import HomeScreen from "../screens/logged-users/home-screen";
import ProfileScreen from "../screens/logged-users/profile-screen";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { AntDesign } from '@expo/vector-icons';
import { Platform, Text } from "react-native";
import stylesSivaria from "../styles/styles-sivaria";
import { useContext } from "react";
import { UserContext } from "../context/user-context";
import HistoryScreen from "../screens/logged-users/history-screen";
import ContactScreen from "../screens/logged-users/contact-screen";
import PatientsScreen from "../screens/logged-users/patients-screen";
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

//<AntDesign name="solution1" size={24} color="black" />

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
              case 'History':
                  return <Text style={{color: color}}>Historial</Text>;
              case 'Patients':
                  let title = userData.rolSlug === 'padre' || userData.rolSlug === 'madre' 
                    ? 'Familias' 
                    : 'Pacientes';
                  return <Text style={{color: color}}>{title}</Text>;
              case 'Profile':
                return <Text style={{color: color}}>Perfil</Text>
                case 'Contact':
                return <Text style={{color: color}}>Contacto</Text>
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
                case 'History':
                    iconName = 'solution1';
                    break;
                case 'Patients':
                    iconName = 'team';
                    break;
                case 'Profile':
                  iconName = 'user'
                  break;
                case 'Contact':
                  iconName = 'phone'
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
        {userData.rolSlug && userData.rolSlug !== 'joven' &&
          (
          <>
            <Tab.Screen 
              name="History" 
              component={HistoryScreen}
            />
            <Tab.Screen 
              name="Patients" 
              component={PatientsScreen}
            />
          </>
        )
        }
        <Tab.Screen 
            name="Profile" 
            component={ProfileScreen}
        />
        <Tab.Screen 
            name="Contact" 
            component={ContactScreen}
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