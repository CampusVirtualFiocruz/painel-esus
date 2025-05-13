import { Api } from "../../services/api";
import { Icon } from "bold-ui";
import { capitalizeName } from "../../utils/stringUtils";

export const footerNotes = {
  Diabetes: `O número total de pessoas com Diabetes incluídas na Lista Nominal equivale ao conjunto de indivíduos que tiveram atendimentos individuais com registro do código CID e/ou CIAP correspondente ao Diabetes na Ficha de Atendimento Individual, somado ao conjunto de pessoas com registro autorreferido de Diabetes na Ficha de Cadastro Individual.`,
  Hipertensão: `O número total de pessoas com Hipertensão incluídas na Lista Nominal equivale ao conjunto de indivíduos que tiveram atendimentos individuais com registro do código CID e/ou CIAP correspondente à Hipertensão na Ficha de Atendimento Individual, somado ao conjunto de pessoas com registro autorreferido de Hipertensão na Ficha de Cadastro Individual.`,
} as any;

export const columns = ({ handleClick, condicao }: any) => {
  const baseColumns = [
    {
      name: "name",
      header: "Nome",
      sortable: true,
      render: (item: any) => (
        <span
          onClick={() => handleClick(item)}
          style={{ marginLeft: "16px", cursor: "pointer" }}
        >
          {capitalizeName(
            item?.nomeSocialSelecionado && item?.nomeSocialSelecionado !== "-"
              ? `${item?.nomeSocialSelecionado} *`
              : item?.nome
          )}
        </span>
      ),
    },
    {
      name: "alert",
      header: <div className="iconHeader iconAlerta ms-2"></div>,
      sortable: false,
      render: (item: any) => {
        if (item.possuiAlertas) {
          return (
            <span className="iconCircle iconAlerta ms-2" title="Alertas">
              !
            </span>
          );
        }
      },
    },
    {
      name: "cpf",
      header: "CPF",
      sortable: true,
      render: (item: any) => <b>{item?.cpf || "-"}</b>,
    },
    {
      name: "cns",
      header: "CNS",
      sortable: true,
      render: (item: any) => item?.cns || "-",
    },
    {
      name: "idade",
      header: "Idade",
      sortable: true,
      render: (item: any) => <center>{item?.idade || "-"}</center>,
    },
    {
      name: "sexo",
      header: "Sexo",
      sortable: true,
      render: (item: any) => (
        <center>{item.sexo === "MASCULINO" ? "M" : "F"}</center>
      ),
    },
    {
      name: "raca",
      header: "Raça",
      sortable: false,
      render: (item: any) => <span>{item?.racaCor || "-"}</span>,
    },
    {
      name: "equipe",
      header: "Equipe",
      sortable: true,
      render: (item: any) => (
        <span title={item.equipe}>
          {capitalizeName(String(item.equipe)?.toUpperCase().slice(0, 30))}
          {String(item.equipe).length > 30 ? "..." : ""}
        </span>
      ),
    },
    {
      name: "micro_area",
      header: "Microárea",
      sortable: true,
      render: (item: any) => <center>{item.microarea}</center>,
    },
  ];

  if (condicao && !["Idosa", "Infantil", "Qualidade"].includes(condicao)) {
    baseColumns.splice(5, 0, {
      name: "grupo_ condicao",
      header: "Grupo/Condição",
      sortable: true,
      render: (item: any) => (item?.diagnostico || "-").toUpperCase(),
    });
  }

  if (condicao === "Bucal") {
    baseColumns.push({
      name: "identidadeGenero",
      header: "Identidade de Gênero",
      sortable: false,
      render: (item: any) => <span>{item?.identidadeGenero || "-"}</span>,
    });
    baseColumns.push({
      name: "necessidadesEspeciais",
      header: "Necessidades Especiais",
      sortable: false,
      render: (item: any) => <span>{item?.necessidadesEspeciais || "-"}</span>,
    });
    baseColumns.push({
      name: "povosComunidades",
      header: "Povos de Comunidades",
      sortable: false,
      render: (item: any) => <span>{item?.povosComunidades || "-"}</span>,
    });
  }

  return baseColumns;
};

export const Footer = ({ pathToReport, condicao, id }: any) => {
  return (
    <div className="legend">
      <div>
        <p>* Nome Social</p>
      </div>
      <div className="legend-icons">
        <p>
          <span className="iconCircle iconAlerta ms-2">!</span>
          Alertas
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
            a.download = "lista_nominal.xlsx";
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
