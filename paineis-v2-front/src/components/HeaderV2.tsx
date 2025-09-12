import { memo, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Dropdown, DropdownDivider, DropdownItem, Icon } from 'bold-ui';

import { useAuth } from '../context/AuthProvider/useAuth';
import { getUserLocalStorage } from '../context/AuthProvider/util';
import '../styles/header.scss';

import imgLogo from '../assets/images/logo.svg';

import { getFirstName, profiles } from '../utils';
import { useInfo } from '../context/infoProvider/useInfo';
import { Modal } from '../components/Modal';

export function Header() {
  const { logout } = useAuth();
  const user = getUserLocalStorage();
  const navigate = useNavigate();

  const [showModal, setShowModal] = useState(false);
  const [data, setData] = useState<any>({ loaded: 8 });
  const [profile, setProfile] = useState(profiles[0]);

  const handleProfileSelect = () => {
    setData({ loaded: 8 });
    setShowModal(true);
  };

  function handleHome() {
    navigate('/selecionarubs');
  }

  function handleVizSelect() {
    navigate('/selecionarvisualizacao');
  }

  function handleLogout() {
    logout();
    navigate('/');
  }

  const infoContext = useInfo();
  const city = infoContext.cityInformation;

  const [linkRef, setlinkRef] = useState<HTMLDivElement | null>(null);
  const [open, setOpen] = useState(false);

  const handleClick = () => setOpen(true);
  const handleClose = () => setOpen(false);

  return (
    <>
      {showModal && (
        <Modal
          data={data}
          setShowModal={setShowModal}
          setProfile={setProfile}
          initialProfile={profile}
        />
      )}
      <header id='header'>
        <div className='siteInfo'>
          <div className='logoName' onClick={handleHome}>
            <img src={imgLogo} alt='e-SUS' />
            <strong>
              PAINEL e-SUS APS /{' '}
              <span>
                {city?.municipio} - {city?.uf}
              </span>
            </strong>
          </div>
        </div>
        <div className='userInfo'>
          <Icon
            icon='userFilled'
            style={{ marginRight: '10px', color: '#ffffff' }}
          />
          <div className='container-info'>
            <span className='info-name'>{getFirstName(user?.fullName)}</span>
            <span className='info-perfil'>{profile}</span>
          </div>
          <div
            ref={setlinkRef}
            onClick={handleClick}
            style={{
              cursor: 'pointer',
            }}
          >
            <Icon
              icon='angleDown'
              style={{
                width: '18px',
                marginLeft: '15px',
                marginRight: '1rem',
                color: '#ffffff',
              }}
            />
          </div>
          <Dropdown anchorRef={linkRef} open={open} onClose={handleClose}>
            <DropdownItem onClick={handleProfileSelect}>
              <Icon
                icon='userFilled'
                style={{ width: '18px', marginRight: '10px', color: '#343131' }}
              />
              Trocar de Perfil
            </DropdownItem>
            <DropdownDivider />
            <DropdownItem onClick={handleVizSelect}>
              <Icon
                icon='houseFilled'
                style={{ width: '18px', marginRight: '10px', color: '#343131' }}
              />
              Trocar Visualização
            </DropdownItem>
            <DropdownDivider />
            <DropdownItem onClick={handleLogout}>
              <Icon
                icon='signOut'
                style={{
                  width: '24px',
                  marginLeft: '-5px',
                  marginRight: '10px',
                  color: '#343131',
                }}
              />
              Sair
            </DropdownItem>
          </Dropdown>
        </div>
      </header>
    </>
  );
}

export const MemoizedHeader = memo(Header);
