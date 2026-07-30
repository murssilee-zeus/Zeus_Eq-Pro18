[app]

title = Zeus EQ Pro18
package.name = zeuseqpro18
package.domain = org.zeus.audio

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,kt,java,xml

version = 1.0.0

requirements = python3,kivy,pyjnius

orientation = portrait

fullscreen = 0

android.permissions = FOREGROUND_SERVICE, FOREGROUND_SERVICE_MEDIA_PLAYBACK, MODIFY_AUDIO_SETTINGS, RECORD_AUDIO

android.api = 34
android.minapi = 28
android.sdk = 34
android.ndk = 25b

android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1
