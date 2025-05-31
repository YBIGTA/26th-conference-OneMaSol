import React from 'react';
import { StyleSheet, View } from 'react-native';

interface CalendarLayoutProps {
  children: React.ReactNode;
}

export default function CalendarLayout({ children }: CalendarLayoutProps) {
  return (
    <View style={styles.container}>
      {children}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
}); 