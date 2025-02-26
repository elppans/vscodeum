#!/bin/bash

# Diretórios e arquivos importantes
CONFIG_DIR="$HOME/.config/VSCodium/User"
BACKUP_DIR="$HOME/Backup_VSCodium"
EXTENSIONS_FILE="extensions_list.txt"
BACKUP_FILE="vscodium_backup_$(date +%Y%m%d_%H%M%S).tar.gz"

# Criar diretório de backup (se não existir)
mkdir -p "$BACKUP_DIR"

# Salvar a lista de extensões instaladas
codium --list-extensions > "$BACKUP_DIR/$EXTENSIONS_FILE"

# Criar o pacote de backup incluindo configurações e lista de extensões
tar -czvf "$BACKUP_DIR/$BACKUP_FILE" -C "$CONFIG_DIR" . -C "$BACKUP_DIR" "$EXTENSIONS_FILE"

# Remover o arquivo temporário da lista de extensões
rm "$BACKUP_DIR/$EXTENSIONS_FILE"

# Mensagem de sucesso
echo "Backup criado com sucesso: $BACKUP_DIR/$BACKUP_FILE"
