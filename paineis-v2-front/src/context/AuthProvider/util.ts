import { Api } from "../../services/api";
import { IUser } from "./types";

export function setUserLocalStorage(user: IUser | null) {
  localStorage.setItem("u", JSON.stringify(user));
}

export function getUserLocalStorage() {
  const json = localStorage.getItem("u");

  if (!json) {
    return null;
  }

  const user = JSON.parse(json);

  return user ?? null;
}

export async function LoginRequest(username: string, password: string) {
  try {
    const response = await Api.post("auth", { username, password });

    return response.data;
  } catch (error) {
    return null;
  }
}

export async function ProfilesRequest(profileData: any) {
  try {
    if(typeof profileData === "object"){
      const response = await Api.post("auth/profile", profileData);
      return { ...response.data, info: "success" };
    }else{
      return { info: "not-configured" }
    }
  } catch (error) {
    return null;
  }
}
