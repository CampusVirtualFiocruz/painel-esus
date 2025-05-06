import type { Meta, StoryObj } from '@storybook/react';
import { Bar } from './index';

const meta = {
  title: 'Charts/Bar',
  component: Bar,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {
  },
  args: { 
},
} satisfies Meta<typeof Bar>;

export default meta;
type Story = StoryObj<typeof meta>;


export const Primary: Story = {
  args: {
    data: [
        {
          tag: "1-meses",
          value: {
            "urbana": 10,
            "rural": 20,
          },
        },
        {
          tag: "2-meses",
          value: {
            "urbana": 20,
            "rural": 30,
          },
        },
        {
          tag: "9-meses",
          value: {
            "urbana": 60,
            "rural": 80,
          },
        },
      ]
  },
};