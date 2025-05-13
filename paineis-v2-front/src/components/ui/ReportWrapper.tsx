import { HTMLProps, ReactNode } from "react";
import { Header } from "../HeaderNew";
import { Footer } from "../Footer";
import { getNomeUbs } from "../../utils";
import { useInfo } from "../../context/infoProvider/useInfo";
import { useQuery } from "react-query";
import { Api } from "../../services/api";
import { useNavigate, useParams, useSearchParams } from "react-router-dom";
import { PainelParams } from "./ReportFooter";
import { useAuth } from "../../context/AuthProvider/useAuth";
import { getUserLocalStorage } from "../../context/AuthProvider/util";

type Lista = {
  nome_equipe: string;
  codigo_equipe: number;
};

type ResponseData = {
  data: Lista[];
};

type TypeUbs = {
  label: string;
  value: number | string;
  nome_equipe: string;
  codigo_equipe: number;
};

const ReportWrapper = ({
  title,
  subtitle,
  children,
  header,
  footer,
  footerNote,
  ...props
}: {
  title: string;
  subtitle?: string;
  header?: ReactNode;
  footer?: ReactNode;
  children: ReactNode;
  footerNote?: string;
} & HTMLProps<HTMLDivElement>) => {
  const { id } = useParams<PainelParams>();
  const infoContext = useInfo();
  console.log(infoContext);
  const { logout } = useAuth();
  const user = getUserLocalStorage();
  let navigate = useNavigate();

  const [params] = useSearchParams();
  const equipe = params.get("equipe");

  const { data: dataUbs, isLoading: isLoadingUbs } = useQuery(
    "ubs",
    async () => {
      const response = await Api.get<any>("get-units");
      const data = response.data;

      const listData: any[] = data.data.map((ubs: any) => {
        return {
          label: ubs.no_unidade_saude,
          value: ubs.co_seq_dim_unidade_saude,
          id: ubs.co_seq_dim_unidade_saude,
          qtd: ubs.qtd,
        };
      });

      return listData;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const { data: teamsData, isLoading: isLoadingTeam } = useQuery(
    "get-teams/" + id,
    async () => {
      const response = await Api.get<ResponseData>("get-teams/" + id);
      const data = response.data;
      const listData: TypeUbs[] = data.data.map((i: any) => {
        return {
          ...i,
          label: i.nome_equipe + " (" + i.codigo_equipe + ")",
          value: i.codigo_equipe,
        };
      });

      return listData;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const nomeUbs = !isLoadingUbs && id ? getNomeUbs(dataUbs, id) : infoContext?.city;
  const prefix = (() => {
    if (equipe) {
      return equipe
        ? !isLoadingTeam && teamsData
          ? teamsData.find((t) => String(t?.codigo_equipe) === String(equipe))
              ?.nome_equipe
          : "Carregando nome equipe..."
        : equipe;
    }

    return id ? (!isLoadingUbs ? nomeUbs : "Carregando nome UBS...") : nomeUbs;
  })();

  const titleWithDetails = `${prefix ? prefix + "/" : ""} ${title}`;

  return (
    <div
      style={{
        display: "flex",
        flex: 1,
        flexDirection: "column",
        minHeight: "100vh",
      }}
      {...props}
    >
      <Header logout={logout} user={user} navigate={navigate} infoContext={infoContext} />
      <div
        style={{
          flex: 1,
          color: "#24252E",
          backgroundColor: "white",
        }}
      >
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <div
            style={{
              marginTop: "50px",
              display: "block",
              width: "40px",
              height: "4px",
              backgroundColor: "black",
              content: " ",
            }}
          />
          <h1
            style={{
              display: "inline-block",
              textAlign: "center",
              marginTop: "20px",
              fontWeight: "bold",
              marginRight: "10px",
            }}
          >
            {titleWithDetails}
          </h1>
          {Boolean(subtitle) && (
            <p
              style={{
                display: "inline-block",
              }}
            >
              {subtitle}
            </p>
          )}
        </div>
        <div style={{ width: "100%" }}>{header}</div>
        <div className="container" style={{ marginTop: "20px" }}>
          <div className="row justify-content-center">{children}</div>
          {Boolean(footerNote) && (
            <div
              style={{
                backgroundColor: "#edf3f8",
                borderRadius: "10px",
                padding: "16px 20px",
                marginBottom: "26px",
              }}
            >
              {footerNote}
            </div>
          )}
        </div>
        {footer}
      </div>
      <Footer />
    </div>
  );
};

export default ReportWrapper;
