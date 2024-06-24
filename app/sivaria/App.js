import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { HomeStack } from './src/navigation/stack';

export default function App() {
  return (
    <NavigationContainer>
      <HomeStack />
    </NavigationContainer>
  );
}

/*
export default function App() {
  return (
    <View style={styles.container}>
      <Text>Open up App.js to star working on your app!</Text>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
*/