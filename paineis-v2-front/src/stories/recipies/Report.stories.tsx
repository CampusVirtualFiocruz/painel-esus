import React from 'react';
import { QueryClient, QueryClientProvider } from 'react-query';
import { MemoryRouter, Route, Routes } from 'react-router-dom';
import type { Meta, StoryObj } from "@storybook/react";
import { content } from "./../../assets/content/content";
import {
  Bar,
  Donut,
  ShallowTreemap,
  ValueCard,
  ProgressBar,
} from "./../../components/charts";
import { charts } from "../../components/charts/infantil.mock";
import ReportWrapper from '../../components/ui/ReportWrapper';
import { AuthContext } from '../../context/AuthProvider';
import { InfoProvider } from '../../context/infoProvider';
import { http } from 'msw';

const mockAuth = { 
  authenticate: async () => {},
  logout: () => {},
  chooseProfile: (profileData: any) => {},
  profilesList: [],
 };

const reportHeader = [
  {
    "total-criancas-cadastradas-2-anos": {
      Chart: ValueCard,
      config: {
        description: "Total de crianças até 2 anos cadastradas",
        icon: "paperdark",
      },
    },
    "total-criancas-atendidas-2-anos": {
      Chart: ValueCard,
      config: {
        description: "Total de crianças até 2 anos atendidas",
        icon: "paper",
      },
    },
  },
];

const reportSections = [
  {
    "total-cadastros-criancas-raca-cor": {
      Chart: ShallowTreemap,
      config: {
        colors: ["#0b5b98", "#6595ff", "#0066b4", "#49e8db", "#0066b4"],
      },
    },
    "total-extratificacao-por-profissional": {
      Chart: ProgressBar,
    },
  },
  {
    "distribuicao-criancas-faixa-etaria": {
      Chart: Bar,
      config: {
        hideLegend: true,
        colors: ["#0069d0", "#e4e4e4", "#84aaff", "#5c7ea0"],
        yAxis: {
          name: content?.["total-cadastros"],
        },
      },
    },
    "distribuicao-criancas-sexo": {
      Chart: Bar,
      config: {
        colors: ["rgba(57,150,193,255)", "rgba(92,210,200,255)", "#dddddd"],
        yAxis: {
          name: content?.["total-cadastros"],
        },
      },
    },
    "distribuicao-criancas-local": {
      Chart: Donut,
      config: {
        formatterKind: "perc",
        radiusStart: "0%",
        colors: ["#0069d0", "#e4e4e4", "#84aaff", "#5c7ea0"],
        yAxis: {
          name: content?.["total-cadastros"],
        },
      },
    },
  },
];

const Infantil = () => {
  const report = charts;

  return (
    <>
      {reportSections.map((chartList: any, colIndex) => (
        <div className="col-12 col-md-6">
          {colIndex === 0 && (
            <>
              <div
                style={{
                  display: "flex",
                  justifyContent: "center",
                  alignItems: "center",
                  marginTop: "50px",
                  marginBottom: "66px",
                }}
              >
                <div
                  style={{
                    display: "flex",
                    flex: "1",
                    flexDirection: "row",
                    gap: "30px",
                    width: "100%",
                    maxWidth: "600px",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  {reportHeader.map((chartList: any) =>
                    Object.keys(chartList).map((chartKey) => {
                      const CustomChart = chartList?.[chartKey]?.Chart;
                      const chartConfigs = chartList?.[chartKey]?.config;
                      const data = (report as any)?.[chartKey]?.data;
                      return <CustomChart data={data} config={chartConfigs} />;
                    })
                  )}
                </div>
              </div>
            </>
          )}
          {colIndex === 1 && (
            <div style={{ paddingTop: "60px", content: " " }} />
          )}
          {Object.keys(chartList).map((chartKey) => {
            const CustomChart = chartList?.[chartKey]?.Chart;
            const chartConfigs = chartList?.[chartKey]?.config;
            const data = (report as any)?.[chartKey]?.data;

            if (chartConfigs) {
              const xAxisNames = data?.map(
                (d: any) => content?.[d?.tag] ?? d?.tag
              );
              chartConfigs.xAxis = {};
              chartConfigs.xAxis.data = xAxisNames;
            }

            return (
              <div style={{ marginBottom: "40px" }}>
                <h5 style={{ fontWeight: "bold", textAlign: "center" }}>
                  {content?.[chartKey] || chartKey}
                </h5>
                <CustomChart data={data} config={chartConfigs} />
              </div>
            );
          })}
        </div>
      ))}
    </>
  );
};

// Story component with routing
const ReportStory: React.FC = () => (
  <MemoryRouter initialEntries={["/painel/1?equipe=1"]}>
    <Routes>
      <Route
        path="/painel/:id"
        element={
          <ReportWrapper
            title="Documentação - Relatório Exemplo"
            subtitle="(cuidado até o 2º ano de vida de acordo com a data da última atualização pelo município)"
          >
            <Infantil />
          </ReportWrapper>
        }
      />
    </Routes>
  </MemoryRouter>
);

const meta: Meta<typeof ReportStory> = {
  title: 'Recipies/Report',
  component: ReportStory,
  decorators: [
    (Story) => {
      const queryClient = new QueryClient();
      window.localStorage.setItem('u', JSON.stringify({ fullName: 'João Silva' }));
      return (
        <QueryClientProvider client={queryClient}>
          <AuthContext.Provider value={mockAuth}>
            <InfoProvider>
              <Story />
            </InfoProvider>
          </AuthContext.Provider>
        </QueryClientProvider>
      );
    },
  ],
  parameters: {
    msw: {
      handlers: [
        http.get('/v1/get-units', () => {
          return new Response(JSON.stringify({
            data: [
              { no_unidade_saude: 'UBS Central', co_seq_dim_unidade_saude: 1 },
              { no_unidade_saude: 'UBS Norte', co_seq_dim_unidade_saude: 2 },
            ],
          }))
        }),
        http.get('/v1/get-teams/:id', ({ params }) => {
          return new Response(JSON.stringify({
            data: [
              { nome_equipe: 'Equipe Alpha', codigo_equipe: Number(params.id) || 2 },
              { nome_equipe: 'Equipe Beta', codigo_equipe: Number(params.id) + 1 || 3 },
            ],
          }))
        }),
        http.get('/v1/city-informations', () => {
          return new Response(JSON.stringify({
            cep: '55000000',
            codIgbe: '2604106',
            estado: 'Pernambuco',
            municipio: 'Caruaru',
            uf: 'PE',
          }))
        }),
      ],
    },
  },
  tags: ['autodocs'],
} satisfies Meta<typeof ReportStory>;

export default meta;
export const Primary: StoryObj<typeof ReportStory> = {};