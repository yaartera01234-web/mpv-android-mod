package `is`.xyz.mpv

import android.Manifest
import android.content.Intent
import android.content.pm.PackageManager
import android.os.Build
import android.os.Bundle
import android.preference.PreferenceManager
import android.text.Editable
import android.text.TextWatcher
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.LinearLayout
import android.widget.TextView
import android.widget.Toast
import androidx.activity.OnBackPressedCallback
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import androidx.recyclerview.widget.GridLayoutManager
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

/**
 * MX-Player jaisa Gallery: Videos / Music / Folders / Recent.
 *
 * - List Android ke MediaStore se (koi scanning nahi)
 * - Thumbnails background thread + cache se
 * - Tap = file usi mpv player mein khulti hai (kuch bhi player mein badla nahi)
 * - Purana file browser (📁 button) waise hi mojood hai
 */
class GalleryActivity : AppCompatActivity() {

    private lateinit var list: RecyclerView
    private lateinit var statusText: TextView
    private lateinit var searchBox: EditText
    private lateinit var permBox: LinearLayout

    private lateinit var tabViews: List<TextView>

    private val tileAdapter = TileAdapter { play(it) }
    private val rowAdapter = RowAdapter { play(it) }
    private val folderAdapter = FolderAdapter { openFolder(it) }

    private var videos: List<GItem> = emptyList()
    private var music: List<GItem> = emptyList()
    private var recent: List<GItem> = emptyList()
    private var folders: List<GFolder> = emptyList()

    private var tab = TAB_VIDEOS
    private var sortMode = SORT_DATE
    private var query = ""
    private var openFolder: String? = null
    private var columns = 3
    private var loaded = false

    private val permLauncher = registerForActivityResult(
        ActivityResultContracts.RequestMultiplePermissions()
    ) { _ ->
        if (hasPermission()) {
            permBox.visibility = View.GONE
            loadData()
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(null)
        setContentView(R.layout.activity_gallery)

        list = findViewById(R.id.gridList)
        statusText = findViewById(R.id.statusText)
        searchBox = findViewById(R.id.searchBox)
        permBox = findViewById(R.id.permBox)
        tabViews = listOf(
            findViewById(R.id.tabVideos),
            findViewById(R.id.tabMusic),
            findViewById(R.id.tabFolders),
            findViewById(R.id.tabRecent)
        )

        val prefs = PreferenceManager.getDefaultSharedPreferences(this)
        columns = prefs.getInt(PREF_COLUMNS, 3)
        sortMode = prefs.getInt(PREF_SORT, SORT_DATE)

        list.setHasFixedSize(true)

        for ((i, v) in tabViews.withIndex()) {
            v.setOnClickListener { selectTab(i) }
        }

        findViewById<View>(R.id.btnSearch).setOnClickListener {
            if (searchBox.visibility == View.VISIBLE) {
                searchBox.setText("")
                searchBox.visibility = View.GONE
            } else {
                searchBox.visibility = View.VISIBLE
                searchBox.requestFocus()
            }
        }

        findViewById<View>(R.id.btnSort).setOnClickListener { showSortDialog() }

        findViewById<View>(R.id.btnGrid).setOnClickListener {
            columns = if (columns == 3) 2 else 3
            prefs.edit().putInt(PREF_COLUMNS, columns).apply()
            statusToast(getString(R.string.gallery_columns, columns))
            if (tab == TAB_VIDEOS && openFolder == null) setLayoutManager()
        }

        findViewById<View>(R.id.btnBrowse).setOnClickListener {
            try {
                startActivity(Intent(this, FilePickerActivity::class.java).apply {
                    putExtra("skip", FilePickerActivity.FILE_PICKER)
                })
            } catch (t: Throwable) {
            }
        }

        searchBox.addTextChangedListener(object : TextWatcher {
            override fun afterTextChanged(s: Editable?) {
                query = s?.toString()?.trim() ?: ""
                renderList()
            }

            override fun beforeTextChanged(s: CharSequence?, a: Int, b: Int, c: Int) {}
            override fun onTextChanged(s: CharSequence?, a: Int, b: Int, c: Int) {}
        })

        findViewById<Button>(R.id.permAllow).setOnClickListener {
            requestPermissionsNow()
        }
        findViewById<Button>(R.id.permBrowse).setOnClickListener {
            try {
                startActivity(Intent(this, FilePickerActivity::class.java).apply {
                    putExtra("skip", FilePickerActivity.FILE_PICKER)
                })
            } catch (t: Throwable) {
            }
        }

        onBackPressedDispatcher.addCallback(this, object : OnBackPressedCallback(true) {
            override fun handleOnBackPressed() {
                if (openFolder != null) {
                    openFolder = null
                    renderList()
                } else {
                    isEnabled = false
                    onBackPressedDispatcher.onBackPressed()
                }
            }
        })

        selectTab(TAB_VIDEOS)

        if (hasPermission()) {
            permBox.visibility = View.GONE
            loadData()
        } else {
            permBox.visibility = View.VISIBLE
            statusText.text = getString(R.string.gallery_no_permission)
        }
    }

    // ---------------------------------------------------------------- permission

    private fun requiredPerms(): Array<String> =
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU)
            arrayOf(Manifest.permission.READ_MEDIA_VIDEO, Manifest.permission.READ_MEDIA_AUDIO)
        else
            arrayOf(Manifest.permission.READ_EXTERNAL_STORAGE)

