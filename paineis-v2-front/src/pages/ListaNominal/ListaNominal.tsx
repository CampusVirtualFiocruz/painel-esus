import { useState } from "react";
import { useParams, useLocation } from "react-router-dom";
import { useQuery } from "react-query";
import { DataTable, PagedTable, TextField } from "bold-ui";

import { Modal } from "../../components/Modal";
import { ReportFooter } from "../../components/ui/ReportFooter";
import ReportWrapper from "../../components/ui/ReportWrapper";
import { useInfo } from "../../context/infoProvider/useInfo";
import { capitalize, getNomeUbs } from "../../utils";
import { wait } from "../../utils/reports";
import { Api } from "../../services/api";

import "../../styles/gestanteList.scss";
import "../../styles/listaNominal.scss";

import listMock from "./HipertensosList.mock.json";

type PainelParams = {
  id: string;
};

interface RowType {
  nome: string;
  nomeSocialSelecionado: boolean;
  zonaUrbana: boolean;
  zonaRural: boolean;
  possuiAlertas: boolean;
  cpf: string;
  cns: string;
  idade: number;
  diagnostico: string;
  sexo: string;
  equipe: string;
  microarea: string;
}

const ListaNominal = () => {
  const { id } = useParams<PainelParams>();
  const [showModal, setShowModal] = useState(false);
  const [data, setData] = useState<any>({ loaded: 7 });
  const [searchTerm, setSearchTerm] = useState("");

  const handleClick = (item: any) => {
    console.log("seleciona!! ", item);
    setData({ loaded: 7, ...item });
    setShowModal(true);
  };

  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  const condicao = String(queryParams.get("condicao"));

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

  const pathToReport = {
    Diabetes: "diabetes",
    Hipertensão: "arterial-hypertension",
  } as any;

  const {
    data: info,
    isLoading: isLoadingInfo,
    error: listError,
  } = useQuery(
    ["diabetes-list", {}],
    async () => {
      let path = `${pathToReport?.[condicao]}/get-nominal-list/${id}`;
      const response = await Api.get(path, {
        params: {
          itemsPerPage: 9999,
          page: 0,
        },
      });
      return response?.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  console.log({ info });

  const nomeUbs = !isLoadingUbs && id ? getNomeUbs(dataUbs, id) : city;
  const UBS = id ? (!isLoadingUbs ? nomeUbs : "Carregando...") : nomeUbs;
  const title = `${UBS} / Lista Nominal / ${condicao}`;
  const subtitle = "(referente aos últimos 12 meses)";

  const list: any = listMock;

  const [params, setParams] = useState({
    page: 1,
    size: 9999,
    totalElements: list.length,
    totalPages: Math.ceil(list.length / 30),
    sort: ["name", "alert", "zone"],
  });

  const handleSortChange = (sort: string[]) =>
    setParams((state) => ({ ...state, sort }));
  const handlePageChange = (page: number) =>
    setParams((state) => ({ ...state, page }));
  const handleSizeChange = (size: number) =>
    setParams((state) => ({
      ...state,
      size,
      totalPages: Math.max(1, Math.ceil(state.totalElements / size)),
    }));

  const filteredList = list.filter((item: RowType) => {
    const search = searchTerm.toLowerCase();
    return (
      item.nome.toLowerCase().includes(search) ||
      item.cpf.toLowerCase().includes(search) ||
      item.cns.toLowerCase().includes(search)
    );
  });

  const rows = filteredList
    .sort((a: any, b: any) => {
      const [sortField, sortOrder] = params.sort[0].startsWith("-")
        ? [params.sort[0].substring(1), "desc"]
        : [params.sort[0], "asc"];

      if (sortField === "nome") {
        return sortOrder === "asc"
          ? a?.nome.localeCompare(b?.nome)
          : b?.nome.localeCompare(a?.nome);
      }
      if (sortField === "alert") {
        return sortOrder === "asc"
          ? a?.possuiAlertas - b?.possuiAlertas
          : b?.possuiAlertas - a?.possuiAlertas;
      }
      if (sortField === "zone") {
        const zoneA = a.zonaUrbana ? "Urbana" : a.zonaRural ? "Rural" : "";
        const zoneB = b.zonaUrbana ? "Urbana" : b.zonaRural ? "Rural" : "";
        return sortOrder === "asc"
          ? zoneA.localeCompare(zoneB)
          : zoneB.localeCompare(zoneA);
      }
      return 0;
    })
    .slice(params.page * params.size, params.page * params.size + params.size);

  return (
    <div id="page-painel">
      {showModal && <Modal data={data} setShowModal={setShowModal} />}
      <ReportWrapper title={title} subtitle={subtitle}>
        {/*  <div className="search">
          <TextField
            name="iconized"
            id="iconized"
            placeholder="Busca por nome, CPF ou CNS"
            icon="zoomOutline"
            required
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div> */}
        <DataTable<RowType>
          rows={info?.items || []}
          sort={params.sort}
          // page={params.page}
          //   size={params.size}
          // totalElements={params.totalElements}
          //totalPages={params.totalPages}
          onSortChange={handleSortChange}
          //onPageChange={handlePageChange}
          //onSizeChange={handleSizeChange}
          loading={false}
          columns={[
            {
              name: "nome",
              header: "Nome",
              sortable: true,
              render: (item: any) => (
                <span
                  onClick={() => handleClick(item)}
                  style={{ marginLeft: "16px", cursor: "pointer" }}
                >
                  {item?.nomeSocialSelecionado &&
                  item?.nomeSocialSelecionado !== "-"
                    ? `${item?.nomeSocialSelecionado} *`
                    : item?.nome}
                </span>
              ),
            },
            {
              name: "alert",
              header: <div className="iconHeader iconAlerta ms-2"></div>,
              sortable: true,
              render: (item) => {
                if (item.possuiAlertas) {
                  return (
                    <span
                      className="iconCircle iconAlerta ms-2"
                      title="Possui Alertas"
                    >
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
              render: (item) => {
                if (item.zonaUrbana) {
                  return (
                    <span
                      className="iconCircle iconUrbano ms-2"
                      title="Zona Urbana"
                    >
                      U
                    </span>
                  );
                } else if (item.zonaRural) {
                  return (
                    <span
                      className="iconCircle iconRural ms-2"
                      title="Zona Rural"
                    >
                      R
                    </span>
                  );
                }
              },
            },
            {
              name: "cpf",
              header: "CPF",
              render: (item) => <b>{item.cpf}</b>,
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
              header: "Microárea",
              render: (item) => item.microarea,
            },
          ]}
        />
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
          </div>
        </div>
        <ReportFooter />
      </ReportWrapper>
    </div>
  );
};

export default ListaNominal;
