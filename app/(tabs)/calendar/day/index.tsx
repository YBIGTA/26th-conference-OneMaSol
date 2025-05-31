import { router, useLocalSearchParams } from 'expo-router';
import React from 'react';
import { StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import CalendarLayout from '../_layout';

export default function DayScheduleScreen() {
  const { date } = useLocalSearchParams<{ date: string }>();

  const handleTaskPress = () => {
    router.push('./task');
  };

  return (
    <CalendarLayout>
      <View style={styles.container}>
        <Text style={styles.title}>{date} 일정</Text>
        <TouchableOpacity style={styles.button} onPress={handleTaskPress}>
          <Text style={styles.buttonText}>일정 상세 보기</Text>
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