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
>* O usuário utilizado é o mesmo configurado no arquivo `~/.ssh/config`
