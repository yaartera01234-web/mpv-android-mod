package `is`.xyz.mpv

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

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
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): VH =
        VH(LayoutInflater.from(parent.context).inflate(R.layout.item_gallery_folder, parent, false))

    override fun getItemCount(): Int = items.size

    override fun onBindViewHolder(h: VH, position: Int) {
        val f = items[position]
        h.name.text = f.name
        h.sub.text = f.count.toString() + " files"
        h.action.text = "\u203A"
        h.itemView.setOnClickListener { v ->
            val pos = h.bindingAdapterPosition
            if (pos in items.indices) onClick(items[pos])
        }
    }
}
