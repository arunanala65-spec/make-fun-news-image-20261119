#!/usr/bin/env python3
"""Draw the 19 November 2026 world-news infographic (1024x1024 PNG).

Six verified stories from Thursday 19 November 2026 -- events of the day
and developments first reported that morning, each checked against at
least two sources (see README.md) -- arranged as a bento grid under one
date banner. Style: retro-pop-grid, flat pop colours with thick ink
outlines. Every word is drawn by code with DejaVu fonts, so no text can
come out garbled. No image model and no network are used.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

SIZE = (1024, 1024)
INK = (26, 26, 46)
PAPER = (255, 246, 229)
CARD = (255, 255, 255)
GREY = (70, 70, 90)
RED = (230, 57, 70)
TEAL = (42, 157, 143)
GOLD = (233, 196, 106)
BLUE = (69, 123, 157)
TANGERINE = (244, 162, 97)
VIOLET = (123, 94, 167)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
PLAIN = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

TITLE = ImageFont.truetype(BOLD, 78)
SUBTITLE = ImageFont.truetype(BOLD, 26)
KICKER = ImageFont.truetype(BOLD, 22)
HEADLINE = ImageFont.truetype(BOLD, 28)
BODY = ImageFont.truetype(PLAIN, 20)
FOOTNOTE = ImageFont.truetype(PLAIN, 19)
TAG = ImageFont.truetype(BOLD, 17)

# tag, accent colour, headline, body, icon
STORIES = [
    ("GAMES  •  LAUNCH", RED,
     "GTA VI rolls out worldwide",
     "After 13 years, Vice City opens at midnight market by market; 99 on Metacritic.",
     "pad"),
    ("ASIA  •  SUMMIT", TANGERINE,
     "Trump, Putin, Xi meet in Shenzhen",
     "First trilateral of the three leaders, on APEC's sidelines.",
     "dome"),
    ("LAW  •  THE HAGUE", TEAL,
     "World Court rules on Rohingya case",
     "The ICJ delivers its judgment today on Myanmar and the Rohingya.",
     "gavel"),
    ("WEATHER  •  INDIA", BLUE,
     "Cyclone Akvan nears India's coast",
     "Red alert as the storm brings extremely heavy rain; landfall due on Friday.",
     "swirl"),
    ("ASIA  •  DEFENCE", VIOLET,
     "India, Japan hold 2+2 talks",
     "Foreign and defence ministers meet in Tokyo to deepen security and maritime ties.",
     "flags"),
    ("WEATHER  •  USA", GOLD,
     "Storm soaks California again",
     "Atmospheric river brings a second day of rain; flood watch in Los Angeles, Highway 1 shut.",
     "cloud"),
]


def flow(text, face, limit, pen):
    """Split text into lines no wider than `limit` pixels."""
    out, current = [], ""
    for word in text.split():
        trial = f"{current} {word}".strip()
        if pen.textlength(trial, font=face) <= limit:
            current = trial
        else:
            if current:
                out.append(current)
            current = word
    if current:
        out.append(current)
    return out


def icon_pad(pen, cx, cy, accent):
    """Game controller."""
    x, y = cx - 48, cy - 48
    pen.rounded_rectangle([x + 8, y + 34, x + 88, y + 76], 16, fill=INK)
    pen.polygon([(x + 8, y + 52), (x + 2, y + 66), (x + 8, y + 82),
                 (x + 16, y + 82), (x + 22, y + 66)], fill=INK)
    pen.polygon([(x + 88, y + 52), (x + 94, y + 66), (x + 88, y + 82),
                 (x + 80, y + 82), (x + 74, y + 66)], fill=INK)
    pen.rectangle([x + 22, y + 50, x + 30, y + 66], fill=accent)
    pen.rectangle([x + 18, y + 54, x + 34, y + 62], fill=accent)
    pen.ellipse([x + 62, y + 48, x + 72, y + 58], fill=accent)
    pen.ellipse([x + 74, y + 56, x + 84, y + 66], fill=accent)
    pen.ellipse([x + 40, y + 62, x + 48, y + 70], fill=PAPER)
    pen.ellipse([x + 52, y + 62, x + 60, y + 70], fill=PAPER)


def icon_dome(pen, cx, cy, accent):
    """Summit hall with a dome."""
    x, y = cx - 48, cy - 48
    pen.rectangle([x + 14, y + 58, x + 82, y + 82], fill=INK)
    pen.pieslice([x + 28, y + 22, x + 68, y + 62], 180, 360, fill=INK)
    pen.line([x + 48, y + 10, x + 48, y + 22], fill=INK, width=5)
    pen.ellipse([x + 44, y + 6, x + 52, y + 14], fill=accent)
    for col in (x + 24, x + 44, x + 64):
        pen.rectangle([col, y + 66, col + 8, y + 82], fill=PAPER)
    pen.polygon([(x + 70, y + 82), (x + 92, y + 82), (x + 92, y + 60)],
                fill=accent)


def icon_gavel(pen, cx, cy, accent):
    """Judge's gavel and sounding block."""
    x, y = cx - 48, cy - 48
    pen.line([x + 20, y + 76, x + 76, y + 20], fill=INK, width=8)
    pen.rounded_rectangle([x + 52, y + 8, x + 90, y + 30], 6, fill=INK)
    pen.rounded_rectangle([x + 6, y + 78, x + 44, y + 90], 4, fill=accent)
    pen.ellipse([x + 8, y + 14, x + 34, y + 40], outline=accent, width=5)


