mpv-android custom control bar - source patch
=============================================
Date: 2026-09-23
Base: upstream mpv-android master (versionCode 48 / versionName 2026-09-17-release)

What this is
------------
Only the UI layer was changed (control bar + new buttons). The video engine is untouched:
all 10 native .so files are byte-identical to the official release APK.

Changed / new files
-------------------
app/src/main/res/layout/player.xml            (transparent 2-row bar, 96 dp)
app/src/main/res/values/colors.xml            (+4 player colors)
app/src/main/res/values/styles.xml            (+PlayerBar / PlayerBarTransparent / PlayerIconButton / PlayerPlayButton / PlayerChip)
app/src/main/res/values/strings.xml           (+13 strings: back, lock, screenshot, delay, sliders...)
app/src/main/res/drawable/                    (13 new icons/drawables)
app/src/main/java/is/xyz/mpv/MPVActivity.kt   (UI only: bar buttons, aspect dialog, screenshot, brightness/volume slider panel, audio delay)
gradle.properties                             (local build tweak for 2 GB RAM machines - optional)

How to rebuild
--------------
1) git clone https://github.com/mpv-android/mpv-android
2) copy the files above over the same paths
3) native libs (not included, 31 MB) - extract from the official APK:
   https://github.com/mpv-android/mpv-android/releases/download/2026-09-17/app-default-arm64-v8a-release.apk
   -> unzip lib/arm64-v8a/*.so  into  app/src/main/jniLibs/arm64-v8a/
4) JAVA_HOME=<jdk21> ANDROID_HOME=<android-sdk> ./gradlew :app:assembleDefaultDebug

tools/  = preview generators (HTML/SVG mockups used for design approval)
Built APKs: see releases design-preview-1 (174 dp box) and design-preview-2 (transparent, 96 dp)
