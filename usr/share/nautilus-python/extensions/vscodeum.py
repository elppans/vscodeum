import os
import subprocess
import shutil
import urllib.parse
from gi.repository import Nautilus, GObject


# ---------------------------------------------------------------------------
# Definição dos editores suportados e como detectá-los.
#   - native_cmd : nome do binário procurado no PATH (ex.: 'code', 'codium')
#   - flatpak_id : ID do aplicativo Flatpak
#   - snap_name  : nome do pacote snap (o binário fica em /snap/bin/<nome>)
#
# Prioridade quando o mesmo editor tem mais de uma forma de instalação:
#   nativo (deb/rpm/tar) > flatpak > snap
# ---------------------------------------------------------------------------
EDITORS = [
    {
        "key": "vscode",
        "label": {"pt": "VS Code", "en": "VS Code"},
        "native_cmd": "code",
        "flatpak_id": "com.visualstudio.code",
        "snap_name": "code",
    },
    {
        "key": "vscodium",
        "label": {"pt": "VSCodium", "en": "VSCodium"},
        "native_cmd": "codium",
        "flatpak_id": "com.vscodium.codium",
        "snap_name": "codium",
    },
]

STRINGS = {
    "pt": {
        "open_folder_bg": "Abrir pasta atual com {editor}",
        "open_folder": "Abrir pasta com {editor}",
        "open_file": "Abrir arquivo com {editor}",
        "open_selection": "Abrir {n} itens selecionados com {editor}",
    },
    "en": {
        "open_folder_bg": "Open current folder with {editor}",
        "open_folder": "Open folder with {editor}",
        "open_file": "Open file with {editor}",
        "open_selection": "Open {n} selected items with {editor}",
    },
}


def _get_language():
    """Detecta o idioma do sistema. Retorna 'pt' ou 'en'."""
    for var in ("LANGUAGE", "LC_ALL", "LC_MESSAGES", "LANG"):
        val = os.environ.get(var)
        if val:
            val = val.split(":")[0]
            return "pt" if val.lower().startswith("pt") else "en"
    return "en"


def _list_flatpak_apps():
    """Lista os IDs de aplicativos Flatpak instalados (sistema + usuário)."""
    apps = set()
    for scope in ("--system", "--user"):
        try:
            out = subprocess.check_output(
                ["flatpak", "list", scope, "--app", "--columns=application"],
                stderr=subprocess.DEVNULL,
                timeout=3,
            )
            apps.update(out.decode("utf-8", "ignore").splitlines())
        except Exception:
            continue
    return apps


def _detect_editors():
    """
    Detecta quais editores (VS Code / VSCodium) estão instalados e por qual
    meio (native, flatpak, snap), respeitando a prioridade native > flatpak > snap.

    Retorna uma lista de dicts: {"key", "label", "source", "cmd": [...]}
    """
    flatpak_apps = None  # calculado sob demanda (lazy) para evitar custo desnecessário
    found = []

    for editor in EDITORS:
        # 1) Binário nativo no PATH (mas cuidado: em muitas distros /snap/bin
        #    também está no PATH, então um "which" positivo pode na verdade
        #    ser um snap. Filtramos esse caso.)
        which_path = shutil.which(editor["native_cmd"])
        if which_path and not which_path.startswith("/snap/"):
            found.append({
                "key": editor["key"],
                "label": editor["label"],
                "source": "native",
                "cmd": [which_path],
            })
            continue

        # 2) Snap (binário explícito em /snap/bin/<nome>)
        snap_path = "/snap/bin/{}".format(editor["snap_name"])
        is_snap = which_path is not None and which_path.startswith("/snap/")
        if not is_snap and os.path.exists(snap_path):
            is_snap = True
            which_path = snap_path

        # 3) Flatpak
        if flatpak_apps is None:
            flatpak_apps = _list_flatpak_apps()
        is_flatpak = editor["flatpak_id"] in flatpak_apps

        # Prioridade entre as alternativas restantes: flatpak > snap
        if is_flatpak:
            found.append({
                "key": editor["key"],
                "label": editor["label"],
                "source": "flatpak",
                "cmd": ["flatpak", "run", editor["flatpak_id"]],
            })
        elif is_snap:
            found.append({
                "key": editor["key"],
                "label": editor["label"],
                "source": "snap",
                "cmd": [which_path or snap_path],
            })

    return found


def _uri_to_path(uri):
    if uri and uri.startswith("file://"):
        return urllib.parse.unquote(uri[7:])
    return None


class VSCodiumExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        super().__init__()
        # Detecta idioma e editores instalados uma única vez.
        self._lang = _get_language()
        self._editors = _detect_editors()

    # -----------------------------------------------------------------
    # Ação: abre o(s) caminho(s) informado(s) com o editor escolhido.
    # -----------------------------------------------------------------
    def _open_with_editor(self, menu, paths, editor):
        cmd = list(editor["cmd"]) + list(paths)
        try:
            subprocess.Popen(
                cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                stdin=subprocess.DEVNULL,
                start_new_session=True,
            )
        except Exception:
            # Se algo falhar (ex.: binário sumiu entre a detecção e o clique),
            # falha silenciosamente para não travar o Nautilus.
            pass

    def _make_item(self, name_suffix, label, editor, paths):
        item = Nautilus.MenuItem(
            name="NautilusExtension::{}::{}".format(name_suffix, editor["key"]),
            label=label,
            tip=label,
        )
        item.connect("activate", self._open_with_editor, paths, editor)
        return item

    # -----------------------------------------------------------------
    # Menu de contexto em área vazia (fundo) de uma pasta.
    # -----------------------------------------------------------------
    def get_background_items(self, *args):
        if not self._editors:
            return []

        current_folder = args[-1]
        if not current_folder or not current_folder.is_directory():
            return []

        path = _uri_to_path(current_folder.get_uri())
        if not path:
            return []

        strings = STRINGS[self._lang]
        items = []
        for editor in self._editors:
            label = strings["open_folder_bg"].format(editor=editor["label"][self._lang])
            items.append(self._make_item("OpenBackground", label, editor, [path]))
        return items

    # -----------------------------------------------------------------
    # Menu de contexto sobre item(ns) selecionado(s): arquivo(s) e/ou pasta(s).
    # -----------------------------------------------------------------
    def get_file_items(self, *args):
        if not self._editors:
            return []

        files = args[-1]
        if not files:
            return []

        paths = []
        for f in files:
            path = _uri_to_path(f.get_uri())
            if path:
                paths.append(path)

        if not paths:
            return []

        strings = STRINGS[self._lang]

        if len(paths) == 1:
            is_dir = files[0].is_directory()
            key = "open_folder" if is_dir else "open_file"
        else:
            key = "open_selection"

        items = []
        for editor in self._editors:
            editor_label = editor["label"][self._lang]
            if key == "open_selection":
                label = strings[key].format(n=len(paths), editor=editor_label)
            else:
                label = strings[key].format(editor=editor_label)
            items.append(self._make_item("OpenSelection", label, editor, paths))
        return items