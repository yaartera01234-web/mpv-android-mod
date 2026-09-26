package `is`.xyz.mpv

import android.content.Context
import android.graphics.drawable.GradientDrawable
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView


/** aesthetic: item ke hisaab se palette (accent bar / folder stack ke liye) */
private val PALETTE = arrayOf(
    intArrayOf(0xFFC084FC.toInt(), 0xFF8B5CF6.toInt()),
    intArrayOf(0xFF22D3EE.toInt(), 0xFF3B82F6.toInt()),
    intArrayOf(0xFFFF5EBC.toInt(), 0xFF8B72FF.toInt()),
    intArrayOf(0xFF34D399.toInt(), 0xFF0EA5E9.toInt()),
    intArrayOf(0xFFFBBF24.toInt(), 0xFFFF7A59.toInt())
)

private fun withA(c: Int): Int = (c and 0x00FFFFFF) or (0x73 shl 24)

private fun paletteFor(seed: Int): IntArray = PALETTE[((seed % PALETTE.size) + PALETTE.size) % PALETTE.size]

private fun thumbPx(ctx: Context): Int {
    val d = ctx.resources.displayMetrics.density
    return (128f * d).toInt()
}

private fun metaLine(it: GItem): String {
    val parts = ArrayList<String>(3)
    if (it.isVideo) {
        if (it.sizeBytes > 0) parts.add(GalleryData.fmtSize(it.sizeBytes))
        if (it.bucket.isNotEmpty()) parts.add(it.bucket)
    } else {
        if (it.sub.isNotEmpty()) parts.add(it.sub)
        if (it.sizeBytes > 0) parts.add(GalleryData.fmtSize(it.sizeBytes))
    }
    return parts.joinToString(" · ")
}

/** Grid view (Videos tab) — thumbnail tiles. */
class TileAdapter(private val onClick: (GItem) -> Unit) : RecyclerView.Adapter<TileAdapter.VH>() {

    private val items = ArrayList<GItem>()

    fun submit(list: List<GItem>) {
        items.clear()
        items.addAll(list)
        notifyDataSetChanged()
    }

    class VH(v: View) : RecyclerView.ViewHolder(v) {
        val img: ImageView = v.findViewById(R.id.gThumb)
        val icon: TextView = v.findViewById(R.id.gIcon)
        val dur: TextView = v.findViewById(R.id.gDur)
        val res: TextView = v.findViewById(R.id.gRes)
        val name: TextView = v.findViewById(R.id.gName)
        val meta: TextView = v.findViewById(R.id.gMeta)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): VH =
        VH(LayoutInflater.from(parent.context).inflate(R.layout.item_gallery_tile, parent, false))

    override fun getItemCount(): Int = items.size

    override fun onBindViewHolder(h: VH, position: Int) {
        val item = items[position]
        h.name.text = item.name
        h.meta.text = metaLine(item)
        h.dur.text = GalleryData.fmtDuration(item.durationMs)
        h.dur.visibility = if (h.dur.text.isNullOrEmpty()) View.GONE else View.VISIBLE
        val res = if (item.isVideo) GalleryData.fmtRes(item.width, item.height) else ""
        h.res.text = res
        h.res.visibility = if (res.isEmpty()) View.GONE else View.VISIBLE

        h.itemView.tag = item.uri
        h.img.setImageDrawable(null)
        h.img.visibility = View.INVISIBLE
        h.icon.visibility = View.VISIBLE
        h.icon.text = if (item.isVideo) "\uD83C\uDFAC" else "\uD83C\uDFB5"

        val cols = paletteFor(item.name.hashCode())
        val bar = h.itemView.findViewById<View>(R.id.gBar)
        bar?.let {
            val gd = GradientDrawable(GradientDrawable.Orientation.LEFT_RIGHT, cols)
            it.background = gd
            val w = h.itemView.context.resources.displayMetrics.density
            it.layoutParams.width = ((18 + (Math.abs(item.name.hashCode()) % 26)) * w).toInt()
        }

        val ctx = h.itemView.context
        GalleryThumbs.load(ctx, item, thumbPx(ctx)) { bmp ->
            if (h.itemView.tag == item.uri && bmp != null) {
                h.img.setImageBitmap(bmp)
                h.img.visibility = View.VISIBLE
                h.icon.visibility = View.GONE
            }
        }

        h.itemView.setOnClickListener { v ->
            val pos = h.bindingAdapterPosition
            if (pos in items.indices) onClick(items[pos])
        }
    }
}

/** List view (Music / Recent / folder ke andar ki files). */
class RowAdapter(private val onClick: (GItem) -> Unit) : RecyclerView.Adapter<RowAdapter.VH>() {

    private val items = ArrayList<GItem>()

