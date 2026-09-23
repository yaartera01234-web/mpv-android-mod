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

# ---------- top bar (same in all) ----------
def topbar(h=52):
    M=10; y=M
    s=[rrect(M,y,SW-2*M,h,16)]
    s.append(icon("back",M+11,y+h/2-11,22))
    s.append(txt(M+44,y+h/2+5,"Big Buck Bunny 1080p",13,anchor="start"))
    x=SW-M-11-44*3
    for nm in ["lock","pip","more"]:
        s.append(icon(nm,x+11,y+h/2-11,22)); x+=44
    return "".join(s)

# ---------- CURRENT (v1) : 3 rows, 174dp ----------
def v_current():
    M=10; barH=174; by=SH-M-barH
    s=[rrect(M,by,SW-2*M,barH,16)]
    # seek row
    y=by+8
    s.append(icon("prev",M+14,y+8,22))
    s.append(txt(M+66,y+28,"00:11",12))
    s.append(seekbar(M+92,y+18,SW-M*2-92-70-46))
    s.append(txt(SW-M-46-16,y+28,"4:37:47",12))
    s.append(icon("next",SW-M-36,y+8,22))
    # transport row
    y=by+56
    items=[("audio",48),("subs",48),("PLAY",58),("HW+",0),("1.00x",0)]
    x=M+(SW-2*M-48*2-58-66-70)/2
    s.append(icon("audio",x+13,y+17,22)); x+=48
    s.append(icon("subs",x+13,y+17,22)); x+=48
    s.append(f'<circle cx="{x+29}" cy="{y+28}" r="29" fill="{ACCENT}"/>')
    s.append(icon("pause",x+17,y+16,24)); x+=58+12
    s.append(chip(x,y+9,66,38,"HW+")); x+=66+12
    s.append(chip(x,y+9,70,38,"1.00x"))
    # tools row
    y=by+124
    tools=["aspect","camera","bright","volume","lock","more"]
    x=M+(SW-2*M-46*len(tools))/2
    for nm in tools:
        s.append(icon(nm,x+12,y+12,22)); x+=46
    return "".join(s)

# ---------- OPTION A : MX slim, 2 rows, 96dp ----------
def v_A():
    M=10; barH=96; by=SH-M-barH
    s=[rrect(M,by,SW-2*M,barH,16)]
    y=by+6
    s.append(icon("prev",M+12,y+7,22))
    s.append(txt(M+62,y+26,"00:11",12))
    sbx=M+88; sbw=SW-M*2-88-46-40
    s.append(seekbar(sbx,y+16,sbw))
    s.append(txt(SW-M-62,y+26,"4:37:47",12))
    s.append(icon("next",SW-M-34,y+7,22))
    # single tools row: everything, play in middle
    y=by+44
    items=[("aspect","i"),("subs","i"),("audio","i"),("delay","i"),("prev","i"),
           ("PLAY","p"),("next","i"),("speed","c"),("camera","i"),("bright","i"),
           ("volume","i"),("lock","i"),("more","i")]
    w=sum(42 if t=="i" else (52 if t=="p" else 62) for _,t in items)
    x=M+(SW-2*M-w)/2
    for nm,t in items:
        if t=="i":
            s.append(icon(nm,x+10,y+5,22)); x+=42
        elif t=="p":
            s.append(f'<circle cx="{x+26}" cy="{y+26}" r="26" fill="{ACCENT}"/>')
            s.append(icon("pause",x+15,y+14,22)); x+=52
        else:
            s.append(chip(x,y+5,62,34,"1.00x")); x+=62
    return "".join(s)

