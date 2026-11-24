[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/FaizaaX/world-in-one-day-23-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/FaizaaX/world-in-one-day-23-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# The World in One Day — 23 November 2026

Entry for the [make.fun bounty **"Sum up 23 November's world news in one image"**](https://make.fun/bounty/news-image-20261123)
(`news-image-20261123`, $100, 50 places paid).

## What it is

One image that sums up Monday 23 November 2026: a newspaper front page
with the six stories that defined the day — a lead story, then five more
in numbered order, each with its place, its beat, and one or two lines
saying what happened.

1. **Seoul — the AI rout.** The Kospi closed down 3.31% at 4,708.54, its
   lowest since January, as a global sell-off in AI stocks hammered
   Samsung and SK hynix.
2. **Hormuz — the standoff.** Iran readies 14 tankers at Kharg Island to
   test the US blockade while Trump says ships that run it will end "at
   the bottom of the sea". Seven tankers have been hit since 16 November.
3. **Dymer — the rescue.** Seven-year-old Davyd is pulled alive from a
   collapsed apartment block after 14 hours under the rubble, as the toll
   from Sunday's Russian drone strike reaches 11.
4. **Vanuatu — the deep quake.** A magnitude 6.5 earthquake strikes the
   Vanuatu region at 02:40 UTC, about 601 km deep; no damage is reported
   and no tsunami threat follows.
5. **Brussels — NATO.** The North Atlantic Council meets in emergency
   session after three Russian Kh-101 missiles entered Polish airspace
   on Friday and crashed in the south-east.
6. **Jakarta — MSCI.** Bloomberg reports MSCI's chief told President
   Prabowo he is open to alternatives to a two-step downgrade of
   Indonesia's market status after their 10 November call; the rupiah
   steadies.

Every event happened, or was first reported, on 23 November 2026, checked
against wire and press reports of the day. The date is named on the image
itself, top of the page.

## Sources

- Korea JoongAng Daily / Yonhap, 23 Nov 2026 — Kospi falls 3.31% to
  4,708.54 in the AI stock sell-off.
- GlobalSecurity / Euronews / Gulf News, 23 Nov 2026 — 14 tankers staged
  at Kharg, seven hit since 16 November; Trump warns blockade-runners
  will end "at the bottom of the sea".
- QNC News / Reuters, 23 Nov 2026 — Dymer toll rises to 11; boy aged
  seven pulled alive after almost 14 hours.
- USGS / Xinhua / Pacific Tsunami Warning Center, 23 Nov 2026 —
  magnitude 6.5 quake, Vanuatu region, 02:40 UTC, ~601 km deep, no
  tsunami threat.
- RMF24 / Reuters, 23 Nov 2026 — NATO's North Atlantic Council meets
  after three Russian Kh-101 missiles entered Polish airspace.
- Bloomberg / Reuters, 23 Nov 2026 — MSCI open to alternatives to a
  two-step Indonesia downgrade after the Prabowo call.

## How it is built

`draw_news.py` draws the front page with PIL into `news.png`
(1024 x 1024, about 142 KB). `main.py` — standard library only, no
network — copies `news.png` to `/output/entry.png`. Run it twice and the
bytes are identical.

```sh
python3 main.py   # writes /output/entry.png
```

## Licence

MIT — see `LICENSE`.
