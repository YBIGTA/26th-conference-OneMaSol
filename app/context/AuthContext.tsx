import AsyncStorage from '@react-native-async-storage/async-storage';
import * as Google from 'expo-auth-session/providers/google';
import * as WebBrowser from 'expo-web-browser';
import React, { createContext, useContext, useEffect, useState } from 'react';

WebBrowser.maybeCompleteAuthSession();

type User = {
  id: string;
  email: string;
  name: string;
  photoUrl?: string;
};

type AuthContextType = {
  user: User | null;
  isLoading: boolean;
  signIn: (token: string) => Promise<void>;
  signOut: () => Promise<void>;
};

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // 앱 시작 시 저장된 사용자 정보 로드
    loadUser();
  }, []);

  const loadUser = async () => {
    try {
      const userData = await AsyncStorage.getItem('user');
      if (userData) {
        setUser(JSON.parse(userData));
      }
    } catch (error) {
      console.error('Failed to load user data:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const signIn = async (token: string) => {
    try {
      const response = await fetch(`${process.env.EXPO_PUBLIC_API_URL}/auth/oauth/google`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to authenticate');
      }

      const data = await response.json();
      setUser(data.user);
      await AsyncStorage.setItem('user', JSON.stringify(data.user));
      await AsyncStorage.setItem('access_token', data.access_token);
    } catch (error) {
      console.error('Sign in error:', error);
      throw error;
    }
  };

  const signOut = async () => {
    try {
      await AsyncStorage.removeItem('user');
      await AsyncStorage.removeItem('access_token');
      setUser(null);
    } catch (error) {
      console.error('Sign out error:', error);
      throw error;
    }
  };

  return (
    <AuthContext.Provider value={{ user, isLoading, signIn, signOut }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}

export function useGoogleAuth() {
  const { signIn } = useAuth();
  const [request, response, promptAsync] = Google.useAuthRequest({
    iosClientId: process.env.EXPO_PUBLIC_GOOGLE_IOS_ID,
    androidClientId: process.env.EXPO_PUBLIC_GOOGLE_ANDROID_ID,
    webClientId: process.env.EXPO_PUBLIC_GOOGLE_WEB_ID,
    usePKCE: true,
    responseType: 'token',
  });

  useEffect(() => {
    if (response?.type === 'success') {
      const { access_token } = response.params;
      signIn(access_token);
    }
  }, [response]);

  return { promptAsync, request };
}

export default AuthProvider; 