package `is`.xyz.mpv

import android.content.Context
import android.os.Looper
import android.view.MotionEvent
import android.view.View
import androidx.preference.Preference
import androidx.preference.PreferenceManager
import androidx.test.core.app.ApplicationProvider
import org.junit.Assert.*
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.Robolectric
import org.robolectric.RobolectricTestRunner
import org.robolectric.Shadows.shadowOf
import org.robolectric.annotation.Config
import java.time.Duration

@RunWith(RobolectricTestRunner::class)
@Config(sdk = [34])
class UiSmokeTest {

    private fun ctx(): Context = ApplicationProvider.getApplicationContext()

    /** virtual clock aage barhao (SystemClock.uptimeMillis bhi barhta hai) */
    private fun tick(ms: Long) = shadowOf(Looper.getMainLooper()).idleFor(Duration.ofMillis(ms))

    // ---------- 1. home screen inflate (yehi crash ho raha tha) ----------
    @Test
    fun homeScreenInflates() {
        val activity = Robolectric.buildActivity(MainActivity::class.java).setup().get()
        val fragment = activity.supportFragmentManager.fragments.firstOrNull()
        assertNotNull("fragment add nahi hua", fragment)
        val v = fragment!!.view
        assertNotNull("fragment view null", v)
        val root: View = v!!
        val ids = listOf(R.id.docBtn, R.id.urlBtn, R.id.filepickerBtn, R.id.settingsBtn, R.id.switch1, R.id.logo)
        for (id in ids) assertNotNull("view missing: $id", root.findViewById<View>(id))
        // cards clickable hain?
        for (id in ids.take(4)) assertTrue("clickable nahi: $id", root.findViewById<View>(id).isClickable)
        println("HOME SCREEN INFLATE OK - sab views mojood ✅")
    }

    // ---------- 2. Settings > Gestures screen ----------
    @Test
    fun gesturePrefsInflate() {
        val c = ctx()
        val screen = PreferenceManager(c).inflateFromResource(c, R.xml.pref_gestures, null)
        assertNotNull(screen)
        val sw: Preference? = screen.findPreference("gesture_single_tap_zones")
        assertNotNull("single tap switch nahi mila", sw)
        println("GESTURES SCREEN OK - switch mojood ✅")
    }

    // ---------- 3. tap zones ----------
    private class Rec {
        val events = mutableListOf<Pair<PropertyChange, Float>>()
        fun observer() = object : TouchGesturesObserver {
            override fun onPropertyChange(p: PropertyChange, diff: Float) {
                events += p to diff
            }
        }
    }

    private fun ev(action: Int, x: Float, y: Float, t: Long): MotionEvent =
        MotionEvent.obtain(t, t, action, x, y, 0)

    private fun newGestures(rec: Rec): TouchGestures {
        val g = TouchGestures(rec.observer())
        g.syncSettings(PreferenceManager.getDefaultSharedPreferences(ctx()), ctx().resources)
        g.setMetrics(1080f, 1920f)
        return g
    }

    private fun tap(g: TouchGestures, x: Float, y: Float) {
        val t = android.os.SystemClock.uptimeMillis()
        g.onTouchEvent(ev(MotionEvent.ACTION_DOWN, x, y, t))
        g.onTouchEvent(ev(MotionEvent.ACTION_UP, x, y, t + 20))
    }

    @Test
    fun singleTapZones_fire() {
        tick(5000) // clock ko sane value pe le jao
        val rec = Rec(); val g = newGestures(rec)

        tap(g, 100f, 900f)                       // LEFT
        tick(600)
        assertEquals("left tap = -10s", listOf(PropertyChange.SeekFixed to -1f), rec.events)

        rec.events.clear(); tick(2000)
        tap(g, 540f, 900f)                       // CENTER
        tick(600)
        assertEquals("center tap = play/pause", listOf(PropertyChange.PlayPause to 0f), rec.events)

        rec.events.clear(); tick(2000)
        tap(g, 980f, 900f)                       // RIGHT
        tick(600)
        assertEquals("right tap = +10s", listOf(PropertyChange.SeekFixed to 1f), rec.events)
        println("SINGLE TAP ZONES OK ✅ (left -10s, center pause, right +10s)")
    }

    @Test
    fun doubleTap_firesOnce() {
        tick(5000)
        val rec = Rec(); val g = newGestures(rec)

        tap(g, 980f, 900f)      // pehla tap
        tick(120)               // 300ms se kam - double tap window
        tap(g, 980f, 900f)      // doosra tap
        tick(600)

        assertEquals("double tap = sirf ek event", 1, rec.events.size)
        assertEquals(PropertyChange.SeekFixed, rec.events[0].first)
        assertEquals(1f, rec.events[0].second, 0.001f)
        println("DOUBLE TAP OK ✅ (ek hi baar chalta hai, do bar nahi)")
    }

    @Test
    fun swipe_doesNotTap() {
        tick(5000)
        val rec = Rec(); val g = newGestures(rec)
        val t = android.os.SystemClock.uptimeMillis()
        g.onTouchEvent(ev(MotionEvent.ACTION_DOWN, 500f, 900f, t))
        g.onTouchEvent(ev(MotionEvent.ACTION_MOVE, 820f, 900f, t + 60))
        g.onTouchEvent(ev(MotionEvent.ACTION_UP, 880f, 900f, t + 90))
        tick(800)
        val taps = rec.events.filter { it.first == PropertyChange.SeekFixed || it.first == PropertyChange.PlayPause }
        assertTrue("swipe pe tap nahi hona chahiye, mila: $taps", taps.isEmpty())
        println("SWIPE OK ✅ (swipe se seek nahi hota, sirf drag-seek)")
    }

    @Test
    fun longPress_doesNotTap() {
        tick(5000)
        val rec = Rec(); val g = newGestures(rec)
        val t = android.os.SystemClock.uptimeMillis()
        g.onTouchEvent(ev(MotionEvent.ACTION_DOWN, 540f, 900f, t))
        tick(900)                                   // ungli dabi rahi -> long press
        g.onTouchEvent(ev(MotionEvent.ACTION_UP, 540f, 900f, t + 900))
        tick(800)
        assertTrue("long press pe tap nahi hona chahiye: ${rec.events}", rec.events.isEmpty())
        println("LONG PRESS OK ✅ (bar khulne ke liye jagah bachi)")
    }
}
