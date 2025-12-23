[app]
title = AccessMask
package.name = accessmask
package.domain = org.accessmask
source.dir = .
source.include_exts = py
version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 1

android.permissions = CAMERA
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
