import { create } from "@storybook/theming";
import logo from "../src/assets/images/logo.svg";

export default create({
  base: "dark",
  brandTitle: "Painel e-SUS APS - Fiocruz",
  brandUrl: "https://www.fiocruz.br/",
  brandImage: logo,
  brandTarget: "_self",
});
