import { createPortal } from "react-dom";
import { FaMapMarkerAlt, FaUserAlt, FaUserAltSlash, FaUserFriends } from "react-icons/fa";
import { useAuth } from "../../context/AuthProvider/useAuth";
import { useNavigate } from "react-router-dom";

const ProfileSelector = () => {
  const { profilesList, chooseProfile } = useAuth();
  let navigate = useNavigate();

  return createPortal(
    <div
      style={{
        width: "100vw",
        height: "100vh",
        backgroundColor: "rgba(255, 255, 255, 0.4)",
        position: "fixed",
        color: "black",
        top: 0,
        left: 0,
        display: "flex",
        justifyContent: "center",
        alignItems: "center"
    }}
    >
        <div style={{ margin: "0 auto", border: "1px solid black", padding: "20px", backgroundColor: "white" }}>
          <h4 style={{ fontWeight: "bold", marginBottom: "20px" }}>Em qual perfil você deseja logar:</h4>
            {(profilesList ?? [])?.map((i) => {
              return <div
              style={{
                  border: "1px solid black",
                  padding: "20px",
                  marginBottom: "10px",
                  userSelect: "none",
                  cursor: "pointer"
                }}
                onClick={async () => {
                  await chooseProfile(i);
                  navigate("/selecionarvisualizacao");
                }}
              >
                  <b>CBO {i.cbo}</b>: <span style={{ fontSize: "14px" }}> {i.profissao}</span>
                  {Boolean(i?.ubs?.nome) && <div style={{ fontSize: "12px", marginTop: "6px" }}> <FaMapMarkerAlt color="#1c1a92" /> {i?.ubs?.nome}</div>}
                  {Boolean(i?.equipe) && <div style={{ fontSize: "12px", marginTop: "6px" }}> <FaUserFriends color="#1c1a92" /> {i?.equipe?.nome}</div>}
                </div>
            })}
        </div>
    </div>,
    document.body
  )};

export default ProfileSelector;
