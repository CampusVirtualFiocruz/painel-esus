import { Link } from "react-router-dom";
import { useAuth } from "../../context/AuthProvider/useAuth";

export const ProtectedLayout = ({ children }: { children: JSX.Element }) => {
  const auth = useAuth();

  if (!auth.username) {
    return (
      <>
        <h1>Você não tem permissão para acessar esta página.</h1>
        <Link to="/">Fazer login</Link>
      </>
    );
  }

  return children;
};
