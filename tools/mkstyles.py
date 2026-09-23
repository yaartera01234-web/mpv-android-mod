# -*- coding: utf-8 -*-
ACCENT="#3EA6FF"
ICONS = {
 "aspect":"M19,12h-2v3h-3v2h5v-5zM7,9h3V7H5v5h2V9zM21,3H3c-1.1,0 -2,0.9 -2,2v14c0,1.1 0.9,2 2,2h18c1.1,0 2,-0.9 2,-2V5c0,-1.1 -0.9,-2 -2,-2zM21,19.01H3V4.99h18v14.02z",
 "subs":"M20,4H4c-1.1,0 -2,0.9 -2,2v12c0,1.1 0.9,2 2,2h16c1.1,0 2,-0.9 2,-2V6c0,-1.1 -0.9,-2 -2,-2zM4,12h4v2H4v-2zM14,18H4v-2h10v2zM20,18h-4v-2h4v2zM20,14H10v-2h10v2z",
 "audio":"M12,3v10.55c-0.59,-0.34 -1.27,-0.55 -2,-0.55 -2.21,0 -4,1.79 -4,4s1.79,4 4,4 4,-1.79 4,-4V7h4V3h-6z",

 "prev":"M6,6h2v12H6V6zM9.5,12l8.5,6V6L9.5,12z",
 "next":"M6,18l8.5,-6L6,6v12zM16,6v12h2V6h-2z",
 "play":"M8,5v14l11,-7z",
 "pause":"M6,19h4V5H6v14zM14,5v14h4V5h-4z",
 "camera":"M9,2L7.17,4H4c-1.1,0 -2,0.9 -2,2v12c0,1.1 0.9,2 2,2h16c1.1,0 2,-0.9 2,-2V6c0,-1.1 -0.9,-2 -2,-2h-3.17L15,2H9zm3,15c-2.76,0 -5,-2.24 -5,-5s2.24,-5 5,-5 5,2.24 5,5 -2.24,5 -5,5zm0,-2.5c1.38,0 2.5,-1.12 2.5,-2.5s-1.12,-2.5 -2.5,-2.5 -2.5,1.12 -2.5,2.5 1.12,2.5 2.5,2.5z",
 "bright":"M20,8.69V4h-4.69L12,0.69 8.69,4H4v4.69L0.69,12 4,15.31V20h4.69L12,23.31 15.31,20H20v-4.69L23.31,12 20,8.69zM12,18c-3.31,0 -6,-2.69 -6,-6s2.69,-6 6,-6 6,2.69 6,6 -2.69,6 -6,6zM12,8v8c2.21,0 4,-1.79 4,-4s-1.79,-4 -4,-4z",
 "volume":"M3,9v6h4l5,5V4L7,9H3zm13.5,3c0,-1.77 -1.02,-3.29 -2.5,-4.03v8.05c1.48,-0.73 2.5,-2.25 2.5,-4.02zM14,3.23v2.06c2.89,0.86 5,3.54 5,6.71s-2.11,5.85 -5,6.71v2.06c4.01,-0.91 7,-4.49 7,-8.77s-2.99,-7.86 -7,-8.77z",
 "lock":"M18,8h-1L17,6c0,-2.76 -2.24,-5 -5,-5S7,3.24 7,6v2L6,8c-1.1,0 -2,0.9 -2,2v10c0,1.1 0.9,2 2,2h12c1.1,0 2,-0.9 2,-2L20,10c0,-1.1 -0.9,-2 -2,-2zM12,17c-1.1,0 -2,-0.9 -2,-2s0.9,-2 2,-2 2,0.9 2,2 -0.9,2 -2,2zM15.1,8L8.9,8L8.9,6c0,-1.71 1.39,-3.1 3.1,-3.1 1.71,0 3.1,1.39 3.1,3.1v2z",
 "more":"M12,8c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2zm0,2c-1.1,0 -2,0.9 -2,2s0.9,2 2,2 2,-0.9 2,-2 -0.9,-2 -2,-2zm0,6c-1.1,0 -2,0.9 -2,2s0.9,2 2,2 2,-0.9 2,-2 -0.9,-2 -2,-2z",
 "back":"M20,11H7.83l5.59,-5.59L12,4l-8,8 8,8 1.41,-1.41L7.83,13H20v-2z",
 "pip":"M19,11h-8v6h8v-6zM21,3H3c-1.1,0 -2,0.9 -2,2v14c0,1.1 0.9,2 2,2h18c1.1,0 2,-0.9 2,-2V5c0,-1.1 -0.9,-2 -2,-2zM21,19.02H3V4.98h18v14.04z",
 "speed":"M20.38,8.57l-1.23,1.23a8.5,8.5 0,0 1,0 11.77h2.84A10.9,10.9 0,0 0,22 12c0,-1.22 -0.2,-2.4 -0.58,-3.49l-1.04,0.06zM11,4v5.15L2.74,2.74 1.33,4.15 8.5,11.32 3.5,16.32 4.91,17.73 12,10.65l7.09,7.08 1.41,-1.41 -9.5,-9.5V4h-1z",
}
def syms():
    out=[]
    for k,d in ICONS.items():
        out.append(f'<symbol id="i-{k}" viewBox="0 0 24 24"><path d="{d}"/></symbol>')
    # clock icon for audio delay: stroked, so it renders reliably
    out.append('<symbol id="i-delay" viewBox="0 0 24 24">'
               '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/>'
               '<path d="M12,6.5v6l4,2.2" fill="none" stroke="currentColor" stroke-width="2" '
               'stroke-linecap="round" stroke-linejoin="round"/></symbol>')
    return "".join(out)

