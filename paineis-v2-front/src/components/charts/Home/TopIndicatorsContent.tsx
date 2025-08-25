import { MdInfoOutline } from "react-icons/md";
import homem from "../../../assets/images/homem.svg";
import mulher from "../../../assets/images/mulher.svg";
import { Zonas } from "../../../charts/Zonas";
import { formataNumero } from "../../../utils";
import Card from "../../ui/Card";
import { Tooltip, TooltipContent, TooltipTrigger } from "../../ui/Tooltip";
import { Typography } from "../../ui/Typography";

const TopIndicatorsContent = ({ charts }: any) => {
  const CounterCard = () => (
    <div className="col-xl-3">
      <div className="container-card d-flex flex-column flex-md-row align-items-center justify-content-center my-2 py-2 px-4">
        <div className="w-50 d-flex flex-column align-items-center justify-content-center">
          <h4 className="text-center">Cidadãos Cadastrados</h4>
          <span>
            {formataNumero(
              charts?.["total-cidadaos-cadastrados"]?.data?.find(
                      ({ tag }: any) => tag === "total"
                    )?.value)}
          </span>
        </div>
        <div
          className="mx-2"
          style={{
            height: "100px",
            width: "1px",
            backgroundColor: "#FFFFFF",
          }}
        />
        <div className="w-50 d-flex flex-column align-items-center justify-content-center">
          <Tooltip>
            <TooltipContent className="Tooltip">
              <div>
                Informação extraída da Relação da População Municipal enviada ao
                TCU em 2023,
                <br /> pelo IBGE. (clique para acessar o portal do IBGE)
              </div>
            </TooltipContent>
            <a
              target="_blank"
              href="https://www.ibge.gov.br/estatisticas/sociais/populacao/37734-relacao-da-populacao-dos-municipios-para-publicacao-no-dou.html?=&t=resultados"
              rel="noreferrer"
            >
              <h4 className="text-center">
                <TooltipTrigger>
                  População Apurada&nbsp;
                  <MdInfoOutline
                    style={{
                      cursor: "pointer",
                      color: "#ffffff",
                      height: 20,
                      width: 20,
                    }}
                  />
                </TooltipTrigger>
              </h4>
            </a>
          </Tooltip>
          <span>
            {formataNumero(charts?.["total-cidadaos-cadastrados"]?.data?.find(
                      ({ tag }: any) => tag === "ibgePopulation"
                    )?.value)}
          </span>
        </div>
      </div>
    </div>
  );

  const DonutCard = () => (
    <div className="col-xl-6" style={{ overflow: "visible" }}>
      <Card
        className="container-card-alt"
        style={{ padding: 0, marginTop: "8px" }}
      >
        <div className="d-flex flex-column flex-md-row align-items-center justify-content-center my-2">
          <div className="me-2">
            <Zonas data={charts?.["tipo-localizacao"]?.data} />
          </div>
          <div>
            <Tooltip>
              <Typography.Details>
                <TooltipTrigger>
                  Tipo de localização&nbsp;
                  <MdInfoOutline
                    style={{
                      cursor: "pointer",
                      color: "#222222",
                      height: 20,
                      width: 20,
                    }}
                  />
                </TooltipTrigger>
                <TooltipContent className="Tooltip">
                  "Não informado" refere-se aos cadastros realizados em
                  <br />
                  Ficha de Cadastro Individual sem associação com uma
                  <br />
                  Ficha de Cadastro Domiciliar e Territorial.
                </TooltipContent>
              </Typography.Details>
            </Tooltip>
            <div
              className="d-flex flex-column flex-md-row align-items-center justify-content-center my-2"
              style={{ gap: "15px" }}
            >
              <div className="container-dados-zona">
                <div className="d-flex align-items-center mb-2">
                  <div className="box-container-light me-2"></div>
                  <h4>Zona Urbana</h4>
                </div>
                <span>
                  {formataNumero(
                    charts?.["tipo-localizacao"]?.data?.find(
                      ({ tag }: any) => tag === "urbano"
                    )?.value
                  )}
                </span>
              </div>
              <div className="container-dados-zona">
                <div className="d-flex align-items-center mb-2">
                  <div className="box-container-dark me-2"></div>
                  <h4>Zona Rural</h4>
                </div>
                <span>
                  {formataNumero(
                    charts?.["tipo-localizacao"]?.data?.find(
                      ({ tag }: any) => tag === "rural"
                    )?.value
                  )}
                </span>
              </div>
              <div className="container-dados-zona">
                <div className="d-flex align-items-center mb-2">
                  <div className="box-container-nonactive me-2"></div>
                  <h4>Não informado</h4>
                </div>
                <span>
                  {formataNumero(
                    charts?.["tipo-localizacao"]?.data?.find(
                      ({ tag }: any) => tag === "nao_informado"
                    )?.value
                  )}
                </span>
              </div>
            </div>
          </div>
        </div>
      </Card>
    </div>
  );

  const GenderCard = () => (
    <div className="col-xl-3">
      <div className="container-card d-flex align-items-center justify-content-center my-2 py-1">
        <div className="d-flex flex-column align-items-center ms-2 me-4">
          <img
            className="my-2 force-white"
            src={homem}
            alt="Homem"
            width={60}
          />
          <span>{formataNumero(
                    charts?.["total-por-sexo"]?.data?.find(
                      ({ tag }: any) => tag === "masculino"
                    )?.value
                  )}</span>
        </div>
        <div
          className="mx-2"
          style={{
            height: "100px",
            width: "1px",
            backgroundColor: "#FFFFFF",
          }}
        />
        <div className="d-flex flex-column align-items-center ms-4 me-2">
          <img
            className="my-2 force-white"
            src={mulher}
            alt="Mulher"
            width={60}
          />
          <span>{formataNumero(
                    charts?.["total-por-sexo"]?.data?.find(
                      ({ tag }: any) => tag === "feminino"
                    )?.value
                  )}</span>
        </div>
      </div>
    </div>
  );

  return (
    <div
      className="container container-cards-principal"
      style={{ overflow: "visible" }}
    >
      <div className="row align-items-start">
        <CounterCard />
        <DonutCard />
        <GenderCard />
      </div>
    </div>
  );
};

export default TopIndicatorsContent;
