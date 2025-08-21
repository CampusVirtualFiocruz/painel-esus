import { Icon } from "bold-ui";
import { Api } from "../../services/api";
import { capitalizeName } from "../../utils/stringUtils";

export const footerNotes = {
  Diabetes: `O número total de pessoas com Diabetes incluídas na Lista Nominal equivale ao conjunto de indivíduos que tiveram atendimentos individuais com registro do código CID e/ou CIAP correspondente ao Diabetes na Ficha de Atendimento Individual, somado ao conjunto de pessoas com registro autorreferido de Diabetes na Ficha de Cadastro Individual.`,
  Hipertensão: `O número total de pessoas com Hipertensão incluídas na Lista Nominal equivale ao conjunto de indivíduos que tiveram atendimentos individuais com registro do código CID e/ou CIAP correspondente à Hipertensão na Ficha de Atendimento Individual, somado ao conjunto de pessoas com registro autorreferido de Hipertensão na Ficha de Cadastro Individual.`,
} as any;

const renderString = (s: string) => (s === "Sem Informação" ? "-" : s || "-");

export const columns = ({ handleClick, condicao }: any) => {
  const baseColumns = [
    {
      name: "name",
      header: "Nome",
      sortable: true,
      render: (item: any) => (
        <div
          onClick={() => handleClick(item)}
          style={{
            padding: "4px 16px",
            cursor: "pointer",
            textDecoration: "underline",
          }}
        >
          {capitalizeName(
            item?.nomeSocialSelecionado &&
              item?.nomeSocialSelecionado !== "-" &&
              item?.nomeSocialSelecionado.length > 2
              ? `${item?.nomeSocialSelecionado} *`
              : item?.nome
          )}
        </div>
      ),
    },
    {
      name: "alert",
      header: <div className="iconHeader iconAlerta ms-2"></div>,
      sortable: true,
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
      render: (item: any) => (
        <b style={{ padding: "4px 8px" }}>{renderString(item?.cpf)}</b>
      ),
    },
    {
      name: "cns",
      header: "CNS",
      sortable: true,
      render: (item: any) => renderString(item?.cns),
    },
    {
      name: "idade",
      header: "Idade",
      sortable: true,
      render: (item: any) => (
        <center style={{ padding: "4px" }}>{renderString(item?.idade)}</center>
      ),
    },
    {
      name: "sexo",
      header: "Sexo",
      sortable: true,
      render: (item: any) => (
        <center style={{ padding: "4px" }}>
          {item.sexo === "MASCULINO" ? "M" : "F"}
        </center>
      ),
    },
    {
      name: "raca",
      header: "Raça",
      sortable: false,
      render: (item: any) => (
        <span style={{ padding: "4px" }}>{renderString(item?.racaCor)}</span>
      ),
    },
    {
      name: "equipe",
      header: "Equipe",
      sortable: true,
      render: (item: any) => (
        <span title={item.equipe} style={{ padding: "4px" }}>
          {capitalizeName(String(item.equipe)?.toUpperCase().slice(0, 30))}
          {String(item.equipe).length > 30 ? "..." : ""}
        </span>
      ),
    },
    {
      name: "micro_area",
      header: "Microárea",
      sortable: true,
      render: (item: any) => (
        <center style={{ padding: "4px" }}>{item.microarea}</center>
      ),
    },
  ];

  // Adiciona coluna "gestante" na segunda posição se não for infantil nem idosa
  if (condicao !== "Infantil" && condicao !== "Idosa") {
    baseColumns.splice(1, 0, {
      name: "gestante",
      header: <div className="iconHeader iconGestante ms-2"></div>,
      sortable: true,
      render: (item: any) => {
        if (String(item.gestante).toUpperCase() === "SIM") {
          return (
            <span className="iconCircle iconGestante ms-2" title="Alertas">
              G
            </span>
          );
        }
      },
    });
  }

  if (
    condicao &&
    !["Idosa", "Infantil", "Qualidade", "Bucal"].includes(condicao)
  ) {
    const targetIndex = condicao !== "Infantil" && condicao !== "Idosa" ? 6 : 5;
    baseColumns.splice(targetIndex, 0, {
      name: "grupo_ condicao",
      header: "Grupo/Condição",
      sortable: true,
      render: (item: any) => renderString(item?.diagnostico).toUpperCase(),
    });
  }

  if (condicao === "Bucal") {
    baseColumns.push({
      name: "identidadeGenero",
      header: "Identidade de Gênero",
      sortable: true,
      render: (item: any) => (
        <span>{renderString(item?.identidadeGenero)}</span>
      ),
    });
    baseColumns.push({
      name: "necessidadesEspeciais",
      header: "Necessidades Especiais",
      sortable: true,
      render: (item: any) => (
        <span>{renderString(item?.necessidadesEspeciais)}</span>
      ),
    });
    baseColumns.push({
      name: "povosComunidades",
      header: "Povos de Comunidades",
      sortable: true,
      render: (item: any) => (
        <span>{renderString(item?.povosComunidades)}</span>
      ),
    });
  }

  return baseColumns;
};

export const Footer = ({ pathToReport, condicao, id, recorte }: any) => {
  let recorteQuery = '';
  if (recorte !== undefined || recorte !== null) {
    recorteQuery=`?recorte=${recorte}`;
  }
  return (
    <div className="legend">
      <div>
        <p>* Nome Social</p>
      </div>
      <div className="legend-icons">
        {condicao !== "Infantil" && condicao !== 'Idosa' && (
          <p>
            <span className="iconCircle iconGestante" title="Alertas">
              G
            </span>
            Gestantes/Idade Gestacional
          </p>
        )}
        <p>
          <span className="iconCircle iconAlerta ms-2">!</span>
          Pendências/Alertas
        </p>
        <p
          onClick={async () => {
            let path = `${pathToReport?.[condicao]}/get-nominal-list/download/${id}${recorteQuery}`;
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