def icon_swirl(pen, cx, cy, accent):
    """Cyclone: spiral arms around a calm eye."""
    for step, deg in enumerate(range(0, 360, 30)):
        theta = math.radians(deg)
        inner = 14 + (step % 4) * 4
        outer = 34 + (step % 3) * 4
        x1 = cx + int(inner * math.cos(theta))
        y1 = cy + int(inner * math.sin(theta))
        x2 = cx + int(outer * math.cos(theta))
        y2 = cy + int(outer * math.sin(theta))
        pen.line([x1, y1, x2, y2], fill=INK, width=6)
    pen.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], fill=accent,
                outline=INK, width=3)


def icon_flags(pen, cx, cy, accent):
    """Two crossed flags on poles."""
    x, y = cx - 48, cy - 48
    pen.line([x + 30, y + 12, x + 30, y + 88], fill=INK, width=5)
    pen.line([x + 66, y + 12, x + 66, y + 88], fill=INK, width=5)
    pen.polygon([(x + 30, y + 12), (x + 62, y + 22), (x + 30, y + 34)],
                fill=accent)
    pen.polygon([(x + 66, y + 12), (x + 34, y + 22), (x + 66, y + 34)],
                fill=INK)
    pen.rectangle([x + 18, y + 84, x + 78, y + 90], fill=INK)


def icon_cloud(pen, cx, cy, accent):
    """Rain cloud with three drops."""
    x, y = cx - 48, cy - 48
    pen.ellipse([x + 16, y + 18, x + 52, y + 54], fill=INK)
    pen.ellipse([x + 38, y + 8, x + 74, y + 44], fill=INK)
    pen.ellipse([x + 58, y + 22, x + 88, y + 52], fill=INK)
    pen.rectangle([x + 16, y + 40, x + 88, y + 54], fill=INK)
    for drop in (x + 28, x + 48, x + 68):
        pen.polygon([(drop, y + 64), (drop - 6, y + 78), (drop + 6, y + 78)],
                    fill=accent)
        pen.ellipse([drop - 6, y + 72, drop + 6, y + 84], fill=accent)


ICONS = {
    "pad": icon_pad,
    "dome": icon_dome,
    "gavel": icon_gavel,
    "swirl": icon_swirl,
    "flags": icon_flags,
    "cloud": icon_cloud,
}


def draw_banner(pen):
    pen.rectangle([0, 0, SIZE[0], 168], fill=INK)
    pen.rectangle([0, 168, SIZE[0], 176], fill=RED)
    pen.text((40, 14), "THE WORLD IN ONE DAY", font=KICKER, fill=GOLD)
    pen.text((40, 44), "19 NOVEMBER 2026", font=TITLE, fill=CARD)
    pen.text((40, 128), "THURSDAY  •  SIX STORIES THAT LED THE DAY",
             font=SUBTITLE, fill=CARD)


def draw_tile(pen, story, x, y, width, height):
    tag, accent, head, body, kind = story
    pen.rounded_rectangle([x, y, x + width, y + height], 14, fill=CARD,
                          outline=INK, width=4)
    chip = pen.textlength(tag, font=TAG) + 20
    pen.rounded_rectangle([x + 16, y + 14, x + 16 + chip, y + 42], 8,
                          fill=accent, outline=INK, width=3)
    pen.text((x + 26, y + 18), tag, font=TAG, fill=INK)
    badge_x, badge_y = x + 62, y + 118
    pen.ellipse([badge_x - 56, badge_y - 56, badge_x + 56, badge_y + 56],
                fill=PAPER, outline=INK, width=4)
    ICONS[kind](pen, badge_x, badge_y, accent)
    text_x = x + 132
    text_w = x + width - 18 - text_x
    line_y = y + 56
    for line in flow(head, HEADLINE, text_w, pen)[:2]:
        pen.text((text_x, line_y), line, font=HEADLINE, fill=INK)
        line_y += 36
    for line in flow(body, BODY, text_w, pen)[:3]:
        pen.text((text_x, line_y), line, font=BODY, fill=GREY)
        line_y += 26


def draw_footer(pen, top):
    pen.text((40, top), "Events of 19 November 2026, as reported that morning.",
             font=FOOTNOTE, fill=INK)
    pen.text((40, top + 26),
             "Sources: Reuters, Le Monde, AP, India Meteorological Dept, PIB, NWS.",
             font=FOOTNOTE, fill=GREY)


def build():
    canvas = Image.new("RGB", SIZE, PAPER)
    pen = ImageDraw.Draw(canvas)
    draw_banner(pen)
    margin, gutter = 24, 20
    tile_w = (SIZE[0] - 2 * margin - gutter) // 2
    tile_h = 238
    start_y = 196
    for index, story in enumerate(STORIES):
        row, col = divmod(index, 2)
        tile_x = margin + col * (tile_w + gutter)
        tile_y = start_y + row * (tile_h + gutter)
        draw_tile(pen, story, tile_x, tile_y, tile_w, tile_h)
    draw_footer(pen, start_y + 3 * tile_h + 2 * gutter + 12)
    canvas.save("entry.png", optimize=True)
    size = os.path.getsize("entry.png")
    print(f"saved entry.png {canvas.size} ({size} bytes)")


if __name__ == "__main__":
    build()
