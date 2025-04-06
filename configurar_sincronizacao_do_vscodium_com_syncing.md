# Configurar sincronização do VSCodium com Syncing

## 1. Criar um GitHub Personal Access Token

1. Acesse a página [Tokens de Acesso Pessoal do GitHub](https://github.com/settings/tokens) e clique em **"Gerar novo token"**.
2. Defina os parâmetros:
   - **Nome do token**: `VSCodium`
   - **Descrição**: Sincronização das configurações do VSCodium
   - **Expiração**: Sem expiração *(ou ajuste conforme necessidade)*
   - **Acesso ao repositório**: Apenas **repositórios públicos**
   - **Permissões**: **Gists**
3. Copie e guarde seu token em um local seguro. **Não compartilhe publicamente!**

## 2. Sincronizar configurações do VSCodium

### **Upload de configurações**
1. Pressione `CTRL + Shift + P` e digite `"upload"` na **Command Palette**.
2. Selecione **"Syncing: Upload Settings"**.
3. Insira seu **GitHub Personal Access Token** criado anteriormente.
4. Escolha um **Gist ID** já existente ou deixe em branco para criar um novo.
5. Concluído! Você pode visualizar suas configurações no seu [GitHub Gist](https://gist.github.com/).

### **Download de configurações**
1. Pressione `CTRL + Shift + P` e digite `"download"` na **Command Palette**.
2. Insira seu **GitHub Personal Access Token**.
3. Escolha um **Gist ID público** (caso queira baixar configurações de outra pessoa) ou insira seu próprio Gist ID.
4. Concluído! Suas configurações serão restauradas.

## 3. Configurar sincronização automática

1. Pressione `CTRL + Shift + P` e digite `"opensync"`, selecione **"Syncing: Open Syncing Settings"**.
2. Edite o arquivo `syncing.json` e adicione:
   ```json
   {
      "auto_sync": true
   }
   ```
3. Salve as alterações e reinicie o VSCodium para aplicá-las.

---

- Fonte:

[Marketplace.nonoroazoro.syncing](https://marketplace.visualstudio.com/items?itemName=nonoroazoro.syncing)  

