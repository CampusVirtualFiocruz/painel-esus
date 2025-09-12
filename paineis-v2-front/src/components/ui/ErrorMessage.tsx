import React from 'react';

interface ErrorMessageProps {
  error: any;
  title?: string;
  className?: string;
  showRetry?: boolean;
  onRetry?: () => void;
}

const ErrorMessage: React.FC<ErrorMessageProps> = ({
  error,
  title = 'Erro ao carregar dados',
  className = '',
  showRetry = false,
  onRetry,
}) => {
  const getErrorMessage = (error: any): string => {
    if (typeof error === 'string') {
      return error;
    }

    if (error?.message) {
      return error.message;
    }

    if (error?.response?.data?.message) {
      return error.response.data.message;
    }

    if (error?.response?.status) {
      return `Erro ${error.response.status}: ${error.response.statusText || 'Erro desconhecido'}`;
    }

    return 'Erro desconhecido';
  };

  return (
    <div
      style={{
        textAlign: 'center',
        padding: '20px',
        color: '#dc3545',
        backgroundColor: '#f8d7da',
        border: '1px solid #f5c6cb',
        borderRadius: '4px',
        margin: '10px 0',
      }}
      className={className}
    >
      <div style={{ fontWeight: 'bold', marginBottom: '8px' }}>{title}</div>
      <div style={{ fontSize: '14px', marginBottom: showRetry ? '12px' : '0' }}>
        {getErrorMessage(error)}
      </div>
      {showRetry && onRetry && (
        <button
          onClick={onRetry}
          style={{
            backgroundColor: '#dc3545',
            color: 'white',
            border: 'none',
            padding: '8px 16px',
            borderRadius: '4px',
            cursor: 'pointer',
            fontSize: '14px',
          }}
          onMouseOver={e => {
            e.currentTarget.style.backgroundColor = '#c82333';
          }}
          onMouseOut={e => {
            e.currentTarget.style.backgroundColor = '#dc3545';
          }}
        >
          Tentar Novamente
        </button>
      )}
    </div>
  );
};

export default ErrorMessage;
