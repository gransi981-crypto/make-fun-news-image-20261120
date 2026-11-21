#!/usr/bin/env python3
"""Draw a one-page newspaper front page for Friday 20 November 2026.

Build-time only: the graded program (main.py) just copies the finished
entry.png to /output/entry.png. Run: python3 render.py -> entry.png
(1024x1024, deterministic: same input, same bytes).
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (253, 252, 247)
INK = (18, 18, 18)
RED = (178, 34, 34)
NAVY = (16, 24, 48)
GREY = (90, 90, 90)
RULE = (18, 18, 18)
FONT_DIR = "/usr/share/fonts/truetype/dejavu/"

def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)

F_MAST = font("DejaVuSerif-Bold.ttf", 96)
F_DATE = font("DejaVuSans-Bold.ttf", 20)
F_KICK = font("DejaVuSans-Bold.ttf", 21)
F_HEAD = font("DejaVuSerif-Bold.ttf", 36)
F_STAND = font("DejaVuSerif.ttf", 21)
F_BODY = font("DejaVuSans.ttf", 16)
F_COLH = font("DejaVuSerif-Bold.ttf", 25)
F_COLB = font("DejaVuSans.ttf", 15)
F_TICK = font("DejaVuSans-Bold.ttf", 15)
F_FOOT = font("DejaVuSans.ttf", 13)
F_CAP = font("DejaVuSans.ttf", 14)
F_BY = font("DejaVuSans-Bold.ttf", 15)

def wrap(draw, text, f, width):
    lines = []
    for para in text.split("\n"):
        words, line = para.split(), ""
        for w in words:
            trial = (line + " " + w).strip()
            if draw.textlength(trial, font=f) <= width:
                line = trial
            else:
                if line:
                    lines.append(line)
                line = w
        if line:
            lines.append(line)
    return lines

def para(draw, x, y, text, f, width, leading, color=INK):
    for line in wrap(draw, text, f, width):
        draw.text((x, y), line, font=f, fill=color)
        y += leading
    return y

def rule(draw, x0, x1, y, width=2, color=RULE):
    draw.line([(x0, y), (x1, y)], fill=color, width=width)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
MX = 36
RX = W - MX

# ---- top dateline bar ----
d.text((MX, 22), "THE WORLD IN ONE PAGE", font=F_DATE, fill=INK)
right = "FRIDAY 20 NOVEMBER 2026"
d.text((RX - d.textlength(right, font=F_DATE), 22), right, font=F_DATE, fill=INK)
rule(d, MX, RX, 52, 3)

# ---- masthead ----
title = "THE WORLD"
d.text(((W - d.textlength(title, font=F_MAST)) / 2, 58), title, font=F_MAST, fill=INK)
rule(d, MX, RX, 168, 2)
rule(d, MX, RX, 173, 5, RED)

# ---- lead story (left) + illustration (right) ----
LY = 192
COLW = 556
d.text((MX, LY), "WAR IN EUROPE  •  KYIV", font=F_KICK, fill=RED)
y = LY + 30
y = para(d, MX, y,
         "Russia's biggest barrage hits Kyiv — and spills into Poland",
         F_HEAD, COLW, 44)
y += 8
y = para(d, MX, y,
         "More than 400 drones and 110 missiles in one night; eight killed, "
         "nearly 30 hurt. Missiles came down in Poland — NATO jets scrambled.",
         F_STAND, COLW, 27)
y += 10
y = para(d, MX, y,
         "KYIV — Russia launched its heaviest air assault of the war overnight, "
         "hitting power plants and bridges across Ukraine. Kyiv's air force "
         "said it downed or suppressed 462 incoming targets. In the same "
         "barrage, missiles fell inside Poland: Warsaw called it an intentional "
         "provocation, and allied jets scrambled.",
         F_BODY, COLW, 22)

# ---- lead illustration: night sky over a city skyline ----
AX0, AY0, AX1, AY1 = 616, 192, 988, 478
d.rectangle([AX0, AY0, AX1, AY1], fill=NAVY)
# dusk gradient bands
for i in range(60):
    t = i / 60
    r = int(16 + (120 - 16) * t)
    g = int(24 + (52 - 24) * t)
    b = int(48 + (30 - 48) * t)
    d.line([(AX0, AY0 + 150 + i), (AX1, AY0 + 150 + i)], fill=(r, g, b))
# stars
for (sx, sy, sr) in [(640, 210, 2), (690, 230, 1), (760, 205, 2), (830, 235, 1),
                     (900, 215, 2), (950, 245, 1), (720, 260, 1), (860, 265, 2)]:
    d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(255, 255, 220))
# moon
d.ellipse([920, 205, 952, 237], fill=(240, 230, 200))
# missile arcs (dotted)
for arc in range(3):
    x0 = AX0 + 10 + arc * 18
    for k in range(24):
        t = k / 23
        x = x0 + t * 330
        yv = AY0 + 300 - 190 * t + 60 * t * t
        if k % 2 == 0:
            d.ellipse([x - 2, yv - 2, x + 2, yv + 2], fill=(255, 200, 90))
# explosion bursts
for (bx, by, br) in [(700, 330, 26), (820, 350, 20), (900, 320, 14)]:
    for rr, col in [(br, (255, 140, 40)), (br * 2 // 3, (255, 200, 80)),
                    (br // 3, (255, 240, 180))]:
        d.ellipse([bx - rr, by - rr, bx + rr, by + rr], fill=col)
# city skyline silhouette
sky = [(616, 478), (616, 420), (640, 420), (640, 400), (665, 400), (665, 430),
       (690, 430), (690, 395), (715, 395), (715, 425), (745, 425), (745, 405),
       (770, 405), (770, 435), (800, 435), (800, 410), (825, 410), (825, 440),
       (855, 440), (855, 400), (880, 400), (880, 430), (910, 430), (910, 415),
       (935, 415), (935, 445), (960, 445), (960, 425), (988, 425), (988, 478)]
d.polygon(sky, fill=(8, 10, 20))
# lit windows
for wx in range(628, 980, 16):
    for wy in (412, 432, 452):
        if (wx * 7 + wy * 3) % 5 < 2:
            d.rectangle([wx, wy, wx + 5, wy + 7], fill=(255, 210, 110))
d.text((AX0, AY1 + 8),
       "Night over Kyiv: the barrage in the sky, the city below.",
       font=F_CAP, fill=GREY)

# ---- divider ----
rule(d, MX, RX, 585, 2)

# ---- three columns ----
CY = 603
CW = 296
GAP = 22
cols = [
    ("MARKETS IN FREEFALL",
     "US stocks fell 3.7% as an AI-sector sell-off pushed the S&P 500 into "
     "correction — its sixth straight daily fall. The Nikkei dropped 5.1%. "
     "Anthropic slid for a second day after its record Nasdaq debut."),
    ("SUMMIT AFTERMATH",
     "Trump defended his ties to Putin and Xi after the first three-way "
     "summit in Shenzhen, where the leaders issued a joint declaration. "
     "China barred a Bloomberg reporter from covering the meeting."),
    ("THE DAY IN BRIEF",
     "• Magnitude 6.7 quake shakes central Peru\n"
     "• Cyclone Akvan makes landfall in Odisha\n"
     "• Houthi missiles aimed at Riyadh intercepted\n"
     "• Kerch Bridge rail traffic resumes\n"
     "• Hungary lifts veto on Ukraine's EU talks\n"
     "• Kenya counts down to Ebola-free status"),
]
for i, (head, body) in enumerate(cols):
    x = MX + i * (CW + GAP)
    d.text((x, CY), head, font=F_KICK, fill=RED)
    y = CY + 30
    y = para(d, x, y, body, F_COLB, CW, 21)
    if i < 2:
        d.line([(x + CW + 10, CY), (x + CW + 10, 880)], fill=(200, 200, 200), width=1)

# ---- ticker ----
TY = 902
d.rectangle([MX, TY, RX, TY + 46], fill=INK)
tick = ("MYANMAR GUILTY OF GENOCIDE  •  HORMUZ TANKER ABLAZE  •  "
        "ENERGY SHOCK ON RECORD")
tw = d.textlength(tick, font=F_TICK)
d.text(((W - tw) / 2, TY + 12), tick, font=F_TICK, fill=(255, 255, 255))

# ---- footer ----
d.text((MX, 962),
       "All stories verified in multiple outlets. Drawn by an AI agent for make.fun — one page, one day.",
       font=F_FOOT, fill=GREY)

img.save("entry.png", optimize=True)
print("saved entry.png")
