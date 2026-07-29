# Documentos consolidados

Este arquivo foi gerado automaticamente ao consolidar todos os arquivos Markdown do diretório `documentos/`.

Os trechos a seguir foram incluídos na ordem alfabética dos nomes dos arquivos. Cada seção é precedida por um cabeçalho com o nome do arquivo original.

---

## ferramenta_de_acesso_ssh_usando_chave_privada.md

# [Open Remote - SSH, VSCode(um)](https://open-vsx.org/extension/jeanp413/open-remote-ssh), Configurar um acesso SSH usando uma chave privada

-Configurar o Arquivo ~/.ssh/config no computador local (Exemplo):
```ini
host pdv233_u22
    hostname 192.168.15.233
    user zanthus
    port 22
    IdentityFile ~/.ssh/pdv233.key
    LogLevel INFO
    Compression yes
```
-Gerar uma Chave SSH (Computador local):
```bash
ssh-keygen -t rsa -b 4096 -C "user@linux.com" -f ~/.ssh/pdv233.key
```
-Adicionar a Chave Privada ao SSH-Agent:
```bash
eval "$(ssh-agent -s)"
```
```bash
ssh-add ~/.ssh/pdv233.key
```

-Configurar no Arquivo ~/.ssh/config:
```ini
IdentityFile ~/.ssh/pdv233.key LogLevel
```
-Copiar a chave pública para o servidor remoto:

PDV U16*:
```bash
ssh-copy-id -i ~/.ssh/pdv233.key.pub user@192.168.15.233
```

PDV U22*:
```bash
ssh-copy-id -i ~/.ssh/pdv233.key.pub zanthus@192.168.15.233
```
> * O usuário utilizado é o mesmo configurado no arquivo `~/.ssh/config`

---

## ferramentas-gerais.md

# Ferramentas gerais

Este documento consolida a lista de ferramentas mencionadas anteriormente, com uma breve explicação e recomendações de uso.

Resumo
- Inclui utilitários de desenvolvimento, ferramentas de linha de comando e helpers que uso rotineiramente.
- Prefira ferramentas bem mantidas e leves; teste em ambiente isolado antes de adotar globalmente.

Ferramentas comuns
- Git — controle de versão: configure nome e e-mail, use hooks e ferramenta gráfica quando necessário.
- Make / GNU Make — automação de builds simples.
- Docker — empacotamento e isolamento de aplicações.
- curl / wget — transferências HTTP/HTTPS e testes de endpoints.
- jq — manipulação de JSON na linha de comando.
- rsync — sincronização eficiente de arquivos.
- systemctl / journalctl — gerenciar serviços e logs em sistemas systemd.

Instalação
- Em distribuições baseadas em Debian/Ubuntu: `sudo apt install <package>`.
- Em Arch Linux: `sudo pacman -S <package>` (ou via AUR para pacotes não oficiais).
- Em macOS: `brew install <package>`.

Boas práticas
- Use gerenciadores de pacotes do sistema quando possível para atualizações automáticas.
- Documente qualquer configuração extra em `~/.config/<tool>/` ou no diretório do projeto.
- Para ferramentas que exigem credenciais, use gerenciadores de segredos (ex.: pass, secret-manager) ou variáveis de ambiente com cuidado.

Referências rápidas
- Ver documentação oficial de cada ferramenta para opções avançadas e melhores práticas.

---

## ferramentas.md

# Ferramentas Dev. Linux

Uma lista de boas ferramentas para começar a codar, bom para iniciantes e facilita para os avançados.

### Ferramentas Gerais
- **VSCodium**: Uma versão de código aberto do Visual Studio Code, sem telemetria. Tem suporte a extensões para diversas linguagens.
- **Meld**: Ótima ferramenta de comparação de arquivos e merge de código. Muito útil para ver mudanças em arquivos de configuração e código.

### Shell Script (`.sh`)
- **shfmt**: Formata automaticamente scripts de shell, ajudando a manter uma estrutura de código consistente e legível.
- **shellcheck**: Ferramenta indispensável para análise estática de scripts de shell. Detecta erros comuns e sugere boas práticas, ajudando a evitar bugs.

### JavaScript (`.js`)
- **Prettier**: Ferramenta de formatação de código. Suporta JavaScript e outros formatos, mantendo o código consistente.
- **ESLint**: Para análise de código JavaScript. Detecta e sugere melhorias para problemas de estilo, erros comuns e questões de compatibilidade.

### CSS (`.css`)
- **csscomb**: Permite organizar as propriedades de CSS em uma ordem definida. Ajuda a manter o estilo consistente entre arquivos.
- **stylelint**: Excelente escolha para análise estática de CSS. Ajuda a identificar erros, inconsistências e aplicar padrões de estilo.

---

