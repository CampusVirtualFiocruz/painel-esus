---
sidebar_position: 3
---

# Estrutura e responsabilidades

## `data/`

**Contratos e camadas de aplicação mais próximas de dados.**

- `interfaces/`: Portas do lado de saída (repository/gateway contracts) que o domínio consome. Definem como o domínio conversa com o mundo externo. Subpastas como `create_bases/` agrupam contratos por contexto.
- `use_cases/`: Implementações e variações orientadas a dados, composições específicas.

## `domain/`

**Regras de negócio.**

- `entities/`: Entidades de domínio (modelos centrais).
- `dict_types/`: Tipos estruturados/Value Objects do domínio.
- `use_cases/`: Casos de uso puros (sem dependências de infra), organizados por subdomínios.

## `env/`

**Configuração de ambiente, além de manter parâmetros (ambiente, chaves, URLs, etc) desacoplados do código.**

## `errors/`

**Cross-cutting (infraestrutura compartilhada) de observabilidade e tratamento de error padronizado.**

- `types/`: tipos/estruturas de erro.
- `logging.py`, `logger/`, `log/`: infraestrutura de logging.
- `config.py`, `error_handler.py`: configuração centralizada e manipuladores de erro.

## `infra/`

**Implementações concretas dos contratos de `data/interfaces/` e integrações externas. Depende de frameworks/bibliotecas.**

- `db/`: acesso a banco de dados, queries, conexões.
    - `repositories/`: implementação do Repository Pattern. Encapsula SQL e mapeia resultados para DTOs/entidades, sem regra de negócio. Está agrupado por domínios.
- `requests/`: clientes HTTP/REST para provedores externos.
- `bridge_provider/`: camadas de ponte para serviços/SDKs externos.
- `create_base/`: rotinas de preparação/criação de bases.

## `main/`

**Inicia a aplicação e monta as dependências.**

- `adapters/`: adaptadores entre HTTP/framework e controladores/casos de uso.
- `composers/`: composição/injeção de dependências conectando controladores, casos de uso e repositórios concretos da `infra/`.
- `routes/`: definição das rotas/endpoints e apontamento para os controladores.
- `server/`: bootstrap do servidor/aplicação.

## `presentations/`

**Adapta a camada de entrada (HTTP/UI) para o domínio e não contém regras de negócio.**

- `controllers/`: controladores de interface (HTTP/controller) que recebem a requisição, validam entrada, chamam casos de uso e formatam a resposta.
- `validators/`: validação de payloads de entrada.
- `helpers/`: auxiliares de formatação/conversão do layer de apresentação.
- `http_types/`: contratos de Request/Response/Status, padronizando a camada HTTP.
- `interfaces/`: contratos para controladores/apresentação.

## `utils/`

**Código compartilhado e helpers.**
