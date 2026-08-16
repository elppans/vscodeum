# [vscode(um)](./vscode.md)

Repositório para documentar anotações sobre o VSCode e VSCodium, conforme pesquisa.  
Bom para iniciantes  
___

Há um arquivo de configuração interessante, do repositório [HyDE](https://github.com/HyDE-Project/HyDE). Vale testar:  

- [VSCodium/User/settings.json](https://raw.githubusercontent.com/HyDE-Project/HyDE/refs/heads/master/Configs/.config/VSCodium/User/settings.json)  

É a mesma configuração para os seguintes diretórios:  

```bash
~/.config/VSCodium/User
~/.config/Code/User
~/.config/Code - OSS/User
```

Porém, se o pacote for em Flatpak, o caminho é diferente. Foi testado com o VSCodium:  

```
~/.var/app/com.vscodium.codium/config/VSCodium/User/settings.json

```

Pode testar e modificar conforme as necessidades. Eu mesmo gosto da barra de Status, então deixei comentado a seguinte linha:

```ini
"workbench.activityBar.location": "top",
```
