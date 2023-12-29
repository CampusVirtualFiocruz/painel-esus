import { memo } from 'react';
import '../styles/footer.scss';

//import fiocruzImg from '../assets/images/logo_fiocruz.svg';
//import susImg from '../assets/images/SUS.svg';
//import msGovernoImg from '../assets/images/ms_governo.svg';

export function Footer() {
    return (
        <footer id='footer'>
            <div className="grid-sponsors">
                {/* <img src={'https://paineis-esus-bucket-new.s3.sa-east-1.amazonaws.com/footer-resize2.jpg'} className="img-fluid" alt="Fiocruz" style={{maxWidth: '100%'}}/> */}
                <img src={'https://www.rondonia.fiocruz.br/wp-content/uploads/2022/01/fiocruz.png'} className="img-fluid" alt="Fiocruz" style={{ maxWidth: '170px' }} />
                <img src={'https://logodownload.org/wp-content/uploads/2017/02/sus-logo-0.png'} className="img-fluid" alt="Fiocruz" style={{ maxWidth: '170px' }} />
                <img src={'https://www.gov.br/secom/pt-br/central-de-conteudo/manuais/uso-da-marca-do-governo-federal/2023_br_govfederal_marcaoficial_rgb.png/@@images/image'} className="img-fluid" alt="Fiocruz" style={{ maxWidth: '170px' }} />
            </div>
            <div className="version">
                <div>Versão {process.env.REACT_APP_VERSION}</div>
                <br />
                <div><small>Última atualização: {process.env.REACT_APP_LAST_UPDATE}</small></div>
            </div>
        </footer>
    )
}

export const MemoizedFooter = memo(Footer);
