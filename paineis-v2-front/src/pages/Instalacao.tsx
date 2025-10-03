import { useState, useEffect, useCallback } from "react";
import { useNavigate } from "react-router-dom";
import { Api } from "../services/api";
import "../styles/instalacao.scss";
import { ConfiguracaoData } from "./Configuracao";
import { Button } from "bold-ui";
import { useInstalationReady } from "../hooks/useInstalationReady";

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
  const { isReady } = useInstalationReady();
  const [instalacaoStatus, setInstalacaoStatus] =
    useState<InstalacaoStatus | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [showConfig, setShowConfig] = useState(false);

  const fetchConfiguracao = useCallback(async () => {
    try {
      setError(null);

      const response = await Api.get<ConfiguracaoData>(
        "/settings/check-instalation"
      );
      const data = response.data;
      setShowConfig(data.showSetupWizardOnLaunch);
    } catch (err: any) {
      console.error("Erro ao buscar configuração:", err);
      setError("Erro ao carregar configurações. Tente novamente.");
    }
  }, []);

  useEffect(() => {
    fetchConfiguracao();
  }, [fetchConfiguracao]);

  const fetchInstalacaoStatus = async () => {
    try {
      setError(null);
      const response = await Api.get("/settings/instalation-status");
      setInstalacaoStatus(response.data);
    } catch (err: any) {
      if (err.response.status === 403) {
        navigate("/");
        return;
      } else {
        setError("Erro ao carregar o status da instalação");
      }
    }
  };

  useEffect(() => {
    fetchInstalacaoStatus();
    const interval = setInterval(
      fetchInstalacaoStatus,
      isReady ? 10 * 1000 : 600
    );
    return () => clearInterval(interval);
  }, [isReady]);

  const getProgressColor = (percentual: number) => {
    if (percentual === 0) return "#e9ecef";
    if (percentual < 50) return "#ffc107";
    if (percentual < 100) return "#17a2b8";
    return "#28a745";
  };

  const handlePararInstalacao = async () => {
    try {
      setError(null);
      await Api.post("/settings/stop-instalation");
      navigate("/");
    } catch (err) {
      setError("Erro ao finalizar a instalação. Tente novamente.");
    }
  };

  const handleIniciarInstalacao = async () => {
    try {
      setError(null);
      await Api.get("/settings/start-instalation");
      fetchInstalacaoStatus();
    } catch (err) {
      setError("Erro ao iniciar a instalação. Tente novamente.");
    }
  };

  const handlePausarInstalacao = async () => {
    try {
      setError(null);
      await Api.get("/settings/stop-instalation");
      fetchInstalacaoStatus();
    } catch (err) {
      setError("Erro ao pausar a instalação. Tente novamente.");
    }
  };

  const isInstallationComplete =
    instalacaoStatus?.progresso_instalacao?.percentual === 100;

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
      {isReady && (
        <div
          className="success-message"
          style={{ textAlign: "center", marginBottom: "20px" }}
        >
          <div
            style={{
              backgroundColor: "#d4edda",
              color: "#155724",
              padding: "15px",
              borderRadius: "5px",
              display: "inline-block",
              width: "100%",
              margin: "0 auto",
            }}
          >
            <p style={{ margin: 0 }}>Instalação concluída com sucesso!</p>
            <button
              style={{
                marginTop: "10px",
                padding: "10px 20px",
                backgroundColor: "#28a745",
                color: "white",
                border: "none",
                borderRadius: "5px",
                cursor: "pointer",
              }}
              onClick={() => navigate("/")}
            >
              Ir para Login
            </button>
          </div>
        </div>
      )}
      <div className="instalacao-header">
        <h1>Status da Instalação</h1>
        <div className="header-buttons">
          {showConfig && (
            <Button
              kind="primary"
              size="small"
              onClick={() => navigate("/configuracao")}
              title="Configurações do Sistema"
            >
              ⚙️ Configurações
            </Button>
          )}
          {!isInstallationComplete && (
            <>
              <Button
                kind="normal"
                size="small"
                onClick={handleIniciarInstalacao}
                title="Iniciar Instalação"
              >
                {"▶️ Iniciar"}
              </Button>
              <Button
                kind="normal"
                size="small"
                onClick={handlePausarInstalacao}
                title="Pausar Instalação"
              >
                {"⏸️ Pausar"}
              </Button>
            </>
          )}
          {isInstallationComplete && (
            <Button
              kind="primary"
              size="small"
              onClick={handlePararInstalacao}
              title="Finalizar Instalação"
            >
              {"✅ Parar"}
            </Button>
          )}
        </div>
      </div>
      <div className="instalacao-content">
        <div className="progress-section">
          <h2>Progresso Geral</h2>
          <div className="progress-info">
            <span className="status-text">
              {instalacaoStatus && instalacaoStatus.progresso_instalacao.status}
            </span>
            <span className="percentage">
              {instalacaoStatus &&
                instalacaoStatus.progresso_instalacao.percentual * 100}
              %
            </span>
          </div>
          <div className="progress-bar">
            <div
              className="progress-fill"
              style={{
                width: `${
                  instalacaoStatus
                    ? instalacaoStatus.progresso_instalacao.percentual * 100
                    : 0
                }%`,
                backgroundColor: getProgressColor(
                  instalacaoStatus
                    ? instalacaoStatus.progresso_instalacao.percentual * 100
                    : 0
                ),
              }}
            ></div>
          </div>
        </div>
        <div className="jobs-section">
          <h2>Tarefas</h2>
          <div className="jobs-list">
            {instalacaoStatus &&
              instalacaoStatus.jobs.map((job, index) => (
                <div key={index} className="job-item">
                  <div className="job-info">
                    <span className="job-name">{job.nome}</span>
                    <span className="job-percentage">
                      {job.percentual * 100}%
                    </span>
                  </div>
                  <div className="progress-bar">
                    <div
                      className="progress-fill"
                      style={{
                        width: `${job.percentual * 100}%`,
                        backgroundColor: getProgressColor(job.percentual * 100),
                      }}
                    ></div>
                  </div>
                </div>
              ))}
          </div>
        </div>
        {(instalacaoStatus?.logs?.length || 0) > 0 && (
          <div className="logs-section">
            <h2>Logs</h2>
            <div className="logs-container">
              {(instalacaoStatus?.logs || []).map((log: any, index) => (
                <div key={index} className="log-entry">
                  {log.tabela} {log.tempo}
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
