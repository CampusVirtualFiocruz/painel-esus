import * as React from 'react';
import { STALE_TIME } from '../../config/stale-time';
import { useQuery } from 'react-query';
import { Api } from '../../services/api2';
import { Alert, Spinner } from 'reactstrap';

type ReactText = string | number;
type ReactChild = React.ReactElement | ReactText;

interface ReactNodeArray extends Array<ReactNode> { }
type ReactFragment = {} | ReactNodeArray;
type ReactNode = Element | ReactChild | ReactFragment | React.ReactPortal | boolean | null | undefined;


type AsyncDataLoadProps = {
    isLoading: boolean;
    error?: unknown | boolean | undefined;
    children: ReactNode
}
const AsyncDataLoad = ({ isLoading, error, children }: AsyncDataLoadProps) => {

    return (<>
        {isLoading ? (
            <div className="d-flex align-items-center justify-content-center">
                <Spinner size="sm" type="grow" className="me-2" />
                Carregando...
            </div>
        ) : error ? (
            <div className="d-flex align-items-center justify-content-center">
                <Alert color="danger">
                    Erro ao carregar dados.
                </Alert>
            </div>
        ) : (
            children
        )}

    </>);
}

export default AsyncDataLoad;