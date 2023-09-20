import { useContext } from "react";
import { InfoContext } from ".";

export const useInfo = () => {
  const context = useContext(InfoContext);

  return context;
};
