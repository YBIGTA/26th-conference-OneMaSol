import { router } from 'expo-router';
import React from 'react';
import { StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import CalendarLayout from './_layout';

export default function CalendarScreen() {
  const handleDayPress = () => {
    router.push('./day');
  };

  return (
    <CalendarLayout>
      <View style={styles.container}>
        <Text style={styles.title}>캘린더</Text>
        <TouchableOpacity style={styles.button} onPress={handleDayPress}>
          <Text style={styles.buttonText}>오늘의 일정 보기</Text>
        </TouchableOpacity>
      </View>
    </CalendarLayout>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 16,
  },
  button: {
    backgroundColor: '#007AFF',
    padding: 16,
    borderRadius: 8,
    alignItems: 'center',
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
}); 