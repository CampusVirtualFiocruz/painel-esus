import * as React from 'react';
import { Header } from '../../components/Header';
import AtendimentoLinhaCuidado from './atendimentos-linha-cuidado/AtendimentoLinhaCuidado';
import TotalAtendimentos from './total-atendimentos/TotalAtendimentos';
import TipoConsulta from './tipo-consulta/TipoConsulta';
import Exodontia from './exodontia/Exodontia';
import FaixaEtaria, { PainelParams } from './faixa-etaria/FaixaEtaria';
import Sexo from './sexo/Sexo';
import LocalAtendimento from './local-atendimento/LocalAtendimento';
import Desfecho from './desfecho/Desfecho';
import './style.scss'
import { Api } from "../../services/api";
import { useQuery } from 'react-query';
import { getNomeUbs } from '../../utils';
import { useParams } from 'react-router';
import { getUserLocalStorage } from '../../context/AuthProvider/util';
import { Footer } from '../../components/Footer';
import { useInfo } from '../../context/infoProvider/useInfo';

type TypeUbs = {
    label: string;
    value: number | string;
    id: string;
};
type Lista = {
    co_dim_unidade_saude_1: number;
    no_unidade_saude: string;
    nu_cnes: number;
}

type ResponseDataListUbs = {
    data: Lista[];
}

const SaudeBucal = () => {
    const { id } = useParams<PainelParams>();
    const user = getUserLocalStorage();
     const { cityInformation, city } = useInfo();

    const { data: dataUbs, isLoading: isLoadingUbs } = useQuery('ubs', async () => {
        const response = await Api.get<ResponseDataListUbs>('get-units')
        const data = response.data

        const listData: TypeUbs[] = data.data.map((ubs: any) => {
            return {
                "label": ubs.no_unidade_saude,
                "value": ubs.nu_cnes,
                "id": ubs.co_seq_dim_unidade_saude
            }
        })

        return listData
    }, {
        staleTime: 1000 * 60 * 10, //10 minutos
    });

    const nomeUbs = !isLoadingUbs && id ? getNomeUbs(dataUbs, id) : city;
    function handleToPainelUbs() {
        window.location.href=`/painel/${id}`;
    }

    function handleToPainelMunicipio() {
        window.location.href="/painelx";
    }
    return (
        <div id="page-painel">
            <Header />
            <div className="contentWrapper">
                <hr className="linha my-4" />
                <h2 style={{textAlign: 'center'}}>{id ? (!isLoadingUbs ? nomeUbs : 'Carregando...') : nomeUbs} / <br />Painel Saúde Bucal <small>(Últimos 12 meses)</small></h2>
                <div className="container-fluid">
                    <div className="row gx-5" style={{ justifyContent: 'center', padding: '50px 0' }}>
                        <div className="col-12 col-lg-5">
                            <TotalAtendimentos></TotalAtendimentos>
                        </div>
                        <div className="col-12 col-lg-5">
                            <AtendimentoLinhaCuidado></AtendimentoLinhaCuidado>
                        </div>
                    </div>
                </div>

                <div className="container-fluid">
                    <div className="row gx-5" style={{ justifyContent: 'center', padding: '50px 0' }}>
                        <div className="col-12 col-lg-5">
                            <TipoConsulta></TipoConsulta>
                        </div>
                        <div className="col-12 col-lg-5">
                            <Exodontia></Exodontia>
                        </div>
                    </div>
                </div>

                <div className="container-fluid">
                    <div className="row gx-5" style={{ justifyContent: 'center', padding: '50px 0' }}>
                        <div className="col-12 col-lg-5">
                            <FaixaEtaria></FaixaEtaria>
                        </div>
                        <div className="col-12 col-lg-5">
                            <Sexo></Sexo>
                        </div>
                    </div>
                </div>

                <div className="container-fluid">
                    <div className="row gx-5" style={{ justifyContent: 'center', padding: '50px 0' }}>
                        <div className="col-12 col-lg-5">
                            <Desfecho></Desfecho>
                        </div>
                        <div className="col-12 col-lg-5">
                            <LocalAtendimento></LocalAtendimento>
                        </div>
                    </div>
                </div>


            <div className="d-flex flex-column align-items-center mt-5">
                    {id &&
                        <button
                            type="button"
                            onClick={handleToPainelUbs}
                            className="btn btn-light my-2">
                            Voltar para o Painel da UBS
                        </button>
                    }

                    <button
                        type="button"
                        onClick={handleToPainelMunicipio}
                        className="btn btn-primary my-4">
                        Visualizar dados do painel do Município
                    </button>
                </div>
            </div>
            <Footer/>
        </div>
    );
}

export default SaudeBucal;
