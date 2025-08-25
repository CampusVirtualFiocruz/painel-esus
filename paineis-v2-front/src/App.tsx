import { useLayoutEffect } from "react";
import { BrowserRouter, Route, Routes, useLocation } from "react-router-dom";
import BarraBrasil from "./components/BarraBrasil";
import { ProtectedLayout } from "./components/ProtectedLayout";
import { AuthProvider } from "./context/AuthProvider";
import { getUserLocalStorage } from "./context/AuthProvider/util";
import { InfoProvider } from "./context/infoProvider";

import Bucal from "./pages/Bucal";
import Diabetes from "./pages/Diabetes";
import FeridaVascular from "./pages/FeridaVascular";
import { Gestante } from "./pages/Gestante";
import { Gestantes } from "./pages/Gestantes";
import { GestantesList } from "./pages/GestantesList";
import Hipertensao from "./pages/Hipertensao";
import Idosa from "./pages/Idosa";
import Infantil from "./pages/Infantil";
import ListaNominal from "./pages/ListaNominal";
import { Login } from "./pages/Login";
import NovoPainel from "./pages/NovoPainel";
import { Painel } from "./pages/Painel";
import Qualidade from "./pages/Qualidade";
import { SelecionarUbs } from "./pages/SelecionarUbs";
import { SelecionarVisualizacao } from "./pages/SelecionarVisualizacao";
import { SindromesAgudas } from "./pages/SindromesAgudas/SindromesAgudas";
import Tabagismo from "./pages/Tabagismo";

const Wrapper = ({ children }: { children: JSX.Element }) => {
  const location = useLocation();

  useLayoutEffect(() => {
    document.documentElement.scrollTo(0, 0);
  }, [location.pathname]);
  return children;
};

export function getProfile() {
  const user = getUserLocalStorage();
  const parts = user?.token.split(".");
  if (parts.length !== 3) {
    console.error("Token JWT inválido");
    return;
  }
  const payload = parts?.[1];

  if (!payload) {
    return;
  }

  const decodedPayload = atob(payload);
  return JSON.parse(decodedPayload)?.profiles[0];
}

export function getUBS() {
  const user = getUserLocalStorage();
  const parts = user?.token.split(".");

  if (parts && parts.length !== 3) {
    console.error("Token JWT inválido");
    return;
  }
  const payload = parts?.[1];

  if (!payload) {
    return;
  }

  const decodedPayload = atob(payload);
  return JSON.parse(decodedPayload)?.ubs;
}

export function userCanSelectUBS() {
  const user = getUserLocalStorage();
  const parts = user?.token.split(".");

  if (parts && parts.length !== 3) {
    console.error("Token JWT inválido");
    return;
  }
  const payload = parts?.[1];

  if (!payload) {
    return;
  }

  const decodedPayload = atob(payload);

  return (
    String(JSON.parse(decodedPayload)?.profiles[0]).toUpperCase() === "ADMIN"
  );
}

export function isUserFromUBS() {
  const user = getUserLocalStorage();
  const parts = user?.token.split(".");
  if (parts.length !== 3) {
    console.error("Token JWT inválido");
    return;
  }
  const payload = parts?.[1];

  if (!payload) {
    return;
  }

  const decodedPayload = atob(payload);

  return !Number.isNaN(Number(String(JSON.parse(decodedPayload)?.ubs)));
}

function App() {
  return (
    <AuthProvider>
      <InfoProvider>
        <BrowserRouter>
          <BarraBrasil />
          <Wrapper>
            <Routes>
              <Route path="/" element={<Login />} />
              <Route
                path="/selecionarubs"
                element={
                  <ProtectedLayout>
                    <SelecionarUbs />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/selecionarvisualizacao"
                element={
                  <ProtectedLayout>
                    <SelecionarVisualizacao />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/antigo-painelx"
                element={
                  <ProtectedLayout>
                    <Painel />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/antigo-painel/:id"
                element={
                  <ProtectedLayout>
                    <Painel />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/home"
                element={
                  <ProtectedLayout>
                    <NovoPainel />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/home/:id"
                element={
                  <ProtectedLayout>
                    <NovoPainel />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/gestantes"
                element={
                  <ProtectedLayout>
                    <Gestantes />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/tabagismo"
                element={
                  <ProtectedLayout>
                    <Tabagismo />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/ferida-vascular"
                element={
                  <ProtectedLayout>
                    <FeridaVascular />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/gestantes/:id"
                element={
                  <ProtectedLayout>
                    <Gestantes />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/gestante/:id"
                element={
                  <ProtectedLayout>
                    <Gestante />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/gestantes/list"
                element={
                  <ProtectedLayout>
                    <GestantesList />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/qualidade"
                element={
                  <ProtectedLayout>
                    <Qualidade />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/qualidade/:id"
                element={
                  <ProtectedLayout>
                    <Qualidade />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/infantil"
                element={
                  <ProtectedLayout>
                    <Infantil />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/infantil/:id"
                element={
                  <ProtectedLayout>
                    <Infantil />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/idosa"
                element={
                  <ProtectedLayout>
                    <Idosa />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/idosa/:id"
                element={
                  <ProtectedLayout>
                    <Idosa />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/gestantes/list/:id"
                element={
                  <ProtectedLayout>
                    <GestantesList />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/diabetes"
                element={
                  <ProtectedLayout>
                    <Diabetes />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/diabetes/:id"
                element={
                  <ProtectedLayout>
                    <Diabetes />
                  </ProtectedLayout>
                }
              />
               <Route
                path="/hipertensao"
                element={
                  <ProtectedLayout>
                    <Hipertensao />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/hipertensao/:id"
                element={
                  <ProtectedLayout>
                    <Hipertensao />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/lista-nominal/:id"
                element={
                  <ProtectedLayout>
                    <ListaNominal />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/sindromes-agudas"
                element={
                  <ProtectedLayout>
                    <SindromesAgudas />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/sindromes-agudas/:id"
                element={
                  <ProtectedLayout>
                    <SindromesAgudas />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/saude-bucal"
                element={
                  <ProtectedLayout>
                    <Bucal />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/saude-bucal/:id"
                element={
                  <ProtectedLayout>
                    <Bucal />
                  </ProtectedLayout>
                }
              />
            </Routes>
          </Wrapper>
        </BrowserRouter>
      </InfoProvider>
    </AuthProvider>
  );
}

export default App;
