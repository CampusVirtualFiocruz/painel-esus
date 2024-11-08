export interface IUser {
  username?: string;
  token?: string;
  refreshToken?: string;
}

export interface IContext extends IUser {
  authenticate: (username: string, password: string) => Promise<any>;
  logout: () => void;
  chooseProfile: (profileData: any) => void;
  profilesList: Array<any> | null
}

export interface IAuthProvider {
  children: JSX.Element;
}
