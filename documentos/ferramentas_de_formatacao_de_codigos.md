## Ferramentas de Formatação de Código para .js, .css e .sh

**O que são ferramentas de formatação de código?**

Imagine um texto escrito à mão, com letras de tamanhos diferentes, algumas maiúsculas, outras minúsculas, e sem parágrafos. Difícil de ler, certo? O mesmo acontece com o código. As **ferramentas de formatação de código** são como editores de texto inteligentes que reorganizam o seu código de forma consistente e fácil de entender. Elas adicionam indentação, quebras de linha e outros elementos visuais que tornam o código mais legível e organizado.

**Por que formatar o código?**

* **Melhora a legibilidade:** Código bem formatado é mais fácil de ler e entender, tanto para você quanto para outros desenvolvedores.
* **Facilita a depuração:** Quando o código está organizado, é mais fácil encontrar erros.
* **Aumenta a consistência:** Um estilo de formatação consistente em todo o projeto facilita a colaboração entre desenvolvedores.

**Ferramentas populares:**

* **Linters:** Além de formatar, os linters analisam o código em busca de possíveis erros e problemas de estilo. Exemplos: ESLint (JavaScript), Stylelint (CSS), ShellCheck (Shell scripts).
* **Formatadores:** Focam especificamente na formatação do código. Exemplos: Prettier (multi-linguagem), CSScomb (CSS).
* **Editores de código:** Muitos editores de código modernos, como Visual Studio Code, Sublime Text e Atom, possuem recursos de formatação de código integrados ou podem ser configurados para usar ferramentas externas.

**Comandos comuns:**

Os comandos específicos variam de acordo com a ferramenta e o editor de código que você está usando. No entanto, alguns comandos comuns incluem:

* **Formatar o arquivo inteiro:**
  * **Linters:** `eslint --fix arquivo.js`, `stylelint --fix arquivo.css`
  * **Formatadores:** `prettier --write arquivo.js`, `csscomb -s arquivo.css`
* **Formatar uma seleção:**
  * Geralmente, você pode selecionar o código que deseja formatar no editor e pressionar um atalho de teclado (por exemplo, Ctrl+Shift+I no Visual Studio Code).

**Para .js, .css e .sh, você pode usar:**

* **JavaScript (.js):** ESLint, Prettier, StandardJS
* **CSS (.css):** Stylelint, Prettier, CSScomb
* **Shell scripts (.sh):** ShellCheck, Shellfmt
___

## Formatando Código via Linha de Comando no Linux

### Ferramentas Comuns e seus Comandos

As ferramentas mais populares para formatação de código no Linux, junto com seus comandos básicos, são:

#### **JavaScript (.js):**

* **ESLint:**
  * **Instalação:** `npm install -g eslint`
  * **Formatação:** `eslint --fix arquivo.js`
  * **Configuração:** Crie um arquivo `.eslintrc.js` para personalizar as regras.

* **Prettier:**
  * **Instalação:** `npm install -g prettier`
  * **Formatação:** `prettier --write arquivo.js`
  * **Configuração:** Crie um arquivo `.prettierrc.js` para personalizar as opções.

#### **CSS (.css):**

* **Stylelint:**
  * **Instalação:** `npm install -g stylelint`
  * **Formatação:** `stylelint --fix arquivo.css`
  * **Configuração:** Crie um arquivo `.stylelintrc.json` para personalizar as regras.

* **Prettier:**
  * **Instalação:** (já instalado para JavaScript)
  * **Formatação:** `prettier --write arquivo.css`

#### **Shell scripts (.sh):**

* **ShellCheck:**
  * **Instalação:** `sudo apt install shellcheck` (Debian/Ubuntu) ou `brew install shellcheck` (macOS)
  * **Verificação:** `shellcheck arquivo.sh`

* **Shellfmt:**
  * **Instalação:** `sudo apt install shellfmt` (Debian/Ubuntu)
  * **Formatação:** `shellfmt arquivo.sh`

### Exemplos de Uso em Scripts

Para integrar a formatação em seus fluxos de trabalho, você pode criar scripts simples. Por exemplo, para formatar todos os arquivos JavaScript em um diretório:

```bash
for file in *.js; do
  prettier --write "$file"
done
```

### Integração com Editores de Texto

A maioria dos editores de texto modernos oferece integração com essas ferramentas, permitindo que você formate o código com um simples atalho de teclado ou ao salvar o arquivo.

* **Visual Studio Code:** Extensões como ESLint, Prettier e Stylelint oferecem integração nativa.
* **Vim:** Plugins como ALE e neoformat podem ser configurados para usar essas ferramentas.
* **Emacs:** Pacotes como flycheck e prettier-mode fornecem suporte similar.

### Dicas Adicionais

* **Configuração:** Configure as ferramentas para que elas sigam as convenções de estilo do seu projeto.
* **Automatização:** Use ferramentas como `make` ou `npm scripts` para criar tarefas de formatação automatizadas.
* **Pré-commit:** Integre a formatação em seus hooks de pré-commit para garantir que o código sempre seja formatado antes de ser commitado.

### Por que Formatar o Código?

* **Legibilidade:** Código bem formatado é mais fácil de ler e entender.
* **Consistência:** Garante que todos os membros da equipe sigam o mesmo estilo de codificação.
* **Manutenção:** Facilita a identificação e correção de erros.
* **Colaboração:** Melhora a colaboração em projetos de código aberto.

