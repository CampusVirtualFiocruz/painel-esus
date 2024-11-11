import { useLayoutEffect } from "react";
import { BrowserRouter, Routes, Route, useLocation } from "react-router-dom";
import { AuthProvider } from "./context/AuthProvider";
import { InfoProvider } from "./context/infoProvider";
import { ProtectedLayout } from "./components/ProtectedLayout";
import { LocaleContext } from "bold-ui";
//import ptBr from "bold-ui/i18n/locales/pt-BR";
import { Login } from "./pages/Login";
import { Painel } from "./pages/Painel";
import { Gestantes } from "./pages/Gestantes";
import { Gestante } from "./pages/Gestante";
import { GestantesList } from "./pages/GestantesList";
import { Diabetes } from "./pages/Diabetes";
import { Hipertensao } from "./pages/Hipertensao";
import ListaNominal from "./pages/ListaNominal";
import { DiabeticosList } from "./pages/DiabeticosList";
import { SindromesAgudas } from "./pages/SindromesAgudas/SindromesAgudas";
import { SelecionarUbs } from "./pages/SelecionarUbs";
import { SelecionarVisualizacao } from "./pages/SelecionarVisualizacao";
import Tabagismo from "./pages/Tabagismo";
import FeridaVascular from "./pages/FeridaVascular";
import { SaudeBucal } from "./pages/SaudeBucal/SaudeBucal";
import BarraBrasil from "./components/BarraBrasil";
import { getUserLocalStorage } from "./context/AuthProvider/util";
import Qualidade from "./pages/Qualidade";
import Infantil from "./pages/Infantil";

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
                path="/painelx"
                element={
                  <ProtectedLayout>
                    <Painel />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/painel/:id"
                element={
                  <ProtectedLayout>
                    <Painel />
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
                path="/infantil"
                element={
                  <ProtectedLayout>
                    <Infantil />
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
                path="/diabeticos"
                element={
                  <ProtectedLayout>
                    <DiabeticosList />
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
                    <SaudeBucal />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/saude-bucal/:id"
                element={
                  <ProtectedLayout>
                    <SaudeBucal />
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
