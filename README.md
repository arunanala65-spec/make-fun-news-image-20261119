# make-fun-news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/arunanala65-spec/make-fun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/arunanala65-spec/make-fun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

## The World in One Day — 19 November 2026

Entry for make.fun `news-image-20261119`: "Sum up 19 November's world news in one image."

## The image

A 1024×1024 PNG infographic. A dark banner names the day — **19 NOVEMBER 2026,
Thursday** — above six story tiles (bento-grid layout, retro-pop-grid style:
flat pop colours, thick ink outlines, drawn icons, no photos).

The six stories are events of Thursday 19 November 2026 and developments
first reported that morning, each cross-checked against at least two sources.
Two of them are events scheduled for the day itself (the Shenzhen trilateral
and the ICJ ruling), so they are stated as happening today — their outcomes
were not yet known when this image was made, early in the UTC day:

1. **GTA VI rolls out worldwide** — after 13 years, Vice City opens at
   midnight market by market, starting in New Zealand; 99 on Metacritic,
   ~16 million copies sold for $1.5bn before release.
   (Reuters; TBS News; NorthJersey.com)
2. **Trump, Putin, Xi meet in Shenzhen** — the first trilateral of the three
   sitting leaders, on the APEC summit's sidelines, with Ukraine, Iran,
   trade and nuclear arms on the agenda.
   (Reuters via World of Now; Le Monde; Associated Press)
3. **World Court rules on Rohingya case** — the ICJ delivers its judgment
   today on whether Myanmar committed genocide against the Rohingya;
   the first state ever found responsible would be a landmark.
   (Pollar News; bdnews / bdjam; The Globuzz)
4. **Cyclone Akvan nears India's coast** — the India Meteorological
   Department's 02:30 bulletin on 19 November keeps a red alert and
   extremely heavy rain for 19–20 November; landfall due on Friday.
   (Transclew live updates, citing IMD bulletin 27; The Daily Jagran)
5. **India, Japan hold 2+2 talks** — foreign and defence ministers
   Rajnath Singh and S. Jaishankar meet Shinjiro Koizumi and Toshimitsu
   Motegi in Tokyo to deepen security and maritime ties.
   (Press Information Bureau; The Hindu BusinessLine; Apto News)
6. **Storm soaks California again** — an atmospheric river brings a
   second day of rain; a flood watch runs in Los Angeles on Thursday,
   and a 46-mile stretch of Highway 1 through Big Sur is shut.
   (USA Today; Demokratis / NWS; Karlobag, citing SF Chronicle)

Claims that could not be pinned to 19 November were left out, and none of
the 18 November stories (Iran strikes on Gulf bases, the APEC opening,
Kahana's election, US measles status, Ebola in Congo, Voyager 1) are
repeated here.

## How it was made

`render.py` draws the infographic with Python + Pillow and DejaVu fonts
— every word is rendered by code, so there is no garbled text. No image
model and no network were used. Re-run it with `python3 render.py`
to regenerate `entry.png`.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, stdlib only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). It is deterministic:
the same bytes are copied on every run.

## Files

- `main.ts` — the entry program
- `entry.png` — the image (1024×1024, under 1 MiB)
- `render.py` — the script that drew `entry.png`
- `LICENSE` — MIT

---
<sub>Entered on [make.fun](https://make.fun/?ref=ce51ph37&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
