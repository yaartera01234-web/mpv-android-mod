# mpv-android — custom build (flat purple home + MX-style tap zones)

Base: upstream [mpv-android](https://github.com/mpv-android/mpv-android) master,
`versionCode 48` / `versionName 2026-09-17-release`.

**Video engine bilkul chhua nahi gaya** — saare 10 native `.so` official release APK ke saath
byte-identical hain (verify: `cmp` har file ka).

---

## Is build mein kya-kya hai

### 1. Home screen — flat purple (design #2)
* `res/layout/fragment_main_screen.xml` — naya layout: dark plum background, chhota flat logo,
  2×2 purple cards (Document tree / URL / File picker / Settings) + neeche "Remember choice" switch.
* `res/drawable/home_logo_flat.xml` — naya flat logo (gradient hata diya; purana `mpv_logo.xml`
  waisa hi hai, app icon bhi wahi rehta hai).
* `res/drawable/home_card_bg.xml` — solid purple card (ripple press effect), koi gradient nahi.
* `res/values/colors.xml` — naye `home_*` colours.
* `res/values/styles.xml` — `HomeCard` / `HomeCardText` / `HomeCardIcon` + `HomeTheme`.
* Buttons ke ids wahi hain (`docBtn`, `urlBtn`, `filepickerBtn`, `settingsBtn`, `switch1`),
  is liye `MainScreenFragment.kt` ko chhune ki zaroorat nahi padi.

### 2. Tap gestures — dono kaam karte hain
| Tap | Left | Center | Right |
|---|---|---|---|
| **Ek tap (naya)** | −10 sec | play/pause | +10 sec |
| **Do tap (mpv ka purana)** | −10 sec | play/pause | +10 sec |

* **Single tap zones** (`TouchGestures.kt`): naya code. Ek tap kaam karne se pehle 300 ms rukta hai
  (taake double tap pehle jeet jaye — warna ek double tap se 20 sec chala jata).
  Ek tap se control bar **nahi** khulti — bar ke liye **ungli dabaye rakho (long press)** ya pause kar do.
* **Pause karte hi control bar khud aa jati hai** (`MPVActivity.kt`).
* **Defaults ON** (`res/values/strings.xml`): `pref_gesture_tap_left/center/right_default`
  = `seek` / `playpause` / `seek` — yani **jise ye APK bhejo, usay koi setting nahi karni**.
* Switch mojood hai: **Settings → Gestures → "Single tap zones (MX style)"** (default ON.
  OFF karo to bilkul stock mpv jaisa behaviour — ek tap se bar).

### 3. Control bar (pehle se, subah ka kaam)
96 dp transparent 2-row bar — `res/layout/player.xml`, `res/values/{colors,styles,strings}.xml`,
13 drawables, `MPVActivity.kt` ki UI wiring.

---

## Build kaise karein

### GitHub Actions (recommended)
`ci/build-apk.yml` ko `.github/workflows/build.yml` mein copy karo (GitHub web UI → Add file →
Create new file → path ` .github/workflows/build.yml`). Phir Actions tab → **Build APK (arm64)** → Run.

### Local
```bash
git clone https://github.com/yaartera01234-web/mpv-android-mod
cd mpv-android-mod

# native libs (repo mein nahi hain - 31 MB)
curl -L -o mpv.apk https://github.com/mpv-android/mpv-android/releases/download/2026-09-17/app-default-arm64-v8a-release.apk
mkdir -p app/src/main/libs/arm64-v8a
unzip -j -o mpv.apk 'lib/arm64-v8a/*' -d app/src/main/libs/arm64-v8a

# JDK 21 + Android SDK 36 chahiye
echo "sdk.dir=$ANDROID_HOME" > local.properties
./gradlew :app:assembleDefaultDebug

# output (arm64 only ship karo, universal mat bhejo)
ls app/build/outputs/apk/default/debug/
```

### Signature (update-install)
Purana installed APK `debug.keystore` (alias `androiddebugkey`, password `android`) se signed tha.
Usi key se sign karo warna app uninstall karni paregi:
```bash
$ANDROID_HOME/build-tools/36.0.0/zipalign -p -f 4 app-default-arm64-v8a-debug.apk aligned.apk
$ANDROID_HOME/build-tools/36.0.0/apksigner sign --ks debug.keystore --ks-pass pass:android \
    --key-pass pass:android --ks-key-alias androiddebugkey --out final.apk aligned.apk
```


---

## v2 fix (2026-09-24) — crash ka asal masla

Pehla build phone pe crash ho jata tha:

```
InflateException: Binary XML file line #40 in layout/fragment_main_screen:
You must supply a layout_width attribute.
```

Wajah: `fragment_main_screen.xml` mein TextViews ka `layout_width`/`layout_height`
sirf `HomeCardText` style se aa raha tha — Android **LayoutParams in attributes ko
style se nahi padhta**, sirf element ke upar likhe hue attributes padhta hai.
Isi liye home screen inflate hote hi app band ho jati thi.

**Fix:** ab har view ke `layout_width` / `layout_height` / `layout_weight` layout XML mein
inline hain. Styles mein sirf visual cheezein (background, textColor, letterSpacing...) hain.

### Test (Robolectric) — 6/6 PASS
```bash
./gradlew :app:testDefaultDebugUnitTest --tests "*UiSmokeTest*"
```
* `homeScreenInflates` — home screen inflate (yehi crash tha)
* `singleTapZones_fire` — left −10s / center play-pause / right +10s
* `doubleTap_firesOnce` — double tap sirf ek baar chalta hai
* `swipe_doesNotTap` — swipe se tap trigger nahi hota
* `longPress_doesNotTap` — long press se tap trigger nahi hota
* `gesturePrefsInflate` — Settings > Gestures screen


---

## v3 (2026-09-24) — double tap only

Pehle single-tap zones ghalti se default ON the (user ne double tap kaha tha). Ab:

| Tap | Kya hota hai |
|---|---|
| **Single tap** | control bar aati / chhup jati hai (stock mpv) |
| **Double tap** | left = −10 sec, center = play/pause, right = +10 sec — **default ON** |

Single tap zones ab **optional** hai: `Settings > Gestures > "Single tap zones (MX style)"`, default **OFF**.
On karne par ek tap se hi seek/pause hota hai (bar ke liye long-press).

Test: `singleTap_byDefault_doesNotSeek` — default haalat mein single tap se koi seek nahi hota.
