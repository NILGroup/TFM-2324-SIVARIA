import HomeScreen from "../screens/logged-users/home-screen";
import ProfileScreen from "../screens/logged-users/profile-screen";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { AntDesign } from '@expo/vector-icons';
import { Platform, Text } from "react-native";
import { useContext } from "react";
import { UserContext } from "../context/user-context";
import HistoryScreen from "../screens/logged-users/history-screen";
import ContactScreen from "../screens/logged-users/contact-screen";
import PatientsScreen from "../screens/logged-users/patients-screen";

const Tab = createBottomTabNavigator();

export const DashboardTabsScreen = ({navigation}) => {
  const userData = useContext(UserContext);
  return (
    <Tab.Navigator 
        screenOptions={({ route }) => ({
          tabBarLabel: ({focused}) => {
            let color = focused ? "white" : "#96bf96";
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
        {(userData.rolSlug !== 'joven') &&
          (
            <Tab.Screen 
              name="History" 
              component={HistoryScreen}
            />
          )
        }
        {(userData.rolSlug !== 'joven') &&
          (
            <Tab.Screen 
              name="Patients" 
              component={PatientsScreen}
            />
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