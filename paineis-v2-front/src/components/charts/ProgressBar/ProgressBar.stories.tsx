import type { Meta, StoryObj } from '@storybook/react';
import { ProgressBar } from './index';

const meta = {
  title: 'Charts/Progress Bar',
  component: ProgressBar,
  parameters: {
  },
  tags: ['autodocs'],
  argTypes: {
  },
  args: { 
},
} satisfies Meta<typeof ProgressBar>;

export default meta;
type Story = StoryObj<typeof meta>;


export const Primary: Story = {
  args: {
    data: [
      { tag: "Assistente Social", value: 0.1 },
      { tag: "Cirurgião Dentista", value: 2 },
      { tag: "Enfermeiro", value: 35 },
      { tag: "Farmacêutico", value: 0 },
      { tag: "Fisioterapeuta", value: 0 },
      { tag: "Fonoaudiólogo", value: 0 },
      { tag: "Médico", value: 68.42 },
      { tag: "Nutricionista", value: 12 },
      { tag: "Professor da Educação Física", value: 0 },
      { tag: "Psicólogo", value: 0 },
      { tag: "Terapeuta Ocupacional", value: 0 },
      { tag: "Outros", value: 5 },
    ],
  },
};