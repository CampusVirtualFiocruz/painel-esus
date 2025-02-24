import { Api } from "../../services/api";
import { Icon } from "bold-ui";
import { capitalizeName } from "../../utils/stringUtils";

export const footerNotes = {
  Diabetes: `
O número total de pessoas com Diabetes atendidas nos últimos 12 meses incluídas na Lista Nominal
equivale ao conjunto de indivíduos que tiveram atendimentos individuais realizados nos últimos
12 meses com registro do código CID e/ou CIAP correspondente ao Diabetes em Ficha de
Atendimento Individual, somado ao conjunto de pessoas com registro autorreferido de Diabetes em
Ficha de Cadastro Individual que também tiveram atendimentos individuais realizados nos últimos 12 meses.
Todas essas pessoas serão contabilizadas em todas as Listas nominais de cada uma das UBS e Equipes em que
tiver ocorrido contato assistencial registrado em Ficha de Atendimento Individual, Ficha de Atendimento
Odontológico ou Ficha de Procedimentos.
  `,
  Hipertensão: `
O número total de pessoas com Hipertensão atendidas nos últimos 12 meses incluídas na Lista Nominal
equivale ao conjunto de indivíduos que tiveram atendimentos individuais realizados nos últimos 12 meses
com registro do código CID e/ou CIAP correspondente à Hipertensão em Ficha de Atendimento Individual,
somado ao conjunto de pessoas com registro autorreferido de Hipertensão em Ficha de Cadastro Individual
que também tiveram atendimentos individuais realizados nos últimos 12 meses. Todas essas pessoas serão
contabilizadas em todas as Listas nominais de cada uma das UBS e Equipes em que tiver ocorrido contato
assistencial registrado em Ficha de Atendimento Individual, Ficha de Atendimento Odontológico ou Ficha de Procedimentos.
`,
} as any;

export const columns = ({ handleClick, condicao }: any) => {
  const baseColumns = [
    {
      name: "nome",
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
    // {
    //   name: "zone",
    //   header: (
    //     <div className="headerZone ms-2">
    //       <div className="iconHeader iconRural"></div>
    //       <div className="iconHeader iconUrbano"></div>
    //     </div>
    //   ),
    //   sortable: true,
    //   render: (item: any) => {
    //     if (item.zonaUrbana) {
    //       return (
    //         <span className="iconCircle iconUrbano ms-2" title="Zona Urbana">
    //           U
    //         </span>
    //       );
    //     } else if (item.zonaRural) {
    //       return (
    //         <span className="iconCircle iconRural ms-2" title="Zona Rural">
    //           R
    //         </span>
    //       );
    //     }
    //   },
    // },
    {
      name: "cpf",
      header: "CPF",
      render: (item: any) => <b>{item?.cpf || "-"}</b>,
    },
    {
      name: "cns",
      header: "CNS",
      render: (item: any) => item?.cns || "-",
    },
    {
      name: "idade",
      header: "Idade",
      render: (item: any) => <center>{item?.idade || "-"}</center>,
    },
    // {
    //   name: "diagnostico",
    //   header: "Diagnóstico",
    //   render: (item: any) => <center>{capitalize(item.diagnostico)}</center>,
    // },
    // {
    //   name: "grupo-codicao",
    //   header: "Grupo/Condição",
    //   render: (item: any) => (item?.diagnostico || "-").toUpperCase(),
    // },
    {
      name: "sexo",
      header: "Sexo",
      render: (item: any) => (
        <center>{item.sexo === "MASCULINO" ? "M" : "F"}</center>
      ),
    },
    {
      name: "equipe",
      header: "Equipe",
      render: (item: any) => (
        <span title={item.equipe}>
          {capitalizeName(String(item.equipe)?.toUpperCase().slice(0, 30))}
          {String(item.equipe).length > 30 ? "..." : ""}
        </span>
      ),
    },
    {
      name: "microarea",
      header: "Microárea",
      render: (item: any) => <center>{item.microarea}</center>,
    },
  ];

  if (condicao && !["Idosa", "Infantil", "Qualidade"].includes(condicao)) {
    baseColumns.splice(5, 0, {
      name: "grupo-condicao",
      header: "Grupo/Condição",
      render: (item: any) => (item?.diagnostico || "-").toUpperCase(),
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
