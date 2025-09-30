import { themes as prismThemes } from "prism-react-renderer";
import type { Config } from "@docusaurus/types";
import type * as Preset from "@docusaurus/preset-classic";

const config: Config = {
  title: "Painel e-SUS APS",
  tagline: "Ferramenta estratégica para aprimorar a gestão da informação, da clínica e do cuidado na APS em nível municipal",
  favicon: "img/favicon.svg",

  // Set the production url of your site here
  url: "https://campusvirtualfiocruz.github.io/",
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: "/painel-esus/",

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: "campusvirtualfiocruz", // Usually your GitHub org/user name.
  projectName: "painel-esus", // Usually your repo name.
  trailingSlash: false,

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: "pt-BR",
    locales: ["pt-BR"],
  },

  presets: [
    [
      "classic",
      {
        docs: {
          sidebarPath: "./sidebars.ts"
        },
        blog: {
          showReadingTime: true,
        },
        theme: {
          customCss: "./src/css/custom.css",
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: "img/painel-social-card.jpg",
    navbar: {
      title: "Painel e-SUS APS",
      logo: {
        alt: "Painel e-SUS APS",
        src: "img/logo.svg",
      },
      items: [
        {
          type: "docSidebar",
          sidebarId: "tutorialSidebar",
          position: "left",
          label: "Documentação",
        },
        {
          href: "https://sisaps.saude.gov.br/sistemas/painelesusaps/",
          label: "Download",
          position: "right",
        },
        {
          href: "https://github.com/CampusVirtualFiocruz/painel-esus",
          label: "GitHub",
          position: "right",
        },
      ],
    },
    footer: {
      style: "dark",
      links: [
        {
          title: "Midiateca",
          items: [
            {
              label: "Manual de Instalação",
              href: "https://sisaps.saude.gov.br/sistemas/painelesusaps/docs/manuais/manual_instalacao/",
            },
            {
              label: "Manual de Uso",
              href: "https://sisaps.saude.gov.br/sistemas/painelesusaps/docs/manuais/manual_uso/",
            },
            {
              label: "Educa e-SUS APS",
              href: "https://educaesusaps.medicina.ufmg.br/",
            },
          ],
        },
        {
          title: "Créditos",
          items: [
            {
              label: "Apoio",
              href: "https://github.com/CampusVirtualFiocruz/painel-esus?tab=readme-ov-file#cr%C3%A9ditos",
            },
            {
              label: "Equipe",
              href: "https://github.com/CampusVirtualFiocruz/painel-esus?tab=readme-ov-file#equipe",
            },
          ],
        },
        {
          title: "Licença de Uso",
          items: [
            {
              label: "GPL 2.0",
              href: "https://www.gnu.org/licenses/old-licenses/gpl-2.0.html",
            },
          ],
        },
        {
          title: "Reconhecimentos",
          items: [
            {
              label: "MIT Solve 2022",
              href: "https://solve.mit.edu/solutions/63515",
            },
          ],
        }
      ],
      copyright: `Copyright © 2020 - ${new Date().getFullYear()} Fundação Oswaldo Cruz - Fiocruz.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
