import { createContext, useEffect, useState } from 'react';
import jwt from 'jwt-decode';
import { IAuthProvider, IContext, IUser } from './types';
import {
  getUserLocalStorage,
  LoginRequest,
  ProfilesRequest,
  setUserLocalStorage,
} from './util';

export const AuthContext = createContext<IContext>({} as IContext);

type PayloadJwt = {
  cns: string;
  municipio: string;
  uf: string;
  username: string;
  exp: number;
};

export const AuthProvider = ({ children }: IAuthProvider) => {
  const [user, setUser] = useState<IUser | null>();
  const [profilesList, setProfiles] = useState<Array<any> | null>(null);

  useEffect(() => {
    const user = getUserLocalStorage();

    if (user) {
      setUser(user);
    }
  }, []);

  async function authenticate(username: string, password: string) {
    const response = await LoginRequest(username, password);
    const payload: PayloadJwt = jwt(response.data);

    const user = {
      token: response.data,
      expirationDate: response.exp,
      username,
      fullName: payload.username,
      cns: payload.cns,
      municipio: payload.municipio,
      uf: payload.uf,
    };

    setUser(user);
    setUserLocalStorage(user);
    setProfiles(response?.profiles);

    return { response, payload, user };
  }

  async function chooseProfile(profileData: any) {
    const response = await ProfilesRequest(profileData);
    const userWithNewToken = {
      ...user,
      token: response.data || user?.token,
      currentProfile: {
        currentTeam: profileData?.equipe?.id,
        currentUbs: profileData?.ubs?.id,
        info: response?.info,
      },
    };

    setUser(userWithNewToken);
    setUserLocalStorage(userWithNewToken);
    setProfiles(response?.profiles);
  }

  function logout() {
    setUser(null);
    setUserLocalStorage(null);
  }

  return (
    <AuthContext.Provider
      value={{ ...user, authenticate, chooseProfile, profilesList, logout }}
    >
      {children}
    </AuthContext.Provider>
  );
};
