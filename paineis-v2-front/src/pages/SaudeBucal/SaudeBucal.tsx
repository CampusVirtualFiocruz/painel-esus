import * as React from 'react';
import { Header } from '../../components/Header';
import AtendimentoLinhaCuidado from './atendimentos-linha-cuidado/AtendimentoLinhaCuidado';
import TotalAtendimentos from './total-atendimentos/TotalAtendimentos';
import TipoConsulta from './tipo-consulta/TipoConsulta';
import Exodontia from './exodontia/Exodontia';
import FaixaEtaria from './faixa-etaria/FaixaEtaria';
import Sexo from './sexo/Sexo';
import LocalAtendimento from './local-atendimento/LocalAtendimento';
import Desfecho from './desfecho/Desfecho';
import './style.scss'
const SaudeBucal = () => {
    return (
        <div id="page-painel">
            <Header />
            <div className="contentWrapper">
                <hr className="linha my-4" />
                <h1>Painel Saúde Bucal <small>(Últimos 12 meses)</small></h1>
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


            </div>
        </div>
    );
}

export default SaudeBucal;