def icon(name,x,y,size,color="#fff",op=1.0):
    return f'<use href="#i-{name}" x="{x}" y="{y}" width="{size}" height="{size}" fill="{color}" opacity="{op}"/>'

BAR="rgba(10,10,12,0.82)"; EDGE="rgba(255,255,255,0.14)"
def rrect(x,y,w,h,r,fill= BAR,stroke=EDGE):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="1"/>'
def txt(x,y,t,size=11,fill="#fff",anchor="middle",weight="normal"):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" font-family="sans-serif" text-anchor="{anchor}" font-weight="{weight}">{t}</text>'
def chip(x,y,w,h,label):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="rgba(255,255,255,0.10)" stroke="rgba(255,255,255,0.18)"/>'
            + txt(x+w/2,y+h/2+4,label,11))
def seekbar(x,y,w,progress=0.34):
    p=x+w*progress
    return (f'<rect x="{x}" y="{y}" width="{w}" height="4" rx="2" fill="rgba(255,255,255,0.22)"/>'
            f'<rect x="{x}" y="{y}" width="{w*progress:.1f}" height="4" rx="2" fill="{ACCENT}"/>'
            f'<circle cx="{p:.1f}" cy="{y+2}" r="7" fill="#fff" stroke="{ACCENT}" stroke-width="2"/>')

SW, SH = 894, 393    # landscape screen in dp
def screen(bars_svg, label, note=""):
    return f'''<figure>
<svg viewBox="0 0 {SW} {SH}" class="scr" xmlns="http://www.w3.org/2000/svg">
 <defs>{syms()}<linearGradient id="vid" x1="0" y1="0" x2="0" y2="1">
   <stop offset="0" stop-color="#2b3038"/><stop offset="0.5" stop-color="#8a6a2a"/><stop offset="1" stop-color="#1a1c22"/></linearGradient></defs>
 <rect width="{SW}" height="{SH}" fill="url(#vid)"/>
 {txt(SW/2,SH/2-30,"VIDEO AREA",13,"rgba(255,255,255,0.35)")}
 {bars_svg}
</svg>
<figcaption><b>{label}</b>{note}</figcaption>
</figure>'''


SHADOW = ('<filter id="ish" x="-40%" y="-40%" width="180%" height="180%">'
          '<feDropShadow dx="0" dy="1" stdDeviation="1.6" flood-color="#000" flood-opacity="0.85"/></filter>')

def icon_shadow(name,x,y,size,color="#fff"):
    return (f'<g filter="url(#ish)"><use href="#i-{name}" x="{x}" y="{y}" width="{size}" height="{size}" '
            f'fill="{color}" color="{color}"/></g>')

def bg_rect(mode, by, bh):
    if mode == "none":
        return ""
    if mode == "solid":
        return rrect(10, by, 874, bh, 16)
    if mode == "glass":
        return (f'<rect x="10" y="{by}" width="874" height="{bh}" rx="16" fill="rgba(10,10,12,0.40)" '
                f'stroke="rgba(255,255,255,0.12)" stroke-width="1"/>')
    if mode == "fade":
        return f'<rect x="0" y="{by-18}" width="{SW}" height="{SH-(by-18)}" fill="url(#fadebot)"/>'
    return ""

