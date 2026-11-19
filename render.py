#!/usr/bin/env python3
"""Render the 19 November 2026 world-news summary infographic (1024x1024 PNG).

Layout (baoyu-infographic): bento-grid -- six equal story tiles under one
date banner. Style: retro-pop-grid -- flat pop colours, thick ink outlines,
Swiss grid. All text is drawn by code with DejaVu fonts, so nothing is garbled.
Stories are events of Thursday 19 November 2026 and developments first
reported that morning, each verified against >=2 sources (see README.md).
None of the 18 November stories are repeated.
"""
import math
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
INK = (26, 26, 46)
CREAM = (255, 246, 229)
WHITE = (255, 255, 255)
MUTED = (70, 70, 90)
RED = (230, 57, 70)
TEAL = (42, 157, 143)
MUSTARD = (233, 196, 106)
BLUE = (69, 123, 157)
ORANGE = (244, 162, 97)
PURPLE = (123, 94, 167)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


F_TITLE = font(FB, 78)
F_SUB = font(FB, 26)
F_KICK = font(FB, 22)
F_HEAD = font(FB, 28)
F_BODY = font(FR, 20)
F_FOOT = font(FR, 19)
F_TAG = font(FB, 17)

STORIES = [
    dict(tag="GAMES  •  LAUNCH", colour=RED,
         head="GTA VI rolls out worldwide",
         body="After 13 years, Vice City opens at midnight market by market; 99 on Metacritic.",
         icon="controller"),
    dict(tag="ASIA  •  SUMMIT", colour=ORANGE,
         head="Trump, Putin, Xi meet in Shenzhen",
         body="First trilateral of the three leaders, on APEC's sidelines.",
         icon="dome"),
    dict(tag="LAW  •  THE HAGUE", colour=TEAL,
         head="World Court rules on Rohingya case",
         body="The ICJ delivers its judgment today on Myanmar and the Rohingya.",
         icon="gavel"),
    dict(tag="WEATHER  •  INDIA", colour=BLUE,
         head="Cyclone Akvan nears India's coast",
         body="Red alert as the storm brings extremely heavy rain; landfall due on Friday.",
         icon="swirl"),
    dict(tag="ASIA  •  DEFENCE", colour=PURPLE,
         head="India, Japan hold 2+2 talks",
         body="Foreign and defence ministers meet in Tokyo to deepen security and maritime ties.",
         icon="flags"),
    dict(tag="WEATHER  •  USA", colour=MUSTARD,
         head="Storm soaks California again",
         body="Atmospheric river brings a second day of rain; flood watch in Los Angeles, Highway 1 shut.",
         icon="cloud"),
]


