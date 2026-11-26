#!/usr/bin/env python3
"""Draw the news-image-20261125 entry: a one-page newspaper summary of
Wednesday 25 November 2026. All text is drawn with PIL (crisp, no garbled
AI text). Output: entry.png, 1024x1024, under 1 MiB.
"""
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

PAPER = (247, 243, 232)
INK = (17, 17, 17)
MUTED = (90, 86, 76)
RULE = (176, 42, 30)
LIGHT_RULE = (200, 192, 172)

FONT_DIR = "/usr/share/fonts/truetype/noto"


def font(name, size):
    p = os.path.join(FONT_DIR, name)
    try:
        return ImageFont.truetype(p, size)
    except OSError:
        return ImageFont.load_default()


F_MAST = font("NotoSans-Bold.ttf", 64)
F_DATE = font("NotoSans-Bold.ttf", 30)
F_SUB = font("NotoSans-Regular.ttf", 21)
F_LEAD = font("NotoSans-Bold.ttf", 32)
F_LEAD_BODY = font("NotoSans-Regular.ttf", 20)
F_TAG = font("NotoSans-Bold.ttf", 13)
F_HEAD = font("NotoSans-Bold.ttf", 18)
F_BODY = font("NotoSans-Regular.ttf", 14)
F_TIME = font("NotoSans-Bold.ttf", 15)
F_FOOT = font("NotoSans-Regular.ttf", 14)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def wrap(text, fnt, width):
    lines, cur = [], ""
    for word in text.split():
        t = (cur + " " + word).strip()
        if d.textlength(t, font=fnt) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_h(lines, fnt, leading):
    return len(lines) * leading


# ---------- header ----------
d.text((32, 22), "THE WORLD IN ONE DAY", font=F_MAST, fill=INK)
d.line([(32, 100), (992, 100)], fill=RULE, width=4)
d.text((32, 112), "WEDNESDAY, 25 NOVEMBER 2026", font=F_DATE, fill=RULE)
d.text((32, 150), "19 stories  ·  6 regions  ·  9 fields  —  every event from one day",
       font=F_SUB, fill=MUTED)

# ---------- lead story ----------
d.line([(32, 188), (992, 188)], fill=LIGHT_RULE, width=2)
lead_head = "Two oil tankers hit mines and burn in the Strait of Hormuz"
for i, ln in enumerate(wrap(lead_head, F_LEAD, 960)):
    d.text((32, 200 + i * 38), ln, font=F_LEAD, fill=INK)
lead_body = ("Iran's Revolutionary Guard says the tankers struck naval mines on an unauthorised "
             "route; Tehran also claims it downed a US MQ-9 drone over the strait.")
for i, ln in enumerate(wrap(lead_body, F_LEAD_BODY, 960)):
    d.text((32, 244 + i * 25), ln, font=F_LEAD_BODY, fill=MUTED)

# ---------- columns ----------
CAT_COLORS = {
    "CONFLICT": (176, 42, 30),
    "ENERGY": (140, 90, 10),
    "TECH": (30, 80, 160),
    "SPACE": (90, 50, 140),
    "CLIMATE": (20, 120, 80),
    "ECONOMY": (40, 110, 130),
    "LAW": (120, 60, 120),
    "CYBER": (60, 60, 60),
    "LABOUR": (150, 70, 20),
}

