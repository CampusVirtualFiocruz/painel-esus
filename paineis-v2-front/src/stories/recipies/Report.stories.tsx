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
import { Footer } from "../../components/Footer";
import { Button, Link } from "bold-ui";
import { FaUser } from "react-icons/fa";
import ReportWrapper from '../../components/ui/ReportWrapper';
import { AuthContext } from '../../context/AuthProvider';
import { InfoProvider } from '../../context/infoProvider';
import { http, HttpResponse, delay } from 'msw';

const queryClient = new QueryClient();

// const MockAuthProvider = ({ children }: { children: React.ReactNode }) => (
//   <AuthContext.Provider value={{
//     logout: () => {},
//     user: { fullName: 'Usuário Storybook' }
//   }}>
//     {children}
//   </AuthContext.Provider>
// );

queryClient.setQueryData('ubs', [
  {
    label: 'UBS Teste',
    value: 1,
    id: 1,
    qtd: 100,
  },
]);

queryClient.setQueryData('get-teams/1', [
  {
    label: 'Equipe 1 (1)',
    value: 1,
    nome_equipe: 'Equipe 1',
    codigo_equipe: 1,
  },
]);

queryClient.setQueryData('city-informations', {
  municipio: 'Cidade Storybook',
  uf: 'SB',
  cep: '00000-000',
  codIgbe: '1234567',
  estado: 'Estado SB'
});

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

const Report = () => {
  return (
    <QueryClientProvider client={queryClient}>
      {/* <MockAuthProvider> */}
        <InfoProvider>
          <MemoryRouter initialEntries={['/painel/1?equipe=1']}>
            <Routes>
              <Route
                path="/painel/:id"
                element={
                  <ReportWrapper title="Documentação - Relatório Exemplo" subtitle="(cuidado até o 2º ano de vida de acordo com a data da última atualização pelo município)">
                    <Infantil />
                  </ReportWrapper>
                }
              />
            </Routes>
          </MemoryRouter>
        </InfoProvider>
      {/* </MockAuthProvider> */}
    </QueryClientProvider>
  );
};

const meta = {
  title: "Recipies/Report",
  component: Report,
  parameters: {
    //layout: 'centered',
  },
  tags: ["autodocs"],
  argTypes: {},
  args: {},
} satisfies Meta;

export default meta;
type Story = StoryObj<typeof meta>;

export const MockedSuccess: Story = {
  parameters: {
    msw: {
      handlers: [
        http.get('/city-informations', () => {
          return HttpResponse.json({
            cep: '00000-000',
            codIgbe: '12345',
            estado: 'PERNAMBUCO',
            municipio: 'LIVRAMENTO',
            uf: 'PE',
          });
        }),
      ],
    },
  },
};

export const Basic: Story = {
  args: {},
};
