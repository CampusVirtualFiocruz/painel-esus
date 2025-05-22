import type { Preview } from "@storybook/react";
import { initialize, mswLoader } from 'msw-storybook-addon';

import "bootstrap/dist/css/bootstrap.min.css";
import "../src/styles/global.scss";
import "../src/pages/SaudeBucal/desfecho/style.scss";

initialize();

const preview: Preview = {
  loaders: [mswLoader],
  parameters: {
    controls: {
      matchers: {
        color: /(background|color)$/i,
        date: /Date$/i,
      },
    },
  },
};

export default preview;
