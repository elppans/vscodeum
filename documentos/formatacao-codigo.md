# Formatação de código

Este guia reúne as recomendações e comandos para formatação de código automatizada em diferentes linguagens.

Por que usar formatadores?
- Mantêm um estilo consistente no projeto.
- Reduzem discussões de estilo em code review.
- Permitem usar `format on save` no editor.

Ferramentas populares
- Prettier — JavaScript, TypeScript, JSON, CSS, Markdown.
- ESLint (com --fix) — linter + correções para JS/TS.
- Black — Python (opinioso, formato consistente).
- isort — ordenação de imports em Python.
- clang-format — C/C++/Objective-C.
- gofmt / goimports — formato padrão para Go.

Integração com VS Code / VSCodium
- Instale a extensão correspondente (Prettier, Black, clang-format etc.).
- Configure `editor.formatOnSave` no `settings.json` ou habilite por workspace.
- Configure o formatador padrão por linguagem (ex.: `"[python]": { "editor.defaultFormatter": "ms-python.python" }`).

Usando na linha de comando
- Prettier: `npx prettier --write "src/**/*.{js,ts,jsx,tsx,json,css,md}"`
- Black: `black .`
- gofmt: `gofmt -w .`

CI / Pre-commit
- Adicione hooks com pre-commit (https://pre-commit.com) para aplicar formatação antes do commit.
- Em CI, rode os formatadores no pipeline para garantir consistência.

Dicas
- Escolha um conjunto mínimo de regras e documente no README do projeto.
- Se migrar de um formatador para outro, faça um commit único com a aplicação do novo formatador para facilitar diffs.

---
Este arquivo consolida e substitui o conteúdo de `documentos/ferramentas_de_formatacao_de_codigos.md`.