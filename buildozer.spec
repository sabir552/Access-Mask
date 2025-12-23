[app]
title = AccessMask
package.name = accessmask
package.domain = org.accessmask
source.dir = ./python_app
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 1.0
requirements = python==3.9,kivy==2.2.1,kivymd==1.1.1,pyjnius,android
orientation = portrait
fullscreen = 0
android.permissions = CAMERA
android.api = 33
android.minapi = 28
android.ndk = 23.1.7779620
android.sdk = 33
android.archs = arm64-v8a,armeabi-v7a
android.allow_backup = false
android.accept_sdk_license = true
p4a.branch = master
p4a.options = --debug
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1
