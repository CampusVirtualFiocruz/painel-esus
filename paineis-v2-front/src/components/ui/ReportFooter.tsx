import { Button, Link } from "bold-ui";
import { useNavigate, useParams } from "react-router-dom";
import { FaUser } from "react-icons/fa";
import { isUserFromUBS, userCanSelectUBS } from "../../App";

const content = {
  buttonViewList: "Ver lista nominal",
  buttonBackToCity: "Visualizar dados do Município",
  buttonBackToUbs: "Voltar página dados da UBS",
};

export type PainelParams = {
  id: string;
};

export const ReportFooter = ({
  chaveListaNominal,
}: {
  chaveListaNominal?: "Hipertensão" | "Diabetes";
}) => {
  const { id } = useParams<PainelParams>();
  const navigate = useNavigate();

  const handleToViewList = () =>
    navigate(`/lista-nominal/${id}?condicao=${chaveListaNominal}`);

  const handleToPainelMunicipio = () => navigate("/painelx");

  const handleToPainelUBS = () => navigate(-1);

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        gap: "20px",
        marginTop: "30px",
        marginBottom: "120px",
      }}
    >
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          justifyContent: "center",
          gap: "20px",
        }}
      >
        {chaveListaNominal && id && (
          <Button
            style={{
              backgroundColor: "#343131",
              color: "white",
              width: "250px",
            }}
            onClick={handleToViewList}
          >
            <FaUser style={{ marginRight: "10px" }} />
            {content.buttonViewList}
          </Button>
        )}
        <Button
          kind="primary"
          onClick={handleToPainelUBS}
          style={{
            width: "250px",
          }}
        >
          {content.buttonBackToUbs}
        </Button>
      </div>

      {userCanSelectUBS() && (
        <Link onClick={handleToPainelMunicipio} style={{ color: "#343131" }}>
          {content.buttonBackToCity}
        </Link>
      )}
    </div>
  );
};
