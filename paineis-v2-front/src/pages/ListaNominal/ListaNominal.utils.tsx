import { Api } from "../../services/api";
import { capitalize } from "../../utils";
import { Icon } from "bold-ui";

export const columns = ({ handleClick }: any) => [
  {
    name: "nome",
    header: "Nome",
    sortable: true,
    render: (item: any) => (
      <span
        onClick={() => handleClick(item)}
        style={{ marginLeft: "16px", cursor: "pointer" }}
      >
        {item?.nomeSocialSelecionado && item?.nomeSocialSelecionado !== "-"
          ? `${item?.nomeSocialSelecionado} *`
          : item?.nome}
      </span>
    ),
  },
  {
    name: "alert",
    header: <div className="iconHeader iconAlerta ms-2"></div>,
    sortable: true,
    render: (item: any) => {
      if (item.possuiAlertas) {
        return (
          <span className="iconCircle iconAlerta ms-2" title="Possui Alertas">
            !
          </span>
        );
      }
    },
  },
  {
    name: "zone",
    header: (
      <div className="headerZone ms-2">
        <div className="iconHeader iconRural"></div>
        <div className="iconHeader iconUrbano"></div>
      </div>
    ),
    sortable: true,
    render: (item: any) => {
      if (item.zonaUrbana) {
        return (
          <span className="iconCircle iconUrbano ms-2" title="Zona Urbana">
            U
          </span>
        );
      } else if (item.zonaRural) {
        return (
          <span className="iconCircle iconRural ms-2" title="Zona Rural">
            R
          </span>
        );
      }
    },
  },
  {
    name: "cpf",
    header: "CPF",
    render: (item: any) => <b>{item.cpf}</b>,
  },
  {
    name: "cns",
    header: "CNS",
    render: (item: any) => item.cns,
  },
  {
    name: "idade",
    header: "Idade",
    render: (item: any) => item.idade,
  },
  {
    name: "diagnostico",
    header: "Diagnóstico",
    render: (item: any) => capitalize(item.diagnostico),
  },
  {
    name: "sexo",
    header: "Sexo",
    render: (item: any) => (item.sexo === "MASCULINO" ? "M" : "F"),
  },
  {
    name: "equipe",
    header: "Equipe",
    render: (item: any) => (
      <p style={{ fontSize: "13px", transform: "translateY(8px)" }}>
        {String(item.equipe)?.toUpperCase()}
      </p>
    ),
  },
  {
    name: "microarea",
    header: "Microárea",
    render: (item: any) => item.microarea,
  },
];

export const Footer = ({ pathToReport, condicao, id }: any) => {
  return (
    <div className="legend">
      <div>
        <p>* Nome Social</p>
      </div>
      <div className="legend-icons">
        <p>
          <span className="iconCircle iconUrbano ms-2">U</span>
          Zona Urbana
        </p>
        <p>
          <span className="iconCircle iconRural ms-2">R</span>
          Zona Rural
        </p>
        <p>
          <span className="iconCircle iconAlerta ms-2">!</span>
          Possui Alertas
        </p>
        <p
          onClick={async () => {
            let path = `${pathToReport?.[condicao]}/get-nominal-list/download/${id}`;
            const response: any = await Api.get(path, {
              headers: {
                "Content-Type":
                  "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
              },
              responseType: "blob",
            });

            const downloadUrl = URL.createObjectURL(response?.data);

            const a = document.createElement("a");
            a.href = downloadUrl;
            a.download = "lista_nominal.xlsx"; // Nome do arquivo a ser baixado
            document.body.appendChild(a);
            a.click();
            a.remove();
          }}
          style={{ cursor: "pointer", color: "#0069d0", paddingLeft: "0" }}
        >
          <span
            style={{
              paddingLeft: "15px",
              marginRight: "0px",
              marginTop: "-3px",
            }}
          >
            <Icon icon="download" style={{ color: "#0069d0" }} />
          </span>
          Exportar lista
        </p>
      </div>
    </div>
  );
};
