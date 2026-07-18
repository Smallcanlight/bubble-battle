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
android.api = 34
android.minapi = 24
android.archs = arm64-v8a,armeabi-v7a
android.allow_backup = True
# 觸控與藍牙手把皆由 SDL2 原生支援,毋須額外權限

[buildozer]
log_level = 2
warn_on_root = 0
