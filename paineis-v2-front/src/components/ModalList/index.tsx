import { useRef, useState } from "react";
import { useQuery } from "react-query";
import ReactDom from "react-dom";
import { CgClose } from "react-icons/cg";
import { Alert, Spinner } from "reactstrap";

import './style.scss';
import { Api } from "../../services/api";
import Pagination from "../Pagination";

import { useNavigate } from "react-router-dom";

interface IModal {
    params: {
        loaded: number;
        tipo?: string;
        cnes?: string | undefined;
    }
    setShowModalList: (status: boolean) => void;
}

type IParams = {
    cns: string | undefined;
    nome: string | undefined;
    co_fat_cidadao_pec: number;
}

/* MODAL DE GESTANTES */
export const ModalList = ({ params, setShowModalList }: IModal) => {
    let navigate = useNavigate();

    // close the modal when clicking outside the modal.
    const modalListRef = useRef<HTMLDivElement | null>(null);

    const closeModal = (e: any) => {
        if (e.target === modalListRef.current) {
            setShowModalList(false);
        }
    };

    let titulo = ''

    if (params.tipo === "semana") {
        switch (params.loaded) {
            case 1:
                titulo = 'Gestantes entre 1 a 12 semanas:';
                break;
            case 2:
                titulo = 'Gestantes entre 13 a 16 semanas:';
                break;
            case 3:
                titulo = 'Gestantes entre 17 a 20 semanas:';
                break;
            case 4:
                titulo = 'Gestantes entre 21 a 24 semanas:';
                break;
            case 5:
                titulo = 'Gestantes entre 25 a 28 semanas:';
                break;
            case 6:
                titulo = 'Gestantes entre 29 a 32 semanas:';
                break;
            case 7:
                titulo = 'Gestantes entre 33 a 36 semanas:';
                break;
            case 8:
                titulo = 'Gestantes entre 37 a 41 semanas:';
                break;
            default:
                titulo = ''
        }
    }

    if (params.tipo === "trimestre") {
        titulo = `Gestantes no ${params.loaded}º trimestre:`;
    }

    let pageSize = 10
    let queryName = params.cnes ? `gestantes-${params.tipo}-ubs-${params.cnes}` : `gestantes-${params.tipo}-municipio`
    let path = ''

    const [currentPage, setCurrentPage] = useState<any>(1)
    const { isLoading, isFetching, error, data } = useQuery(
        [queryName, `${params.loaded}-${params.tipo}`, currentPage], async () => {

            if (params.tipo === "trimestre") {
                path = params.cnes
                    ? `pregnants/per-trimester/${params.loaded}/${params.cnes}?page=${currentPage}`
                    : `pregnants/per-trimester/${params.loaded}?page=${currentPage}`;
            }

            if (params.tipo === "semana") {
                path = params.cnes
                    ? `pregnants/per-weekly-range/${params.loaded}/${params.cnes}?page=${currentPage}`
                    : `pregnants/per-weekly-range/${params.loaded}?page=${currentPage}`;
            }

            const response = await Api.get(path)
            const { data, total }: any = response.data

            return { "gestantes": data, "total": total }
        },
        {
            keepPreviousData: true,
            cacheTime: 600000
        }
    )

    function handleToGestante(gestante: IParams) {
        navigate(`/gestante/${gestante.co_fat_cidadao_pec}`);
    }

    // render the modal JSX in the portal div.
    return ReactDom.createPortal(
        <div className="container-modal-list" ref={modalListRef} onClick={closeModal}>
            <div className="modal d-flex flex-column px-5 py-2">
                <hr className="separador mb-3" />

                <div className="d-flex flex-column w-100">
                    <div className="d-flex align-items-baseline">
                        <h1 className="mb-4">{titulo} </h1>{!isLoading && isFetching && <div className="barsLoading">
                            <span></span>
                            <span></span>
                            <span></span>
                            <span></span>
                        </div>}
                    </div>

                    {isLoading
                        ? (
                            <div className="d-flex align-items-center justify-content-center" style={{ height: '290px', maxHeight: '100%' }}>
                                <Spinner className="me-2" /> Carregando...
                            </div>
                        ) : error ? (
                            <div className="d-flex align-items-center justify-content-center" style={{ height: '290px', maxHeight: '100%' }}>
                                <Alert color="danger">
                                    Erro ao carregar dados.
                                </Alert>
                            </div>
                        ) : (
                            <>
                                <div style={{ height: '290px', maxHeight: '100%' }}>
                                    <ul className="grid-list">
                                        {data?.gestantes.map((gestante: IParams, i: number) => {
                                            return (
                                                <li onClick={() => handleToGestante(gestante)} className="mb-3" key={i}>
                                                    {gestante.nome ? gestante.nome : 'NOME NÃO CADASTRADO'}
                                                </li>
                                            )
                                        })}
                                    </ul>
                                </div>

                                <Pagination
                                    className="pagination-bar"
                                    currentPage={currentPage}
                                    totalCount={data?.total}
                                    pageSize={pageSize}
                                    onPageChange={page => setCurrentPage(page)}
                                />
                            </>
                        )}
                </div>

                <CgClose size={'1.5rem'} onClick={() => setShowModalList(false)} className="closeButton" />
            </div>
        </div>,
        document.getElementById("modal")!
    );
};
