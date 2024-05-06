import { memo } from "react";
import { useNavigate } from "react-router-dom";

import { useAuth } from "../context/AuthProvider/useAuth";
import { getUserLocalStorage } from "../context/AuthProvider/util";
import "../styles/header.scss";

import imgLogo from "../assets/images/logo.svg";
import imgUser from "../assets/images/user-alt.svg";
import imgLogout from "../assets/images/logout.svg";

import { getFirstName } from "../utils";
import { useInfo } from "../context/infoProvider/useInfo";
import BarraBrasil from "./BarraBrasil";

export function Header() {
  const { logout } = useAuth();
  const user = getUserLocalStorage();
  let navigate = useNavigate();

  function handleHome() {
    navigate("/selecionarubs");
  }

  function handleLogout() {
    logout();
    navigate("/");
  }
  const infoContext = useInfo();
  const city = infoContext.cityInformation;
  return (
    <>
      <BarraBrasil />
      <header id="header">
        <div className="siteInfo">
          <div className="logoName" onClick={handleHome}>
            <img src={imgLogo} alt="e-SUS" />
            <strong>
              Painel e-SUS /{" "}
              <span>
                {city?.municipio} - {city?.uf}
              </span>
            </strong>
          </div>
        </div>

        <div className="userInfo">
          <img src={imgUser} alt="Profissional" />
          <span>{getFirstName(user?.fullName)}</span>

          <div className="logoutWrapper" onClick={handleLogout}>
            <img src={imgLogout} alt="Sair" />

            <a href="/" onClick={handleLogout} className="logout">
              Sair
            </a>
          </div>
        </div>
      </header>
    </>
  );
}

export const MemoizedHeader = memo(Header);
