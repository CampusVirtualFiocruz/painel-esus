# Configuração de ESLint e Prettier

Este projeto foi configurado com ESLint e Prettier para manter a qualidade e consistência do código.

## 📋 **Dependências Instaladas**

- `@typescript-eslint/eslint-plugin@^5.62.0`
- `@typescript-eslint/parser@^5.62.0`
- `eslint-config-prettier`
- `eslint-plugin-prettier`
- `prettier`
- `eslint-plugin-react`
- `eslint-plugin-jsx-a11y`
- `eslint-plugin-import`

## 🛠️ **Scripts Disponíveis**

### Linting
```bash
# Verificar problemas de linting
npm run lint

# Corrigir automaticamente problemas de linting
npm run lint:fix
```

### Formatação
```bash
# Formatar todos os arquivos
npm run format

# Verificar se os arquivos estão formatados
npm run format:check
```

### Combinado
```bash
# Executar lint:fix + format
npm run lint:format
```

## 📁 **Arquivos de Configuração**

### ESLint (`.eslintrc.js`)
- Configuração para React + TypeScript
- Regras para acessibilidade (jsx-a11y)
- Integração com Prettier
- Suporte para Storybook

### Prettier (`.prettierrc.js`)
- Aspas simples por padrão
- Semicolons obrigatórios
- Largura máxima de 80 caracteres
- Configurações específicas para diferentes tipos de arquivo

### Arquivos de Ignore
- `.eslintignore` - Arquivos ignorados pelo ESLint
- `.prettierignore` - Arquivos ignorados pelo Prettier

## 🔧 **Configuração do VS Code**

### Extensões Recomendadas (`.vscode/extensions.json`)
- ESLint
- Prettier
- TypeScript Importer
- Auto Rename Tag
- Path Intellisense

### Configurações (`.vscode/settings.json`)
- Formatação automática ao salvar
- Correção automática do ESLint
- Organização automática de imports
- Configurações específicas para TypeScript e React

## 📝 **Regras Principais**

### ESLint
- **React**: Regras para componentes, hooks e JSX
- **TypeScript**: Verificação de tipos e boas práticas
- **Acessibilidade**: Regras jsx-a11y para componentes acessíveis
- **Importação**: Organização e validação de imports

### Prettier
- **Aspas**: Simples por padrão
- **Semicolons**: Obrigatórios
- **Indentação**: 2 espaços
- **Quebra de linha**: LF (Unix)

## 🚀 **Como Usar**

### 1. Verificar Problemas
```bash
npm run lint
```

### 2. Corrigir Automaticamente
```bash
npm run lint:fix
```

### 3. Formatar Código
```bash
npm run format
```

### 4. Verificar Formatação
```bash
npm run format:check
```

## ⚠️ **Problemas Conhecidos**

- **TypeScript 5.4.5**: Versão não oficialmente suportada pelo @typescript-eslint, mas funciona normalmente
- **Warnings de `any`**: Muitos warnings sobre uso de `any` - considere tipar adequadamente
- **Console statements**: Warnings sobre uso de `console.log` - remova em produção

## 🔄 **Integração com Git**

Para integrar com Git hooks, você pode usar `husky` e `lint-staged`:

```bash
npm install --save-dev husky lint-staged
```

E adicionar ao `package.json`:
```json
{
  "lint-staged": {
    "src/**/*.{ts,tsx,js,jsx}": [
      "eslint --fix",
      "prettier --write"
    ]
  }
}
```

## 📚 **Recursos Adicionais**

- [ESLint Documentation](https://eslint.org/)
- [Prettier Documentation](https://prettier.io/)
- [TypeScript ESLint](https://typescript-eslint.io/)
- [React ESLint Plugin](https://github.com/jsx-eslint/eslint-plugin-react)
