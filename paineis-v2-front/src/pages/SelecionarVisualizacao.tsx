import { Button } from 'bold-ui';
import { CSSProperties, useState } from 'react';
import { useQuery } from 'react-query';
import { useNavigate } from 'react-router-dom';
import Select, { StylesConfig } from 'react-select';
import { Spinner } from 'reactstrap';

import iconeEquipe from '../assets/images/visualizacao/Icone_Equipe.svg';
import iconeMunicipio from '../assets/images/visualizacao/Icone_Municipio.svg';
import iconeUbs from '../assets/images/visualizacao/Icone_UBS.svg';
import { Footer } from '../components/Footer';
import { Header } from '../components/Header';
import { useAuth } from '../context/AuthProvider/useAuth';
import { Api } from '../services/api';
import variables from '../styles/_exports.module.scss';
import { navigateHome } from '../utils';

import '../styles/selecionarubs.scss';
import '../styles/selecionarvisualizacao.scss';

type Lista = {
  co_seq_dim_unidade_saude: number;
  no_unidade_saude: string;
  nu_cnes: number;
};

type ResponseData = {
  data: Lista[];
};

type TypeUbs = {
  label: string;
  value: number | string;
};

const customControlStyles: CSSProperties = {
  backgroundColor: variables['--primary-color'],
  width: '250px',
  height: '40px',
  color: variables['--text-color'],
};

type IsMulti = false;

const selectStyle: StylesConfig<TypeUbs, IsMulti> = {
  control: provided => {
    return {
      marginTop: '10px',
      ...provided,
      ...customControlStyles,
    };
  },
  option: (provided, state) => ({
    ...provided,
    color: state.isSelected ? '#FFFFFF' : '',
    backgroundColor: state.isSelected ? '#343131' : '',
    padding: 16,
  }),
  clearIndicator: () => ({
    color: '#343131',
  }),
  dropdownIndicator: () => ({
    color: '#343131',
  }),
};

export function SelecionarVisualizacao() {
  const navigate = useNavigate();
  const { currentProfile }: any = useAuth();

  const [currentUbs, setCurrentUbs] = useState<any>(
    currentProfile?.currentUbs || undefined
  );
  const [currentTeam, setCurrentTeam] = useState<any>(
    currentProfile?.currentTeam || undefined
  );

  const { data, isLoading, error } = useQuery(
    'ubs',
    async () => {
      const response = await Api.get<ResponseData>('get-units');
      const data = response.data;
      const listData: TypeUbs[] = data.data.map(ubs => {
        return {
          label: ubs.no_unidade_saude,
          value: ubs.co_seq_dim_unidade_saude,
        };
      });

      return listData;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const { data: teamsData } = useQuery(
    `get-teams/${currentUbs}`,
    async () => {
      let listData: TypeUbs[] = [];
      if (currentUbs) {
        const response = await Api.get<ResponseData>(`get-teams/${currentUbs}`);
        const data = response.data;
        listData = data.data.map((i: any) => {
          return {
            ...i,
            label: `${i.nome_equipe} (${i.codigo_equipe})`,
            value: i.codigo_equipe,
          };
        });
      }
      return listData;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const teamSuggestion = currentTeam || currentProfile?.currentTeam;
  const ubsSuggestion = currentUbs || currentProfile?.currentUbs;

  const handleToPainelWithTeam = () => {
    navigateHome(navigate, `/${ubsSuggestion}?equipe=${teamSuggestion}`);
  };

  const handleToPainelWithUbs = () => {
    navigateHome(navigate, `/${ubsSuggestion}`);
  };

  const onChangeSelection = (e: any) => {
    setCurrentUbs(e.value);
  };

  const onChangeTeamSelection = (e: any) => {
    setCurrentTeam(e.value);
  };

  return (
    <div id='page-selecionar-ubs'>
      <Header />
      <div className='contentWrapper'>
        <div className='container-titulo mb-5'>
          <h2>Visualizar dados por:</h2>
        </div>
        <div className='container-escolher d-flex flex-column flex-md-row'>
          <div className='container-combo-ubs ms-md-4'>
            <div className='container-icone'>
              <img
                className='icone-municipio'
                src={iconeMunicipio}
                alt='Ícone de Município'
              />
              <Button
                onClick={() => navigateHome(navigate)}
                type='button'
                kind='primary'
                style={{ marginTop: '10px' }}
              >
                Município
              </Button>
            </div>
          </div>
          <div className='container-combo-ubs ms-md-4'>
            <div className='container-icone'>
              <img className='icone-ubs' src={iconeUbs} alt='Ícone de UBS' />
              {isLoading ? (
                <div className='combo-ubs d-flex align-items-center justify-content-center'>
                  <Spinner size='sm' /> Carregando lista de UBS&apos;s
                </div>
              ) : error ? (
                <div className='combo-ubs d-flex align-items-center justify-content-center'>
                  Falha ao carregar lista de UBS&apos;s
                </div>
              ) : (
                <>
                  {!currentProfile?.currentUbs && (
                    <Select
                      isClearable
                      placeholder='UBS'
                      noOptionsMessage={() => 'Nenhuma UBS encontrada'}
                      options={data}
                      styles={selectStyle}
                      onChange={onChangeSelection}
                    />
                  )}
                  {(currentUbs || currentProfile?.currentUbs) && (
                    <Button
                      onClick={handleToPainelWithUbs}
                      type='button'
                      kind='primary'
                      style={{ marginTop: '10px' }}
                    >
                      Acessar UBS
                    </Button>
                  )}
                </>
              )}
            </div>
          </div>
          {String(currentProfile?.info) !== 'not-configured' && (
            <div
              className='container-combo-ubs ms-md-4'
              style={{
                opacity: currentUbs || currentProfile?.currentUbs ? 1 : 0.5,
              }}
            >
              <div className='container-icone'>
                <img
                  className='icone-equipe'
                  src={iconeEquipe}
                  alt='Ícone de Equipe'
                />
                {isLoading ? (
                  <div className='combo-ubs d-flex align-items-center justify-content-center'>
                    <Spinner size='sm' /> Carregando lista de equipes
                  </div>
                ) : error ? (
                  <div className='combo-ubs d-flex align-items-center justify-content-center'>
                    Falha ao carregar lista de equipes
                  </div>
                ) : (
                  <>
                    {!currentProfile?.currentTeam && (
                      <Select
                        isClearable
                        placeholder={'Equipe'}
                        noOptionsMessage={() => 'Nenhuma equipe encontrada'}
                        options={teamsData}
                        styles={selectStyle}
                        onChange={onChangeTeamSelection}
                        isDisabled={!currentUbs}
                      />
                    )}
                    {!(currentUbs || currentProfile?.currentUbs) ? (
                      <p style={{ fontSize: '12px' }}>
                        Selecione uma ubs para continuar
                      </p>
                    ) : null}
                    {(currentTeam || currentProfile?.currentTeam) && (
                      <Button
                        onClick={handleToPainelWithTeam}
                        type='button'
                        kind='primary'
                        style={{ marginTop: '10px' }}
                      >
                        Acessar Equipe
                      </Button>
                    )}
                  </>
                )}
              </div>
            </div>
          )}
        </div>
      </div>
      <Footer />
    </div>
  );
}
