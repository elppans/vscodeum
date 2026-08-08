import os
import urllib.parse
from gi.repository import Nautilus, GObject, Gio

class VSCodiumExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        super().__init__()

    def _open_in_codium(self, menu, file_path):
        # Executa o comando 'codium .' dentro da pasta correspondente
        Gio.AppInfo.launch_default_for_uri(f"file://{file_path}", None)
        os.system(f"cd '{file_path}' && codium . &")

    def get_background_items(self, *args):
        # args[0] em versões antigas era a janela, em versões recentes do Nautilus é o folder/file.
        # Para garantir compatibilidade com o Nautilus 43+, buscamos o diretório atual de forma segura.
        
        # O Nautilus passa o diretório atual no último argumento da lista
        current_folder = args[-1]
        
        if not current_folder or current_folder.is_directory() is False:
            return []

        # Extrai o caminho local da pasta vazia clicada
        uri = current_folder.get_uri()
        if uri.startswith("file://"):
            file_path = urllib.parse.unquote(uri[7:])
        else:
            return []

        # Cria o item do menu de contexto
        item = Nautilus.MenuItem(
            name="NautilusExtension::OpenCodiumBackground",
            label="Abrir pasta no VSCodium",
            tip="Abrir o diretório atual com VSCodium"
        )
        
        # Conecta o clique do botão à função que abre o Codium
        item.connect('activate', self._open_in_codium, file_path)
        
        return [item]
