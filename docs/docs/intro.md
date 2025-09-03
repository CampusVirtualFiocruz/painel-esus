---
sidebar_position: 1
---

# Visão Geral do Projeto

Este repositório contém dois projetos principais:

- **painel-esus**: Backend Python para processamento, análise e exportação de dados de saúde pública.
- **paineis-v2-front**: Frontend React para visualização dos dados processados, com gráficos interativos e dashboards.

---

## Estrutura dos Projetos

### painel-esus (Backend)

- **Linguagem:** Python 3
- **Principais diretórios:**
  - `src/`: Código principal, dividido em camadas (domain, infra, main, presentations, utils).
  - `dados/`: Dados de entrada e saída em formato parquet.
  - `interface/`: Scripts e interface para interação com o sistema.
  - `setup/`, `local_ssl/`: Scripts de configuração e utilitários.
- **Principais funcionalidades:**
  - Processamento de dados de saúde (cadastro, atendimentos, condições clínicas).
  - Exportação de logs e relatórios.
  - Integração com bancos de dados e arquivos parquet.
  - APIs para consumo pelo frontend.

### paineis-v2-front (Frontend)

- **Linguagem:** TypeScript + React
- **Principais diretórios:**
  - `src/`: Componentes, páginas, hooks, serviços, estilos e utilitários.
  - `public/`: Arquivos estáticos e HTML base.
  - `.storybook/`: Configuração de Storybook para documentação de componentes.
- **Principais funcionalidades:**
  - Dashboards interativos para visualização dos dados processados.
  - Gráficos e tabelas dinâmicas.
  - Autenticação e seleção de perfis.
  - Integração com APIs do painel-esus.

---

## Como contribuir

1. Faça um fork do repositório.
2. Crie uma branch para sua feature ou correção.
3. Envie um Pull Request detalhando as alterações.

Consulte os arquivos README.md de cada projeto para instruções específicas de instalação e execução.

---

## Referências

- [Documentação Docusaurus](https://docusaurus.io/docs)
- [Documentação React](https://react.dev/)
- [Documentação Python](https://docs.python.org/3/)
