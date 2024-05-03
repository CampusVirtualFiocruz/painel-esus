import { createContext, useEffect, useState } from "react";
import { IAuthProvider, IContext, IUser } from "./types";
import { getUserLocalStorage, LoginRequest, setUserLocalStorage } from "./util";
import jwt from 'jwt-decode';

export const AuthContext = createContext<IContext>({} as IContext);

type PayloadJwt = {
  cns: string;
  municipio: string;
  uf: string;
  username: string;
  exp: number;
}

export const AuthProvider = ({ children }: IAuthProvider) => {
  const [user, setUser] = useState<IUser | null>();

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
      uf: payload.uf
    };

    setUser(user);
    setUserLocalStorage(user);
  }

  function logout() {
    setUser(null);
    setUserLocalStorage(null);
  }

  return (
    <AuthContext.Provider value={{ ...user, authenticate, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
