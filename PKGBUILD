# Maintainer: Marcelo K. <marcelo.elven@...>
# shellcheck disable=all

pkgname=vscodeum
_pkgname="${pkgname}"
datever="$(date +%y.%m.%d)"
daterel="$(date +%H%M)"
pkgver="${datever}"
pkgrel="${daterel}"
arch=('any')
license=('MIT')
depends=('bash' 'coreutils' 'nautilus-python')
optdepends=('flatpak: Support for managing extensions in Flatpak versions'
	'snapd: Support for managing extensions in Snap versions'
	'visual-studio-code-bin: Support for the official VS Code (Microsoft)'
	'code: Support for the Code - OSS version'
	'vscodium-bin: Support for VSCodium (Open Source)'
	'bash-completion: Autocomplete commands in Bash')
pkgdesc="It facilitates the export and import of extensions in VSCode and VScodium"
url="https://github.com/elppans/${pkgname}"
source=("git+${url}.git#branch=main")
sha256sums=('SKIP')
md5sums=('SKIP')

# Automatically detect and use the correct install file
if [ -e "${pkgname}.install" ]; then
	install=${pkgname}.install
elif [ -e "pkgbuild.install" ]; then
	install=pkgbuild.install
fi

pkgver() {
	cd "$srcdir/$_pkgname" || return 1
	printf 'r%s.%s' "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}
prepare() {
	cd "${srcdir}/${pkgname}"
	# Add any preparation steps here, if needed
	# For example: patch -p1 < "${srcdir}/patch-file.patch"
}
package() {
	cd "${srcdir}/${pkgname}"

	# Determine the correct source directory
	if [ -d "${pkgname}" ]; then
		srcdir="${srcdir}/${pkgname}/${pkgname}"
	else
		srcdir="${srcdir}/${pkgname}"
	fi

	# Install files
	local dirs=("usr" "etc")
	for dir in "${dirs[@]}"; do
		if [ -d "${srcdir}/${dir}" ]; then
			cp -a "${srcdir}/${dir}" "${pkgdir}/"
		fi
	done

	# Define Version
	CONFIG_FILE="${pkgdir}/etc/${pkgname}/${pkgname}.conf"

	if [ -f "$CONFIG_FILE" ]; then
		# 1. Se o arquivo estiver completamente vazio
		if [ ! -s "$CONFIG_FILE" ]; then
			echo "VERSION=\"${pkgver}\"" >"$CONFIG_FILE"

		# 2. Se já contiver a variável VERSION (com ou sem aspas/espaços)
		elif grep -qE '^[[:space:]]*VERSION=' "$CONFIG_FILE"; then
			sed -i -E "s/^[[:space:]]*VERSION=.*/VERSION=\"${pkgver}\"/" "$CONFIG_FILE"

		# 3. Se o arquivo não estiver vazio, mas a variável VERSION ainda não existir
		else
			echo "VERSION=\"${pkgver}\"" >>"$CONFIG_FILE"
		fi
	fi

	# Install license file if present
	if [ -f "LICENSE" ]; then
		install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
	fi

	# Install documentation if present
	if [ -f "README.md" ]; then
		install -Dm644 README.md "${pkgdir}/usr/share/doc/${pkgname}/README.md"
	fi
}
# cat > "${pkgname}.install" <<EOF
# post_install() {
# 	cat <<END

# O pacote foi instalado com sucesso...

# END
# }

# post_upgrade() {
#     post_install
# }

# post_remove() {

# 	cat <<END

# O "pacote" foi removido.

# END
# }
# EOF
