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
     
   - Isso criará um arquivo `extensoes.txt` com a lista de extensões instaladas.

5. **Atalhos de teclado** (opcional):
   - Vá até `Arquivo` > `Preferências` > `Atalhos de Teclado`.
   - Clique no ícone de exportação no canto superior direito para salvar como `keybindings.json`.

### **Importando Configurações**
1. No novo ambiente, abra o VSCode/VSCodium.
2. Acesse o `settings.json` novamente e substitua pelo backup salvo.
3. Para restaurar as extensões, execute:
   ```sh
   cat extensoes.txt | xargs -L 1 code --install-extension
   ```
   >No VSCodium, o comando é `codium`
   
4. Caso tenha exportado atalhos, substitua o `keybindings.json` pelo backup.

- **Dica:** Você também pode sincronizar automaticamente com a conta Microsoft/GitHub usando a opção **Settings Sync** (`Ctrl + Shift + P` → "Turn on Settings Sync").
___
# Configurar a **Sincronização de Configurações** manualmente no **VSCode/VSCodium**

### **1 Habilitar o Settings Sync**
1. No **VSCode/VSCodium**, vá até:
   - **Menu** → `Gerenciar` (ícone de engrenagem no canto inferior esquerdo) → `Configurações` → Pesquise **Sync**.
   - Ou acesse diretamente:  
     **Arquivo** → **Preferências** → **Configurações**.

2. Role até encontrar a opção **"Configuração de Sincronização" (Settings Sync)**.

3. **Ative a sincronização** clicando em `Ativar`.

---

### **2 Escolher o que sincronizar**
- Na janela que aparece, escolha **quais configurações serão sincronizadas**:
  -  Configurações (`settings.json`)
  -  Extensões
  -  Atalhos (`keybindings.json`)
  -  Snippets
  -  Temas e Ícones

---

### **3 Conectar a uma conta**
- O VSCode pede para você **fazer login** com uma conta da **Microsoft** ou **GitHub**.
- **Se estiver usando o VSCodium** e não quiser uma conta, pode sincronizar manualmente copiando os arquivos mencionados antes (`settings.json`, `keybindings.json`, etc.).

---

### **4 Exportar e Importar Manualmente (Sem Conta)**
Se preferir **não usar a sincronização automática**, copie os seguintes arquivos:

 - **No Windows**  
