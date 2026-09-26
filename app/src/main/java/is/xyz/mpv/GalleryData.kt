package `is`.xyz.mpv

import android.content.ContentResolver
import android.content.ContentUris
import android.database.Cursor
import android.net.Uri
import android.provider.MediaStore

/**
 * Gallery (MX-style media browser) ke liye data model + MediaStore queries.
 *
 * Sab kuch Android ke apne MediaStore index se aata hai — koi lambi scanning nahi,
 * jo gallery app use karti hai wahi index.
 */
data class GItem(
    val uri: Uri,
    val id: Long,
    val name: String,
    val sub: String,
    val durationMs: Long,
    val sizeBytes: Long,
    val dateAddedSec: Long,
    val isVideo: Boolean,
    val width: Int,
    val height: Int,
    val bucket: String,
    val albumId: Long
)

data class GFolder(
    val name: String,
    val count: Int,
    val sample: GItem?
)

object GalleryData {

    // ---------------------------------------------------------------- videos

    fun loadVideos(cr: ContentResolver): List<GItem> {
        val out = ArrayList<GItem>()
        val cols = arrayOf(
            MediaStore.Video.Media._ID,
            MediaStore.Video.Media.DISPLAY_NAME,
            MediaStore.Video.Media.DURATION,
            MediaStore.Video.Media.SIZE,
            MediaStore.Video.Media.DATE_ADDED,
            MediaStore.Video.Media.WIDTH,
            MediaStore.Video.Media.HEIGHT,
            MediaStore.Video.Media.BUCKET_DISPLAY_NAME
        )
        try {
            cr.query(
                MediaStore.Video.Media.EXTERNAL_CONTENT_URI, cols, null, null,
                MediaStore.Video.Media.DATE_ADDED + " DESC"
            )?.use { c ->
                while (c.moveToNext()) out.add(readVideo(c))
            }
        } catch (t: Throwable) {
            // permission nahi / vendor ka ajeeb behaviour — khali list theek hai
        }
        return out
    }

    private fun readVideo(c: Cursor): GItem {
        val id = c.getLong(0)
        val name = c.getString(1) ?: ""
        val dur = c.getLong(2)
        val size = c.getLong(3)
        val date = c.getLong(4)
        val w = c.getInt(5)
        val h = c.getInt(6)
        val bucket = c.getString(7) ?: ""
        val uri = ContentUris.withAppendedId(MediaStore.Video.Media.EXTERNAL_CONTENT_URI, id)
        return GItem(uri, id, name, bucket, dur, size, date, true, w, h, bucket, 0L)
    }

    // ---------------------------------------------------------------- music

    fun loadAudio(cr: ContentResolver): List<GItem> {
        val out = ArrayList<GItem>()
        val cols = arrayOf(
            MediaStore.Audio.Media._ID,
            MediaStore.Audio.Media.DISPLAY_NAME,
            MediaStore.Audio.Media.TITLE,
            MediaStore.Audio.Media.ARTIST,
            MediaStore.Audio.Media.DURATION,
            MediaStore.Audio.Media.SIZE,
            MediaStore.Audio.Media.DATE_ADDED,
            MediaStore.Audio.Media.ALBUM_ID
        )
        try {
            cr.query(
                MediaStore.Audio.Media.EXTERNAL_CONTENT_URI, cols,
                MediaStore.Audio.Media.IS_MUSIC + " != 0", null,
                MediaStore.Audio.Media.DATE_ADDED + " DESC"
            )?.use { c ->
                while (c.moveToNext()) out.add(readAudio(c))
            }
        } catch (t: Throwable) {
        }
        return out
    }

    private fun readAudio(c: Cursor): GItem {
        val id = c.getLong(0)
        val display = c.getString(1) ?: ""
        val title = c.getString(2) ?: ""
        val artist = c.getString(3) ?: ""
        val dur = c.getLong(4)
        val size = c.getLong(5)
        val date = c.getLong(6)
        val album = c.getLong(7)
        val name = if (title.isNotEmpty()) title else display
        val uri = ContentUris.withAppendedId(MediaStore.Audio.Media.EXTERNAL_CONTENT_URI, id)
        return GItem(uri, id, name, artist, dur, size, date, false, 0, 0, "", album)
    }

    // ---------------------------------------------------------------- folders

    /** Videos ko folder (bucket) ke hisab se group karta hai. */
    fun foldersOf(videos: List<GItem>): List<GFolder> {
        val map = LinkedHashMap<String, MutableList<GItem>>()
        for (v in videos) {
            val key = if (v.bucket.isNotEmpty()) v.bucket else "Unknown"
            map.getOrPut(key) { ArrayList() }.add(v)
        }
        return map.entries
            .map { GFolder(it.key, it.value.size, it.value.firstOrNull()) }
            .sortedByDescending { it.count }
    }

    // ---------------------------------------------------------------- formatting

    fun fmtDuration(ms: Long): String {
        if (ms <= 0) return ""
        val total = ms / 1000
        val h = total / 3600
        val m = (total % 3600) / 60
        val s = total % 60
        return if (h > 0) String.format("%d:%02d:%02d", h, m, s)
        else String.format("%d:%02d", m, s)
    }

    fun fmtSize(bytes: Long): String {
        if (bytes <= 0) return ""
        val mb = bytes / (1024.0 * 1024.0)
        return if (mb >= 1024) String.format("%.1f GB", mb / 1024.0)
        else if (mb >= 10) String.format("%.0f MB", mb)
        else String.format("%.1f MB", mb)
    }

    fun fmtRes(w: Int, h: Int): String {
        if (w <= 0 || h <= 0) return ""
        val shortSide = if (w < h) w else h
        return when {
            shortSide >= 2000 -> "${shortSide}p"
            shortSide >= 1000 -> "${shortSide}p"
            shortSide >= 700 -> "720p"
            shortSide >= 460 -> "480p"
            else -> "${shortSide}p"
        }
    }
}
