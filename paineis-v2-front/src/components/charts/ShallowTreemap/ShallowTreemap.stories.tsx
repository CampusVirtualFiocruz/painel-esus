import type { Meta, StoryObj } from '@storybook/react';
import { ShallowTreemap } from './index';

const meta = {
  title: 'Charts/Treemap',
  component: ShallowTreemap,
  parameters: {
  },
  tags: ['autodocs'],
  argTypes: {
  },
  args: { 
},
} satisfies Meta<typeof ShallowTreemap>;

export default meta;
type Story = StoryObj<typeof meta>;


export const Primary: Story = {
  args: {
    data: [
      {
        tag: 'parda',
        value: 10,
        percent: 0.1,
      },
      {
        tag: 'branca',
        value: 10,
        percent: 0.1,
      },
      {
        tag: 'preta',
        value: 10,
        percent: 0.1,
      },
      {
        tag: 'indigena',
        value: 5,
        percent: 0.05,
      },
      {
        tag: 'amarela',
        value: 60,
        percent: 0.6,
      },
    ],
  },
};