import { Button } from "bold-ui";
import { useNavigate } from "react-router-dom";

const content = {
  buttonBackToCity: "Visualizar dados do painel do Município",
};

export type PainelParams = {
  id: string;
};

export const ReportFooter = () => {
  const navigate = useNavigate();

  const handleToPainelMunicipio = () => {
    navigate("/painelx");
  };

  return (
    <div className="d-flex flex-column align-items-center mt-5 gap-3">
      <Button onClick={handleToPainelMunicipio}>
        {content.buttonBackToCity}
      </Button>
    </div>
  );
};
