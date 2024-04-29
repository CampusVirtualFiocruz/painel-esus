import * as React from 'react';
import { Header } from '../components/Header';
import { Footer } from '../components/Footer';
import "../styles/diabetesHipertensao.scss";
const RelatoriosQualidadeInformacao = () => {

    function handleToPainelMunicipio() {
        window.location.href="/painelx";
    }

  return (
    <div id="page-painel">
        <Header />
        <div className="contentWrapper">
            <hr className="linha my-4" />
            <h2>Relatório de qualidade da Informação</h2>
            <div className="container container-cards-principal">
                <div className="row align-items-start">
                    <div className="col-12">
                        <ul>
                            <li><a className="relatorio-link" href="./Painel/P10.html" target='_blank'>Boas práticas na APS - Indicador P10 - Ferida Vascular</a></li>
                            <li><a className="relatorio-link" href="./Painel/P11.html" target='_blank'>Boas práticas na APS - Indicador P11 - Tuberculose</a></li>
                            <li><a className="relatorio-link" href="./Painel/P12.html" target='_blank'>Boas práticas na APS - Indicador P12 - Hanseníase</a></li>
                            <li><a className="relatorio-link" href="./Painel/P13.html" target='_blank'>Boas práticas na APS - Indicador P13 - Tabagismo</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div className="container container-cards-principal">
                <div className="row align-items-start">
                    <div className="col-12">
                        <button
                                type="button"
                                onClick={handleToPainelMunicipio}
                                className="btn btn-primary my-4">
                                Visualizar dados do painel do Município
                            </button>
                    </div>
                </div>
            </div>
        </div>
        <Footer />
    </div>
  )
}

export default RelatoriosQualidadeInformacao