def topbar(h, mode):
    M=10; y=M
    if mode == "solid":
        bg = rrect(M,y,SW-2*M,h,16)
    elif mode == "glass":
        bg = (f'<rect x="{M}" y="{y}" width="{SW-2*M}" height="{h}" rx="16" '
              f'fill="rgba(10,10,12,0.40)" stroke="rgba(255,255,255,0.12)"/>')
    elif mode == "fade":
        bg = f'<rect x="0" y="0" width="{SW}" height="{y+h+16}" fill="url(#fadetop)"/>'
    else:
        bg = ""
    ic = icon_shadow if mode == "none" else icon
    s=[bg]
    s.append(ic("back",M+12,y+h/2-11,22))
    s.append(txt(M+44,y+h/2+5,"Big Buck Bunny 1080p",13,anchor="start"))
    x=SW-M-11-44*3
    for nm in ["lock","pip","more"]:
        s.append(ic(nm,x+11,y+h/2-11,22)); x+=44
    return "".join(s)

def rows_bottom(by, mode, barH):
    """returns rows svg for given bar; layout A (2 rows) or C (single row)"""
    M=10
    ic = icon_shadow if mode == "none" else icon
    s=[]
    if barH <= 70:   # Option C single row
        y=by+8; x=M+8
        s.append(ic("prev",x,y+12,22)); x+=34
        s.append(txt(x+17,y+35,"00:11",11)); x+=34
        icons=["aspect","subs","audio","delay","camera","bright","volume","lock","more"]
        fixed = 34+34+40+40+52+62 + 38*len(icons)
        sbw = SW-2*M-8-fixed
        s.append(seekbar(x,y+22,sbw)); x=x+sbw+6
        s.append(txt(x+20,y+35,"4:37:47",11)); x+=40
        s.append(ic("next",x,y+12,22)); x+=40
        s.append(f'<circle cx="{x+23}" cy="{y+22}" r="23" fill="{ACCENT}"/>')
        s.append(icon("pause",x+13,y+12,20)); x+=52
        s.append(chip(x,y+10,62,32,"1.00x")); x+=62
        for nm in icons:
            s.append(ic(nm,x+8,y+11,22)); x+=38
        return "".join(s)
    # Option A: seek row + one tools row (play in middle)
    y=by+6
    s.append(ic("prev",M+12,y+7,22))
    s.append(txt(M+62,y+26,"00:11",12))
    s.append(seekbar(M+88,y+16,SW-M*2-88-46-40))
    s.append(txt(SW-M-62,y+26,"4:37:47",12))
    s.append(ic("next",SW-M-34,y+7,22))
    y=by+44
    items=[("aspect","i"),("subs","i"),("audio","i"),("delay","i"),("prev","i"),
           ("PLAY","p"),("next","i"),("speed","c"),("camera","i"),("bright","i"),
           ("volume","i"),("lock","i"),("more","i")]
    w=sum(42 if t=="i" else (52 if t=="p" else 62) for _,t in items)
    x=M+(SW-2*M-w)/2
    for nm,t in items:
        if t=="i":
            s.append(ic(nm,x+10,y+5,22)); x+=42
        elif t=="p":
            s.append(f'<circle cx="{x+26}" cy="{y+26}" r="26" fill="{ACCENT}"/>')
            s.append(icon("pause",x+15,y+14,22)); x+=52
        else:
            s.append(chip(x,y+5,62,34,"1.00x")); x+=62
    return "".join(s)

DEFS = ('<defs>' + syms() + SHADOW +
 '<linearGradient id="vid2" x1="0" y1="0" x2="1" y2="1">'
 '<stop offset="0" stop-color="#4d6fa8"/><stop offset="0.45" stop-color="#d8a13c"/>'
 '<stop offset="1" stop-color="#6a3f7a"/></linearGradient>'
 '<linearGradient id="fadebot" x1="0" y1="0" x2="0" y2="1">'
 '<stop offset="0" stop-color="#000" stop-opacity="0"/><stop offset="0.45" stop-color="#000" stop-opacity="0.55"/>'
 '<stop offset="1" stop-color="#000" stop-opacity="0.85"/></linearGradient>'
 '<linearGradient id="fadetop" x1="0" y1="0" x2="0" y2="1">'
 '<stop offset="0" stop-color="#000" stop-opacity="0.75"/><stop offset="1" stop-color="#000" stop-opacity="0"/></linearGradient>'
 '</defs>')

