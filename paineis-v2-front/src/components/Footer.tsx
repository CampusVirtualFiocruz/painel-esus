import { memo } from 'react';
import FooterImage from '../assets/images/ReguaLogosPainel.png';
import '../styles/footer.scss';

export function Footer() {
  return (
    <footer id='footer'>
      <div className='grid-sponsors'>
        <img
          src={FooterImage}
          className='img-fluid'
          alt='Rodapé com logomarca da Fiocruz'
          style={{ width: '100%', maxWidth: '870px' }}
        />
      </div>
      <div className='version'>
        <div>Versão {process.env.REACT_APP_VERSION}</div>
        <br />
        <div>
          <small>Última atualização: {process.env.REACT_APP_LAST_UPDATE}</small>
        </div>
      </div>
    </footer>
  );
}

export const MemoizedFooter = memo(Footer);
