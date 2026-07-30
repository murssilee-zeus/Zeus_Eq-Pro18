[app]

# (str) Title of your application
title = Zeus EQ Pro18

# (str) Package name
package.name = zeuseqpro18

# (str) Package domain (needed for android/ios packaging)
package.domain = org.zeus.audio

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (include JAVA and KT for native engine)
source.include_exts = py,png,jpg,kv,atlas,kt,java,xml

# (list) Application version
version = 1.0.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,pyjnius

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = FOREGROUND_SERVICE, FOREGROUND_SERVICE_MEDIA_PLAYBACK, MODIFY_AUDIO_SETTINGS, RECORD_AUDIO

# (str) Android NDK / SDK versions
android.api = 34
android.minapi = 28
android.sdk = 34
android.ndk = 25b

# (bool) Accept SDK license
android.accept_sdk_license = True

# (list) Additional Java source directories to include
android.add_src = android/src

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = disable, 1 = enable)
warn_on_root = 1
