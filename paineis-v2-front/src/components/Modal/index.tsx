import { useRef, useState, useEffect } from "react";
import ReactDom from "react-dom";
import { CgClose } from "react-icons/cg";

import { VFlow, Radio } from "bold-ui";

import "./style.scss";
import "../../styles/listaNominal.scss";
import { capitalize, profiles } from "../../utils";
import { capitalizeName } from "../../utils/stringUtils";

interface IModal {
  data: {
    loaded: number;
    cnes?: string | undefined;
  };
  setShowModal: (status: boolean) => void;
  setProfile?: (profile: string) => void;
  initialProfile?: string;
}

function parseText(text: string): number | string {
  // Verifica se o texto pode ser convertido em número
  const parsedNumber = Number(text);
  if (!isNaN(parsedNumber)) {
    return parsedNumber;
  }

  // Verifica se o texto é uma data válida
  const parsedDate = new Date(new Date(text));
  if (!isNaN(parsedDate.getTime())) {
    // Retorna a data formatada para o padrão localizado
    return parsedDate.toLocaleDateString("pt-BR");
  }
  if (text == "-") return text;
  throw new Error("O texto não é nem um número nem uma data válida.");
}

export function bodyPrimeiroTrimestre() {
  return (
    <div className="d-flex flex-column">
      <h1 className="mb-4">Orientações para o 1º trimestre:</h1>
      <p className="mb-1">
        As consultas médicas ou de enfermagem devem ser realizadas conforme este
        cronograma:
      </p>
      <ul className="ms-4">
        <li className="mb-1">- até a 28ª semana - mensalmente;</li>
        <li className="mb-1">- da 28ª até a 36ª semana - quinzenalmente;</li>
        <li className="mb-1">- da 36ª até a 41ª semana - semanalmente.</li>
      </ul>
      <p className="my-4">
        Avaliar prescrição de ácido fólico e sulfato ferroso.
      </p>
    </div>
  );
}
export function bodySegundoTrimestre() {
  return (
    <div className="d-flex flex-column">
      <h1 className="mb-4">Orientações para o 2º trimestre:</h1>
      <p className="mb-4">Reforçar os cuidados odontológicos de higiene:</p>
      <p>
        caso necessário, o segundo trimestre é o período mais adequado para a
        realização de intervenções clínicas e procedimentos odontológicos
        essencias, sempre de acordo com as indicações.
      </p>
    </div>
  );
}
export function bodyTerceiroTrimestre() {
  return (
    <div className="d-flex flex-column">
      <h1 className="mb-4">Orientações para o 3º trimestre:</h1>
      <p className="mb-1">Avaliar sinais de:</p>
      <ul className="ms-4">
        <li className="mb-1">- Trabalho de parto prematuro</li>
        <li className="mb-1">- Pré-eclâmpsia e eclampsia</li>
        <li className="mb-1">- Aminiorrexe prematura</li>
        <li className="mb-1">- Risco de óbito fetal</li>
      </ul>

      <p className="my-4">
        Encaminhar gestante para avaliação de bem-estar fetal após 41 semanas de
        gestação
      </p>
      <p>
        Agendar consulta médica ou de enfermagem de retorno 42 dias após o parto
      </p>
    </div>
  );
}
export function bodyBoasPraticasAssistenciaPreNatal() {
  return (
    <div className="d-flex flex-column mb-4">
      <h1 className="mb-4">Boas práticas na assistência do Pré-Natal:</h1>
      <ul className="ms-4">
        <li className="mb-1">- Encaminhar a grupos educativos</li>
        <li className="mb-1">- Sempre pesquisar por queixas</li>
        <li className="mb-1">
          - Realizar exame físico (edema, altura uterina, PA, mamas)
        </li>
        <li className="mb-1">- Avaliar resultado de exames complementares</li>
        <li className="mb-1">
          - Atualizar o Cartão de Gestante e a Ficha Pré-Natal
        </li>
        <li className="mb-1">- Registrar as informações</li>
        <li className="mb-1">- Acompanhar ganho de peso gestacional</li>
        <li className="mb-1">
          - Avaliar batimentos cardiofetais e movimentações do bebê
        </li>
        <li className="mb-1">- Incentivar aleitamento materno</li>
      </ul>
    </div>
  );
}

export function bodyBoasPraticasAssistenciaPessoaDiabetes() {
  return (
    <div className="d-flex flex-column mb-4">
      <h1 className="mb-4">Boas práticas no cuidado da pessoa com diabetes:</h1>
      <ul className="ms-4">
        <li className="mb-1">
          - Orientar sobre efeitos deletérios do tabagismo
        </li>
        <li className="mb-1">- Monitorar a pressão arterial</li>
        <li className="mb-1">
          - Orientar quanto ao uso de medicações, quando houver
        </li>
        <li className="mb-1">
          - Orientar quanto ao exame e cuidados com o pé diabético
        </li>
        <li className="mb-1">- Realizar o controle glicêmico</li>
        <li className="mb-1">
          - Realizar avaliação antropométrica (IMC e Circunferência abdominal)
        </li>
        <li className="mb-1">
          - Realizar orientação nutricional (individual ou em grupo)
        </li>
        <li className="mb-1">- Acompanhamento multiprofissional</li>
        <li className="mb-1">- Incentivar prática de atividade física</li>
      </ul>
    </div>
  );
}

