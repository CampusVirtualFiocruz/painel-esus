import { useRef } from "react";
import ReactDom from "react-dom";
import { CgClose } from "react-icons/cg";

import "./style.scss";

interface IModal {
  data: {
    loaded: number;
    cnes?: string | undefined;
  };
  setShowModal: (status: boolean) => void;
}

export function bodyPrimeiroTrimestre() {
  return (
    <div className="d-flex flex-column">
      <h1 className="mb-4">Orientações para o 1º trimestre:</h1>
      <p className="mb-1">
        As consultas devem ser realizadas conforme este cronograma:
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
      <p>Agendar consulta de retorno 42 dias após o parto</p>
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

export const Modal = ({ data, setShowModal }: IModal) => {
  // close the modal when clicking outside the modal.
  const modalRef = useRef<HTMLDivElement | null>(null);

  const closeModal = (e: any) => {
    if (e.target === modalRef.current) {
      setShowModal(false);
    }
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