# ---------- OPTION B : compact + more (96dp / 144dp expanded) ----------
def v_B(expanded):
    M=10; barH=130 if expanded else 96; by=SH-M-barH
    s=[rrect(M,by,SW-2*M,barH,16)]
    y=by+6
    s.append(icon("prev",M+12,y+4,22))
    s.append(txt(M+62,y+24,"00:11",12))
    s.append(seekbar(M+88,y+13,SW-M*2-88-46-40))
    s.append(txt(SW-M-62,y+24,"4:37:47",12))
    s.append(icon("next",SW-M-34,y+4,22))
    y=by+42; dy = 8 if expanded else 12
    items=[("aspect","i"),("subs","i"),("audio","i"),("delay","i"),("prev","i"),
           ("PLAY","p"),("next","i"),("speed","c"),("more","i")]
    w=sum(42 if t=="i" else (52 if t=="p" else 62) for _,t in items)
    x=M+(SW-2*M-w)/2
    pc = 24 if expanded else 26
    for nm,t in items:
        if t=="i":
            s.append(icon(nm,x+10,y+dy,22)); x+=42
        elif t=="p":
            s.append(f'<circle cx="{x+pc+2}" cy="{y+dy+11}" r="{pc}" fill="{ACCENT}"/>')
            s.append(icon("pause",x+pc-8,y+dy+2,20)); x+=52
        else:
            s.append(chip(x,y+dy-2,62,34,"1.00x")); x+=62
    if expanded:
        y=by+84
        s.append(f'<line x1="{M+30}" y1="{y}" x2="{SW-M-30}" y2="{y}" stroke="rgba(255,255,255,0.10)"/>')
        extra=["camera","bright","volume","lock"]
        w=42*4+100
        x=M+(SW-2*M-w)/2
        for nm in extra:
            s.append(icon(nm,x+10,y+11,22)); x+=42
        s.append(chip(x+4,y+3,92,34,"HW+ / SW"))
    return "".join(s)

# ---------- OPTION C : ultra slim, single row, 60dp ----------
def v_C():
    M=10; barH=60; by=SH-M-barH
    s=[rrect(M,by,SW-2*M,barH,16)]
    y=by+8
    x=M+8
    s.append(icon("prev",x,y+12,22)); x+=34
    s.append(txt(x+17,y+35,"00:11",11)); x+=34
    icons=["aspect","subs","audio","delay","camera","bright","volume","lock","more"]
    fixed = 34+34+40+40+52+62 + 38*len(icons)
    sbw = SW-2*M-8-fixed
    s.append(seekbar(x,y+22,sbw)); x = x+sbw+6
    s.append(txt(x+20,y+35,"4:37:47",11)); x+=40
    s.append(icon("next",x,y+12,22)); x+=40
    s.append(f'<circle cx="{x+23}" cy="{y+22}" r="23" fill="{ACCENT}"/>')
    s.append(icon("pause",x+13,y+12,20)); x+=52
    s.append(chip(x,y+10,62,32,"1.00x")); x+=62
    for nm in icons:
        s.append(icon(nm,x+8,y+11,22)); x+=38
    return "".join(s)

