import * as React from "react";
import { useState } from "react";
import { useParams, useLocation } from "react-router-dom";
import { useQuery } from "react-query";
import { Alert, Spinner } from "reactstrap";
import {
  AiFillExclamationCircle,
  AiFillCheckCircle,
  AiFillCloseCircle,
} from "react-icons/ai";
import { DataTable, } from "bold-ui";

import { Modal } from "../../components/Modal";
import Pagination from "../../components/Pagination";
import { ReportFooter } from "../../components/ui/ReportFooter";
import ReportWrapper from "../../components/ui/ReportWrapper";
import { useInfo } from "../../context/infoProvider/useInfo";
import { capitalize, getNomeUbs } from "../../utils";
import { wait } from "../../utils/reports";
import { Api } from "../../services/api";

import listMock from "./HipertensosList.mock.json";

import "../../styles/gestanteList.scss";
import "../../styles/ListaNominal.scss";

type TModal = {
  loaded: number;
  tipo?: string;
  cnes?: string | undefined;
};

type PainelParams = {
  id: string;
};

const ListaNominal = () => {
  const { id } = useParams<PainelParams>();
  const [showModal, setShowModal] = useState(false);
  const [data, setData] = useState<TModal>({ loaded: 0 });

  const getData = async (idModal: number, tipo?: string) => {
    await wait(100);
    setData({ loaded: idModal, tipo, cnes: id });
  };

  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  const condicao = queryParams.get('condicao');

  const handleClick = (idModal: number) => {
    setData({ loaded: 0 });
    setShowModal(true);
    getData(idModal);
  };

  const { city } = useInfo();

  const { data: dataUbs, isLoading: isLoadingUbs } = useQuery(
    "ubs",
    async () => {
      const response = await Api.get<any>("get-units");
      const data = response.data;

      const listData: any[] = data.data.map((ubs: any) => {
        return {
          label: ubs.no_unidade_saude,
          value: ubs.co_seq_dim_unidade_saude,
          id: ubs.co_seq_dim_unidade_saude,
        };
      });

      return listData;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const nomeUbs = !isLoadingUbs && id ? getNomeUbs(dataUbs, id) : city;
  const UBS = id ? (!isLoadingUbs ? nomeUbs : "Carregando...") : nomeUbs;
  const title = `${UBS} / Lista Nominal / ${condicao}`;
  const subtitle = "(referente aos últimos 12 meses)";

  const [currentPage, setCurrentPage] = React.useState<any>(1);
  const [totalPages, setTotalPages] = React.useState<any>(1);
  const [response, setResponse] = React.useState<any>(null);

  const error = false;
  const isLoading = false;
  const list: any = listMock;

  const [sort, setSort] = React.useState(["id"]);

  const rows = list.sort((a: any, b: any) => {
    if (sort[0] === "nome") {
      return a?.nome.localeCompare(b?.nome);
    }
    if (sort[0] === "-nome") {
      return b?.nome.localeCompare(a?.nome);
    }
    return 0;
  });

  return (
    <div id="page-painel">
      {showModal && <Modal data={data} setShowModal={setShowModal} />}
      <ReportWrapper title={title} subtitle={subtitle}>
      <DataTable<any>
                rows={rows}
                sort={sort}
                onSortChange={setSort}
                loading={false}
                columns={[
                  {
                    name: "nome",
                    header: "Nome",
                    sortable: true,
                    render: (item) => (
                      <u onClick={() => handleClick(6)} style={{ cursor: 'pointer' }}>
                        {`${item.nome} ${
                          item?.nomeSocialSelecionado ? "*" : ""
                        }`}
                      </u>
                    ),
                  },
                  {
                    name: "cpf",
                    header: "CPF",
                    render: (item) => item.cpf,
                  },
                  {
                    name: "cns",
                    header: "CNS",
                    render: (item) => item.cns,
                  },
                  {
                    name: "idade",
                    header: "Idade",
                    render: (item) => item.idade,
                  },
                  {
                    name: "diagnostico",
                    header: "Diagnóstico",
                    render: (item) => capitalize(item.diagnostico),
                  },
                  {
                    name: "sexo",
                    header: "Sexo",
                    render: (item) => capitalize(item.sexo),
                  },
                  {
                    name: "equipe",
                    header: "Equipe",
                    render: (item) => String(item.equipe)?.toUpperCase(),
                  },
                  {
                    name: "microarea",
                    header: "Microarea",
                    render: (item) => item.microarea,
                  },
                ]}
              />
              <Pagination
              className="pagination-bar"
              currentPage={currentPage}
              totalCount={totalPages}
              pageSize={10}
              onPageChange={(page) => {
                setCurrentPage(page);
              }}
            />
      <ReportFooter />
      </ReportWrapper>
    </div>
  );
};

export default ListaNominal;
