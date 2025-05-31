import { Ionicons } from '@expo/vector-icons';
import { router } from 'expo-router';
import React from 'react';
import { FlatList, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import ChatLayout from './_layout';

// 임시 데이터
const mockChats = [
  { id: '1', title: '채팅방 1', lastMessage: '마지막 메시지 1', timestamp: '2024-03-20' },
  { id: '2', title: '채팅방 2', lastMessage: '마지막 메시지 2', timestamp: '2024-03-19' },
];

export default function ChatHistoryScreen() {
  const handleBackPress = () => {
    router.back();
  };

  const handleChatPress = (chatId: string) => {
    router.replace({
      pathname: '/chat',
      params: { chatId }
    });
  };

  return (
    <ChatLayout>
      <View style={styles.container}>
        <View style={styles.header}>
          <TouchableOpacity onPress={handleBackPress} style={styles.backButton}>
            <Ionicons name="arrow-back" size={24} color="#000" />
          </TouchableOpacity>
          <Text style={styles.title}>과거 채팅</Text>
        </View>
        <FlatList
          data={mockChats}
          keyExtractor={(item) => item.id}
          renderItem={({ item }) => (
            <TouchableOpacity
              style={styles.chatItem}
              onPress={() => handleChatPress(item.id)}
            >
              <Text style={styles.chatTitle}>{item.title}</Text>
              <Text style={styles.lastMessage}>{item.lastMessage}</Text>
              <Text style={styles.timestamp}>{item.timestamp}</Text>
            </TouchableOpacity>
          )}
        />
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
  backButton: {
    marginRight: 16,
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  chatItem: {
    padding: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#eee',
  },
  chatTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 4,
  },
  lastMessage: {
    fontSize: 14,
    color: '#666',
    marginBottom: 4,
  },
  timestamp: {
    fontSize: 12,
    color: '#999',
  },
}); 