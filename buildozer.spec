# Zeus EQ Pro18 - Buildozer Configuration File

[app]

# (str) Title of your application
title = Zeus EQ Pro18

# (str) Package name
package.name = zeuseqpro18

# (str) Package domain (needed for android/ios packaging)
package.domain = com.bearinmind

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json,wav,mp3

# (list) List of directory to exclude
source.exclude_dirs = tests, bin, .venv, .github, .git

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy==2.3.0,pyjnius,android

# (str) Custom source folders for requirements
android.add_src = android/src

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,RECORD_AUDIO,MODIFY_AUDIO_SETTINGS

# (int) Target Android API
android.api = 34

# (int) Minimum API required
android.minapi = 28

# (int) Android NDK version
android.ndk = 25b

# (bool) Use --private data storage
android.private_storage = True

# (list) The Android archs to build for
android.archs = arm64-v8a

# (bool) Enable AndroidX support
android.enable_androidx = True

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

# (str) The format used to package the app
android.release_artifact = apk
android.debug_artifact = apk

[buildozer]

# (int) Log level
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