def frame(mode, label, note, barH=96):
    by = SH-10-barH
    body = bg_rect(mode, by, barH) + rows_bottom(by, mode, barH)
    top = topbar(52, mode)
    return ('<figure>\n<svg viewBox="0 0 894 393" class="scr" xmlns="http://www.w3.org/2000/svg">'
            + DEFS
            + '<rect width="894" height="393" fill="url(#vid2)"/>'
            + txt(447,157,"VIDEO (poori screen)",13,"rgba(255,255,255,0.50)")
            + txt(447,177,"koi kaali patti nahi",11,"rgba(255,255,255,0.32)")
            + body + top
            + '</svg>\n<figcaption><b>' + label + '</b>' + note + '</figcaption>\n</figure>')

html = ('<!DOCTYPE html>\n<html lang="ur"><head><meta charset="utf-8">\n'
 '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
 '<title>mpv bar - black bars ke bagair</title>\n<style>\n'
 ' body{margin:0;background:#0d0f13;color:#e8ecf3;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;padding:14px 12px 40px}\n'
 ' h1{font-size:19px;margin:2px 0 6px}\n h2{font-size:15px;margin:24px 0 8px;color:#7FDBFF}\n'
 ' p{font-size:13.5px;line-height:1.55;color:#b9c2d0;margin:6px 0}\n'
 ' .scr{width:100%;height:auto;display:block;border-radius:10px}\n'
 ' figure{margin:10px 0 20px}\n'
 ' figcaption{font-size:12.5px;color:#8e99a8;margin-top:6px;line-height:1.5}\n'
 ' .ok{color:#7CE38B} .bad{color:#ff8a8a}\n'
 ' .ask{background:#141c26;border:1px solid #24344a;border-radius:10px;padding:12px 14px;margin-top:18px;font-size:13.5px;line-height:1.55}\n'
 ' .tag{display:inline-block;background:#1b2130;border:1px solid #2a3243;border-radius:6px;padding:1px 6px;font-size:11.5px;color:#9fb0c6}\n'
 '</style></head><body>\n'
 '<h1>Bar "black box" na lage - 4 tareeqe</h1>\n'
 '<p>Har frame mein <b>poori screen video</b> hai aur bar (Option A, 96 dp) usi ke upar. Sirf bar ka <b>background</b> badla hai - buttons wahi hain.</p>\n'
 '<h2>1) Jo abhi hai - <span class="bad">thick black box</span></h2>\n'
 + frame("solid","Abhi: 82% kaala box + border"," - bar aur top patti dono theek box lagti hain. Yeh aapko pasand nahi aaya.") + '\n'
 '<h2>2) Glass - <span class="ok">halka saaya, video nazar aati hai</span></h2>\n'
 + frame("glass","Glass (40% kaala + patli border)"," - video bar ke andar se dikhti rehti hai, box bhaari nahi lagta.") + '\n'
 '<h2>3) Gradient fade - <span class="ok">sab se saaf (MX / YouTube style)</span></h2>\n'
 + frame("fade","Gradient fade (kinare se kaala, ooper transparent)"," - koi box nahi, koi border nahi. Sirf neeche se halka kaala parda. Upar ki patti bhi isi tarah fade hoti hai.") + '\n'
 '<h2>4) Bilkul transparent - <span class="ok">koi background hi nahi</span></h2>\n'
 + frame("none","Transparent (sirf icons + shadow)"," - sab se halka. Video bohot bright ho to icons kamzor lag sakte hain (is liye shadow lagai hai).") + '\n'
 '<h2>5) Sab se chhoti + fade - <span class="ok">60 dp bar (15% screen)</span></h2>\n'
 + frame("fade","Option C (60 dp) + gradient fade"," - sab se slim bar, ek hi row mein saare buttons, black box bilkul nahi.") + '\n'
 '<div class="ask"><b>Batao kaunsa background?</b> Meray khayal se <b>#3 (gradient fade)</b> ya <b>#2 (glass)</b> - dono mein black box khatam ho jata hai, buttons saaf rehte hain.\n'
 '<br><br>Agar aapka matlab <i>letterbox</i> (video ke apne upar-neeche kaali patti, jo video ke shape ki wajah se hoti hai) tha, to alag se batao - wo app se nahi, video ki aspect ratio se banti hai.</div>\n'
 '</body></html>')

open("/home/user/mpv_bar_styles.html","w").write(html)
print("written:", len(html), "bytes")
