import type { Meta, StoryObj } from '@storybook/react';
import { ValueCard } from './index';

const meta = {
  title: 'Charts/ValueCard',
  component: ValueCard,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {
  },
  args: { 
},
} satisfies Meta<typeof ValueCard>;

export default meta;
type Story = StoryObj<typeof meta>;


export const Primary: Story = {
  args: {
      data: 523,
      config: {
        description: "Total de crianças até 2 anos cadastradas",
        icon: "paperdark",
      },
  },
};