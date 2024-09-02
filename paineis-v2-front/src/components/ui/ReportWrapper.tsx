import { HTMLProps, ReactNode } from "react";
import { useNavigate } from "react-router-dom";
import { Header } from "../Header";
import { Footer } from "../Footer";
import { Button } from "bold-ui";

const ReportWrapper = ({
  title,
  subtitle,
  children,
  ...props
}: {
  title: string;
  subtitle?: string;
  children: ReactNode;
} & HTMLProps<HTMLDivElement>) => {
  const navigate = useNavigate();

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
      <Header />
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
            {title}
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
        <div className="container" style={{ marginTop: "20px" }}>
          <div className="row justify-content-center">{children}</div>
        </div>
        <div className="container">
          <div className="row justify-content-center mb-2">
            <div className="col-12 col-md-8 containerButtons d-flex justify-content-center my-5">
              <Button
                type="button"
                kind="primary"
                onClick={() => {
                  navigate(-1);
                }}
              >
                Voltar
              </Button>
            </div>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default ReportWrapper;