# (tag, headline, one-line summary)
STORIES = [
    ("CONFLICT", "Houthis strike Saudi refinery and Riyadh tower",
     "Fires at Ras Tanura; 11 people injured in the Riyadh attack."),
    ("CONFLICT", "Israel kills Hamas security chief in Gaza",
     "Colonel Mohammad Abuelouf killed with his wife and two children."),
    ("CONFLICT", "Russian strike kills 2 in Odesa region",
     "Three injured, including a child; Kyiv also attacked overnight."),
    ("CONFLICT", "BBC: 490,334 Russian soldiers dead since 2022",
     "Figure from leaked Russian statistics analysed by the BBC."),
    ("CONFLICT", "Putin: Ukraine keeps hitting Russian refineries",
     "Moscow accuses Kyiv of continued strikes on oil refineries."),
    ("CONFLICT", "Sudan: RSF drone strikes kill 19 civilians",
     "Twenty more wounded in drone attacks on two cities."),
    ("CONFLICT", "Trump: US war funding on Iran secured to January",
     "Washington says funding for operations against Iran is secured."),
    ("CLIMATE", "COP31 climate talks end with no agreement",
     "Negotiators fail to reach a deal as the summit closes."),
    ("CLIMATE", "Pope Leo XIV warns on climate extremes",
     "Pope voices concern as extreme weather grows more frequent."),
    ("ECONOMY", "US to unveil tariffs on 14 partners, 20–40%",
     "New duties loom over fourteen trading partners."),
    ("ECONOMY", "Wall Street slides: S&P -2.2%, Nasdaq -3.2%",
     "US stocks fall sharply on tariff and AI worries."),
    ("ECONOMY", "Asian chip stocks rout; Kospi falls 6.2%",
     "Doubts over AI spending hit chip shares across Asia."),
    ("TECH", "Huawei convicted in US federal court",
     "Guilty of trade-secret conspiracy and bank fraud."),
    ("SPACE", "Shenzhou-24 docks with first foreign astronaut",
     "Pakistan's Muhammad Zeeshan Ali joins China's space station."),
    ("CYBER", "CIA and ODNI hit by cybersecurity breach",
     "US intelligence agencies suffer a cyber intrusion."),
    ("LAW", "US charges 800+ in global anti-scam crackdown",
     "More than 400 cases in a worldwide fraud sweep."),
    ("LAW", "Solomon Islands–Australia treaty bars foreign bases",
     "Deal precludes any foreign military base on the islands."),
    ("LABOUR", "Bangladesh lifts garment wage 36% to $139",
     "Minimum wage raised after worker protests."),
]

COL_X = [32, 360, 688]
COL_W = 304
y0 = 305
# distribute stories round-robin into 3 columns (6, 6, 6)
cols = [[], [], []]
for i, s in enumerate(STORIES):
    cols[i % 3].append(s)

for ci, stories in enumerate(cols):
    x = COL_X[ci]
    y = y0
    for tag, head, body in stories:
        color = CAT_COLORS.get(tag, (60, 60, 60))
        d.text((x, y), tag, font=F_TAG, fill=color)
        y += 15
        for ln in wrap(head, F_HEAD, COL_W):
            d.text((x, y), ln, font=F_HEAD, fill=INK)
            y += 19
        for ln in wrap(body, F_BODY, COL_W):
            d.text((x, y), ln, font=F_BODY, fill=MUTED)
            y += 16
        y += 8

# ---------- timeline strip ----------
ty = 890
d.line([(32, ty), (992, ty)], fill=LIGHT_RULE, width=2)
d.text((32, ty + 10), "AROUND THE DAY  ·  UTC", font=F_TAG, fill=RULE)
timeline = [
    ("Morning", "Hormuz tanker blasts reported"),
    ("Midday", "Houthi strikes on Saudi Arabia"),
    ("Afternoon", "Shenzhou-24 docks at station"),
    ("Evening", "US tariffs plan; markets slide"),
]
tx = 32
for label, item in timeline:
    d.text((tx, ty + 34), label.upper(), font=F_TIME, fill=INK)
    for ln in wrap(item, F_BODY, 220):
        d.text((tx, ty + 56), ln, font=F_BODY, fill=MUTED)
    tx += 244

# ---------- footer ----------
fy = 978
d.line([(32, fy), (992, fy)], fill=LIGHT_RULE, width=2)
d.text((32, fy + 10),
       "Sources: Reuters, BBC, Just Security, Open Chronicle  ·  All events reported on 25 November 2026",
       font=F_FOOT, fill=MUTED)

img.save(OUT, optimize=True)
print("saved", OUT, os.path.getsize(OUT), "bytes,", img.size)
