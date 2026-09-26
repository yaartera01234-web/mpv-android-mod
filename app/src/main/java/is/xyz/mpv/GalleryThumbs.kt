package `is`.xyz.mpv

import android.content.Context
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.os.Build
import android.os.Handler
import android.os.Looper
import android.provider.MediaStore
import android.util.LruCache
import android.util.Size
import java.util.concurrent.Executors

/**
 * Gallery thumbnails: background thread pool + memory cache.
 *
 * Android 10 (Q) se upar system ka apna thumbnail API use hota hai (loadThumbnail),
 * purane phones pe video ke liye MediaStore ka purana thumbnail API.
 * Jo na bane (HEVC / 10-bit / kharab file) us pe koi problem nahi — adapter icon dikha deta hai.
 */
object GalleryThumbs {

    private val pool = Executors.newFixedThreadPool(4)
    private val main = Handler(Looper.getMainLooper())

    private val cache = LruCache<String, Bitmap>(
        (Runtime.getRuntime().maxMemory() / 1024 / 8).toInt()
    ) {
        override fun sizeOf(key: String, value: Bitmap): Int = value.byteCount / 1024
    }

    fun load(context: Context, item: GItem, reqPx: Int, cb: (Bitmap?) -> Unit) {
        val key = item.uri.toString() + "@" + reqPx
        cache.get(key)?.let {
            cb(it)
            return
        }
        val app = context.applicationContext
        pool.execute {
            var bmp: Bitmap? = null
            try {
                bmp = loadSync(app, item, reqPx)
            } catch (t: Throwable) {
                bmp = null
            }
            val got = bmp
            if (got != null) cache.put(key, got)
            main.post { cb(got) }
        }
    }

    private fun loadSync(app: Context, item: GItem, reqPx: Int): Bitmap? {
        val cr = app.contentResolver

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
            try {
                return cr.loadThumbnail(item.uri, Size(reqPx, reqPx), null)
            } catch (t: Throwable) {
                // audio files / kharab media pe throw karta hai — niche fallback
            }
        }

        if (item.isVideo) {
            try {
                val opt = BitmapFactory.Options()
                opt.inPreferredConfig = Bitmap.Config.RGB_565
                @Suppress("DEPRECATION")
                val b = MediaStore.Video.Thumbnails.getThumbnail(
                    cr, item.id, MediaStore.Video.Thumbnails.MINI_KIND, opt
                )
                if (b != null) return b
            } catch (t: Throwable) {
            }
        }

        return null
    }
}
