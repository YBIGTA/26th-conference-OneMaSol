import { router } from 'expo-router';
import React from 'react';
import { StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import SettingsLayout from './_layout';

export default function SettingsScreen() {
  const handleNavigateToChat = () => {
    router.push('../chat');
  };

  return (
    <SettingsLayout>
      <View style={styles.container}>
        <Text style={styles.text}>Settings Screen</Text>
        <TouchableOpacity 
          style={styles.button}
          onPress={handleNavigateToChat}
        >
          <Text style={styles.buttonText}>Go to Chat</Text>
        </TouchableOpacity>
      </View>
    </SettingsLayout>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  text: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  button: {
    marginTop: 20,
    padding: 10,
    backgroundColor: '#007AFF',
    borderRadius: 8,
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
  },
}); 