import { useState } from "react";
import { createPortal } from "react-dom";
import { Button } from "bold-ui";
import { Spinner } from "reactstrap";
import { useNavigate } from "react-router-dom";
import { useTermsAcceptance } from "../../hooks";
import termsData from "../../data/termsOfUse.json";

interface TermsOfUseProps {
  onAccept: () => void;
}

const TermsOfUse = ({ onAccept }: TermsOfUseProps) => {
  const [accepted, setAccepted] = useState(false);
  const navigate = useNavigate();
  const { acceptTerms, loading } = useTermsAcceptance();

  const handleAccept = async () => {
    if (!accepted) return;
    
    try {
      await acceptTerms();
      onAccept();
      navigate("/selecionarvisualizacao");
    } catch (error) {
      console.error("Error saving term acceptance:", error);
      onAccept();
      navigate("/selecionarvisualizacao");
    }
  };

  return createPortal(
    <div
      style={{
        width: "100vw",
        height: "100vh",
        backgroundColor: "rgba(0, 0, 0, 0.7)",
        position: "fixed",
        color: "black",
        top: 0,
        left: 0,
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        zIndex: 10000,
      }}
    >
      <div
        style={{
          maxWidth: "800px",
          width: "90%",
          maxHeight: "90vh",
          border: "1px solid #ccc",
          borderRadius: "8px",
          padding: "30px",
          backgroundColor: "white",
          boxShadow: "0 4px 20px rgba(0, 0, 0, 0.3)",
          overflow: "auto",
        }}
      >
        <div>
          <h2 style={{ fontWeight: "bold", marginBottom: "20px", textAlign: "center" }}>
            {termsData.title}
          </h2>
          
          <div style={{ 
            maxHeight: "400px", 
            overflow: "auto", 
            border: "1px solid #ddd", 
            padding: "20px", 
            marginBottom: "20px",
            backgroundColor: "#f9f9f9"
          }}>
            {termsData.sections.map((section, index) => (
              <div key={index} style={{ marginBottom: "20px" }}>
                <h3>{section.title}</h3>
                <p>{section.content}</p>
                {section.list && (
                  <div style={{ marginLeft: "20px" }}>
                    {section.list.map((item, itemIndex) => (
                      <div key={itemIndex} style={{ marginBottom: "5px", display: "flex", alignItems: "flex-start" }}>
                        <span style={{ marginRight: "8px", marginTop: "2px" }}>•</span>
                        <span>{item}</span>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            ))}
          </div>

          <div style={{ 
            display: "flex", 
            alignItems: "center", 
            marginBottom: "20px",
            padding: "15px",
            border: "1px solid #ddd",
            borderRadius: "4px",
            backgroundColor: "#f0f8ff"
          }}>
            <input
              type="checkbox"
              id="terms-checkbox"
              checked={accepted}
              onChange={(e) => setAccepted(e.target.checked)}
              style={{ marginRight: "10px", transform: "scale(1.2)" }}
              disabled={loading}
            />
            <label htmlFor="terms-checkbox" style={{ fontWeight: "bold", cursor: "pointer" }}>
              {termsData.checkboxLabel}
            </label>
          </div>

          <div style={{ display: "flex", justifyContent: "center", gap: "10px" }}>
            <Button
              onClick={handleAccept}
              disabled={!accepted || loading}
              kind="primary"
              size="medium"
              style={{ 
                minWidth: "120px",
                opacity: (!accepted || loading) ? 0.6 : 1
              }}
            >
              {loading ? <Spinner size="sm" /> : "Aceitar e Continuar"}
            </Button>
          </div>
        </div>
      </div>
    </div>,
    document.body
  );
};

export default TermsOfUse;