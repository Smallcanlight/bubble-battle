[app]
title = 泡泡大作戰
package.name = bubblebattle
package.domain = org.smalllight
source.dir = .
source.include_exts = py,png,jpg,ttf,ogg,wav
version = 1.0
requirements = python3,pygame
orientation = landscape
fullscreen = 1
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a
android.accept_sdk_license = True
android.allow_backup = True
p4a.branch = v2024.01.21

[buildozer]
log_level = 2
warn_on_root = 0
