import { useState } from "react";
import { useParams, useLocation, useSearchParams } from "react-router-dom";
import { useQuery } from "react-query";
import { PagedTable, TextField, LocaleContext } from "bold-ui";
import ptBr from "bold-ui/lib/i18n/locales/pt-BR";
import { Modal } from "../../components/Modal";
import ReportWrapper from "../../components/ui/ReportWrapper";
import { useInfo } from "../../context/infoProvider/useInfo";
import { getNomeUbs } from "../../utils";
import { Api } from "../../services/api";
import "../../styles/gestanteList.scss";
import "../../styles/listaNominal.scss";
import usePaginatedList from "./usePaginatedList";
import { columns, Footer, footerNotes } from "./ListaNominal.utils";

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
  const [params] = useSearchParams();
  const equipe = params.get("equipe");

  const handleClick = (item: any) => {
    setData({ loaded: 7, ...item });
    setShowModal(true);
  };

  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  const condicao = String(queryParams.get("condicao"));
  const footerNote = footerNotes?.[condicao];

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

  const { info, setParams, isLoadingInfo, pathToReport } = usePaginatedList({
    condicao,
    equipe,
    id,
    searchTerm,
  });

  const handleSortChange = (sort: string[]) =>
    setParams((state: any) => ({ ...state, sort }));

  const handlePageChange = (page: number) =>
    setParams((state: any) => ({ ...state, page: page + 1 }));

  const handleSizeChange = (size: number) =>
    setParams((state: any) => ({
      ...state,
      size,
      totalPages: Math.max(1, Math.ceil(state.totalElements / size)),
    }));

  return (
    <div id="page-painel">
      {showModal && <Modal data={data} setShowModal={setShowModal} />}
      <ReportWrapper
        title={"Lista Nominal / "+ condicao}
        subtitle={condicao === "Qualidade" ? "(Pessoas registradas a partir de 2019)" : "(Pessoas atendidas nos últimos 12 meses)" }
        footerNote={footerNote}
      >
        <div className="search">
          <TextField
            name="iconized"
            id="iconized"
            placeholder="Busca por CPF, CNS, Nome"
            icon="zoomOutline"
            required
            value={searchTerm}
            onChange={(e: any) => setSearchTerm(e.target.value)}
          />
        </div>
        <LocaleContext.Provider value={ptBr}>
          <PagedTable<RowType>
            rows={info?.items || []}
            page={info?.page - 1}
            size={info?.itemsPerPage}
            totalElements={info?.itemsCount}
            totalPages={info?.pagesCount}
            onSortChange={handleSortChange}
            onPageChange={handlePageChange}
            onSizeChange={handleSizeChange}
            loading={isLoadingInfo}
            columns={columns({ handleClick, condicao })}
          />
        </LocaleContext.Provider>
        <Footer pathToReport={pathToReport} condicao={condicao} id={id} />
      </ReportWrapper>
    </div>
  );
};

export default ListaNominal;
