import useScript from "../hooks/useScript";

const BarraBrasil = () => {
  useScript("//barra.brasil.gov.br/barra_2.0.js");

  return <div id="barra-brasil" />;
};

export default BarraBrasil;
