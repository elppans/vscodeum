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
Este arquivo consolida e substitui o conteúdo relacionado a SSH presente em arquivos anteriores do diretório `documentos`.
