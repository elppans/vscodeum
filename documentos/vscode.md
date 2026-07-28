# VS Code / VSCodium — Guia consolidado

Este documento reúne e organiza as informações sobre instalação, configuração, extensões, temas, integração com shell e procedimentos específicos para VSCodium.

Resumo rápido
- O VS Code (da Microsoft) e o VSCodium (build livre) compartilham a maior parte das configurações e extensões.
- Use este documento como referência única; outros arquivos do diretório "documentos" foram fundidos aqui.

1) Instalação
- Linux (geral): instale o binário do VS Code ou VSCodium via pacote do seu sistema (APT, DNF, pacman) ou RPM/DEB.
- Arch Linux (VSCodium): use o PKGBUILD do AUR ou instruções específicas; veja seção "Instalação no Arch" abaixo.
- Windows/macOS: baixe o instalador oficial ou use gerenciadores de pacotes (scoop/chocolatey, brew).

2) Configuração básica
- Usuário vs Espaço de trabalho: prefira configurações de usuário para preferências globais e configs de workspace para projetos específicos.
- Principais arquivos:
  - settings.json — preferências do usuário
  - keybindings.json — atalhos personalizados
  - extensions.json — recomendações de extensões por workspace
- Dicas:
  - Ative Auto Save e format on save se usar formatadores automáticos.
  - Sincronize configurações quando usar múltiplas máquinas (veja Exportar/Importar).

3) Exportar e importar configurações
- Método manual:
  - Copie os arquivos de configuração (settings.json, keybindings.json, snippets, lista de extensões).
  - Para lista de extensões: `code --list-extensions > extensoes.txt` e `cat extensoes.txt | xargs -L 1 code --install-extension` para reinstalar.
- Método automático:
  - Use a sincronização integrada (Settings Sync) ou uma extensão de terceiros para exportar/importar.

4) Extensões (gerenciamento)
- Instalação CLI: `code --install-extension <publisher.extension>` ou para VSCodium o binário `codium` com a mesma sinalização.
- Marketplace vs VSCodium:
  - VSCodium não inclui a Microsoft Marketplace oficialmente; use o marketplace do Open VSX ou configure acesso ao Marketplace via token/plug-ins.
  - Para instalar extensões do GitHub Marketplace, considere extensões que accessam o Open VSX ou use pacotes .vsix.
- Boas práticas:
  - Mantenha apenas extensões necessárias; prefira extensões leves e bem mantidas.
  - Separe extensões por workspace usando `extensions.json`.

5) Extensões úteis (exemplos)
- Formatação: Prettier, ESLint, Black, clang-format
- Linting/Diagnostics: ESLint, Flake8, Pyright, golangci-lint
- Git: GitLens, Git Graph
- Docker: Docker, Remote - Containers
- Remote/SSH: Remote - SSH (ou extensões equivalentes para VSCodium)

6) Integração com SSH (Remote Development)
- Geração de chave (local): `ssh-keygen -t ed25519 -C "seu-email"` e copie `~/.ssh/id_ed25519.pub` para o servidor.
- Configuração do agent e do arquivo `~/.ssh/config` para facilitar conexões e uso de chaves.
- No VS Code: configure a extensão Remote - SSH apontando para o host no `~/.ssh/config`.
- Em VSCodium, verifique compatibilidade com a extensão de Remote; em alguns casos use Open VSX builds.

7) Temas e aparência
- Instalar temas via Marketplace/Open VSX.
- Ajuste: `workbench.colorTheme`, `editor.fontFamily`, `editor.fontSize`, `window.zoomLevel`.
- Use `settings.json` para alternar tema por workspace se desejar aparência diferente por projeto.

8) Integração com Shell e Terminal integrado
- Terminal padrão: configure `terminal.integrated.shell.linux` (ou terminal profile moderno) para seu shell preferido (bash, zsh, fish).
- Dicas:
  - Defina variáveis de ambiente no arquivo de inicialização do shell para que o terminal integrado herde corretamente.
  - Para problemas com PATH, reinicie o VS Code após modificar arquivos de shell.

9) VSCodium — diferenças e Marketplace
- VSCodium é um build do VS Code sem rastreamento da Microsoft; nem sempre tem acesso ao Marketplace oficial.
- Para usar extensões: habilite Open VSX ou instale `.vsix` manualmente.
- Para usuários de Arch Linux: existe PKGBUILD / AUR com instruções de instalação e atualização.

10) Tips de performance e troubleshooting
- Desative extensões pesadas e reinicie quando sentir lentidão.
- Use Developer Tools (Help > Toggle Developer Tools) para diagnosticar erros.
- Reinstale extensões problemáticas com: `code --uninstall-extension` e `code --install-extension`.

11) Exportando configurações (exemplo rápido)
- Exportar lista de extensões: `code --list-extensions > extensoes.txt`
- Reinstalar: `xargs -L 1 code --install-extension < extensoes.txt`

12) Instalação no Arch (VSCodium) — resumo
- Use AUR/PKGBUILD: instale com um helper AUR (por exemplo, paru/yay) ou construa manualmente com `makepkg -si`.
- Verifique dependências e atualize sempre que necessário.

13) Configuração atual do PC (notas pessoais)
- Anote nesse arquivo as preferências específicas do seu ambiente (plugins essenciais, temas, keybindings) para replicar em outras máquinas.

-----
Notas finais
- Este arquivo substitui e consolida os guias individuais sobre VS Code / VSCodium. Arquivos antigos foram atualizados para apontar para este documento.
- Caso queira separar em arquivos menores no futuro, posso criar a divisão (configuração, extensões, SSH) em commits adicionais.