def wrap(text, fnt, width, draw):
    """Greedy word wrap to pixel width."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_icon(d, kind, cx, cy, colour):
    """Simple flat geometric icon, centred at (cx, cy), inside a 96px box."""
    s = 96
    x0, y0 = cx - s // 2, cy - s // 2
    if kind == "controller":
        # gamepad: rounded body, d-pad, buttons, sticks
        d.rounded_rectangle([x0 + 8, y0 + 34, x0 + 88, y0 + 76], 16,
                            fill=INK)
        d.polygon([(x0 + 8, y0 + 52), (x0 + 2, y0 + 66), (x0 + 8, y0 + 82),
                   (x0 + 16, y0 + 82), (x0 + 22, y0 + 66)],
                  fill=INK)
        d.polygon([(x0 + 88, y0 + 52), (x0 + 94, y0 + 66), (x0 + 88, y0 + 82),
                   (x0 + 80, y0 + 82), (x0 + 74, y0 + 66)],
                  fill=INK)
        d.rectangle([x0 + 22, y0 + 50, x0 + 30, y0 + 66], fill=colour)
        d.rectangle([x0 + 18, y0 + 54, x0 + 34, y0 + 62], fill=colour)
        d.ellipse([x0 + 62, y0 + 48, x0 + 72, y0 + 58], fill=colour)
        d.ellipse([x0 + 74, y0 + 56, x0 + 84, y0 + 66], fill=colour)
        d.ellipse([x0 + 40, y0 + 62, x0 + 48, y0 + 70], fill=CREAM)
        d.ellipse([x0 + 52, y0 + 62, x0 + 60, y0 + 70], fill=CREAM)
    elif kind == "dome":
        d.rectangle([x0 + 14, y0 + 58, x0 + 82, y0 + 82], fill=INK)
        d.pieslice([x0 + 28, y0 + 22, x0 + 68, y0 + 62], 180, 360, fill=INK)
        d.line([x0 + 48, y0 + 10, x0 + 48, y0 + 22], fill=INK, width=5)
        d.ellipse([x0 + 44, y0 + 6, x0 + 52, y0 + 14], fill=colour)
        for x in (x0 + 24, x0 + 44, x0 + 64):
            d.rectangle([x, y0 + 66, x + 8, y0 + 82], fill=CREAM)
        d.polygon([(x0 + 70, y0 + 82), (x0 + 92, y0 + 82), (x0 + 92, y0 + 60)],
                  fill=colour)
    elif kind == "gavel":
        d.line([x0 + 20, y0 + 76, x0 + 76, y0 + 20], fill=INK, width=8)
        d.rounded_rectangle([x0 + 52, y0 + 8, x0 + 90, y0 + 30], 6, fill=INK)
        d.rounded_rectangle([x0 + 6, y0 + 78, x0 + 44, y0 + 90], 4, fill=colour)
        d.ellipse([x0 + 8, y0 + 14, x0 + 34, y0 + 40], outline=colour, width=5)
    elif kind == "swirl":
        # cyclone: spiral arms around a calm eye
        for i, ang in enumerate(range(0, 360, 30)):
            r = math.radians(ang)
            r1 = 14 + (i % 4) * 4
            r2 = 34 + (i % 3) * 4
            x1 = cx + int(r1 * math.cos(r))
            y1 = cy + int(r1 * math.sin(r))
            x2 = cx + int(r2 * math.cos(r))
            y2 = cy + int(r2 * math.sin(r))
            d.line([x1, y1, x2, y2], fill=INK, width=6)
        d.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], fill=colour,
                  outline=INK, width=3)
    elif kind == "flags":
        # two crossed flags on poles
        d.line([x0 + 30, y0 + 12, x0 + 30, y0 + 88], fill=INK, width=5)
        d.line([x0 + 66, y0 + 12, x0 + 66, y0 + 88], fill=INK, width=5)
        d.polygon([(x0 + 30, y0 + 12), (x0 + 62, y0 + 22), (x0 + 30, y0 + 34)],
                  fill=colour)
        d.polygon([(x0 + 66, y0 + 12), (x0 + 34, y0 + 22), (x0 + 66, y0 + 34)],
                  fill=INK)
        d.rectangle([x0 + 18, y0 + 84, x0 + 78, y0 + 90], fill=INK)
    elif kind == "cloud":
        # rain cloud with three drops
        d.ellipse([x0 + 16, y0 + 18, x0 + 52, y0 + 54], fill=INK)
        d.ellipse([x0 + 38, y0 + 8, x0 + 74, y0 + 44], fill=INK)
        d.ellipse([x0 + 58, y0 + 22, x0 + 88, y0 + 52], fill=INK)
        d.rectangle([x0 + 16, y0 + 40, x0 + 88, y0 + 54], fill=INK)
        for x in (x0 + 28, x0 + 48, x0 + 68):
            d.polygon([(x, y0 + 64), (x - 6, y0 + 78), (x + 6, y0 + 78)],
                      fill=colour)
            d.ellipse([x - 6, y0 + 72, x + 6, y0 + 84], fill=colour)


def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)

    # ---- Header banner ----
    d.rectangle([0, 0, W, 168], fill=INK)
    d.rectangle([0, 168, W, 176], fill=RED)
    d.text((40, 14), "THE WORLD IN ONE DAY", font=F_KICK, fill=MUSTARD)
    d.text((40, 44), "19 NOVEMBER 2026", font=F_TITLE, fill=WHITE)
    d.text((40, 128), "THURSDAY  •  SIX STORIES THAT LED THE DAY",
           font=F_SUB, fill=(255, 255, 255))

    # ---- Bento grid: 2 columns x 3 rows ----
    margin, gap = 24, 20
    cw = (W - 2 * margin - gap) // 2
    ch = 238
    top = 196
    for i, s in enumerate(STORIES):
        row, col = divmod(i, 2)
        x = margin + col * (cw + gap)
        y = top + row * (ch + gap)
        # card
        d.rounded_rectangle([x, y, x + cw, y + ch], 14, fill=WHITE,
                            outline=INK, width=4)
        # coloured tag chip
        tag = s["tag"]
        tw = d.textlength(tag, font=F_TAG) + 20
        d.rounded_rectangle([x + 16, y + 14, x + 16 + tw, y + 42], 8,
                            fill=s["colour"], outline=INK, width=3)
        d.text((x + 26, y + 18), tag, font=F_TAG, fill=INK)
        # icon badge
        ix, iy = x + 62, y + 118
        d.ellipse([ix - 56, iy - 56, ix + 56, iy + 56], fill=CREAM,
                  outline=INK, width=4)
        draw_icon(d, s["icon"], ix, iy, s["colour"])
        # headline + body
        tx = x + 132
        twidth = x + cw - 18 - tx
        lines = wrap(s["head"], F_HEAD, twidth, d)[:2]
        ly = y + 56
        for ln in lines:
            d.text((tx, ly), ln, font=F_HEAD, fill=INK)
            ly += 36
        for ln in wrap(s["body"], F_BODY, twidth, d)[:3]:
            d.text((tx, ly), ln, font=F_BODY, fill=MUTED)
            ly += 26

    # ---- Footer ----
    fy = top + 3 * ch + 2 * gap + 12
    d.text((40, fy), "Events of 19 November 2026, as reported that morning.",
           font=F_FOOT, fill=INK)
    d.text((40, fy + 26),
           "Sources: Reuters, Le Monde, AP, India Meteorological Dept, PIB, NWS.",
           font=F_FOOT, fill=MUTED)

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
