# Build transcript — "The World in One Day" (make.fun news-image-20261123)

Built fresh in this session on 24 Nov 2026 (started 06:55 WIB, after the
competition opened 23 Nov 00:00 UTC / 07:00 WIB; deadline 25 Nov 00:00 UTC
/ 07:00 WIB). This is a clean rebuild: the earlier local build (commit
4093794) was abandoned per Bos's decision and none of its files were used.

## What happened, in order

1. Downloaded the official kit fresh from
   https://make.fun/c/news-image-20261123/kit into a new clean work dir.
   Read competition.yaml: slug news-image-20261123, opens 2026-11-23
   00:00 UTC, deadline 2026-11-25 00:00 UTC, $100, 50 places.
2. Re-verified the six stories against web reports of 23 Nov 2026 (all
   confirmed 23 Nov): Kospi -3.31% to 4,708.54 in the AI sell-off; 14
   tankers staged at Kharg, seven hit since 16 Nov, Trump warns
   blockade-runners end "at the bottom of the sea"; Dymer toll 11,
   seven-year-old Davyd pulled alive after 14 hours under the rubble;
   Vanuatu M6.5 quake 02:40 UTC, ~601 km deep, no tsunami; NATO North
   Atlantic Council emergency session after three Russian Kh-101 missiles
   entered Polish airspace; MSCI open to alternatives to a two-step
   Indonesia downgrade after the Prabowo call (Bloomberg, 23 Nov).
   Excluded as stale: Democrats 258 seats, El Chapo Isidro, Anthropic
   IPO, Mets/Skubal, IEU-CEPA, COP31 collapse — all 21/22 Nov news.
3. Wrote `draw_news.py` fresh in this session (PIL, no network, no copy
   from the 21/22 Nov entries or the abandoned build): a broadsheet with
   masthead, dateline, one lead story and five numbered stories, with
   in-code fit asserts. Ran it to draw the front page into `news.png`
   (1024 x 1024, ~142 KB). Viewed the render: masthead, date, lead, all
   five numbered stories and the footer all legible, nothing clipped.
4. Wrote `main.py` fresh in this session (stdlib only): copies `news.png`
   to `/output/entry.png`.
5. Wrote `README.md` (the six stories + sources + how it is built),
   `LICENSE` (MIT + SPDX, from the kit starter, copyright FaizaaX), and
   `.makefun/owner.json` (wallet 3RgSNJfVhENtVFYbR81qgS3v3Wc3sq6ty2D2kjcPhwUE).
6. Ran `main.py` twice; both runs wrote identical bytes to
   `/output/entry.png` (see verification below).
7. Git-committed the entry in this session; kit `check` next, then bundle
   (this session + usage), GitHub push via browser task, and submit before
   the 07:00 WIB deadline.

## Verification

- `python3 draw_news.py` → `news.png` 1024 x 1024 PNG, 141,574 bytes.
- `python3 main.py` → writes to `/output/entry.png`; second run → same
  bytes (sha256 compared, identical).
- Image viewed before committing: masthead, date, lead story, all five
  numbered stories and the footer line all render fully, nothing clipped.

## Files

- `main.py` — the entry program (copies `news.png` to `/output/entry.png`)
- `news.png` — the image (drawn in-session by `draw_news.py`)
- `draw_news.py` — the script that drew the image
- `README.md`, `LICENSE`, `transcript.md` (this file)
