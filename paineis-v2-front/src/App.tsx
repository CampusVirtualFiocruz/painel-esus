import { useLayoutEffect } from "react";
import { BrowserRouter, Routes, Route, useLocation } from "react-router-dom";
import { AuthProvider } from './context/AuthProvider';
import { InfoProvider } from './context/infoProvider';
import { ProtectedLayout } from "./components/ProtectedLayout";

import { Login } from './pages/Login';
import { Painel } from './pages/Painel';
import { Gestantes } from './pages/Gestantes';
import { Gestante } from './pages/Gestante';
import { GestantesList } from './pages/GestantesList';
import { Diabetes } from './pages/Diabetes';
import { Hipertensao } from './pages/Hipertensao';
import { HipertensosList } from './pages/HipertensosList';
import { DiabeticosList } from './pages/DiabeticosList';
import { SindromesAgudas } from './pages/SindromesAgudas/SindromesAgudas';
import { SelecionarUbs } from './pages/SelecionarUbs';
import SaudeBucal from "./pages/SaudeBucal/SaudeBucal";

const Wrapper = ({ children }: { children: JSX.Element }) => {
  const location = useLocation();
  useLayoutEffect(() => {
    document.documentElement.scrollTo(0, 0);
  }, [location.pathname]);
  return children
}

function App() {
  return (
    <AuthProvider>
      <InfoProvider>
        <BrowserRouter>
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
                } />
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
                } />
              <Route
                path="/gestantes/list/:id"
                element={
                  <ProtectedLayout>
                    <GestantesList />
                  </ProtectedLayout>
                } />
              <Route
                path="/diabetes"
                element={
                  <ProtectedLayout>
                    <Diabetes />
                  </ProtectedLayout>
                } />
              <Route
                path="/diabetes/:id"
                element={
                  <ProtectedLayout>
                    <Diabetes />
                  </ProtectedLayout>
                } />
              <Route
                path="/diabeticos"
                element={
                  <ProtectedLayout>
                    <DiabeticosList />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/diabeticos/:id"
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
                } />
              <Route
                path="/hipertensao/:id"
                element={
                  <ProtectedLayout>
                    <Hipertensao />
                  </ProtectedLayout>
                } />
              <Route
                path="/hipertensos"
                element={
                  <ProtectedLayout>
                    <HipertensosList />
                  </ProtectedLayout>
                }
              />
              <Route
                path="/hipertensos/:id"
                element={
                  <ProtectedLayout>
                    <HipertensosList />
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
