import { DefaultTheme, NavigationContainer } from '@react-navigation/native';
import React from 'react';
import AppNavigator from './app/navigation/AppNavigator';

const MyTheme = {
  ...DefaultTheme,
  colors: {
    ...DefaultTheme.colors,
    background: 'black',
  },
};

export default function App() {
  return (
    <NavigationContainer theme={MyTheme}>
      <AppNavigator />
    </NavigationContainer>
  );
} 