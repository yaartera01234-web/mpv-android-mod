# final preview generator: bilkul transparent bar (Option A), exact as in the APK
src = open('/tmp/mkbar.py').read()
head = src[:src.index('# ---------- top bar (same in all) ----------')]
exec(head)   # gives: ICONS, syms(), icon(), txt(), seekbar(), chip(), rrect(), SW, SH, ACCENT

HALO = ('<radialGradient id="halo">'
        '<stop offset="0" stop-color="#000" stop-opacity="0.42"/>'
        '<stop offset="0.55" stop-color="#000" stop-opacity="0.20"/>'
        '<stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>')


def ib(name, cx, cy, size=22, halo=21):
    """icon button: soft halo behind + white icon (exactly like the app)"""
    return (f'<circle cx="{cx}" cy="{cy}" r="{halo}" fill="url(#halo)"/>'
            + icon(name, cx - size / 2.0, cy - size / 2.0, size))


def glow_text(x, y, t, size=12, anchor="start"):
    return (f'<text x="{x}" y="{y}" fill="#fff" font-size="{size}" font-family="sans-serif" '
            f'text-anchor="{anchor}" style="paint-order:stroke" stroke="#000000AA" stroke-width="2.6" '
            f'stroke-linejoin="round">{t}</text>')


def final_frame():
    barH = 96
    by = 393 - 10 - barH
    s = []
    # --- transparent top bar
    s.append(ib("back", 32, 36))
    s.append(glow_text(56, 41, "Big Buck Bunny 1080p", 13))
    for i, nm in enumerate(["lock", "pip", "more"]):
        s.append(ib(nm, 894 - 32 - 44 * (2 - i), 36))
    # --- row 1: position / seekbar / duration
    y1 = by + 4
    s.append(glow_text(20, y1 + 25, "00:11"))
    s.append(seekbar(62, y1 + 17, 894 - 62 - 62 - 6))
    s.append(glow_text(874, y1 + 25, "4:37:47", anchor="end"))
    # --- row 2: every button (same order as player.xml)
    order = [("aspect", "i"), ("subs", "i"), ("audio", "i"), ("delay", "i"),
             ("prev", "i"), ("PLAY", "p"), ("next", "i"),
             ("speed", "c"), ("dec", "c"), ("camera", "i"), ("bright", "i"),
             ("volume", "i"), ("lock", "i"), ("more", "i")]
    w = sum(44 if t == "i" else (56 if t == "p" else 66) for _, t in order)
    x = 10 + (874 - w) / 2.0
    cy = y1 + 40 + 29
    for nm, t in order:
        if t == "i":
            s.append(ib(nm, x + 22, cy)); x += 44
        elif t == "p":
            s.append(f'<circle cx="{x + 28}" cy="{cy}" r="28" fill="{ACCENT}"/>')
            s.append(icon("pause", x + 17, cy - 11, 22)); x += 56
        else:
            label = "1.00x" if nm == "speed" else "HW+"
            s.append(chip(x, cy - 17, 66, 34, label)); x += 66
    return "".join(s)


svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 894 393">'
       '<defs>' + syms() + HALO +
       '<linearGradient id="vid3" x1="0" y1="0" x2="1" y2="1">'
       '<stop offset="0" stop-color="#5b7fb8"/><stop offset="0.45" stop-color="#e0a944"/>'
       '<stop offset="1" stop-color="#7a4a8c"/></linearGradient></defs>'
       '<rect width="894" height="393" fill="url(#vid3)"/>'
       + txt(447, 150, "VIDEO (poori screen)", 14, "rgba(255,255,255,0.60)")
       + txt(447, 172, "transparent bar - koi black box nahi", 11, "rgba(255,255,255,0.40)")
       + final_frame() + '</svg>')

html = ('<!DOCTYPE html><html lang="ur"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>mpv - transparent bar (final)</title><style>'
        'body{margin:0;background:#0d0f13;color:#e8ecf3;font-family:system-ui,sans-serif;padding:14px 12px 40px}'
        'h1{font-size:19px;margin:2px 0 8px} p{font-size:13.5px;line-height:1.6;color:#b9c2d0}'
        '.scr{width:100%;height:auto;border-radius:10px;display:block}'
        '.note{background:#141c26;border:1px solid #24344a;border-radius:10px;padding:12px 14px;margin-top:16px;font-size:13.5px}'
        '</style></head><body>'
        '<h1>Final look — Bilkul Transparent bar (Option A)</h1>'
        '<p>Yeh bilkul wohi hai jo APK mein hai: <b>2 rows, 96 dp</b> (pehle 174 dp tha — aadha). '
        'Background zero; har icon ke peeche sirf halka sa halo hai taake bright video pe bhi icon saaf nazar aaye. '
        'Row 2 (left se): aspect · subs · audio · <b>delay (clock)</b> · prev · PLAY · next · '
        '<b>1.00x</b> · <b>HW+</b> · screenshot · brightness · volume · lock · ⋮ menu.</p>'
        + svg +
        '<div class="note"><b>Naya:</b> 🕐 <b>Delay</b> button seedha bar pe — tap karo, audio delay (-600 se +600) '
        'ka picker khul jayega. Long-press karne se Advanced menu (sub delay bhi wahin hai).</div>'
        '</body></html>')

open("/home/user/mpv_bar_final.html", "w").write(html)
open("/tmp/final.svg", "w").write(svg)
print("written:", len(html), "bytes")
