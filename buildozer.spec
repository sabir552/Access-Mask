name: Build APK

on:
  push:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Install system dependencies
      run: |
        sudo apt update
        sudo apt install -y python3 python3-pip git zip unzip openjdk-17-jdk

    - name: Install Buildozer
      run: |
        pip3 install --user buildozer
        pip3 install --user cython

    - name: Build APK
      run: |
        ~/.local/bin/buildozer android debug

    - name: Upload APK
      uses: actions/upload-artifact@v4
      with:
        name: AccessMask-APK
        path: bin/*.apk
