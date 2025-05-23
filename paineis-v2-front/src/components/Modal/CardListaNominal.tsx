import moment from "moment";
import { capitalizeName } from "../../utils/stringUtils";
import { groupBy } from "../../utils";
import { Tooltip, TooltipContent, TooltipTrigger } from "../ui/Tooltip";

export function parseText(text: string | number): number | string {
  if (text === null || text === 0 || text === "" || text === "0") {
    return "-";
  }

  const parsedNumber = Number(text);
  if (!isNaN(parsedNumber)) {
    return parsedNumber;
  }

  const parsedDate = new Date(new Date(String(text)));
  if (!isNaN(parsedDate.getTime())) {
    return parsedDate.toLocaleDateString("pt-BR", { timeZone: "UTC" });
  }

  return text;
}

const defaultMessage = `
  Os sinais de alertas correspondem à não
  conformidade com as orientações de boas
  práticas, dentro de um período de 12 meses,
  preconizadas pelo Ministério da Saúde
`;

export const CardListaNominal = ({
  item,
  config,
}: {
  item: any;
  config?: { alertMessage?: string; alertBeforeDetails?: string };
}) => {
  return (
    <div className="d-flex flex-column mb-4">
      <div className="user-details">
        <div
          style={{
            display: "flex",
            justifyContent: "start",
            alignItems: "center",
            gap: "6px",
            marginBottom: "10px",
          }}
        >
          {String(item.gestante).toUpperCase() === "SIM" && <span className="iconCircle iconGestante" title="Alertas">
              G
            </span>
          }
          <h1 style={{ padding: "0px", margin: "0px" }}>
            {capitalizeName(
              item?.nomeSocialSelecionado && item?.nomeSocialSelecionado !== "-"
                ? item?.nomeSocialSelecionado
                : item?.nome
            )}
          </h1>
        </div>
        <div className="address">
          <p>
            <strong>CPF:</strong> {item?.cpf} <br />
            <strong>CNS:</strong> {item?.cns} <br />
            <strong>Data de nascimento:</strong>{" "}
            {item?.dataNascimento
              ? moment.utc(item.dataNascimento).format("DD/MM/YYYY")
              : "-"}
            <br />
            {item?.tipoLogradouro && (
              <>
                <strong>Tipo Logradouro: </strong>
                {item.tipoLogradouro}
                <br />
              </>
            )}
            <strong>Endereço:</strong>{" "}
            {item?.endereco && item.endereco !== "None None"
              ? capitalizeName(item.endereco).replace("S/n", "S/N")
              : "-"}{" "}
            <br />
            <strong>Complemento:</strong>{" "}
            {item?.complemento ? capitalizeName(item?.complemento) : "-"} <br />
            <strong>CEP:</strong> {item?.cep ? item?.cep : "-"} <br />
            <strong>Telefone de contato:</strong>{" "}
            {item?.telefone ? item?.telefone : "-"}{" "}
          </p>
        </div>
        {Boolean(config?.alertBeforeDetails) ? (
          <b style={{ lineHeight: "40px" }}>{config?.alertBeforeDetails}</b>
        ) : null}
        {Array.isArray(item?.detalhesCondicaoSaude) &&
          item?.detalhesCondicaoSaude.map((condicao: any) => {
            return (
              <>
                {Boolean(
                  condicao?.cidCondicaoSaude || condicao?.primeiroDiagnostico
                ) ? (
                  <div className="health-condition">
                    {condicao?.cidCondicaoSaude && (
                      <>
                        <p>
                          Condição de saúde:{" "}
                          {item.diagnostico == "autoreferido"
                            ? "AUTORREFERIDO "
                            : "CID "}
                          {condicao?.cidCondicaoSaude.join(", ")}
                        </p>
                      </>
                    )}
                    {condicao?.primeiroDiagnostico && (
                      <>
                        <p>
                          Data do primeiro registro da condição:{" "}
                          {parseText(condicao?.primeiroDiagnostico)}
                        </p>
                      </>
                    )}
                  </div>
                ) : (
                  <br />
                )}
                {groupBy(condicao?.registros, "classificacao").map(
                  ({ content: registerContent }: any) => {
                    return (
                      <div
                        style={{
                          marginLeft: "30px",
                          maxWidth: "500px",
                          cursor: "help",
                        }}
                      >
                        {registerContent.map((registro: any) => (
                          <>
                            <Tooltip>
                              <TooltipContent className="Tooltip">
                                <div>
                                  {config?.alertMessage ?? defaultMessage}
                                </div>
                              </TooltipContent>
                              <TooltipTrigger>
                                <div className="latest-checkups">
                                  <p style={{ position: "relative" }}>
                                    {registro?.descricao !==
                                      "data-da-ultima-glicemia-capilar" && (
                                      <>
                                        {Boolean(registro?.exibirAlerta) && (
                                          <span
                                            className="iconCircle iconAlerta ms-2"
                                            title="Alertas"
                                            style={{
                                              position: "absolute",
                                              left: "-35px",
                                            }}
                                          >
                                            !
                                          </span>
                                        )}
                                        <strong>{registro?.descricao}</strong>
                                        <span>
                                          {Array.isArray(registro?.data) ? (
                                            registro.data?.map(
                                              (registerItem: any) => (
                                                <div
                                                  style={{ display: "block" }}
                                                >
                                                  &nbsp;
                                                  {parseText(registerItem)}
                                                </div>
                                              )
                                            )
                                          ) : (
                                            <div>
                                              &nbsp;
                                              {parseText(registro?.data)}
                                            </div>
                                          )}
                                        </span>
                                      </>
                                    )}
                                  </p>
                                </div>
                              </TooltipTrigger>
                            </Tooltip>
                          </>
                        ))}
                      </div>
                    );
                  }
                )}
              </>
            );
          })}
      </div>
    </div>
  );
};
