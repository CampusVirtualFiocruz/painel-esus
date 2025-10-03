import React, { useState, useEffect, useCallback } from "react";
import { useNavigate } from "react-router-dom";
import { Button, TextField, Alert, Spinner } from "bold-ui";
import { Api } from "../services/api";
import { useInstalationReady } from "../hooks/useInstalationReady";
import "../styles/configuracao.scss";

export interface ConfiguracaoData {
  showSetupWizardOnLaunch: boolean;
  env: {
    DB_HOST: string;
    DB_DATABASE: string;
    DB_USER: string;
    DB_PASSWORD: string;
    DB_PORT: string;
    CIDADE_IBGE: string;
    ADMIN_USERNAME: string;
    ADMIN_PASSWORD: string;
    ADMIN_EMAIL: string;
    ADMIN_NAME: string;
    BRIDGE_LOGIN_URL: string;
  };
}

export function Configuracao() {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [testingConnection, setTestingConnection] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);
  const [connectionStatus, setConnectionStatus] = useState<string | null>(null);
  const [submitErrors, setSubmitErrors] = useState<string[]>([]);

  useInstalationReady();

  const [formData, setFormData] = useState({
    DB_HOST: "",
    DB_DATABASE: "",
    DB_USER: "",
    DB_PASSWORD: "",
    DB_PORT: "",
    CIDADE_IBGE: "",
    ADMIN_USERNAME: "",
    ADMIN_PASSWORD: "",
    ADMIN_EMAIL: "",
    ADMIN_NAME: "",
    BRIDGE_LOGIN_URL: "",
  });

  const fetchConfiguracao = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);

      const response = await Api.get<ConfiguracaoData>(
        "/settings/check-instalation"
      );
      const data = response.data;

      if (!data.showSetupWizardOnLaunch) {
        navigate("/instalacao");
        return;
      }
      setFormData(data.env || {});
    } catch (err: any) {
      console.error("Erro ao buscar configuração:", err);
      setError("Erro ao carregar configurações. Tente novamente.");
    } finally {
      setLoading(false);
    }
  }, [navigate]);

  useEffect(() => {
    fetchConfiguracao();
  }, [fetchConfiguracao]);

  const handleInputChange = (field: string, value: string) => {
    setFormData((prev) => ({
      ...prev,
      [field]: value,
    }));

    if (error) setError(null);
    if (connectionStatus) setConnectionStatus(null);
    if (submitErrors.length > 0) setSubmitErrors([]);
  };

  const validateForm = () => {
    const requiredFields = [
      "DB_HOST",
      "DB_DATABASE",
      "DB_USER",
      "DB_PASSWORD",
      "DB_PORT",
      "CIDADE_IBGE",
      "ADMIN_USERNAME",
      "ADMIN_PASSWORD",
    ];

    for (const field of requiredFields) {
      if (!formData[field as keyof typeof formData].trim()) {
        setError(`O campo ${field.replace("_", " ")} é obrigatório.`);
        return false;
      }
    }

    const port = parseInt(formData.DB_PORT);
    if (isNaN(port) || port < 1 || port > 65535) {
      setError("A porta do banco deve ser um número válido entre 1 e 65535.");
      return false;
    }

    if (
      formData.ADMIN_EMAIL &&
      !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.ADMIN_EMAIL)
    ) {
      setError("O email do administrador deve ter um formato válido.");
      return false;
    }

    return true;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!validateForm()) {
      return;
    }

    try {
      setSaving(true);
      setError(null);
      setSuccess(null);
      setSubmitErrors([]);

      const configData = {
        ...formData,
        DB_PORT: String(formData.DB_PORT),
      };

      await Api.post("/settings/instalation-settings", configData);

      setSuccess(
        "Configurações salvas com sucesso! Redirecionando para a instalação..."
      );

      setTimeout(() => {
        navigate("/instalacao");
      }, 2000);
    } catch (err: any) {
      console.error("Erro ao salvar configuração:", err);

      if (
        err.response?.data?.errors &&
        Array.isArray(err.response.data.errors)
      ) {
        const errorMessages = err.response.data.errors.map((error: any) => {
          if (error.detail) {
            return error.detail;
          }
          return error.title || "Erro desconhecido";
        });
        setSubmitErrors(errorMessages);
      } else {
        const errorMessage =
          err.response?.data?.message ||
          "Erro ao salvar configurações. Tente novamente.";
        setError(errorMessage);
      }
    } finally {
      setSaving(false);
    }
  };

  const handlePularConfiguracao = () => {
    navigate("/instalacao");
  };

  const testDatabaseConnection = async () => {
    try {
      setTestingConnection(true);
      setConnectionStatus(null);
      setError(null);

      const connectionData = {
        DB_HOST: formData.DB_HOST,
        DB_DATABASE: formData.DB_DATABASE,
        DB_USER: formData.DB_USER,
        DB_PASSWORD: formData.DB_PASSWORD,
        DB_PORT: formData.DB_PORT,
      };

      await Api.post("/settings/test-connection", connectionData);

      setConnectionStatus("Conexão com o banco de dados bem-sucedida!");
    } catch (err: any) {
      console.error("Erro ao testar conexão:", err);
      const errorMessage =
        err.response?.data?.message || "Erro ao conectar com o banco de dados.";
      setConnectionStatus(`Erro na conexão: ${errorMessage}`);
    } finally {
      setTestingConnection(false);
    }
  };

  if (loading) {
    return (
      <div className="configuracao-loading">
        <Spinner>Carregando configurações...</Spinner>
      </div>
    );
  }

  return (
    <div className="configuracao-container">
      <div className="configuracao-header">
        <div className="header-content">
          <h1>Configuração do Sistema</h1>
          <p>
            Configure as informações do sistema antes de prosseguir com a
            instalação.
          </p>
        </div>
        <button
          className="voltar-button"
          onClick={() => navigate("/instalacao")}
          title="Voltar para Instalação"
        >
          ← Verificar status da Instalação
        </button>
      </div>
      {error && (
        <Alert type="danger" className="mb-4">
          {error}
        </Alert>
      )}
      {success && (
        <Alert type="success" className="mb-4">
          {success}
        </Alert>
      )}
      <form onSubmit={handleSubmit} className="configuracao-form">
        <div className="configuracao-card mb-4">
          <div className="configuracao-card-body">
            <h3>Configurações do Banco de Dados</h3>
            <div className="form-grid">
              <TextField
                label="Host do Banco"
                value={formData.DB_HOST}
                onChange={(e) => handleInputChange("DB_HOST", e.target.value)}
                placeholder="Ex: localhost"
                required
              />
              <TextField
                label="Porta do Banco"
                value={formData.DB_PORT}
                onChange={(e) => handleInputChange("DB_PORT", e.target.value)}
                placeholder="Ex: 5432"
                required
              />
              <TextField
                label="Nome do Banco"
                value={formData.DB_DATABASE}
                onChange={(e) =>
                  handleInputChange("DB_DATABASE", e.target.value)
                }
                placeholder="Nome do banco de dados"
                required
              />
              <TextField
                label="Usuário do Banco"
                value={formData.DB_USER}
                onChange={(e) => handleInputChange("DB_USER", e.target.value)}
                placeholder="Usuário do banco"
                required
              />
              <TextField
                label="Senha do Banco"
                type="password"
                value={formData.DB_PASSWORD}
                onChange={(e) =>
                  handleInputChange("DB_PASSWORD", e.target.value)
                }
                placeholder="Senha do banco"
                required
              />
            </div>
            <div className="connection-test-section">
              <Button
                type="button"
                kind="normal"
                onClick={testDatabaseConnection}
                disabled={
                  testingConnection || !formData.DB_HOST || !formData.DB_PORT
                }
              >
                {testingConnection ? (
                  <>
                    <Spinner />
                    Testando Conexão...
                  </>
                ) : (
                  "Testar Conexão"
                )}
              </Button>
              {connectionStatus && (
                <div
                  className={`connection-status ${
                    connectionStatus.includes("Erro") ? "error" : "success"
                  }`}
                >
                  {connectionStatus}
                </div>
              )}
            </div>
          </div>
        </div>
        <div className="configuracao-card mb-4">
          <div className="configuracao-card-body">
            <h3>Configurações do Administrador</h3>
            <div className="form-grid">
              <TextField
                label="Nome do Administrador"
                value={formData.ADMIN_NAME}
                onChange={(e) =>
                  handleInputChange("ADMIN_NAME", e.target.value)
                }
                placeholder="Nome completo"
              />
              <TextField
                label="Email do Administrador"
                type="email"
                value={formData.ADMIN_EMAIL}
                onChange={(e) =>
                  handleInputChange("ADMIN_EMAIL", e.target.value)
                }
                placeholder="email@exemplo.com"
              />
              <TextField
                label="Usuário Administrador"
                value={formData.ADMIN_USERNAME}
                onChange={(e) =>
                  handleInputChange("ADMIN_USERNAME", e.target.value)
                }
                placeholder="Nome de usuário"
                required
              />
              <TextField
                label="Senha do Administrador"
                type="password"
                value={formData.ADMIN_PASSWORD}
                onChange={(e) =>
                  handleInputChange("ADMIN_PASSWORD", e.target.value)
                }
                placeholder="Senha"
                required
              />
            </div>
          </div>
        </div>
        <div className="configuracao-card mb-4">
          <div className="configuracao-card-body">
            <h3>Outras Configurações</h3>
            <div className="form-grid">
              <TextField
                label="Código IBGE da Cidade"
                value={formData.CIDADE_IBGE}
                onChange={(e) =>
                  handleInputChange("CIDADE_IBGE", e.target.value)
                }
                placeholder="Código IBGE"
                required
              />
              <TextField
                label="URL de Login Bridge"
                value={formData.BRIDGE_LOGIN_URL}
                onChange={(e) =>
                  handleInputChange("BRIDGE_LOGIN_URL", e.target.value)
                }
                placeholder="http://exemplo.com"
              />
            </div>
          </div>
        </div>
        {submitErrors.length > 0 && (
          <div className="submit-errors">
            {submitErrors.map((errorMsg, index) => (
              <Alert key={index} type="danger" className="mb-2">
                {errorMsg}
              </Alert>
            ))}
          </div>
        )}
        <div className="configuracao-actions">
          <Button
            type="button"
            kind="normal"
            onClick={handlePularConfiguracao}
            disabled={saving}
          >
            Pular Configuração
          </Button>
          <Button type="submit" kind="primary" disabled={saving}>
            {saving ? (
              <>
                <Spinner />
                Salvando...
              </>
            ) : (
              "Salvar e Continuar"
            )}
          </Button>
        </div>
      </form>
    </div>
  );
}
