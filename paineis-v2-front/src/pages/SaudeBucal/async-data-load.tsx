import * as React from "react";
import { Alert, Spinner } from "reactstrap";

type AsyncDataLoadProps = {
  isLoading: boolean;
  error?: unknown | boolean | undefined;
  children: React.ReactNode;
};
const AsyncDataLoad = ({ isLoading, error, children }: AsyncDataLoadProps) =>
  isLoading ? (
    <div className="d-flex align-items-center justify-content-center">
      <Spinner size="sm" type="grow" className="me-2" />
      Carregando...
    </div>
  ) : error ? (
    <div className="d-flex align-items-center justify-content-center">
      <Alert color="danger">Erro ao carregar dados.</Alert>
    </div>
  ) : (
    children
  );

export default AsyncDataLoad;
