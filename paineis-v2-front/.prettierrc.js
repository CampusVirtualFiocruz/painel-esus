module.exports = {
  // Configurações básicas
  semi: true,
  trailingComma: 'es5',
  singleQuote: true,
  printWidth: 80,
  tabWidth: 2,
  useTabs: false,

  // Configurações específicas para diferentes tipos de arquivo
  overrides: [
    {
      files: '*.json',
      options: {
        printWidth: 120,
      },
    },
    {
      files: '*.md',
      options: {
        printWidth: 100,
        proseWrap: 'always',
      },
    },
    {
      files: '*.scss',
      options: {
        singleQuote: false,
      },
    },
    {
      files: '*.css',
      options: {
        singleQuote: false,
      },
    },
  ],

  // Configurações específicas para JSX/TSX
  jsxSingleQuote: true,
  jsxBracketSameLine: false,

  // Configurações de quebra de linha
  endOfLine: 'lf',

  // Configurações de espaçamento
  bracketSpacing: true,
  arrowParens: 'avoid',

  // Configurações específicas para TypeScript
  quoteProps: 'as-needed',
};
