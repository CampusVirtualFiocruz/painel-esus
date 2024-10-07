import { useState } from "react";
import { useParams, useLocation } from "react-router-dom";
import { useQuery } from "react-query";
import { PagedTable, TextField } from "bold-ui";
import { Modal } from "../../components/Modal";
import ReportWrapper from "../../components/ui/ReportWrapper";
import { useInfo } from "../../context/infoProvider/useInfo";
import { getNomeUbs } from "../../utils";
import { Api } from "../../services/api";
import "../../styles/gestanteList.scss";
import "../../styles/listaNominal.scss";
import usePaginatedList from "./usePaginatedList";
import { columns, Footer } from "./ListaNominal.utils";

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

  const { info, setParams, isLoadingInfo, pathToReport } = usePaginatedList({
    condicao,
    id,
    searchTerm,
  });

  const nomeUbs = !isLoadingUbs && id ? getNomeUbs(dataUbs, id) : city;
  const UBS = id ? (!isLoadingUbs ? nomeUbs : "Carregando...") : nomeUbs;
  const title = `${UBS} / Lista Nominal / ${condicao}`;
  const subtitle = "(referente aos últimos 12 meses)";

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
      <ReportWrapper title={title} subtitle={subtitle}>
        <div className="search">
          <TextField
            name="iconized"
            id="iconized"
            placeholder="Busca por CPF"
            icon="zoomOutline"
            required
            value={searchTerm}
            onChange={(e: any) => setSearchTerm(e.target.value)}
          />
        </div>
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
          columns={columns({ handleClick })}
        />
        <Footer pathToReport={pathToReport} condicao={condicao} id={id} />
      </ReportWrapper>
    </div>
  );
};

export default ListaNominal;
