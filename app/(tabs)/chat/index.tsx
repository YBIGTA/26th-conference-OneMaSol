export const options = {
  headerShown: false,
  title: '',
};

import { Ionicons } from '@expo/vector-icons';
import { router, useLocalSearchParams } from 'expo-router';
import React from 'react';
import { StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import ChatLayout from './_layout';

export default function ChatScreen() {
  const { chatId } = useLocalSearchParams<{ chatId?: string }>();

  const handleMorePress = () => {
    router.push('./history');
  };

  return (
    <ChatLayout>
      <View style={styles.container}>
        <View style={styles.header}>
          <TouchableOpacity onPress={handleMorePress} style={styles.moreButton}>
            <Ionicons name="menu" size={24} color="#000" />
          </TouchableOpacity>
          <Text style={styles.title}>
            {chatId ? `채팅방 ${chatId}` : '채팅'}
          </Text>
        </View>
        <TouchableOpacity style={styles.button} onPress={handleMorePress}>
          <Text style={styles.buttonText}>과거 채팅 보기</Text>
        </TouchableOpacity>
      </View>
    </ChatLayout>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#eee',
  },
  moreButton: {
    marginRight: 16,
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  button: {
    backgroundColor: '#007AFF',
    padding: 16,
    borderRadius: 8,
    alignItems: 'center',
    margin: 16,
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
}); 