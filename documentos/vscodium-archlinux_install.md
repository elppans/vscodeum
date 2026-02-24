# Instalação do VSCodium no ArchLinux

- Modo de instalação escolhido:

Pacote: [vscodium-bin*AUR](https://aur.archlinux.org/packages/vscodium-bin)

> Versões binárias do VS Code sem marca/telemetria/licenciamento da MS.

Opcional: [vscodium-marketplace](https://aur.archlinux.org/packages/vscodium-marketplace)

> Habilitar o marketplace vscode no vscodium
> 
> > Não vejo necessidade, mas quem quiser testar, é por própria conta e risco.

- Instalação via yay (Recomendável)

```bash
yay -Syu vscodium-bin
```
___
## Pacotes opcionais recomendado

Lista de outros pacotes opcionais mas que ajudam muito, recomendados para instalar no sistema

- Um comparador de arquivos, diretórios, etc. CLI e GUI
```bash
sudo pacman --needed -S diffutils meld
```
- Formatadores e Lints para Shell, Java, CSS, etc.
```bash
sudo pacman --needed -S shfmt shellcheck prettier eslint stylelint
```

- Formatador Opcional para CSS (AUR)
```bash
sudo pacman --needed -S nodejs-csscomb
```
___
