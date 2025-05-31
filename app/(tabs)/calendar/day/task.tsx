import { useLocalSearchParams } from 'expo-router';
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import CalendarLayout from '../_layout';

export default function TaskDetailScreen() {
  const { date, taskId } = useLocalSearchParams<{ date: string; taskId: string }>();

  return (
    <CalendarLayout>
      <View style={styles.container}>
        <Text style={styles.title}>{date} 일정 상세</Text>
        <Text style={styles.subtitle}>Task ID: {taskId}</Text>
        {/* TODO: Add task details */}
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
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
    marginBottom: 16,
  },
}); 