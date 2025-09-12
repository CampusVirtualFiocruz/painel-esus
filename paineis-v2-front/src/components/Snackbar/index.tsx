import React, { ReactNode } from 'react';
import '../../styles/snackbar.scss';

interface ISnackbar {
  type: string;
  open: boolean;
  children: ReactNode;
  onClose: () => void;
}

export function Snackbar({ type, open, children, onClose }: ISnackbar) {
  return (
    <div className={`snackbar ${open && 'visible'} ${type}`}>
      <span>{children}</span>
      <button className='close' onClick={onClose}>
        &times;
      </button>
    </div>
  );
}