export function bodyBoasPraticasCuidadoPessoasHipertensao() {
  return (
    <div className="d-flex flex-column mb-4">
      <h1 className="mb-4">
        Boas práticas no cuidado da pessoa com hipertensão:
      </h1>
      <ul className="ms-4">
        <li className="mb-1">
          - Realizar avaliação antropométrica (IMC e Circunferência abdominal)
        </li>
        <li className="mb-1">
          - Realizar orientação nutricional (individual ou em grupo)
        </li>
        <li className="mb-1">- Acompanhamento multiprofissional</li>
        <li className="mb-1">- Incentivar prática de atividade física</li>
        <li className="mb-1">
          - Orientar sobre efeitos deletérios do tabagismo
        </li>
        <li className="mb-1">
          - Orientar quanto ao uso de medicações, quando houver
        </li>
      </ul>
    </div>
  );
}

export function bodyDetalhesCadastro(item: any) {
  return (
    <div className="d-flex flex-column mb-4">
      <div className="user-details">
        {/* {JSON.stringify(item)} */}
        <h1>
          {capitalizeName(
            item?.nomeSocialSelecionado && item?.nomeSocialSelecionado !== "-"
              ? item?.nomeSocialSelecionado
              : item?.nome
          )}
        </h1>
        <div className="address">
          <p>
            <strong>CPF:</strong> {item?.cpf} <br />
            <strong>CNS:</strong> {item?.cns} <br />
            {item?.tipoLogradouro && (
              <>
                <strong>Tipo Logradouro:</strong>
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
        {Array.isArray(item?.detalhesCondicaoSaude) &&
          item?.detalhesCondicaoSaude.map((condicao: any) => (
            <>
              <div className="health-condition">
                {condicao?.cidCondicaoSaude && <><p>
                  Condição de saúde: CID {condicao?.cidCondicaoSaude.join(", ")}
                </p></>}
                {condicao?.primeiroDiagnostico && <><p>
                  Data do primeiro registro da condição:{" "}
                  {parseText(condicao?.primeiroDiagnostico)}
                </p></>}
              </div>
              {Array.isArray(condicao?.registros) &&
                condicao?.registros.map((registro: any) => (
                  <div className="latest-checkups">
                    <p>
                      {registro?.descricao !==
                        "data-da-ultima-glicemia-capilar" && (
                        <>
                          <strong>
                            {registro?.descricao
                              .split("-")
                              .map((s: string) => capitalize(s))
                              .join(" ")
                              .replace("S/n", "S/N")
                              .replace("Ultimo", "Último")
                              .replace("Ultima", "Última")
                              .replace("Afericao", "Aferição")
                              .replace("Acs", "ACS")
                              .replace("Pa", "PA")
                              .replace("Medico", "Médico")
                              .replace("Medica", "Médica")
                              .replace("Medicas", "Médicas")
                              .replace("Odontologica", "Odontológica")
                              .replace(/De /g, "de ")
                              .replace(/Da /g, "da ")
                              .replace(/Do /g, "do ")
                              .replace(/Ou /g, "ou ")}
                          </strong>
                          <div>
                            <p>
                              {registro?.data === null ||
                              registro?.data === 0 ||
                              registro?.data === "0"
                                ? "-"
                                : parseText(registro?.data)}
                            </p>
                            {registro?.exibirAlerta && (
                              <span
                                className="iconCircle iconAlerta ms-2"
                                title="Alertas"
                              >
                                !
                              </span>
                            )}
                          </div>
                        </>
                      )}
                    </p>
                  </div>
                ))}
            </>
          ))}
      </div>
    </div>
  );
}

export function bodyPerfil(
  selectedValue: string,
  onChange: (value: string) => void
) {
  return (
    <div className="d-flex flex-column mb-4">
      <h1 className="mb-4">Em qual perfil você deseja logar:</h1>
      <VFlow>
        <Radio
          name="default"
          label={profiles[0]}
          value={profiles[0]}
          checked={selectedValue === profiles[0]}
          onChange={() => onChange(profiles[0])}
        />
        <Radio
          name="default"
          label={profiles[1]}
          value={profiles[1]}
          checked={selectedValue === profiles[1]}
          onChange={() => onChange(profiles[1])}
        />
      </VFlow>
    </div>
  );
}

export const Modal = ({
  data,
  setShowModal,
  setProfile,
  initialProfile,
}: IModal) => {
  // close the modal when clicking outside the modal.
  const modalRef = useRef<HTMLDivElement | null>(null);

  const closeModal = (e: any) => {
    if (e.target === modalRef.current) {
      setShowModal(false);
    }
  };

  // Profile state selection.
  const [selectedValue, setSelectedValue] = useState<string>(
    initialProfile || ""
  );

  useEffect(() => {
    setSelectedValue(initialProfile || "");
  }, [initialProfile]);

  const handleProfileChange = (value: string) => {
    setSelectedValue(value);
    if (setProfile) setProfile(value);
  };

  // render the modal JSX in the portal div.
  return ReactDom.createPortal(
    <div className="container-modal" ref={modalRef} onClick={closeModal}>
      <div className="modal d-flex flex-column align-items-start justify-content-start px-5 py-2">
        <hr className="separador mb-3" />

        {data && data.loaded === 1 && bodyPrimeiroTrimestre()}
        {data && data.loaded === 2 && bodySegundoTrimestre()}
        {data && data.loaded === 3 && bodyTerceiroTrimestre()}
        {data && data.loaded === 4 && bodyBoasPraticasAssistenciaPreNatal()}
        {data &&
          data.loaded === 5 &&
          bodyBoasPraticasAssistenciaPessoaDiabetes()}
        {data &&
          data.loaded === 6 &&
          bodyBoasPraticasCuidadoPessoasHipertensao()}
        {data && data.loaded === 7 && bodyDetalhesCadastro(data)}
        {data &&
          data.loaded === 8 &&
          bodyPerfil(selectedValue, handleProfileChange)}

        <CgClose
          size={"1.5rem"}
          onClick={() => setShowModal(false)}
          className="closeButton"
        />
      </div>
    </div>,
    document.getElementById("modal")!
  );
};
