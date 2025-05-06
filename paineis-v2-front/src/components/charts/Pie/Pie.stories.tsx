import type { Meta, StoryObj } from '@storybook/react';
import { Pie } from './index';

const meta = {
  title: 'Charts/Pie',
  component: Pie,
  parameters: {
  },
  tags: ['autodocs'],
  argTypes: {
  },
  args: { 
},
} satisfies Meta<typeof Pie>;

export default meta;
type Story = StoryObj<typeof meta>;


export const Primary: Story = {
  args: {
    data: [
      {
        tag: "urbana",
        value: 81,
      },
      {
        tag: "rural",
        value: 19,
      },
    ]
  },
};