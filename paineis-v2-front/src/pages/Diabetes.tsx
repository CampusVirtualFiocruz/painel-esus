import { useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { useQuery } from 'react-query';
import { Alert, Progress, Spinner } from 'reactstrap';
import { getUserLocalStorage } from '../context/AuthProvider/util';

import { Footer } from '../components/Footer';
import { Modal } from '../components/Modal';
import { Header } from '../components/Header';

import { Bar } from '../charts/Bar';
import LibraryBar from '../library/charts/Bar';
import { Donut } from '../charts/Donut';
import { Pie } from '../charts/Pie';
import { BarSexo } from '../charts/BarSexo';

import info from '../assets/images/people.svg';
import { Api } from '../services/api';
import { getNomeUbs } from '../utils';
import '../styles/diabetesHipertensao.scss';

type TModal = {
  loaded: number;
  tipo?: string;
  cnes?: string | undefined;
};

type PainelParams = {
  id: string;
};

type TypeUbs = {
  label: string;
  value: number | string;
};

type Lista = {
  co_dim_unidade_saude_1: number;
  no_unidade_saude: string;
  nu_cnes: number;
};

type ResponseDataListUbs = {
  data: Lista[];
};

const defaultOptions = {
  staleTime: 1000 * 60 * 10, //10 minutos
};

// const sampleInput = {
//   labels: ['0 a 17 anos', '18 a 39 anos'],
//   series: [
//     {
//       name: 'Area Urbana',
//       data: [20, 40],
//     },
//     {
//       name: 'Area Rural',
//       data: [10, 20],
//     },
//   ],
// };

// const useDiabetesData = () => {
//   const queryKey = 'diabetes-age-group-location-v2';
//   const reqPath = 'diabetes/age-group-location';

//   const { id } = useParams<PainelParams>();
//   const path = `${reqPath}${id ? `/${id}` : ''}`;

//   const { data, isLoading, error } = useQuery(
//     [queryKey, id ? id : 'all'],
//     async () => (await Api.get(path))?.data,
//     defaultOptions
//   );

//   return {
//     // barChart: info,
//     isLoading,
//     error,
//   };
// };

export function Diabetes() {
  let navigate = useNavigate();
  const user = getUserLocalStorage();
  const { id } = useParams<PainelParams>();
  const [showModal, setShowModal] = useState(false);
  const [data, setData] = useState<TModal>({ loaded: 0 });

  let paramRoute = id ? id : 'all';

  const wait = (milliseconds: number) => {
    return new Promise((resolve) => setTimeout(resolve, milliseconds));
  };

  const getData = async (idModal: number, tipo?: string) => {
    await wait(100);
    setData({ loaded: idModal, tipo, cnes: id });
  };

  //get nome ubs
  const { data: dataUbs, isLoading: isLoadingUbs } = useQuery(
    'ubs',
    async () => {
      const response = await Api.get<ResponseDataListUbs>('get-units');
      const data = response.data;

      const listData: TypeUbs[] = data.data.map((ubs) => {
        return {
          label: ubs.no_unidade_saude,
          value: ubs.nu_cnes,
        };
      });

      return listData;
    },
    defaultOptions
  );

  const nomeUbs = !isLoadingUbs && id ? getNomeUbs(dataUbs, id) : '-';

  const {
    data: dataTotalDiabetes,
    isLoading: isLoadingTotalDiabetes,
    error: errorTotalDiabetes,
  } = useQuery(
    ['diabetes/total', paramRoute],
    async () => {
      const response = await Api.get('diabetes/total');
      const responseData = response.data;

      let total = responseData.data;

      return total.toLocaleString('pt-BR');
    },
    defaultOptions
  );

  const {
    data: dataDiabetesAgeGroupGender,
    isLoading: isLoadingDiabetesAgeGroupGender,
    error: errorDiabetesAgeGroupGender,
  } = useQuery(
    ['diabetes-age-group-gender', paramRoute],
    async () => {
      let path = id
        ? `diabetes/age-group-gender/${id}`
        : 'diabetes/age-group-gender';
      const response = await Api.get(path);
      const responseData = response.data;

      return responseData.data;
    },
    defaultOptions
  );

  const {
    data: dataDiabetes,
    isLoading: isLoadingDiabetes,
    error: errorDiabetes,
  } = useQuery(
    ['diabetes-age-group-location', paramRoute],
    async () => {
      let path = id
        ? `diabetes/age-group-location/${id}`
        : 'diabetes/age-group-location';
      const response = await Api.get(path);
      const responseData = response.data;

      return responseData.data;
    },
    defaultOptions
  );

  const {
    data: dataDiabetesIndicators,
    isLoading: isLoadingDiabetesIndicators,
    error: errorDiabetesIndicators,
  } = useQuery(
    ['diabetes-complications', paramRoute],
    async () => {
      let path = id ? `diabetes/complications/${id}` : 'diabetes/complications';
      const response = await Api.get(path);
      const responseData = response.data;

      const arrData = responseData.data.map((item: any, i: number) => {
        let obj = Object.entries(item);
        return [obj[0][0], obj[0][1]];
      });

      return arrData;
    },
    defaultOptions
  );

  const {
    data: dataDiabetesFactors,
    isLoading: isLoadingDiabetesFactors,
    error: errorDiabetesFactors,
  } = useQuery(
    ['diabetes-factors-imc', paramRoute],
    async () => {
      let path = id ? `diabetes/imc/${id}` : 'diabetes/imc';
      const response = await Api.get(path);
      const responseData = response.data;

      return responseData.data;
    },
    defaultOptions
  );

  const {
    data: dataExamsTable,
    isLoading: isLoadingExamsTable,
    error: errorExamsTable,
  } = useQuery(
    ['diabetes-exams', paramRoute],
    async () => {
      let path = id ? `diabetes/exams/${id}` : 'diabetes/exams';
      const response = await Api.get(path);
      const data = response.data;

      return data.data;
    },
    defaultOptions
  );

  const random_hex_color_code = () => {
    let n = (Math.random() * 0x361949 * 1000000).toString(16);
    return '#' + n.slice(0, 6);
  };

  const {
    data: dataProffessionals,
    isLoading: isLoadingProffessionals,
    error: errorProffessionals,
  } = useQuery(
    ['diabetes-proffessionals', paramRoute],
    async () => {
      let path = id
        ? `diabetes/proffessionals/${id}`
        : 'diabetes/proffessionals';
      const response = await Api.get(path);
      const data = response.data;

      return data.data;
    },
    defaultOptions
  );

  function handleToPainelUbs() {
    navigate(`/painel/${id}`);
  }

  function handleToPainelMunicipio() {
    navigate('/painelx');
  }

  const handleClick = (idModal: number) => {
    setData({ loaded: 0 });
    setShowModal(true);
    getData(idModal);
  };
  const handleToDiabeticosList = () => {
    navigate('/diabeticos');
  };
  return (
    <div id="page-painel">
      <Header />

      <div className="contentWrapper">
        <hr className="linha my-4" />

        <h2>
          {id
            ? !isLoadingUbs
              ? nomeUbs
              : 'Carregando...'
            : user.municipio + ' - ' + user.uf}{' '}
          / Painel Diabetes
        </h2>

        {showModal && <Modal data={data} setShowModal={setShowModal} />}

        <div className="container-fluid">
          <div className="row gx-5">
            <div className="col-12 col-lg-5">
              <div className="painel-lateral">
                <h4 className="mt-5 text-center">
                  Pessoas com diabetes por faixa etária
                </h4>
                {isLoadingDiabetes ? (
                  <div className="d-flex align-items-center justify-content-center">
                    <Spinner size="sm" type="grow" className="me-2" />
                    Carregando...
                  </div>
                ) : errorDiabetes ? (
                  <div className="d-flex align-items-center justify-content-center">
                    <Alert color="danger">Erro ao carregar dados.</Alert>
                  </div>
                ) : (
                  <>
                    <Bar
                      data={dataDiabetes}
                      titulo="Total de pessoas com diabetes no município"
                    />
                    {/* <LibraryBar
                      datasource={sampleInput}
                      title="Total de pessoas com diabetes no município"
                    /> */}
                  </>
                )}
              </div>

              <div className="painel-lateral">
                <h4 className="mt-5 text-center">
                  Pessoas com diabetes por sexo
                </h4>
                {isLoadingDiabetesAgeGroupGender ? (
                  <div className="d-flex align-items-center justify-content-center">
                    <Spinner size="sm" type="grow" className="me-2" />
                    Carregando...
                  </div>
                ) : errorDiabetesAgeGroupGender ? (
                  <div className="d-flex align-items-center justify-content-center">
                    <Alert color="danger">Erro ao carregar dados.</Alert>
                  </div>
                ) : (
                  <BarSexo
                    data={dataDiabetesAgeGroupGender}
                    titulo="Total de pessoas com diabetes no município"
                  />
                )}
              </div>

              <div className="painel-lateral situacao-exames">
                <h3 className="my-5 text-center">
                  Situação dos exames nos últimos 12 meses
                </h3>

                <div className="row gx-4 my-3">
                  <div className="col-5 col-lg-6"></div>
                  <div className="col col-lg-3">
                    <div className="tipo p-2 text-center">
                      Solicitação pendente
                    </div>
                  </div>
                  <div className="col col-lg-3">
                    <div className="tipo p-2 text-center">
                      Avaliação pendente
                    </div>
                  </div>
                </div>

                {isLoadingExamsTable ? (
                  <div className="d-flex align-items-center justify-content-center">
                    <Spinner size="sm" type="grow" className="me-2" />
                    Carregando...
                  </div>
                ) : errorExamsTable ? (
                  <div className="d-flex align-items-center justify-content-center">
                    <Alert color="danger">Erro ao carregar dados.</Alert>
                  </div>
                ) : (
                  <>
                    {dataExamsTable?.map((situacao: any, i: number) => (
                      <div key={i} className="row gx-4 my-3">
                        <div className="col-5 col-lg-6">
                          <div className="tipo p-2 bordas">{situacao.tipo}</div>
                        </div>
                        <div className="col col-lg-3">
                          <div className="tipo p-2 text-center bordas">
                            {situacao.solicitados}
                          </div>
                        </div>
                        <div className="col col-lg-3">
                          <div className="tipo p-2 text-center bordas">
                            {situacao.avaliados}
                          </div>
                        </div>
                      </div>
                    ))}
                  </>
                )}
              </div>
            </div>

            <div className="col-12 col-lg-7 d-flex flex-column">
              <div className="painel-lateral">
                <h4 className="mt-5 mb-4 text-center">
                  Total de atendimento nos últimos 12 meses
                </h4>

                <div className="d-flex flex-wrap flex-lg-nowrap justify-content-center">
                  <div>
                    <div className="container-atendimentos">
                      <div className="titulo d-flex align-items-center">
                        <img
                          src={info}
                          alt="Total de atendimento nos últimos 12 meses"
                          className="info mx-2"
                        />
                      </div>
                      <span className="total-trimestre ms-4">
                        {isLoadingTotalDiabetes ? (
                          <div className="d-flex align-items-center justify-content-center">
                            <Spinner size="sm" type="grow" className="me-2" />0
                          </div>
                        ) : errorTotalDiabetes ? (
                          <div className="d-flex align-items-center justify-content-center">
                            <Alert color="danger">
                              Erro ao carregar dados.
                            </Alert>
                          </div>
                        ) : (
                          dataTotalDiabetes
                        )}
                      </span>
                    </div>
                  </div>
                </div>
              </div>

              <div className="painel-secundario my-2">
                <h4 className="my-4 text-center">
                  Frequência de complicações relacionadas à diabetes
                </h4>

                <div className="d-flex flex-wrap flex-xl-nowrap justify-content-center">
                  {isLoadingDiabetesIndicators ? (
                    <div className="d-flex align-items-center justify-content-center">
                      <Spinner size="sm" type="grow" className="me-2" />
                      Carregando...
                    </div>
                  ) : errorDiabetesIndicators ? (
                    <div className="d-flex align-items-center justify-content-center">
                      <Alert color="danger">Erro ao carregar dados.</Alert>
                    </div>
                  ) : (
                    <>
                      {dataDiabetesIndicators?.map(
                        (indicador: any, i: number) => (
                          <Donut key={i} data={indicador} />
                        )
                      )}
                    </>
                  )}
                </div>

                <button
                  type="button"
                  onClick={() => handleClick(5)}
                  className="btn btn-primary mt-5"
                >
                  Boas práticas na assistência a pessoa com diabetes
                </button>
              </div>

              <div className="painel-secundario">
                <h4 className="mt-5 mb-4 text-center">
                  Adultos com diabetes de acordo com o IMC
                </h4>

                <div className="d-flex flex-wrap flex-lg-nowrap justify-content-center">
                  {isLoadingDiabetesFactors ? (
                    <div className="d-flex align-items-center justify-content-center">
                      <Spinner size="sm" type="grow" className="me-2" />
                      Carregando...
                    </div>
                  ) : errorDiabetesFactors ? (
                    <div className="d-flex align-items-center justify-content-center">
                      <Alert color="danger">Erro ao carregar dados.</Alert>
                    </div>
                  ) : (
                    <>
                      {dataDiabetesFactors?.map((diabete: any, i: number) => (
                        <Pie key={i} data={diabete} />
                      ))}
                    </>
                  )}
                </div>
              </div>

              <div className="painel-secundario">
                <h4 className="mt-5 mb-4 text-center">
                  Extratificação de atendimentos por profissional
                </h4>
                <div className="w-100">
                  {isLoadingProffessionals ? (
                    <div className="d-flex align-items-center justify-content-center">
                      <Spinner size="sm" type="grow" className="me-2" />
                      Carregando...
                    </div>
                  ) : errorProffessionals ? (
                    <div className="d-flex align-items-center justify-content-center">
                      <Alert color="danger">Erro ao carregar dados.</Alert>
                    </div>
                  ) : (
                    <>
                      {dataProffessionals?.map((item: any, i: number) => (
                        <div key={i} className="d-flex align-items-center mt-2">
                          <div className="container-extratificacao-atendimentos">
                            <span className="profissao-nome">
                              {item.profissao}
                            </span>
                            <Progress
                              value={item.total}
                              className="w-75"
                              barStyle={{
                                backgroundColor: random_hex_color_code(),
                              }}
                            />
                          </div>
                          <span className="total ms-2">{item.total}%</span>
                        </div>
                      ))}
                    </>
                  )}
                </div>
              </div>
            </div>
          </div>
          <div className="row my-5 text-center">
            <div className="col-12">
              <button
                type="button"
                onClick={() => handleToDiabeticosList()}
                className="btn btn-secondary my-2"
              >
                Ver todos pacientes com Diabetes
              </button>
            </div>
          </div>
        </div>

        <div className="d-flex flex-column align-items-center mt-5">
          {id && (
            <button
              type="button"
              onClick={handleToPainelUbs}
              className="btn btn-light my-2"
            >
              Voltar para o Painel da UBS
            </button>
          )}
          <button
            type="button"
            onClick={handleToPainelMunicipio}
            className="btn btn-primary my-4"
          >
            Visualizar dados do painel do Município
          </button>
        </div>
      </div>

      <Footer />
    </div>
  );
}
