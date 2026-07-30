[app]

# Nombre de tu aplicación
title = Zeus Eq Pro

# Datos obligatorios del paquete
package.name = zeuseqpro
package.domain = github.com.murssilee-zeus

# Versión
version = 1.0.0

# Ruta y archivos de tu código
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf,otf

# Versión de Python (compatible y sin fallos)
python = 3.10

# 📌 AGREGA AQUÍ TODAS LAS LIBRERÍAS QUE USA TU APP
# Ejemplo: requirements = python3,kivy==2.2.1,pillow,requests
requirements = python3,kivy==2.2.1

# Configuración Android CORREGIDA
android.api = 33
android.ndk = 25b
android.sdk = 24
android.buildtools = 33.0.2
android.accept_sdk_license = True
android.archs = arm64-v8a
android.minapi = 21
android.ndk_api = 21

# Permisos (agrega los que necesites)
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Apariencia
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 0
memory_limit = 4096
