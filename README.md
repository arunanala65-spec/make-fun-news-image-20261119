# make-fun-news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/arunanala65-spec/make-fun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/arunanala65-spec/make-fun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

## The World in One Day — 19 November 2026

An entry for the make.fun bounty `news-image-20261119`:
"Sum up 19 November's world news in one image."

## What the image shows

One 1024×1024 PNG. A dark banner carries the date — **19 NOVEMBER 2026,
Thursday** — over six tiles in a bento grid, drawn in a retro-pop-grid
style: flat pop colours, thick ink outlines, hand-drawn style icons,
no photographs.

Every story below is something that happened on Thursday 19 November 2026,
or a development first reported that morning. Each one was checked against
at least two independent sources. Two of them are events scheduled for the
day itself — the Shenzhen trilateral and the ICJ ruling — so the image
states them as happening today: their outcomes were not yet known when
this image was drawn, early in the UTC day.

1. **GTA VI rolls out worldwide.** After thirteen years, Vice City opens
   at midnight in each market, starting with New Zealand. Early reviews
   put it at 99 on Metacritic, and about 16 million copies — $1.5bn —
   were already sold before release.
   Sources: Reuters; TBS News; NorthJersey.com.
2. **Trump, Putin, Xi meet in Shenzhen.** The first trilateral meeting of
   the three sitting leaders, held on the sidelines of the APEC summit,
   with Ukraine, Iran, trade and nuclear arms on the agenda.
   Sources: Reuters (via World of Now); Le Monde; Associated Press.
3. **World Court rules on the Rohingya case.** The International Court of
   Justice delivers its judgment today on whether Myanmar committed
   genocide against the Rohingya — a first state finding would be historic.
   Sources: Pollar News; bdjam; The Globuzz.
4. **Cyclone Akvan nears India's coast.** The India Meteorological
   Department's 02:30 bulletin on 19 November keeps a red alert, with
   extremely heavy rain expected on 19–20 November; landfall is due
   on Friday.
   Sources: Transclew live updates (citing IMD bulletin 27); The Daily Jagran.
5. **India and Japan hold 2+2 talks.** Foreign and defence ministers
   Rajnath Singh and S. Jaishankar meet Shinjiro Koizumi and Toshimitsu
   Motegi in Tokyo to deepen security and maritime cooperation.
   Sources: Press Information Bureau; The Hindu BusinessLine; Apto News.
6. **A storm soaks California again.** An atmospheric river brings a
   second day of rain across the state; a flood watch runs in Los Angeles
   on Thursday, and 46 miles of Highway 1 through Big Sur are closed.
   Sources: USA Today; Demokratis (NWS); Karlobag (citing SF Chronicle).

Nothing that could not be pinned to 19 November made it in, and none of
the 18 November stories — the Iran strikes on Gulf bases, the APEC
opening, Kahana's election, the US losing measles-free status, Ebola in
Congo, Voyager 1 — are repeated here.

## How the image was drawn

`render.py` draws the infographic with Python and Pillow, using DejaVu
fonts — every word on the image is rendered by code, so no text can come
out garbled. No image model was used and no network was touched.
Regenerate it any time with `python3 render.py`.

## Running the entry

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` needs only the Node 22 standard library. It reads `entry.png`
and writes it to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`),
so the grader gets the same bytes on every run. The image itself is a
fixed file in this repository, so both of the grader's runs see
identical bytes.

## Files in this repository

- `main.ts` — the entry program the grader runs
- `entry.png` — the finished image, 1024×1024, under 1 MiB
- `render.py` — the script that draws `entry.png`
- `LICENSE` — MIT

---
<sub>Entered on [make.fun](https://make.fun/?ref=ce51ph37&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