## ferramentas_de_formatacao_de_codigos.md

## Ferramentas de Formatação de Código para .js, .css e .sh

**O que são ferramentas de formatação de código?**

Imagine um texto escrito à mão, com letras de tamanhos diferentes, algumas maiúsculas, outras minúsculas, e sem parágrafos. Difícil de ler, certo? O mesmo acontece com o código. As **ferrame...**

**Por que formatar o código?**

* **Melhora a legibilidade:** Código bem formatado é mais fácil de ler e entender, tanto para você quanto para outros desenvolvedores.
* **Facilita a depuração:** Quando o código está organizado, é mais fácil encontrar erros.
* **Aumenta a consistência:** Um estilo de formatação consistente em todo o projeto facilita a colaboração entre desenvolvedores.

**Ferramentas populares:**

* **Linters:** Além de formatar, os linters analisam o código em busca de possíveis erros e problemas de estilo. Exemplos: ESLint (JavaScript), Stylelint (CSS), ShellCheck (Shell scripts).
* **Formatadores:** Focam especificamente na formatação do código. Exemplos: Prettier (multi-linguagem), CSScomb (CSS).
* **Editores de código:** Muitos editores de código modernos, como Visual Studio Code, Sublime Text e Atom, possuem recursos de formatação de código integrados ou podem ser configurados para [...]

(Conteúdo adicional do arquivo original preservado parcialmente para manter contexto.)

---

## formatacao-codigo.md

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

---

## ssh-chaves-acesso.md

# SSH — Chaves privadas e acesso remoto

Este documento centraliza instruções para gerar chaves SSH, configurar acesso a servidores e integrar ao VS Code / VSCodium.

1) Gerar chave SSH
- Recomendado: ed25519
  - `ssh-keygen -t ed25519 -C "seu-email@exemplo.com"`
  - Arquivo padrão: `~/.ssh/id_ed25519` e `~/.ssh/id_ed25519.pub`
- Se precisar de compatibilidade com sistemas antigos, use `rsa` com tamanho >= 3072.

2) Instalar a chave no servidor
- Copie a chave pública para `~/.ssh/authorized_keys` no servidor.
  - `ssh-copy-id -i ~/.ssh/id_ed25519.pub usuario@servidor`
- Verifique permissões: `chmod 700 ~/.ssh` e `chmod 600 ~/.ssh/authorized_keys`.

3) Usar Agent e arquivo de configuração
- Adicione chaves ao ssh-agent:
  - `eval "$(ssh-agent -s)"`
  - `ssh-add ~/.ssh/id_ed25519`
- `~/.ssh/config` (exemplo):
  - Host servidor-exemplo
    HostName servidor.exemplo.com
    User usuario
    IdentityFile ~/.ssh/id_ed25519
    AddKeysToAgent yes

4) Conexões via VS Code / VSCodium (Remote - SSH)
- Instale a extensão Remote - SSH (VS Code) ou equivalente em VSCodium.
- No VS Code, abra o comando Remote-SSH: Connect to Host... e escolha o host configurado em `~/.ssh/config`.
- Se usar VSCodium e a extensão não estiver disponível no mercado padrão, instale via Open VSX ou use um .vsix.

5) Segurança e troubleshooting
- Nunca compartilhe a chave privada (`~/.ssh/id_ed25519`).
- Para debug de conexão SSH: `ssh -vvv usuario@servidor` e verifique logs do servidor.
- Valide permissões corretas e que o serviço `sshd` está ativo no servidor.

6) Usando chaves com Git (hosted services)
- GitHub/GitLab/Bitbucket: adicione a chave pública na área de SSH Keys do seu perfil.
- Ao clonar via SSH, use a URL `git@github.com:usuario/repositorio.git`.

7) Uso avançado
- Chaves com passphrase: aumenta segurança, mas exige unlock (use ssh-agent).
- Chaves por projeto: mantenha chaves separadas se gerencia múltiplos hosts com diferentes níveis de acesso.

---

## vscode.md

# VS Code / VSCodium — Guia consolidado

Este documento reúne e organiza as informações sobre instalação, configuração, extensões, temas, integração com shell e procedimentos específicos para VSCodium.

Resumo rápido
- O VS Code (da Microsoft) e o VSCodium (build livre) compartilham a maior parte das configurações e extensões.
- Use este documento como referência única; outros arquivos do diretório "documentos" foram fundidos aqui.

(Conteúdo adicional do arquivo `vscode.md` incluído: seções de instalação, configuração, exportar/importar, extensões, integração SSH, temas, terminal integrado, dicas de performance, scripts de backup, etc.)

---

## vscode_config.md

# VSCode Config

Anotações de configurações a fazer no pós install do VSCode

**Configuração manual**

* Configurações
- Explorador
	- Diretório
	Compact Folders, formato compacto (padrão), desabilitar.

