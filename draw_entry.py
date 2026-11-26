#!/usr/bin/env python3
"""Draw the news-image-20261125 entry v2: a one-page newspaper summary of
Wednesday 25 November 2026, rebuilt to the top entries' pattern:
giant serif date, three illustrated top stories, region bar, KPI row,
UTC timeline, numbered featured grid, world map, numbered list of all
50 stories, DATE CHECK footer. All text drawn with PIL (crisp, no
garbled AI text). Output: entry.png, 1024x1024, under 1 MiB.
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

PAPER = (247, 243, 232)
INK = (17, 17, 17)
MUTED = (90, 86, 76)
RED = (176, 42, 30)
NAVY = (20, 45, 90)
CREAM2 = (238, 231, 214)
LIGHT_RULE = (200, 192, 172)
MAP_LAND = (226, 216, 190)
MAP_LINE = (160, 148, 122)

SANS = "/usr/share/fonts/truetype/noto"
SERIF = "/usr/share/fonts/truetype/noto"


def font(path, name, size):
    p = os.path.join(path, name)
    try:
        return ImageFont.truetype(p, size)
    except OSError:
        return ImageFont.load_default()


F_MAST = font(SANS, "NotoSans-Bold.ttf", 20)
F_DATE = font(SERIF, "NotoSerif-Bold.ttf", 54)
F_SUB = font(SERIF, "NotoSerif-Italic.ttf", 19)
F_SUB_FB = font(SERIF, "NotoSerif-Regular.ttf", 19)
F_REG_N = font(SANS, "NotoSans-Bold.ttf", 11)
F_REG_C = font(SANS, "NotoSans-Bold.ttf", 16)
F_KPI_N = font(SERIF, "NotoSerif-Bold.ttf", 30)
F_KPI_L = font(SANS, "NotoSans-Regular.ttf", 11)
F_TL = font(SANS, "NotoSans-Regular.ttf", 12)
F_TL_B = font(SANS, "NotoSans-Bold.ttf", 12)
F_TAG = font(SANS, "NotoSans-Bold.ttf", 12)
F_BIG_H = font(SANS, "NotoSans-Bold.ttf", 19)
F_BIG_B = font(SANS, "NotoSans-Regular.ttf", 13)
F_WHY = font(SANS, "NotoSans-Italic.ttf", 12)
F_WHY_FB = font(SANS, "NotoSans-Regular.ttf", 12)
F_NUM = font(SANS, "NotoSans-Bold.ttf", 13)
F_FT_H = font(SANS, "NotoSans-Bold.ttf", 14)
F_FT_B = font(SANS, "NotoSans-Regular.ttf", 12)
F_LST = font(SANS, "NotoSans-Regular.ttf", 12)
F_LST_B = font(SANS, "NotoSans-Bold.ttf", 12)
F_SEC = font(SANS, "NotoSans-Bold.ttf", 13)
F_FOOT = font(SANS, "NotoSans-Regular.ttf", 12)
F_FOOT_B = font(SANS, "NotoSans-Bold.ttf", 12)

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


def center(text, fnt, y, fill):
    w = d.textlength(text, font=fnt)
    d.text(((W - w) / 2, y), text, font=fnt, fill=fill)


# ---------- masthead + date ----------
center("THE WORLD IN ONE DAY", F_MAST, 12, INK)
d.line([(32, 40), (992, 40)], fill=RED, width=3)
center("Wednesday 25 November 2026", F_DATE, 46, INK)
sub = "US tariffs up to 20%  ·  Kospi -6.2%  ·  Pakistan's first astronaut docks at Tiangong"
try:
    center(sub, F_SUB, 106, RED)
except Exception:
    center(sub, F_SUB_FB, 106, RED)

# ---------- region bar ----------
REGIONS = [
    ("N. AMERICA", 11, (20, 45, 90)),
    ("LATIN AM.", 1, (30, 120, 70)),
    ("EUROPE", 11, (140, 40, 120)),
    ("MID. EAST", 7, (176, 42, 30)),
    ("N. AFRICA", 3, (200, 120, 20)),
    ("SUB-SAH. AFR.", 3, (120, 80, 20)),
    ("SOUTH ASIA", 1, (0, 130, 130)),
    ("EAST & SE ASIA", 5, (30, 80, 160)),
    ("OCEANIA", 2, (90, 60, 140)),
    ("GLOBAL", 6, (80, 80, 80)),
]
bx, bw, by = 32, 96, 132
for i, (name, count, color) in enumerate(REGIONS):
    x = bx + i * bw
    d.rectangle([x, by, x + bw - 2, by + 30], fill=color)
    nw = d.textlength(name, font=F_REG_N)
    d.text((x + (bw - 2 - nw) / 2, by + 2), name, font=F_REG_N, fill=(255, 255, 255))
    cw = d.textlength(str(count), font=F_REG_C)
    d.text((x + (bw - 2 - cw) / 2, by + 14), str(count), font=F_REG_C, fill=(255, 255, 255))

# ---------- KPI row ----------
KPI = [
    ("20%", "top US tariff proposed"),
    ("-6.2%", "Kospi close"),
    ("+26%", "UK Ofgem energy cap"),
    ("31", "killed in Cairo tanker fire"),
    ("9", "dead in Bogor gold mine"),
    ("1st", "Pakistan astronaut in orbit"),
]
kx = 32
for val, lab in KPI:
    vw = d.textlength(val, font=F_KPI_N)
    d.text((kx + (160 - vw) / 2, 168), val, font=F_KPI_N, fill=RED)
    lw = d.textlength(lab, font=F_KPI_L)
    d.text((kx + (160 - lw) / 2, 200), lab, font=F_KPI_L, fill=MUTED)
    kx += 160
d.line([(32, 220), (992, 220)], fill=LIGHT_RULE, width=2)

# ---------- UTC timeline ----------
d.rectangle([32, 226, 992, 256], fill=NAVY)
tl1 = "THE DAY IN UTC   00:18 Shenzhou-24 lifts  ·  03:56 Tiangong docks  ·  05:30 Taiex -4.8%  ·  06:30 Kospi -6.2%"
tl2 = "07:00 Ofgem cap +26%  ·  08:35 Crew enters Tiangong  ·  13:30 US Q3 GDP 4.3%  ·  21:00 Dow tops 50,000"
for i, tl in enumerate((tl1, tl2)):
    tw = d.textlength(tl, font=F_TL)
    d.text(((W - tw) / 2, 230 + i * 13), tl, font=F_TL, fill=(255, 255, 255))

# ---------- flat illustrations ----------
def draw_ship(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(30, 80, 140))
    d.rectangle([x, y + h - 26, x + w, y + h], fill=(20, 60, 110))
    for i, c in enumerate([(200, 60, 50), (240, 180, 40), (60, 160, 90)]):
        d.rectangle([x + 14 + i * 66, y + 22, x + 14 + i * 66 + 56, y + 56], fill=c)
        d.rectangle([x + 14 + i * 66, y + 22, x + 14 + i * 66 + 56, y + 56], outline=(255, 255, 255), width=1)
    d.polygon([(x + 14, y + h - 26), (x + w - 14, y + h - 26), (x + w - 40, y + h - 4), (x + 40, y + h - 4)], fill=(17, 17, 17))
    d.rectangle([x + w - 104, y + 8, x + w - 8, y + 32], outline=(255, 60, 40), width=3)
    st = "UP TO 20%"
    sw = d.textlength(st, font=F_TAG)
    d.text((x + w - 104 + (96 - sw) / 2, y + 12), st, font=F_TAG, fill=(255, 80, 60))


def draw_chart(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(12, 12, 14))
    pts = [(x + 10, y + 18), (x + 60, y + 26), (x + 110, y + 22), (x + 160, y + 44),
           (x + 210, y + 52), (x + 260, y + 70), (x + w - 12, y + h - 16)]
    d.line(pts, fill=(230, 50, 40), width=4)
    for px, py in pts:
        d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=(255, 255, 255))
    d.rectangle([x + 12, y + h - 30, x + 92, y + h - 8], fill=(230, 50, 40))
    d.text((x + 20, y + h - 27), "KOSPI -6.2%", font=F_TAG, fill=(255, 255, 255))
    d.text((x + w - 118, y + 8), "SK HYNIX -11.1%", font=F_TAG, fill=(255, 120, 100))
    d.text((x + w - 118, y + 26), "SAMSUNG -9.9%", font=F_TAG, fill=(255, 120, 100))


def draw_station(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(10, 20, 50))
    for sx in range(x + 8, x + w - 8, 14):
        for sy in range(y + 6, y + 34, 14):
            if (sx * 7 + sy * 13) % 29 < 6:
                d.ellipse([sx, sy, sx + 2, sy + 2], fill=(255, 255, 255))
    d.rectangle([x + 70, y + 44, x + 110, y + 58], fill=(40, 90, 180))
    d.rectangle([x + 150, y + 44, x + 190, y + 58], fill=(40, 90, 180))
    d.rectangle([x + 112, y + 40, x + 148, y + 62], fill=(230, 230, 230))
    d.rectangle([x + 118, y + 30, x + 142, y + 40], fill=(200, 200, 200))
    d.rectangle([x + 14, y + 66, x + 34, y + 80], fill=(20, 120, 70))
    d.text((x + 17, y + 68), "PK", font=F_TAG, fill=(255, 255, 255))
    d.rectangle([x + 40, y + 66, x + 60, y + 80], fill=(200, 40, 30))
    d.text((x + 43, y + 68), "CN", font=F_TAG, fill=(255, 255, 255))
    d.ellipse([x + w - 52, y + 8, x + w - 16, y + 44], fill=(30, 90, 160), outline=(90, 160, 220), width=2)


BIG = [
    ("ship", "WASHINGTON · TRADE · OFFICIAL",
     "US proposes tariffs of up to 20% on EU, China and 12 more",
     "Fourteen economies in the plan; Vietnam faces up to 35%.",
     "WHY IT MATTERS: the biggest US tariff move of the year hits world trade."),
    ("chart", "SEOUL · MARKETS · OFFICIAL",
     "AI doubts sink Asian chip stocks: Kospi closes -6.2%",
     "SK Hynix -11.1%, Samsung -9.9%, Taiex -4.8% as AI spending fears spread.",
     "WHY IT MATTERS: the AI rally cracks across Asia in one session."),
    ("station", "TIANGONG · SPACE · OFFICIAL",
     "Pakistan's first astronaut docks at China's space station",
     "Shenzhou-24 lifts 00:18 UTC, docks 03:56; Muhammad Zeeshan Ali aboard.",
     "WHY IT MATTERS: the first foreign astronaut on a Chinese mission."),
]

by0 = 262
for i, (kind, tag, head, body, why) in enumerate(BIG):
    x = 32 + i * 328
    if kind == "ship":
        draw_ship(x, by0, 304, 92)
    elif kind == "chart":
        draw_chart(x, by0, 304, 92)
    else:
        draw_station(x, by0, 304, 92)
    yy = by0 + 100
    d.text((x, yy), tag, font=F_TAG, fill=RED)
    yy += 16
    for ln in wrap(head, F_BIG_H, 304):
        d.text((x, yy), ln, font=F_BIG_H, fill=INK)
        yy += 22
    for ln in wrap(body, F_BIG_B, 304):
        d.text((x, yy), ln, font=F_BIG_B, fill=MUTED)
        yy += 16
    for ln in wrap(why, F_WHY, 304):
        d.text((x, yy), ln, font=F_WHY, fill=INK)
        yy += 15
d.line([(32, 472), (992, 472)], fill=LIGHT_RULE, width=2)

# ---------- featured grid 4-13 ----------
FEATURED = [
    (4, "HORMUZ · ENERGY", "Two tankers hit mines and burn in Hormuz", "IRGC: mines on an unauthorised route."),
    (5, "SAUDI ARABIA · WAR", "Houthis strike refinery and Riyadh tower", "Fires at Ras Tanura; 11 injured."),
    (6, "UKRAINE · WAR", "Russian strike kills 2 in Odesa region", "Three injured, incl. a child."),
    (7, "LONDON · ECONOMY", "UK energy price cap rises 26% to £2,166", "Ofgem lifts the household cap."),
    (8, "PACIFIC · DIPLOMACY", "Solomon Islands–Australia treaty bars bases", "No foreign military base allowed."),
    (9, "DHAKA · LABOUR", "Bangladesh lifts garment wage 36% to $139", "Minimum wage after protests."),
    (10, "CAIRO · DISASTER", "Tanker fire kills 31 on Cairo highway", "Blaze after a fuel tanker crash."),
    (11, "GAZA · WAR", "Israel kills Hamas security chief", "Col. Abuelouf dies with family."),
    (12, "CAPE TOWN · JUSTICE", "Court rules in Farmgate case", "Ruling in the Phala Phala case."),
    (13, "COLOMBIA · CRIME", "All hostages freed in Cartagena siege", "One assailant killed by forces."),
]

fy0 = 482
for i, (num, tag, head, body) in enumerate(FEATURED):
    col, row = i % 5, i // 5
    x = 32 + col * 192
    y = fy0 + row * 80
    d.ellipse([x, y, x + 22, y + 22], fill=RED)
    ns = str(num)
    nw = d.textlength(ns, font=F_NUM)
    d.text((x + (22 - nw) / 2, y + 3), ns, font=F_NUM, fill=(255, 255, 255))
    d.text((x + 28, y + 1), tag, font=F_TAG, fill=RED)
    yy = y + 17
    for ln in wrap(head, F_FT_H, 184):
        d.text((x, yy), ln, font=F_FT_H, fill=INK)
        yy += 16
    for ln in wrap(body, F_FT_B, 184):
        d.text((x, yy), ln, font=F_FT_B, fill=MUTED)
        yy += 14
d.line([(32, 646), (992, 646)], fill=LIGHT_RULE, width=2)

# ---------- world map ----------
MAP_X0, MAP_Y0, MAP_W, MAP_H = 32, 668, 268, 176
d.text((32, 652), "WHERE IT HAPPENED", font=F_SEC, fill=INK)


def proj(lon, lat):
    return (MAP_X0 + (lon + 180) / 360 * MAP_W,
            MAP_Y0 + (90 - lat) / 180 * MAP_H)


CONTINENTS = [
    [(-168, 66), (-150, 70), (-130, 71), (-115, 72), (-100, 73), (-90, 74), (-80, 73),
     (-70, 62), (-60, 55), (-55, 47), (-65, 44), (-70, 41), (-75, 35), (-80, 31),
     (-84, 30), (-90, 21), (-97, 16), (-105, 20), (-112, 29), (-120, 34), (-125, 40),
     (-130, 55), (-150, 60), (-165, 60)],
    [(-80, 9), (-72, 11), (-62, 9), (-52, 5), (-44, -3), (-35, -8), (-39, -17),
     (-48, -27), (-57, -38), (-65, -45), (-70, -54), (-73, -37), (-71, -20), (-77, -12), (-81, -5)],
    [(-17, 15), (-11, 27), (-6, 35), (3, 37), (11, 34), (20, 32), (30, 31), (34, 28),
     (40, 15), (48, 11), (51, 12), (46, 5), (42, -2), (40, -12), (36, -18), (33, -26),
     (27, -33), (19, -35), (14, -22), (12, -8), (9, 4), (-8, 5), (-13, 9)],
    [(-10, 36), (-9, 43), (-2, 48), (2, 51), (5, 53), (8, 57), (12, 55), (18, 56),
     (21, 55), (24, 59), (28, 60), (30, 62), (25, 65), (20, 70), (15, 69), (10, 62),
     (6, 58), (2, 55), (-2, 50), (-5, 48), (-9, 43)],
    [(30, 62), (35, 66), (42, 68), (50, 69), (60, 70), (70, 72), (80, 73), (90, 75),
     (100, 77), (110, 76), (120, 73), (130, 72), (140, 71), (150, 70), (160, 69),
     (170, 66), (178, 65), (170, 62), (162, 58), (158, 52), (150, 45), (142, 40),
     (135, 34), (130, 33), (126, 36), (122, 39), (120, 32), (114, 23), (109, 18),
     (106, 10), (102, 8), (99, 10), (96, 15), (93, 20), (89, 22), (85, 19), (81, 14),
     (78, 8), (76, 10), (73, 18), (69, 22), (65, 25), (61, 25), (58, 26), (55, 26),
     (52, 27), (50, 29), (48, 30), (45, 31), (42, 33), (40, 36), (38, 39), (36, 36),
     (33, 36), (30, 36), (27, 38), (24, 39), (22, 40), (20, 42), (18, 44), (16, 44),
     (13, 44), (10, 44), (7, 44), (4, 43), (2, 42), (0, 40), (-2, 37), (4, 37),
     (8, 37), (11, 37), (14, 38), (17, 38), (20, 40), (23, 40), (26, 38), (28, 36), (30, 36)],
    [(113, -22), (114, -30), (115, -34), (118, -35), (124, -33), (130, -32), (135, -35),
     (138, -35), (141, -38), (145, -38), (150, -37), (153, -32), (153, -27), (151, -24),
     (147, -19), (143, -15), (141, -13), (137, -12), (134, -12), (131, -12), (127, -14),
     (124, -15), (120, -20), (116, -20)],
]
for poly in CONTINENTS:
    d.polygon([proj(lon, lat) for lon, lat in poly], fill=MAP_LAND, outline=MAP_LINE)

PINS = [
    (4, 57, 26), (5, 47, 25), (6, 31, 46), (7, 0, 51), (8, 160, -9),
    (9, 90, 24), (10, 31, 30), (11, 34, 31), (12, 18, -34), (13, -75, 10),
]
for num, lon, lat in PINS:
    px, py = proj(lon, lat)
    d.ellipse([px - 7, py - 7, px + 7, py + 7], fill=RED, outline=(255, 255, 255), width=1)
    ns = str(num)
    nw = d.textlength(ns, font=F_NUM)
    d.text((px - nw / 2, py - 6), ns, font=F_NUM, fill=(255, 255, 255))
d.text((32, 850), "Pins = story numbers 4–13", font=F_FOOT, fill=MUTED)

# ---------- also list 14-50 ----------
LISTED = [
    (14, "Iran claims downing US MQ-9 drone"),
    (15, "Trump: war funding on Iran secured"),
    (16, "Yemen strike kills 26 on buses"),
    (17, "Coalition strikes Hodeidah port"),
    (18, "Putin vows retaliation on refineries"),
    (19, "BBC: 490,334 Russian war dead"),
    (20, "Zelensky: Ukraine needs €115bn aid"),
    (21, "US pauses Patriot supplies"),
    (22, "Eurozone inflation rises to 4.0%"),
    (23, "Spain: PP declares coalition win"),
    (24, "Drones hit Samara oil refinery"),
    (25, "Ukraine sinks Russian warship"),
    (26, "Two Libyan officers die in attack"),
    (27, "Sudan: RSF strikes kill 19 civilians"),
    (28, "CAS restores Senegal AFCON title"),
    (29, "N. Korea expels Swiss diplomat"),
    (30, "Bogor mine floods; 9 dead, 17 trapped"),
    (31, "Huawei convicted in US court"),
    (32, "Australia: Labor-Greens tax deal"),
    (33, "Wall Street slides: S&P -2.2%"),
    (34, "PCE inflation 3.8%, core 3.3%"),
    (35, "Nvidia leads sell-off"),
    (36, "CIA and ODNI hit by cyber breach"),
    (37, "DOJ charges 800+ in scam crackdown"),
    (38, "US Army detonates 5 tons in Iowa"),
    (39, "California record tides flood roads"),
    (40, "Microsoft 'Code Red' after outage"),
    (41, "AI agents hack university server"),
    (42, "Anthropic shares below IPO price"),
    (43, "Roche drug Wilserdly FDA-approved"),
    (44, "WHO: 3 bird flu cases, 1 death"),
    (45, "UN: cuts threaten progress vs HIV"),
    (46, "Homo erectus lived with Denisovans"),
    (47, "3D-MINSTED tracks single proteins"),
    (48, "COP31 talks fail; Pope warns"),
    (49, "Man Utd draw with Sporting"),
    (50, "England beat New Zealand 37-12"),
]
d.text((316, 652), "ALSO ON WEDNESDAY 25 NOVEMBER", font=F_SEC, fill=INK)
cols = [LISTED[i::3] for i in range(3)]
for ci, items in enumerate(cols):
    x = 316 + ci * 228
    y = 674
    for num, head in items:
        d.text((x, y), f"{num}.", font=F_LST_B, fill=RED)
        for ln in wrap(head, F_LST, 196):
            d.text((x + 22, y), ln, font=F_LST, fill=INK)
            y += 14
        y += 2

# ---------- footer ----------
fy = 972
d.rectangle([32, fy, 992, 1012], outline=RED, width=2)
d.text((44, fy + 4), "DATE CHECK", font=F_FOOT_B, fill=RED)
credit = "DRAWN BY AN AI AGENT FOR MAKE.FUN"
cw = d.textlength(credit, font=F_FOOT)
d.text((992 - 12 - cw, fy + 4), credit, font=F_FOOT, fill=MUTED)
d.text((44, fy + 20),
       "All 50 stories first reported Wednesday 25 November 2026. Sources: Reuters, BBC, wires.",
       font=F_FOOT, fill=INK)

img.save(OUT, optimize=True)
print("saved", OUT, os.path.getsize(OUT), "bytes,", img.size)