Local dos arquivos:  
`%APPDATA%\Code\User\` *(VSCode)*  
`%APPDATA%\VSCodium\User\` *(VSCodium)*  

 - **No Linux/Mac**  
Local dos arquivos:  
`~/.config/Code/User/` *(VSCode)*  
`~/.config/VSCodium/User/` *(VSCodium)*  

- **Arquivos importantes para backup:**
  - `settings.json` → Configurações gerais.
  - `keybindings.json` → Atalhos de teclado.
  - `snippets/` → Snippets personalizados.
  - `extensions.json` (ou use `code/codium --list-extensions`).

 **Basta copiar esses arquivos para outro computador e substituir na mesma pasta**.

 Dessa forma, você pode sincronizar **sem precisar de conta**, apenas copiando e colando os arquivos entre máquinas.
___
# Se você não encontrou a opção de **Sincronização de Configurações (Settings Sync)**

Pode ser por alguns motivos, dependendo de qual versão do **VSCode/VSCodium** você está usando.  
---

### **1 Verifique se o Settings Sync está disponível**  
- **No VSCode:**  
A sincronização vem embutida no VSCode desde a versão **1.48**. Se estiver usando uma versão antiga, **atualize** para a mais recente.  

- **No VSCodium:**  
O VSCodium **não inclui** a sincronização de fábrica porque não usa os serviços da Microsoft. Porém, você pode sincronizar **manualmente** copiando os arquivos de configuração (explicado abaixo).  

---

### **2 Como acessar o Settings Sync manualmente** (somente no VSCode)  
Se você estiver usando **VSCode oficial** e não encontrou a opção no menu, tente:  

- 1 Vá para **Arquivo** → **Preferências** → **Configurações**  
- 2 No campo de busca, digite:  
   ```
   sync
   ```
- 3 Verifique se há a opção **Settings Sync** (ou "Sincronização de Configuração").  
- 4 Se aparecer, ative e escolha quais itens deseja sincronizar.  

---

### **3 Sincronizar manualmente no VSCodium ou VSCode sem conta**  
Se estiver no **VSCodium** ou quiser uma forma **sem precisar de conta**, siga este método:

- **Backup das Configurações**  
Copie os seguintes arquivos do seu computador atual:  

  - `settings.json` → Configurações gerais  
  - `keybindings.json` → Atalhos de teclado  
  - `snippets/` → Snippets personalizados  
  - `extensions.json` (ou use `code/codium --list-extensions`)  

- **Onde encontrar esses arquivos?**  

  - **Windows:**  
  ```
  %APPDATA%\Code\User\
  ```
  *(Ou `%APPDATA%\VSCodium\User\` no VSCodium)*  

  - **Linux/Mac:**  
  ```
  ~/.config/Code/User/
  ```
  *(Ou `~/.config/VSCodium/User/` no VSCodium)*  

- **Restauração em outro computador**  
No novo ambiente, basta **substituir** os arquivos na mesma pasta!  

---
# Extenção Settings Sync no VSCodium

Para o **VSCodium**, já que ele não tem a sincronização embutida como o VSCode, você pode usar a extensão [**"Settings Sync"**](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync) da [marketplace OpenVSX](https://marketplace.visualstudio.com/vscode).  

---

###  Como Usar a Extensão "Settings Sync" no VSCodium  

- 1 **Instalar a Extensão**  
  - Abra o VSCodium e vá até **Extensões** (`Ctrl + Shift + X`).  
  - Busque por **"Settings Sync"** e instale a extensão de **Shan Khan**.  
    - Se não encontrar na interface do VSCodium, rode este comando no terminal:  
    ```sh
    codium --install-extension Shan.code-settings-sync
    ```

- 2 **Configurar a Sincronização**  
  - Após instalar, pressione `Ctrl + Shift + P` e digite:  
  ```
  Sync: Configure
  ```
  - A extensão pedirá que você faça login no **GitHub Gist**.  
    - Se ainda não tem uma conta no GitHub, crie uma [aqui](https://github.com/).  
    - Autorize a extensão para acessar seus "Gists".

- 3 **Fazer Backup das Configurações**  
  - Após conectar sua conta, rode o comando:  
  ```
  Sync: Update / Upload Settings
  ```
  - Isso criará um arquivo Gist no seu GitHub com todas as configurações.

- 4 **Baixar as Configurações em Outro PC**  
  - No novo PC, instale a extensão novamente.  
  - Pressione `Ctrl + Shift + P` e escolha:  
  ```
  Sync: Download Settings
  ```
  - Ele buscará seu backup no GitHub e restaurará suas configurações!

---

###  O que essa extensão sincroniza?  
- `settings.json` (Configurações)  
- `keybindings.json` (Atalhos de teclado)  
- `snippets/` (Snippets personalizados)  
- Extensões instaladas  
- Ícones e Temas  
___

# Backup do VSCodium via Script no Linux

Você pode baixar e executar o script [backup_vscodium.sh](https://raw.githubusercontent.com/elppans/vscodeum/refs/heads/main/backup_vscodium.sh) no **$HOME** do usuário e fazer um backup dos arquivos de configuração e extenções.  

---

###  Baixando e Executando o Script  
1. **Baixe o script para o diretório `$HOME`**:  
   ```sh
   curl -o ~/backup_vscodium.sh https://raw.githubusercontent.com/elppans/vscodeum/refs/heads/main/backup_vscodium.sh
   ```
   *(Se `curl` não estiver instalado, use `wget` em vez disso:)*  
   ```sh
   wget -O ~/backup_vscodium.sh https://raw.githubusercontent.com/elppans/vscodeum/refs/heads/main/backup_vscodium.sh
   ```

2. **Dê permissão de execução**:  
   ```sh
   chmod +x ~/backup_vscodium.sh
   ```

3. **Execute o script**:  
   ```sh
   ~/backup_vscodium.sh
   ```

---

###  Dica: Criar um Alias para Facilidade
Se você pretende rodar o backup frequentemente, pode criar um **alias** no `.bashrc` ou `.zshrc`:  
```sh
echo "alias backupvsc='~/backup_vscodium.sh'" >> ~/.bashrc
source ~/.bashrc
```
Agora, sempre que quiser fazer um backup, basta rodar:  
```sh
backupvsc
```

---

##  Restaurando o Backup
1. **Extraia o backup para restaurar as configurações**:
   ```sh
   tar -xzvf ~/Backup_VSCodium/vscodium_backup_YYYYMMDD_HHMMSS.tar.gz -C ~/.config/VSCodium/User/
   ```
   *(Substitua `YYYYMMDD_HHMMSS` pelo nome do arquivo gerado.)*

2. **Restaurar as extensões instaladas**:
   ```sh
   cat ~/Backup_VSCodium/extensions_list.txt | xargs -L 1 codium --install-extension
   ```

Agora seu backup inclui tudo: **configurações + extensões!**   
___

- **Vídeos recomendados**  
  - [Não Precisamos Mais nos Preocupar em Reconfigurar o VS Code (2 FORMAS SIMPLES), Canal Código Fonte TV](https://www.youtube.com/watch?v=cTJY-z3TbTw)  
  - [Configurando o GitHub com o VS Code - Aprenda a Criar e Conectar Seus Projetos de Programação!, Canal Mestres da Web](https://www.youtube.com/watch?v=TrDBJ9HO3yE)  
