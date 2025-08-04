import { useEffect, useState } from "react";
import { useQuery } from "react-query";
import { useNavigate, useParams } from "react-router-dom";
import { DonutChart, TDonutChart } from "../../charts/Donut";
import { LineChart } from "../../charts/LineChart";
import { PieChart, TPieChart } from "../../charts/Pie";
import { StackedArea } from "../../charts/StackedArea";
import { Footer } from "../../components/Footer";
import { Header } from "../../components/Header";
import { Api } from "../../services/api2";
import "../../styles/sindromeAguda.scss";
import { navigateHome } from "../../utils";
type PainelParams = {
  id: string;
};

type TResponse = {
  co_dim_tempo: string;
  nu_cnes: string;
  type: string;
  ds_filtro_cids: number;
  local: string;
};
type TStackDataValues = {
  name: string;
  type: string;
  color: string;
  data: number[];
};
type TStackData = {
  labels: string[];
  data: TStackDataValues[];
  setRangeData: (args: string[]) => void;
};
export function SindromesAgudas() {
  let navigate = useNavigate();
  const [loading, setLoading] = useState(true);

  const taxa_atendimento_agudo = 1.53;
  const [infecaoRespiratoriaState, setInfecaoRespiratoriaState] =
    useState<number>(0);
  const [infecaoIntestinalState, setInfecaoIntestinalState] =
    useState<number>(0);
  const [febreExantematicaState, setFebreExantematicaState] =
    useState<number>(0);
  const [febreInespecificaState, setFebreInespecificaState] =
    useState<number>(0);
  const [totalAtendimentosState, setTotalAtendimentosState] =
    useState<number>(0);
  const [stackData, setStackData] = useState<TStackData>({
    labels: [],
    data: [],
    setRangeData: () => {},
  });
  const [lineData, setLineData] = useState<TStackData>({
    labels: [],
    data: [],
    setRangeData: () => {},
  });
  const [rangeData, setRangeData] = useState<string[]>([]);
  const [responseData, setResponseData] = useState<TResponse[]>([]);

  const { id } = useParams<PainelParams>();
  const {
    data: sindromesAgudasData,
    isLoading,
    error,
  } = useQuery(["sindromes-agudas", id], async () => {
    // let path = id ? `pregnants/exams-table/${id}` : 'pregnants/exams-table';
    let path = "/saida.json";
    const response = await Api.get(path);
    let data = response.data;
    if (id) {
      data = data.filter((item: TResponse) => item.nu_cnes == id);
    }
    handleSindromeAgudaData(data);
    setResponseData(data);
    return data;
  });

  function handleSindromeAgudaData(response: TResponse[]) {
    const mapSindromes: { [key: string]: number } = {
      infeccao_respiratorio: 0,
      infeccao_intestinal: 0,
      febre_exantematica: 0,
      febre_inespecifica: 0,
      total: 0,
    };
    const labels: Set<string> = new Set([]);
    const dataSet: any = {};

    const totalSindromeAgura: number[] = [];

    for (const resp of response) {
      labels.add(resp.co_dim_tempo);
      if (!(resp.co_dim_tempo in dataSet)) {
        dataSet[resp.co_dim_tempo] = [resp];
      } else {
        dataSet[resp.co_dim_tempo].push(resp);
      }
      totalSindromeAgura.push(resp.ds_filtro_cids);

      mapSindromes[resp.type] += resp.ds_filtro_cids;
      mapSindromes["total"] += resp.ds_filtro_cids;
    }

    let initZeros: number[] = [];
    labels.forEach((i) => initZeros.push(0));

    const mapSindromesData: { [key: string]: number[] } = {
      infeccao_respiratorio: Array.from(initZeros),
      infeccao_intestinal: Array.from(initZeros),
      febre_exantematica: Array.from(initZeros),
      febre_inespecifica: Array.from(initZeros),
    };

    const mapLabels: { [key: string]: string } = {
      infeccao_respiratorio: "Infecção Respiratoria",
      infeccao_intestinal: "Infecção Intestinal",
      febre_exantematica: "Febre Exantemática",
      febre_inespecifica: "Febre Inespecífica",
    };
    const mapColors: { [key: string]: string } = {
      infeccao_respiratorio: "#5dd2c9",
      infeccao_intestinal: "#3996c1",
      febre_exantematica: "#2675b0",
      febre_inespecifica: "#094069",
    };
    let idx = 0;
    for (const data of Array.from(labels)) {
      if (data in dataSet) {
        for (const item of dataSet[data]) {
          mapSindromesData[item.type][idx] += item.ds_filtro_cids;
        }
      }
      idx++;
    }
    const restulStackData = [];
    for (const item of Object.keys(mapSindromesData)) {
      restulStackData.push({
        name: mapLabels[item],
        type: item,
        color: mapColors[item],
        data: mapSindromesData[item],
      });
    }
    setFebreExantematicaState(mapSindromes.febre_exantematica);
    setFebreInespecificaState(mapSindromes.febre_inespecifica);
    setInfecaoIntestinalState(mapSindromes.infeccao_intestinal);
    setInfecaoRespiratoriaState(mapSindromes.infeccao_respiratorio);
    setTotalAtendimentosState(mapSindromes.total);
    setStackData({
      labels: Array.from(labels),
      data: restulStackData,
      setRangeData: setRangeData,
    });
    setLineData({
      labels: Array.from(labels),
      data: [
        {
          name: "Atendimentos gerais",
          type: "atendimentos gerais",
          color: "#5cd2c8fc",
          data: totalSindromeAgura.map((item: number) =>
            Math.ceil(item * taxa_atendimento_agudo)
          ),
        },
        {
          name: "Atendimentos por síndromes agudas",
          type: "atendimentos por sindrome agudas",
          color: "#09406a",
          data: totalSindromeAgura,
        },
      ],
      setRangeData: setRangeData,
    });
  }
  function filterRange(start: string, end: string) {
    const startDate = new Date(start);
    const endDate = new Date(end);
    return responseData.filter((item: TResponse) => {
      const itemDate = new Date(item.co_dim_tempo);
      return itemDate >= startDate && itemDate <= endDate;
    });
  }
  useEffect(() => {
    let filteredData = [];
    if (rangeData[0] != "0" && rangeData[1] != "0") {
      filteredData = filterRange(rangeData[0], rangeData[1]);
    } else {
      filteredData = responseData;
    }
    handleSindromeAgudaData(filteredData);
  }, [rangeData]);

  return (
    <div id="page-painel">
      <Header />

      <div className="contentWrapper">
        <hr className="linha my-4" />

        <h2>Painel Sindromes Agudas</h2>

        <div className="container-fluid">
          <div className="row gx-5">
            <div className="col-12 col-lg-5">
              <div className="painel-lateral">
                <h4 className="my-5 text-center">
                  Número de atendimentos por síndrome aguda
                </h4>
                <div className="row gx-5  d-flex-center">
                  <div className="col-12 col-lg-5">
                    <PieChart
                      {...new TPieChart(
                        "Infeccoes respiratórias",
                        [
                          { value: infecaoRespiratoriaState },
                          { value: totalAtendimentosState },
                        ],
                        "#5cd2c8"
                      )}
                    />
                  </div>
                  <div className="col-12 col-lg-5">
                    <PieChart
                      {...new TPieChart(
                        "Infeccoes Intestinais",
                        [
                          { value: infecaoIntestinalState },
                          { value: totalAtendimentosState },
                        ],
                        "#3996c1"
                      )}
                    />
                  </div>
                  <div className="col-12 col-lg-5 mt-10">
                    <PieChart
                      {...new TPieChart(
                        "Febres Exantemáticas",
                        [
                          { value: febreExantematicaState },
                          { value: totalAtendimentosState },
                        ],
                        "#0069d0"
                      )}
                    />
                  </div>
                  <div className="col-12 col-lg-5 mt-10">
                    <PieChart
                      {...new TPieChart(
                        "Febres Inespecíficas",
                        [
                          { value: febreInespecificaState },
                          { value: totalAtendimentosState },
                        ],
                        "#09406a"
                      )}
                    />
                  </div>
                </div>
              </div>
            </div>

            <div className="col-12 col-lg-7 ">
              <div className="painel-lateral">
                <h4 className="my-5 text-center">
                  Relação de atendimentos por síndrome aguda
                </h4>
                <StackedArea {...stackData} />
              </div>
            </div>

            <div
              className="col-12 col-lg-4 label-container "
              style={{ marginTop: 30 }}
            >
              <div className="label">
                Número de atendimentos por síndromes agudas
              </div>
              <div className="label-value">{totalAtendimentosState}</div>
            </div>
          </div>
        </div>

        <div className="container-fluid">
          <div className="row gx-5">
            <div className="col-12 col-lg-5">
              <div className="painel-lateral">
                <h4 className="my-5 text-center">
                  Relação de atendimentos gerais x sídromes agudas
                </h4>
              </div>
              <div className="col-12">
                <DonutChart
                  {...new TDonutChart(
                    "Febres Inespecíficas",
                    [
                      {
                        value: Math.ceil(totalAtendimentosState * 1.33),
                        name: "Atendimentos gerais",
                      },
                      {
                        value: totalAtendimentosState,
                        name: "Atendimentos por síndromes agudas",
                      },
                    ],
                    "#5cd2c8"
                  )}
                />
              </div>
            </div>

            <div className="col-12 col-lg-7">
              <div className="painel-lateral">
                <h4 className="my-5 text-center">
                  Comparativo do volume de atendimentos gerais em relacao às
                  síndromes agudas
                </h4>
                <LineChart {...lineData} />
              </div>
            </div>
            <div className="col-12 col-lg-4 label-container">
              <div
                className="label"
                style={{ display: "flex", justifyContent: "center" }}
              >
                Total de atendimentos
              </div>
              <div className="label-value">
                {Math.ceil(totalAtendimentosState * taxa_atendimento_agudo)}
              </div>
            </div>
          </div>
          <div className="row gx-5">
            <div className="col-12 col-lg-12 d-flex-center">
              <button
                type="button"
                onClick={() => navigateHome(navigate)}
                className="btn btn-primary"
              >
                Voltar
              </button>
            </div>
          </div>
        </div>
      </div>

      <Footer />
    </div>
  );
}
