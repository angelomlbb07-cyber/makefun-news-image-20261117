#!/usr/bin/env python3
"""Draw the front page for 17 November 2026 as a 1024x1024 PNG.

Deterministic: no timestamps, no randomness, fixed fonts and geometry,
so every run writes byte-identical output. Run: python3 render.py
Writes entry.png next to this script.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (17, 17, 17)
RED = (163, 22, 33)
GREY = (90, 86, 78)
BLUE = (214, 228, 236)
LAND = (232, 220, 195)
RULE = (17, 17, 17)
M = 34  # margin

FD = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(os.path.join(FD, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns list of lines that fit `width` px."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def centred(draw, text, cx, y, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text((cx - w / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


# ---------------------------------------------------------------- stories
STORIES = [
    ("UKRAINE", "Kerch Bridge partly down",
     "Part of the 19 km bridge falls into the strait; Russia hits Kyiv bridges. 2 killed in Crimea."),
    ("TECH", "Nvidia posts record $115.8bn",
     "Revenue up 103%; guidance near $130bn. Huang, who resigned 12 Nov, will not return."),
    ("MARKETS", "U.S. stocks fall a 4th day",
     "Dow drops 849 (-1.64%) to 50,759 as the sell-off runs to a fourth straight day."),
    ("HEALTH", "U.S. loses measles-free status",
     "Elimination status lost after 26 years. 5,412 cases in 2026, the most since 1991; 10 deaths."),
    ("HEALTH", "Ebola passes 11,000 cases",
     "Outbreak in DR Congo tops 11,000 cases and 5,400 deaths, about 49% fatal; children hit hardest."),
    ("ASIA", "Quad summit opens in Manila",
     "Trump attends the first Quad summit in 2 years; first Trump-Xi-Putin meeting set for 19 Nov in Shenzhen."),
    ("U.S. POLITICS", "Democrats take the Senate",
     "Mary Peltola wins Alaska; Democrats take a 56-44 majority, the 9th flip, most since 1958."),
    ("ASIA", "Mongolia's president resigns",
     "Quits over a $25m railway bribery allegation, which he denies; parliament to vote."),
    ("EUROPE", "France hit by strikes",
     "Nationwide strikes and protests over wages: 146,000 counted officially, 500,000+ claimed."),
    ("ASIA", "Japan scrambles jets",
     "Russian aircraft breach its airspace for ~3 minutes each; first such case since Sept 2024."),
    ("CLIMATE", "COP31 draft: phase out oil",
     "Draft proposes a fossil-fuel phase-out and $120bn a year in adaptation finance by 2035. Not agreed."),
]


def draw_gulf_map(draw, x, y, w, h):
    """Stylised map of the Persian Gulf: Qeshm Island and Bahrain."""
    draw.rectangle([x, y, x + w, y + h], fill=BLUE, outline=INK, width=2)
    # Iran coast (top) and Arabian coast (bottom) as land polygons.
    draw.polygon([(x, y), (x + w, y), (x + w, y + 46),
                  (x + w * 0.62, y + 66), (x + w * 0.30, y + 52),
                  (x, y + 62)], fill=LAND)
    draw.polygon([(x, y + h), (x + w, y + h), (x + w, y + h - 44),
                  (x + w * 0.55, y + h - 78), (x + w * 0.22, y + h - 58),
                  (x, y + h - 62)], fill=LAND)
    draw.text((x + 8, y + 6), "IRAN", font=SANS_B(15), fill=INK)
    draw.text((x + 8, y + h - 24), "ARABIA", font=SANS_B(15), fill=INK)
    draw.text((x + 8, y + 118), "PERSIAN GULF", font=SANS_B(14), fill=(70, 90, 110))
    # Qeshm Island: red dot on the Iranian side, mid-right; label above it.
    qx, qy = x + 252, y + 92
    draw.text((x + 118, y + 44), "QESHM ISLAND", font=SANS_B(15), fill=RED)
    draw.text((x + 118, y + 64), "U.S. jets hit IRGC", font=SANS(13), fill=INK)
    draw.text((x + 118, y + 81), "missile site", font=SANS(13), fill=INK)
    draw.line([(x + 238, y + 88), (qx - 8, qy - 2)], fill=RED, width=2)
    draw.ellipse([qx - 7, qy - 7, qx + 7, qy + 7], fill=RED, outline=INK, width=2)
    # Strait of Hormuz marker (right edge, below the Qeshm dot).
    sx, sy = x + w - 30, y + 138
    draw.line([(sx - 8, sy - 14), (sx + 8, sy + 14)], fill=RED, width=3)
    draw.text((x + 168, y + 132), "STRAIT OF", font=SANS_B(14), fill=INK)
    draw.text((x + 168, y + 150), "HORMUZ", font=SANS_B(14), fill=INK)
    # Bahrain: red dot on the Arabian side, mid-left; label to its right.
    bx, by = x + 62, y + h - 62
    draw.ellipse([bx - 7, by - 7, bx + 7, by + 7], fill=RED, outline=INK, width=2)
    draw.text((bx + 16, by - 24), "BAHRAIN", font=SANS_B(15), fill=RED)
    draw.text((bx + 16, by - 5), "Drones targeted", font=SANS(13), fill=INK)
    draw.text((bx + 16, by + 12), "Sheikh Isa Air Base", font=SANS(13), fill=INK)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    cx = W // 2

    # ---- masthead ------------------------------------------------------
    centred(d, "THE WORLD IN ONE PAGE", cx, 26, SERIF_B(56), INK)
    d.line([(M, 100), (W - M, 100)], fill=RULE, width=3)
    centred(d, "TUESDAY 17 NOVEMBER 2026", cx, 110, SANS_B(42), RED)
    d.line([(M, 168), (W - M, 168)], fill=RED, width=4)
    d.line([(M, 176), (W - M, 176)], fill=RULE, width=2)

    # ---- lead story ----------------------------------------------------
    ly = 196
    d.text((M, ly), "LEAD STORY  ·  MIDDLE EAST", font=SANS_B(19), fill=RED)
    head = wrap(d, "U.S. STRIKES IRAN AFTER BAHRAIN DRONE ATTACK",
                SERIF_B(38), 596)
    y = draw_lines(d, head, M, ly + 30, SERIF_B(38), INK, 46)
    deck = wrap(d, "U.S. jets hit an IRGC missile launch site on Qeshm Island "
                   "after Iranian drones targeted a U.S. radar at Sheikh Isa "
                   "Air Base. The drones were intercepted; no U.S. injuries. "
                   "Iran's 3rd attack on Bahrain in 5 days.",
                SERIF(20), 596)
    draw_lines(d, deck, M, y + 8, SERIF(20), INK, 27)

    # Gulf map, right of the lead text.
    draw_gulf_map(d, 664, ly + 6, 326, 236)
    d.line([(M, 452), (W - M, 452)], fill=RULE, width=2)

    # ---- grid of other stories ----------------------------------------
    gy = 470
    d.text((M, gy), "THE DAY IN BRIEF", font=SANS_B(20), fill=RED)
    gy += 34
    cols, rows = 3, 4
    cw = (W - 2 * M - (cols - 1) * 14) // cols
    ch = 104
    for i, (tag, headline, summary) in enumerate(STORIES):
        r, c = divmod(i, cols)
        x = M + c * (cw + 14)
        yy = gy + r * (ch + 8)
        d.text((x, yy), tag, font=SANS_B(14), fill=RED)
        hl = wrap(d, headline, SANS_B(18), cw)
        y2 = draw_lines(d, hl[:2], x, yy + 20, SANS_B(18), INK, 22)
        # One-line headlines leave room for a 3-line summary; two-line
        # headlines get 2 summary lines so nothing spills into the next row.
        sm_max = 3 if len(hl) <= 1 else 2
        sm = wrap(d, summary, SANS(14), cw)
        draw_lines(d, sm[:sm_max], x, y2 + 2, SANS(14), (40, 40, 40), 17)
        if c < cols - 1:
            d.line([(x + cw + 7, yy), (x + cw + 7, yy + ch - 6)],
                   fill=(200, 192, 175), width=1)

    # 12th cell: the day in numbers.
    r, c = divmod(11, cols)
    x = M + c * (cw + 14)
    yy = gy + r * (ch + 8)
    d.rectangle([x, yy, x + cw, yy + ch - 6], fill=(238, 231, 216),
                outline=RED, width=2)
    d.text((x + 10, yy + 8), "BY THE NUMBERS", font=SANS_B(14), fill=RED)
    d.text((x + 10, yy + 32), "Dow  -849 pts", font=SANS_B(17), fill=INK)
    d.text((x + 10, yy + 56), "Measles  5,412 cases", font=SANS_B(17), fill=INK)
    d.text((x + 10, yy + 78), "Ebola  11,000+ cases", font=SANS_B(17), fill=INK)

    # ---- bottom strip --------------------------------------------------
    by = 948
    d.line([(M, by), (W - M, by)], fill=RULE, width=2)
    centred(d, "MARKETS:  Dow -1.64%   S&P 500 -1.03%   Nasdaq -0.74%   "
               "Gold $3,849   Bitcoin ~$64,666",
            cx, by + 10, SANS_B(17), INK)
    centred(d, "All events reported on Tuesday 17 November 2026  ·  "
               "One page, one day.",
            cx, by + 38, SANS(14), GREY)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG")
    print(f"Wrote {out} ({os.path.getsize(out)} bytes)")


if __name__ == "__main__":
    main()
