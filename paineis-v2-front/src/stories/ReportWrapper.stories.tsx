import React from 'react';
import { Meta } from '@storybook/react';
import { MemoryRouter, Route, Routes } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from 'react-query';
import ReportWrapper from '../components/ui/ReportWrapper';

const InfoContext = React.createContext({ city: 'Cidade Teste' });

const queryClient = new QueryClient();

export default {
  title: 'Components/ReportWrapper',
  component: ReportWrapper,
  decorators: [
    (Story) => (
      <QueryClientProvider client={queryClient}>
        <InfoContext.Provider value={{ city: 'Cidade Teste' }}>
          <MemoryRouter initialEntries={['/painel/1?equipe=1']}>
            <Routes>
              <Route path="/painel/:id" element={<Story />} />
            </Routes>
          </MemoryRouter>
        </InfoContext.Provider>
      </QueryClientProvider>
    ),
  ],
} as Meta;

const Template = (args: any) => (
  <ReportWrapper {...args}>
    <div>Conteúdo do relatório</div>
  </ReportWrapper>
);

export const Default = Template.bind({});
(Default as any).args = {
  title: 'Título do Relatório',
  subtitle: 'Subtítulo do Relatório',
  footerNote: 'Nota de rodapé',
};

export const WithoutSubtitle = Template.bind({});
(WithoutSubtitle as any).args = {
  title: 'Título do Relatório',
  footerNote: 'Nota de rodapé',
};