    private fun hasPermission(): Boolean = requiredPerms().all {
        ContextCompat.checkSelfPermission(this, it) == PackageManager.PERMISSION_GRANTED
    }

    private fun requestPermissionsNow() {
        try {
            permLauncher.launch(requiredPerms())
        } catch (t: Throwable) {
        }
    }

    // ---------------------------------------------------------------- tabs

    private fun selectTab(index: Int) {
        tab = index
        openFolder = null
        for ((i, v) in tabViews.withIndex()) {
            val on = i == index
            v.setBackgroundResource(if (on) R.drawable.gallery_chip_on else R.drawable.gallery_chip_off)
            v.setTextColor(
                ContextCompat.getColor(this, if (on) R.color.home_text else R.color.home_text_dim)
            )
        }
        setLayoutManager()
        renderList()
    }

    private fun setLayoutManager() {
        if (tab == TAB_VIDEOS && openFolder == null) {
            list.layoutManager = GridLayoutManager(this, columns)
            list.adapter = tileAdapter
        } else {
            list.layoutManager = LinearLayoutManager(this)
            if (openFolder != null)
                list.adapter = rowAdapter
            else if (tab == TAB_FOLDERS)
                list.adapter = folderAdapter
            else
                list.adapter = rowAdapter
        }
    }

    // ---------------------------------------------------------------- data

    private fun loadData() {
        statusText.text = getString(R.string.gallery_loading)
        Thread {
            val v = GalleryData.loadVideos(contentResolver)
            val m = GalleryData.loadAudio(contentResolver)
            val f = GalleryData.foldersOf(v)
            val r = (v + m).sortedByDescending { it.dateAddedSec }.take(80)
            runOnUiThread {
                if (isFinishing || isDestroyed) return@runOnUiThread
                videos = v
                music = m
                folders = f
                recent = r
                loaded = true
                renderList()
            }
        }.start()
    }

    private fun sortList(src: List<GItem>): List<GItem> = when (sortMode) {
        SORT_NAME -> src.sortedBy { it.name.lowercase() }
        SORT_DURATION -> src.sortedByDescending { it.durationMs }
        SORT_SIZE -> src.sortedByDescending { it.sizeBytes }
        else -> src.sortedByDescending { it.dateAddedSec }
    }

    private fun matches(it: GItem): Boolean =
        query.isEmpty() || it.name.contains(query, ignoreCase = true)

    private fun renderList() {
        if (!loaded) return

        val folder = openFolder
        if (folder != null) {
            val items = sortList(videos.filter { it.bucket == folder && matches(it) })
            rowAdapter.submit(items)
            statusText.text = getString(R.string.gallery_folder_status, folder, items.size)
            return
        }

        when (tab) {
            TAB_VIDEOS -> {
                val items = sortList(videos.filter { matches(it) })
                tileAdapter.submit(items)
                statusText.text = getString(R.string.gallery_videos_status, items.size)
            }
            TAB_MUSIC -> {
                val items = sortList(music.filter { matches(it) })
                rowAdapter.submit(items)
                statusText.text = getString(R.string.gallery_music_status, items.size)
            }
            TAB_FOLDERS -> {
                val items = folders.filter { query.isEmpty() || it.name.contains(query, ignoreCase = true) }
                folderAdapter.submit(items)
                statusText.text = getString(R.string.gallery_folders_status, items.size)
            }
            else -> {
                val items = sortList(recent.filter { matches(it) })
                rowAdapter.submit(items)
                statusText.text = getString(R.string.gallery_recent_status, items.size)
            }
        }

        if (list.adapter?.itemCount == 0)
            statusText.text = getString(R.string.gallery_empty)
    }

    // ---------------------------------------------------------------- actions

    private fun openFolder(f: GFolder) {
        openFolder = f.name
        setLayoutManager()
        renderList()
        list.scrollToPosition(0)
    }

    private fun play(it: GItem) {
        try {
            val i = Intent(Intent.ACTION_VIEW, it.uri)
            i.setClass(this, MPVActivity::class.java)
            startActivity(i)
        } catch (t: Throwable) {
            statusToast(getString(R.string.gallery_play_failed))
        }
    }

    private fun showSortDialog() {
        val labels = arrayOf(
            getString(R.string.gallery_sort_date),
            getString(R.string.gallery_sort_name),
            getString(R.string.gallery_sort_duration),
            getString(R.string.gallery_sort_size)
        )
        with(AlertDialog.Builder(this)) {
            setTitle(R.string.gallery_sort)
            setSingleChoiceItems(labels, sortMode) { dialog, which ->
                sortMode = which
                PreferenceManager.getDefaultSharedPreferences(this@GalleryActivity)
                    .edit().putInt(PREF_SORT, sortMode).apply()
                dialog.dismiss()
                renderList()
            }
            show()
        }
    }

    private fun statusToast(msg: String) {
        Toast.makeText(this, msg, Toast.LENGTH_SHORT).show()
    }

    companion object {
        private const val TAB_VIDEOS = 0
        private const val TAB_MUSIC = 1
        private const val TAB_FOLDERS = 2
        private const val TAB_RECENT = 3

        private const val SORT_DATE = 0
        private const val SORT_NAME = 1
        private const val SORT_DURATION = 2
        private const val SORT_SIZE = 3

        private const val PREF_COLUMNS = "GalleryActivity_columns"
        private const val PREF_SORT = "GalleryActivity_sort"
    }
}
