[app]
title = Zeus Eq Pro
package.name = zeuseqpro
package.domain = github.com.murssilee-zeus
version = 1.0.0

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf,otf

# FORZAMOS versión exacta compatible
python = 3.10
# Versiones que NO dependen del módulo cgi
requirements = python3==3.10.14,kivy==2.1.0

android.api = 33
android.ndk = 25b
android.sdk = 24
android.buildtools = 33.0.2
android.accept_sdk_license = True
android.archs = arm64-v8a
android.minapi = 21
android.ndk_api = 21

android.permissions = INTERNET, ACCESS_NETWORK_STATE

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 0
memory_limit = 4096
