# Maintainer: Marcelo K. <marcelo.elven@...>
# shellcheck disable=all

pkgname=vscodeum
pkgver=1.0.1
pkgrel=1
arch=('any')
license=('MIT')
depends=('bash' 'coreutils')
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
# if [ -e "${pkgname}.install" ]; then
	# install=${pkgname}.install
# elif [ -e "pkgbuild.install" ]; then
# 	install=pkgbuild.install
# fi

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
	local dirs=("usr")
	for dir in "${dirs[@]}"; do
		if [ -d "${srcdir}/${dir}" ]; then
			cp -a "${srcdir}/${dir}" "${pkgdir}/"
		fi
	done

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

# O "virt-gmod" foi removido.

# END
# }
# EOF
