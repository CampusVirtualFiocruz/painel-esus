import { createPortal } from "react-dom";
import {
  FaMapMarkerAlt,
  FaUserFriends,
} from "react-icons/fa";
import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import { Spinner } from "bold-ui";
import { useAuth } from "../../context/AuthProvider/useAuth";
import { useTermsAcceptance } from "../../hooks";
import TermsOfUse from "../TermsOfUse";

const ProfileSelector = () => {
  const { profilesList, chooseProfile } = useAuth();
  const [loading, setLoading] = useState(true);
  const [showTerms, setShowTerms] = useState(false);
  const [, setSelectedProfile] = useState<any>(null);
  const { checkTermsAcceptance } = useTermsAcceptance();

  let navigate = useNavigate();

  const handleProfileSelection = async (profile: any) => {
    await chooseProfile(profile);
    
    const hasAcceptedTerms = await checkTermsAcceptance();
    
    if (hasAcceptedTerms) {
      navigate("/selecionarvisualizacao");
    } else {
      setSelectedProfile(profile);
      setShowTerms(true);
    }
  };

  const handleTermsAccept = () => {
    setShowTerms(false);
    navigate("/selecionarvisualizacao");
  };

  useEffect(() => {
    const initializeProfileSelection = async () => {
      if ((profilesList || []).length > 1) {
        setLoading(false);
      } else if (profilesList?.[0]) {
        await chooseProfile(profilesList[0]);
        
        const hasAcceptedTerms = await checkTermsAcceptance();
        
        if (hasAcceptedTerms) {
          navigate("/selecionarvisualizacao");
        } else {
          setSelectedProfile(profilesList[0]);
          setShowTerms(true);
          setLoading(false);
        }
      }
    };

    initializeProfileSelection();
  }, [profilesList, navigate, chooseProfile, checkTermsAcceptance]);

  return (
    <>
      {showTerms && <TermsOfUse onAccept={handleTermsAccept} />}
      {!showTerms && createPortal(
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
            alignItems: "center",
          }}
        >
          <div
            style={{
              margin: "0 auto",
              border: "1px solid black",
              padding: "20px",
              backgroundColor: "white",
            }}
          >
            {loading ? (
              <div style={{ width: "300px", height: "300px", textAlign: "center" }}>
                <Spinner />
              </div>
            ) : (
              <div>
                <h4 style={{ fontWeight: "bold", marginBottom: "20px" }}>
                  Em qual perfil você deseja logar:
                </h4>
                <div style={{ maxHeight: "70vh", overflow: "auto" }}>
                  {(profilesList ?? [])?.map((i) => {
                    return (<>
                      <div
                        style={{
                          border: "1px solid black",
                          padding: "20px",
                          marginBottom: "10px",
                          userSelect: "none",
                          cursor: "pointer",
                        }}
                        onClick={() => handleProfileSelection(i)}
                      >
                        <b>CBO {i.cbo}</b>:{" "}
                        <span style={{ fontSize: "14px" }}> {i.profissao}</span>
                        {Boolean(i?.ubs?.nome) && (
                          <div style={{ fontSize: "12px", marginTop: "6px" }}>
                            {" "}
                            <FaMapMarkerAlt color="#1c1a92" /> {i?.ubs?.nome}
                          </div>
                        )}
                        {Boolean(i?.equipe) && (
                          <div style={{ fontSize: "12px", marginTop: "6px" }}>
                            {" "}
                            <FaUserFriends color="#1c1a92" /> {i?.equipe?.nome}
                          </div>
                        )}
                      </div>
                     </>
                    );
                  })}
                </div>
              </div>
            )}
          </div>
        </div>,
        document.body
      )}
    </>
  );
};

export default ProfileSelector;
