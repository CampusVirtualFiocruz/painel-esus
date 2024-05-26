import { HTMLProps, ReactNode } from "react";
import { useNavigate } from "react-router-dom";
import { Header } from "../Header";
import { Footer } from "../Footer";

const ReportWrapper = ({
  title,
  children,
  ...props
}: {
  title: string;
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
        <h1 style={{ textAlign: "center", marginTop: "60px" }}>{title}</h1>
        {children}
        <div className="container">
          <div className="row justify-content-center mb-2">
            <div className="col-12 col-md-8 containerButtons d-flex justify-content-center my-5">
              <button
                type="button"
                onClick={() => {
                  navigate(-1);
                }}
                className="btn btn-light me-5"
              >
                Voltar
              </button>
            </div>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default ReportWrapper;
