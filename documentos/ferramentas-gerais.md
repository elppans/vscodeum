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
Este arquivo substitui e consolida o conteúdo anterior de `documentos/ferramentas.md`.