html = f'''<!DOCTYPE html>
<html lang="ur"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>mpv control bar — design options</title>
<style>
 body{{margin:0;background:#0d0f13;color:#e8ecf3;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;padding:14px 12px 40px}}
 h1{{font-size:19px;margin:2px 0 6px}}
 h2{{font-size:15px;margin:22px 0 8px;color:#7FDBFF}}
 p{{font-size:13.5px;line-height:1.55;color:#b9c2d0;margin:6px 0}}
 .scr{{width:100%;height:auto;display:block;border-radius:10px;border:1px solid #232833}}
 figure{{margin:10px 0 18px}}
 figcaption{{font-size:12.5px;color:#8e99a8;margin-top:6px;line-height:1.5}}
 .bad{{color:#ff8a8a}} .good{{color:#7CE38B}} .warn{{color:#ffd479}}
 table{{width:100%;border-collapse:collapse;font-size:12.5px;margin-top:8px}}
 td,th{{border:1px solid #232833;padding:6px 8px;text-align:left;vertical-align:top}}
 th{{color:#7FDBFF;background:#141821}}
 .tag{{display:inline-block;background:#1b2130;border:1px solid #2a3243;border-radius:6px;padding:1px 6px;font-size:11.5px;color:#9fb0c6}}
 .ask{{background:#141c26;border:1px solid #24344a;border-radius:10px;padding:12px 14px;margin-top:18px}}
</style></head><body>
<h1>mpv control bar — design options</h1>
<p>Aapki screen: <b>894 × 393 dp</b> (landscape). Neeche har option <b>asli naap (dp)</b> mein hai, is liye size ka farq saaf nazar aayega.</p>

<h2>1) Ab jo hai (aap ne yeh dekha) — <span class="bad">174 dp = 44% screen</span></h2>
{screen(topbar()+v_current(),"CURRENT — 3 rows (174 dp)"," — bar ka upar wala kinara screen ke bilkul beech se shuru hota hai, is liye video chhota reh jata hai.")}

<h2>2) OPTION A — MX Slim, 2 rows — <span class="good">96 dp = 24% screen</span></h2>
{screen(topbar()+v_A(),"OPTION A (96 dp)"," — seek row + ek hi tools row. Sab kuch ek row mein: aspect · subs · audio · <b>delay</b> · prev · PLAY · next · speed · screenshot · brightness · volume · lock · menu. Bar pehle se 45% chhoti.")}

<h2>3) OPTION B — Compact + More — <span class="good">96 dp default / 144 dp expanded</span></h2>
{screen(topbar()+v_B(False),"OPTION B — normal (96 dp)"," — sirf rozana wale buttons: aspect · subs · audio · delay · prev · PLAY · next · speed · <b>⋮ More</b>.")}
{screen(topbar()+v_B(True),"OPTION B — jab ⋮ More dabao (146 dp)"," — extra row khulti hai: screenshot · brightness · volume · lock · decoder. Sirf zaroorat par jagah leti hai.")}

<h2>4) OPTION C — Ultra Slim, ek hi row — <span class="good">60 dp = 15% screen</span></h2>
{screen(topbar()+v_C(),"OPTION C (60 dp)"," — seekbar aur <b>saare</b> buttons (aspect · subs · audio · delay · speed · screenshot · brightness · volume · lock · menu) ek hi patti mein. Sirf decoder HW+/SW ⋮ menu mein. Portrait mein row left-right scroll karegi.")}

<h2>Jo cheezein har option mein add hongi</h2>
<table>
<tr><th>Button</th><th>Kaam</th></tr>
<tr><td>Delay (clock icon) <span class="tag">NAYA</span></td><td><b>Audio delay</b> picker seedha bar se (-600 se +600 tak) — lipsing match karne ke liye. Aap ne bilkul theek kaha, yeh pehle 3 tap peeche tha (menu → Advanced).</td></tr>
<tr><td>Subs (long press)</td><td>Subtitle delay + track picker (pehle jaisa)</td></tr>
<tr><td>Aspect</td><td>Ratio list (Fit/Fill/16:9/4:3/Stretch) — long press = Advanced menu</td></tr>
<tr><td>Screenshot</td><td>Video frame → gallery (Pictures/mpv)</td></tr>
<tr><td>Brightness / Volume</td><td>Tap → bar ke upar slim slider; purane swipe gestures barqarar</td></tr>
<tr><td>Lock / Menu / PiP / Decoder / Speed</td><td>Pehle jaisa hi</td></tr>
</table>

<div class="ask">
<b>Aap sirf yeh batao:</b> kaunsa option? <b>A</b>, <b>B</b> ya <b>C</b> — ya phir "A lekin thori si badlav…" bhi bol sakte ho (jaise bar ko upar se neeche sirf 2 rows, ya tools row apne hisaab se).
Phir main wohi design app mein lagata hoon aur naya APK banata hoon.
<br><br><span class="tag">Note</span> Ye HTML sirf dikhane ke liye hai — isme koi cheez app ke andar nahi jaati.
</div>
</body></html>'''
open("/home/user/mpv_bar_options.html","w").write(html)
print("written:", len(html), "bytes")
