[app]

# (Obligatorio) Nombre de tu aplicación
title = Zeus Eq Pro

# (Obligatorio) Nombre del paquete (en minúsculas, sin espacios)
package.name = zeuseqpro

# (Obligatorio) Dominio del paquete (usa tu nombre de usuario o proyecto)
package.domain = github.com.murssilee-zeus

# Versión de tu app
version = 1.0.0

# Punto de entrada: tu archivo principal de Python
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf

# Versión de Python RECOMENDADA (evita errores con 3.11/3.12)
python = 3.10

# Requisitos: agrega TODAS las librerías que usa tu app
requirements = python3,kivy==2.2.1

# Configuración Android (la que fallaba antes)
android.api = 33
android.ndk = 25b
android.sdk = 24
android.archs = arm64-v8a  # Solo compilamos para 64bits, evita quedarse sin memoria
android.minapi = 21
android.ndk_api = 21

# Permisos básicos, agrega los que necesites
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Configuración de compilación
buildozer_verbose = 2
log_level = 2

# Icono y orientación (ajusta a tu gusto)
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 0
memory_limit = 4096  # Más memoria para no cortarse la compilación
