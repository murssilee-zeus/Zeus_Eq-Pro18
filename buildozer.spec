# Zeus EQ Pro18 - Buildozer Configuration File CORREGIDO

[app]

title = Zeus EQ Pro18
package.name = zeuseqpro18
package.domain = com.bearinmind
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json,wav,mp3
source.exclude_dirs = tests, bin, venv,.venv,.github,.git,.buildozer, __pycache__

version = 1.0.0

# --- REQUISITOS CORREGIDOS ---
# Usa recetas estables. Si te da error con pyjnius, quítalo de aquí y pon kivy==2.3.1
requirements = python3,kivy==2.3.1,pyjnius,android
# Si usas kivymd, agrégalo:,kivymd==1.1

# --- ICONO ---
# Si no tienes icon.png, comenta esta linea con #
# icon.filename = %(source.dir)s/icon.png

orientation = portrait
fullscreen = 0

# --- ANDROID ---
android.permissions = INTERNET,RECORD_AUDIO,MODIFY_AUDIO_SETTINGS
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.enable_androidx = True
android.accept_sdk_license = True
android.ant = auto

# --- ESTO ES LO QUE ARREGLA TU ERROR ---
p4a.branch = master
p4a.bootstrap = sdl2
# p4a para que no use python 3.14
p4a.fork = kivy
# Opcional pero recomendado
android.private_storage = True

# Si SÍ tienes la carpeta android/src con tu Java, descomenta esto:
# android.add_src = android/src

android.release_artifact = apk
android.debug_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