    fun submit(list: List<GItem>) {
        items.clear()
        items.addAll(list)
        notifyDataSetChanged()
    }

    class VH(v: View) : RecyclerView.ViewHolder(v) {
        val img: ImageView = v.findViewById(R.id.gThumb)
        val icon: TextView = v.findViewById(R.id.gIcon)
        val name: TextView = v.findViewById(R.id.gName)
        val sub: TextView = v.findViewById(R.id.gSub)
        val action: TextView = v.findViewById(R.id.gAction)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): VH =
        VH(LayoutInflater.from(parent.context).inflate(R.layout.item_gallery_row, parent, false))

    override fun getItemCount(): Int = items.size

    override fun onBindViewHolder(h: VH, position: Int) {
        val item = items[position]
        h.name.text = item.name
        val subLine = if (item.isVideo) metaLine(item) else item.sub
        h.sub.text = subLine
        h.sub.visibility = if (subLine.isEmpty()) View.GONE else View.VISIBLE
        h.action.text = "\u25B6"

        h.itemView.tag = item.uri
        h.img.setImageDrawable(null)
        h.img.visibility = View.INVISIBLE
        h.icon.visibility = View.VISIBLE
        h.icon.text = if (item.isVideo) "\uD83C\uDFAC" else "\uD83C\uDFB5"

        val cols = paletteFor(item.name.hashCode())
        val bar = h.itemView.findViewById<View>(R.id.gBar)
        bar?.let {
            val gd = GradientDrawable(GradientDrawable.Orientation.LEFT_RIGHT, cols)
            it.background = gd
            val w = h.itemView.context.resources.displayMetrics.density
            it.layoutParams.width = ((18 + (Math.abs(item.name.hashCode()) % 26)) * w).toInt()
        }

        val ctx = h.itemView.context
        GalleryThumbs.load(ctx, item, thumbPx(ctx)) { bmp ->
            if (h.itemView.tag == item.uri && bmp != null) {
                h.img.setImageBitmap(bmp)
                h.img.visibility = View.VISIBLE
                h.icon.visibility = View.GONE
            }
        }

        h.itemView.setOnClickListener { v ->
            val pos = h.bindingAdapterPosition
            if (pos in items.indices) onClick(items[pos])
        }
    }
}

/** Folders tab — folder rows (kitni files hain). */
class FolderAdapter(private val onClick: (GFolder) -> Unit) : RecyclerView.Adapter<FolderAdapter.VH>() {

    private val items = ArrayList<GFolder>()

    fun submit(list: List<GFolder>) {
        items.clear()
        items.addAll(list)
        notifyDataSetChanged()
    }

    class VH(v: View) : RecyclerView.ViewHolder(v) {
        val name: TextView = v.findViewById(R.id.gName)
        val sub: TextView = v.findViewById(R.id.gSub)
        val action: TextView = v.findViewById(R.id.gAction)
        val count: TextView = v.findViewById(R.id.gCount)
        val st1: View = v.findViewById(R.id.st1)
        val st2: View = v.findViewById(R.id.st2)
        val st3: View = v.findViewById(R.id.st3)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): VH =
        VH(LayoutInflater.from(parent.context).inflate(R.layout.item_gallery_folder, parent, false))

    override fun getItemCount(): Int = items.size

    override fun onBindViewHolder(h: VH, position: Int) {
        val f = items[position]
        h.name.text = "\uD83D\uDCC1 " + f.name
        h.sub.text = f.count.toString() + " files"
        h.action.text = "\u203A"
        h.count.text = f.count.toString()

        // 3-layer stack: rang seed ke hisaab se, thoda aage-peeche
        val d = h.itemView.context.resources.displayMetrics.density
        val seed = f.name.hashCode()
        val c1 = paletteFor(seed)
        val c2 = paletteFor(seed + 1)
        val c3 = paletteFor(seed + 2)
        val alpha = (255 * 0.45f).toInt()
        h.st3.background = GradientDrawable(GradientDrawable.Orientation.TL_BR, intArrayOf(withA(c3[0]), withA(c3[1]))).apply { cornerRadius = 10 * d }
        h.st2.background = GradientDrawable(GradientDrawable.Orientation.TL_BR, intArrayOf(withA(c2[0]), withA(c2[1]))).apply { cornerRadius = 10 * d }
        h.st1.background = GradientDrawable(GradientDrawable.Orientation.TL_BR, c1).apply { cornerRadius = 10 * d }
        h.st3.translationX = 11 * d; h.st3.translationY = 6 * d
        h.st2.translationX = 5.5f * d; h.st2.translationY = 3 * d
        h.st1.translationX = 0f; h.st1.translationY = 0f

        h.itemView.setOnClickListener { v ->
            val pos = h.bindingAdapterPosition
            if (pos in items.indices) onClick(items[pos])
        }
    }
}
