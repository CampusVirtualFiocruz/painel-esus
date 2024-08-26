import * as React from "react";
import { useQuery } from "react-query";
import { Header } from "../../components/Header";
import { Alert, Spinner } from "reactstrap";
import {
  AiFillExclamationCircle,
  AiFillCheckCircle,
  AiFillCloseCircle,
} from "react-icons/ai";

import { Footer } from "../../components/Footer";
import Pagination from "../../components/Pagination";
import { Api } from "../../services/api";
import "../../styles/gestanteList.scss";
import "../../styles/hipertensosList.scss";
import { Button, DataTable, Icon, Table } from "bold-ui";

import listMock from "./HipertensosList.mock.json";
import { capitalize } from "../../utils";

const HipertensosList = () => {
  const [currentPage, setCurrentPage] = React.useState<any>(1);
  const [totalPages, setTotalPages] = React.useState<any>(1);
  const [response, setResponse] = React.useState<any>(null);

  const error = false;
  const isLoading = false;
  const list: any = listMock;

  const [sort, setSort] = React.useState(["id"]);

  const rows = list.sort((a: any, b: any) => {
    if (sort[0] === "nome") {
      return a?.nome - b?.nome;
    }
    if (sort[0] === "-nome") {
      return b?.nome - a?.nome;
    }
    return 0;
  });

  return (
    <div id="page-painel">
      <Header />

      <div className="contentWrapper">
        <hr className="linha my-4" />

        <h2>Lista de Hipertensos</h2>
        <div className="container my-5">
          <>
            <div className="table-responsive-md">
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
                      <u>
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
                  /*  {
                    name: "actions",
                    align: "right",
                    render: (item) => (
                      <Button size="small" skin="ghost">
                        <Icon icon="penOutline" />
                      </Button>
                    ),
                  }, */
                ]}
              />
            </div>
            <Pagination
              className="pagination-bar"
              currentPage={currentPage}
              totalCount={totalPages}
              pageSize={10}
              onPageChange={(page) => {
                setCurrentPage(page);
              }}
            />
          </>
        </div>
      </div>
    </div>
  );
};

export default HipertensosList;
