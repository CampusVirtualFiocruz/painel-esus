import { useParams } from "react-router";
import { Button } from "bold-ui";
import { useNavigate } from "react-router-dom";

const content = {
  buttonBackToUBS: "Voltar para o Painel da UBS",
  buttonBackToCity: "Visualizar dados do painel do Município",
};

export type PainelParams = {
  id: string;
};

export const ReportFooter = () => {
  const navigate = useNavigate();
  const { id } = useParams<PainelParams>();

  const handleToPainelUbs = () => {
    navigate(`/painel/${id}`);
  };

  const handleToPainelMunicipio = () => {
    navigate("/painelx");
  };

  return (
    <div className="d-flex flex-column align-items-center mt-5 gap-3">
      {id && (
        <Button onClick={handleToPainelUbs}>{content.buttonBackToUBS}</Button>
      )}
      <Button onClick={handleToPainelMunicipio}>
        {content.buttonBackToCity}
      </Button>
    </div>
  );
};
