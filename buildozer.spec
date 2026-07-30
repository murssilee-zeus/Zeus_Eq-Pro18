[app]
title = Zeus EQ Pro18
package.name = zeuseqpro18
package.domain = com.bearinmind
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json,wav,mp3
source.exclude_dirs = tests, bin, venv,.venv,.github,.git,.buildozer, __pycache__
version = 1.0.0

# ESTO ES LO QUE ARREGLA EL ERROR DE PYTHON 3.14
requirements = hostpython3==3.11.9,python3==3.11.9,kivy==2.3.1,pyjnius,android
# Si tienes icon.png, descomenta la siguiente linea:
# icon.filename = %(source.dir)s/icon.png

orientation = portrait
fullscreen = 0
android.permissions = INTERNET,RECORD_AUDIO,MODIFY_AUDIO_SETTINGS
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.enable_androidx = True
android.accept_sdk_license = True
android.private_storage = True

# Esto fuerza a usar recetas compatibles
p4a.branch = master
p4a.bootstrap = sdl2
p4a.fork = kivy

# Tienes carpeta android/? Si SI tienes codigo Java, descomenta esto:
# android.add_src = android/src

android.release_artifact = apk
android.debug_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1