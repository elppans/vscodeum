# VSCodium marketplace

O pacote `vscodium-marketplace` é projetado para permitir o uso da extensão oficial do Marketplace da Microsoft no **VSCodium**, um editor de código aberto que é baseado no Visual Studio Code (VS Code), mas sem a telemetria e alguns outros recursos proprietários.

### **Finalidade e uso:**
Por padrão, o VSCodium não tem acesso ao Marketplace oficial da Microsoft para baixar extensões, devido a restrições de licenciamento. O pacote `vscodium-marketplace` modifica a configuração do VSCodium para permitir que ele acesse esse marketplace, possibilitando o download direto das extensões hospedadas lá. Isso é útil caso você precise de extensões que estão disponíveis apenas no Marketplace da Microsoft.

#### Como usar:
1. Instale o pacote `vscodium-marketplace` no ArchLinux, através de seu gerenciador de pacotes, como o `yay` ou o `pacman`.
2. Após a instalação, reinicie o VSCodium.
3. Agora, você deverá conseguir acessar o Marketplace diretamente na interface do VSCodium e instalar extensões como faria no VS Code.

### **Prós e contras:**

**Prós:**
- Acesso ao vasto catálogo de extensões no Marketplace oficial da Microsoft, incluindo as mais populares usadas por desenvolvedores.
- Facilita a personalização e o aumento da funcionalidade do VSCodium.

**Contras:**
- Pode levantar preocupações de licenciamento, já que o uso do Marketplace da Microsoft no VSCodium não é oficialmente suportado pela Microsoft.
- Ao utilizar o Marketplace oficial, há a possibilidade de compartilhar algumas informações com a Microsoft, o que pode contradizer o objetivo de privacidade do VSCodium.
- Algumas extensões podem não funcionar completamente ou apresentar problemas de compatibilidade no VSCodium, já que não é o ambiente original para o qual foram criadas.

Se você prioriza a privacidade e quer evitar qualquer interação com o ecossistema da Microsoft, pode optar por usar marketplaces de terceiros (como o Open VSX Registry). Caso contrário, o `vscodium-marketplace` pode ser uma solução prática para obter o melhor dos dois mundos.
___