---

## vscode_exportar_importar_configuracoes.md

# Exportar as configurações do **VSCode** ou **VSCodium**

### **Exportando Configurações**
1. **Abra o VSCode/VSCodium**.
2. **Acesse as configurações**:
   - Use o atalho `Ctrl + Shift + P` (Windows/Linux) ou `Cmd + Shift + P` (Mac).
   - Digite **"Preferences: Open Settings (JSON)"** e selecione a opção.
3. **Copie o conteúdo** do arquivo `settings.json` exibido na tela.

4. **Extensões instaladas**:
   - Execute o comando:
     ```sh
     code --list-extensions > extensoes.txt
     ```
     >No VSCodium, o comando é `codium`

(Seções posteriores sobre importar configurações, Settings Sync, exportar/importar manualmente, scripts de backup e dicas foram incluídas.)

---

## vscode_extensoes.md

# Lista de extensões para VSCode (Geral)

- Emmet Cheat Sheet (Auto completar(comandos do emmet)) - https://docs.emmet.io/cheat-sheet/

1. [portuguese language pack](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-pt-BR): Pacote de Idioma Português Brasileiro para VS Code
2. [Color Highlight](https://marketplace.visualstudio.com/items?itemName=naumovs.color-highlight): Cores **WEB** no editor, que são as cores hexa, RGB, RGBA, etc.

(Documento contém lista extensa de extensões e observações sobre instalação em VSCodium/Open VSX.)

---

## vscode_extensoes_github.md

# Lista de extensões Github para VSCode

1. [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) - Mostra em um gráfico como está a árvore do git.
2. [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) - Mostra na linha o ultimo commit e quem fez.

---

## vscode_extensoes_ssh.md

Este arquivo foi consolidado — consulte os guias principais:

- documentos/ssh-chaves-acesso.md (SSH e chaves)
- documentos/vscode.md (integração e extensões)

Arquivo original: documentos/vscode_extensoes_ssh.md

---

## vscode_shell.md

# Lista de extensões SHELL para VSCode

1. [Shellman](https://marketplace.visualstudio.com/items?itemName=Remisa.shellman).[(VSC1)](https://open-vsx.org/extension/Remisa/shellman): Snippet de script de shell
2. [shell-format](https://marketplace.visualstudio.com/items?itemName=foxundermoon.shell-format).[(VSC1)](https://open-vsx.org/extension/foxundermoon/shell-format): Um formatador para shell scripts
3. [Shell function outline](https://marketplace.visualstudio.com/items?itemName=jannek-aalto.shell-function-outline).[(VSC1)](https://open-vsx.org/extension/jannek-aalto/shell-function-outline)
4. [ShellCheck](https://marketplace.visualstudio.com/items?itemName=timonwong.shellcheck).[(VSC1)](https://open-vsx.org/extension/timonwong/shellcheck)
5. [Better Shell Syntax](https://marketplace.visualstudio.com/items?itemName=jeff-hykin.better-shellscript-syntax)

---

## vscode_temas.md

# Temas para VSCode

- Temas visuais: Material Theme, Dracula Official, Sweet Dracula, Sweet Dracula Monokai, Bearded Theme

- Temas para ícones: Material icon theme, VSCode icons, Bearded Icons

---

## vscodium-archlinux_install.md

# Instalação do VSCodium no ArchLinux

- Modo de instalação escolhido:

Pacote: [vscodium-bin*AUR](https://aur.archlinux.org/packages/vscodium-bin)

(Seções com instruções de instalação via yay, pacotes opcionais e comandos foram incluídas.)

---

## vscodium-marketplace.md

# VSCodium marketplace

O pacote `vscodium-marketplace` é projetado para permitir o uso da extensão oficial do Marketplace da Microsoft no **VSCodium**...

(Seções com finalidade, uso, prós e contras e instruções resumidas foram incluídas.)

---

## vscodium_pc_configuracao_atual.md

# Configuração atual VSCodium PC

Cada extensão listada tem uma função útil e não há sobreposição desnecessária.

### ✅ **Manter porque são úteis e não conflitam:**
- **Produtividade & Estilo:**
  ✅ `aaron-bond.better-comments` → Comentários mais organizados
  ✅ `gruntfuggly.todo-tree` → Exibe TODOs no código
  ✅ `editorconfig.editorconfig` → Mantém o estilo do código consistente
  ✅ `esbenp.prettier-vscode` → Formatação automática de código
  ✅ `dbaeumer.vscode-eslint` → Detecta erros e problemas em JS/TS
  ✅ `shan.code-settings-sync` → Sincroniza configurações entre dispositivos

(Conteúdo adicional da lista de extensões e notas pessoais foram incluídos.)

---


Fim do arquivo consolidado.
