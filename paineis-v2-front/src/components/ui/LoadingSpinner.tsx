import React from 'react';

interface LoadingSpinnerProps {
  size?: 'sm' | 'md' | 'lg';
  text?: string;
  className?: string;
}

const LoadingSpinner: React.FC<LoadingSpinnerProps> = ({
  size = 'md',
  text = 'Carregando...',
  className = ''
}) => {
  const sizeClasses = {
    sm: 'spinner-border-sm',
    md: '',
    lg: 'spinner-border-lg'
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }} className={className}>
      <div className={`spinner-border ${sizeClasses[size]}`} role="status">
        <span className="visually-hidden">{text}</span>
      </div>
      {text && (
        <div style={{ marginTop: "10px", fontSize: "14px", color: "#666" }}>
          {text}
        </div>
      )}
    </div>
  );
};

export default LoadingSpinner;
