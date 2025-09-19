import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Api } from "../services/api";
import "../styles/instalacao.scss";

interface Job {
  nome: string;
  percentual: number;
}

interface ProgressoInstalacao {
  status: string;
  percentual: number;
}

interface InstalacaoStatus {
  progresso_instalacao: ProgressoInstalacao;
  jobs: Job[];
  logs: string[];
}

export function Instalacao() {
  const navigate = useNavigate();
  const [instalacaoStatus, setInstalacaoStatus] =
    useState<InstalacaoStatus | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchInstalacaoStatus = async () => {
    try {
      setLoading(true);
      setError(null);
      const response = await Api.get("/settings/instalation-status");
      setInstalacaoStatus(response.data);
    } catch (err) {
      console.error("Erro ao buscar status da instalação:", err);
      setError("Erro ao carregar o status da instalação");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchInstalacaoStatus();
    const interval = setInterval(fetchInstalacaoStatus, 5000);

    return () => clearInterval(interval);
  }, []);

  const getProgressColor = (percentual: number) => {
    if (percentual === 0) return "#e9ecef";
    if (percentual < 50) return "#ffc107";
    if (percentual < 100) return "#17a2b8";
    return "#28a745";
  };

  if (loading && !instalacaoStatus) {
    return (
      <div className="instalacao-container">
        <div className="loading">
          <div className="spinner"></div>
          <p>Carregando status da instalação...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="instalacao-container">
        <div className="error">
          <h2>Erro</h2>
          <p>{error}</p>
          <button onClick={fetchInstalacaoStatus} className="retry-button">
            Tentar Novamente
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="instalacao-container">
      <div className="instalacao-header">
        <h1>Status da Instalação</h1>
        <button 
          className="configuracao-button"
          onClick={() => navigate('/configuracao')}
          title="Configurações do Sistema"
        >
          ⚙️ Configurações
        </button>
      </div>
      {instalacaoStatus && (
        <div className="instalacao-content">
          <div className="progress-section">
            <h2>Progresso Geral</h2>
            <div className="progress-info">
              <span className="status-text">
                {instalacaoStatus.progresso_instalacao.status}
              </span>
              <span className="percentage">
                {instalacaoStatus.progresso_instalacao.percentual}%
              </span>
            </div>
            <div className="progress-bar">
              <div
                className="progress-fill"
                style={{
                  width: `${instalacaoStatus.progresso_instalacao.percentual}%`,
                  backgroundColor: getProgressColor(
                    instalacaoStatus.progresso_instalacao.percentual
                  ),
                }}
              ></div>
            </div>
          </div>
          <div className="jobs-section">
            <h2>Tarefas</h2>
            <div className="jobs-list">
              {instalacaoStatus.jobs.map((job, index) => (
                <div key={index} className="job-item">
                  <div className="job-info">
                    <span className="job-name">{job.nome}</span>
                    <span className="job-percentage">{job.percentual}%</span>
                  </div>
                  <div className="progress-bar">
                    <div
                      className="progress-fill"
                      style={{
                        width: `${job.percentual}%`,
                        backgroundColor: getProgressColor(job.percentual),
                      }}
                    ></div>
                  </div>
                </div>
              ))}
            </div>
          </div>
          {instalacaoStatus.logs && instalacaoStatus.logs.length > 0 && (
            <div className="logs-section">
              <h2>Logs</h2>
              <div className="logs-container">
                {instalacaoStatus.logs.map((log, index) => (
                  <div key={index} className="log-entry">
                    {log}
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
