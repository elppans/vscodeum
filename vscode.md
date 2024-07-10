# **Visual Studio Code (VS Code)** e o **VSCodium**

O **Visual Studio Code (VS Code)** e o **VSCodium** são editores de código populares, mas têm algumas diferenças importantes:

1. **Licença e Propriedade:**

   - **VS Code**: É propriedade da Microsoft e tem partes proprietárias. Embora seja baseado em código-fonte aberto, a licença restrita impede modificações e distribuição livre.
   - **VSCodium**: É um clone do VS Code, 100% gratuito e de código aberto. Ele é publicado sob a licença MIT, permitindo modificações e distribuição sem restrições.

2. **Extensões:**

   - **VS Code**: Suporta uma ampla variedade de extensões, incluindo as proprietárias. É a melhor opção para quem precisa de muitas extensões específicas.
   - **VSCodium**: Não suporta extensões proprietárias por padrão e oferece menos extensões em comparação com o VS Code. Você pode importar extensões manualmente, mas algumas podem não estar disponíveis no marketplace.

3. **Telemetria e Privacidade:**

   - **VS Code**: Possui telemetria ativada por padrão para rastrear o comportamento do usuário.
   - **VSCodium**: Não possui telemetria ativada por padrão, focando em uma experiência totalmente livre de rastreamento de dados.

---

- Links:

VS Code na web: https://vscode.dev
VS Code: https://code.visualstudio.com/download
VS Codium: https://vscodium.com/
VS Codium Github: https://github.com/VSCodium/vscodium
Temas VSCode: [vscodethemes.com](https://vscodethemes.com/)
Extensões para VSCode: https://marketplace.visualstudio.com/vscode
Extensões para VSCodium: https://open-vsx.org/

- Temas:

1. [omni theme](https://marketplace.visualstudio.com/items?itemName=rocketseat.theme-omni): Dark theme created by Rocketseat
2. [Illusion](https://marketplace.visualstudio.com/items?itemName=rwietter.Illusion) - Tema Dark baseado no DraculaCommunity Material Theme
3. [Symbols](https://marketplace.visualstudio.com/items?itemName=miguelsolorio.symbols) - Tema de ícones minimal
4. [Material icon theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme) - Ícones para o VSCode
5. [VSCode icons](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons) - Ícones para o VSCode, identifica o projeto e mostra um ícone.

- Extensões:

  - [Emmet Cheat Sheet]([Cheat Sheet](https://docs.emmet.io/cheat-sheet/)) (Auto completar(comandos do emmet)) -

  > Ps.: Nas últimas atualizações do VSCode incorporou a extensão Emmet, então agora não precisa mais instalar.

1. [portuguese language pack](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-pt-BR): Pacote de Idioma Português Brasileiro para VS Code
2. [Color Highlight](https://marketplace.visualstudio.com/items?itemName=naumovs.color-highlight) - Cores WEB no editor, que são as cores hexa, RGB, RGBA, etc.
3. [indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow): Facilita a identação
4. [Prettier - Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode). Um formatador de código.
5. [Error lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens) - Acha erros no código e mostra
6. [Better comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments) - Ajuda a criar comentários de forma mais fácil e legível
7. [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree) - Marcar comentários para fazer depois. Ao procurar fica mais facil achar
8. [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) - Mostra em um gráfico como está a árvore do git.
9. [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) - Mostra na linha o ultimo commit e quem fez.
10. [live server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer): Servidor local dev. com recarga ao vivo para páginas estáticas e dinâmicas
11. [auto rename tag](https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-rename-tag): Auto rename paired HTML/XML tag
12. EditorConfig for VSCode - Criar arquivos de configuração do projeto
13. ESLint - Mostra alguma formatação errada em Java Script
14. Auto Close tag - Fecha automaticamente as tags html

- Customizações:

[VSCode minimal](https://gist.github.com/henriquesss/e6e4999653441c5c4796aec943bfe3a4)
[VSCode minimal atualizado:](https://gist.github.com/diego3g/b1b189063d21b96d6144ca896755be64)

CTRL+SHIFT+P - Mostrar todos os comandos
Digitar open settings: Preferences: Open user settings (json)

Adicionar:

Ao usar CTRL+S, terá uma ação:

> Quando o código tiver um erro, corrigir automaticamente:
> "editor.codeActionsOnSave": {
> "source.fixAll.eslint": true
> }
> Irá formatar o código automaticamente:
> "editor.formatOnSave": true

- Atalhos úteis:

f2 = renomear por tarde do arquivo;
f2 \* ao selecionar nome - variavel ou funcao, renomea todas as referências dele no projeto;
ctrl + shift + L = seleciona todas referencias de um nome;
ctrl + b = esconder seleção de arquivos;
ctrl + k z = modo zen;
ctrl + p = buscar/abrir aquivo
@ = passa a usar todos os elementos do arquivo aberto;
: = filtro;
ctrl + shift + . = navega entre cada elemento do arquivo;
ctrl + . = ver datalhe (ou corrigir) do erro na linha selecionada;

Ctrl + shift + p = comparar arquivos entre versões;
alt + f5 = pular cada alteração;
shift + f5 = voltar cada alteração;

cltr + k c = comparar arquivo com código no clipboard;
alt + shift + f5 = fechar comparação;

Fontes:
https://www.youtube.com/watch?v=uxln1hT_Ev4
https://www.youtube.com/watch?v=Ni_9mo932nA
https://www.youtube.com/watch?v=TW3KoPkuWEA
https://www.youtube.com/watch?v=qJ_M4W0u5rI
https://www.youtube.com/watch?v=468TtYwJx9w
