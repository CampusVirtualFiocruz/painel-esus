import type { Meta, StoryObj } from "@storybook/react";
import { Donut } from "./index";

const meta = {
  title: "Charts/Donut",
  component: Donut,
  parameters: {},
  tags: ["autodocs"],
  argTypes: {},
  args: {},
} satisfies Meta<typeof Donut>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Basic: Story = {
  args: {
    data: [
      {
        tag: "urbano",
        value: 81,
      },
      {
        tag: "nao-informado",
        value: 20,
      },
      {
        tag: "rural",
        value: 19,
      },
    ],
    config: {
      formatterKind: "perc",
      colors: ["#0069d0", "#84aaff", "#e4e4e4", "#5c7ea0"],
    },
  },
};

export const Pizza: Story = {
  args: {
    data: [
      {
        tag: "urbano",
        value: 81,
      },
      {
        tag: "nao-informado",
        value: 20,
      },
      {
        tag: "rural",
        value: 19,
      },
    ],
    config: {
      formatterKind: "perc",
      radiusStart: "0%",
      colors: ["#0069d0", "#84aaff", "#e4e4e4", "#5c7ea0"],
    },
  },
};
