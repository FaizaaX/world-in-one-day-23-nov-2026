#!/usr/bin/env python3
"""Draw the front page for 'The World in One Day' - 23 November 2026.

A broadsheet: masthead, one lead story, then five numbered stories in a
single column, each with a kicker, a headline and a deck. Renders with PIL
into news.png (1024 x 1024).

Deterministic: fixed text, fixed fonts, fixed geometry, no timestamps, no
randomness, so re-running produces byte-identical output. Every text block
is measured before it is drawn and the script aborts if anything would
overflow its box or run past the footer.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 40
CONTENT_W = W - 2 * MARGIN

PAPER = (250, 248, 240)
INK = (16, 16, 16)
ACCENT = (23, 58, 110)      # deep navy
SOFT = (74, 74, 74)
RULE = (150, 148, 140)
FAINT = (205, 203, 194)

FONTS = Path("/usr/share/fonts/truetype/dejavu")


def load(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


MASTHEAD = load("DejaVuSerif-Bold.ttf", 52)
DATELINE = load("DejaVuSans-Bold.ttf", 19)
LEAD_KICKER = load("DejaVuSans-Bold.ttf", 18)
LEAD_HEAD = load("DejaVuSerif-Bold.ttf", 36)
LEAD_DECK = load("DejaVuSerif.ttf", 20)
NUM = load("DejaVuSans-Bold.ttf", 22)
KICKER = load("DejaVuSans-Bold.ttf", 16)
HEAD = load("DejaVuSerif-Bold.ttf", 24)
DECK = load("DejaVuSerif.ttf", 18)
FOOT = load("DejaVuSans.ttf", 15)

LEAD = (
    "SEOUL  ·  MARKETS",
    "AI rout sinks Kospi 3.3% to its January low",
    "Seoul's Kospi closed down 3.31% at 4,708.54 — its lowest since "
    "January — as a global sell-off in AI stocks hammered Samsung and "
    "SK hynix.",
)

# (number, kicker, headline, deck)
STORIES = [
    (
        "2",
        "HORMUZ  ·  THE GULF",
        "Fourteen tankers mass at Kharg as Trump warns of the deep",
        "Iran readies a tanker convoy to test the US blockade while Trump "
        "says ships that run it will end 'at the bottom of the sea'. Seven "
        "tankers have been hit since 16 November.",
    ),
    (
        "3",
        "DYMER  ·  UKRAINE",
        "Boy, 7, pulled alive after 14 hours under the rubble",
        "Davyd is rescued from a collapsed apartment block in Dymer as the "
        "toll from Sunday's Russian drone strike reaches 11. The Kyiv "
        "region declares a day of mourning.",
    ),
    (
        "4",
        "VANUATU  ·  THE PACIFIC",
        "M6.5 quake strikes 600 km down — no tsunami",
        "A magnitude 6.5 earthquake hits the Vanuatu region at 02:40 UTC, "
        "about 601 km deep. No damage is reported and no tsunami threat "
        "follows.",
    ),
    (
        "5",
        "BRUSSELS  ·  NATO",
        "NATO meets in emergency session over Poland",
        "The North Atlantic Council convenes after three Russian Kh-101 "
        "missiles entered Polish airspace on Friday and crashed in the "
        "south-east.",
    ),
    (
        "6",
        "JAKARTA  ·  MARKETS",
        "MSCI open to alternatives to Indonesia downgrade",
        "Bloomberg reports MSCI's chief told President Prabowo he is open "
        "to alternatives to a two-step downgrade after their 10 November "
        "call. The rupiah steadies.",
    ),
]

FOOTER = "Compiled from wire reports of 23 November 2026  ·  AP · Reuters · Bloomberg · USGS"
FOOTER2 = "make.fun  ·  news-image-20261123  ·  The World in One Day"


def wrap(draw, text, face, max_w):
    """Greedy word wrap; every returned line fits max_w or raises."""
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=face) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
            if draw.textlength(cur, font=face) > max_w:
                raise AssertionError(f"single word too wide: {word!r}")
    if cur:
        lines.append(cur)
    return lines


def text_h(face, n_lines, leading):
    return n_lines * (face.size + leading)


def draw_page():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Outer frame.
    d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=2)
    d.rectangle([22, 22, W - 23, H - 23], outline=FAINT, width=1)

    y = 44
    # Masthead.
    title = "THE WORLD IN ONE DAY"
    tw = d.textlength(title, font=MASTHEAD)
    assert tw <= CONTENT_W, "masthead too wide"
    d.text(((W - tw) / 2, y), title, font=MASTHEAD, fill=INK)
    y += MASTHEAD.size + 14

    # Dateline row: date left, story count right.
    date = "MONDAY 23 NOVEMBER 2026"
    count = "SIX STORIES  ·  ONE DAY"
    d.text((MARGIN, y), date, font=DATELINE, fill=ACCENT)
    cw = d.textlength(count, font=DATELINE)
    d.text((W - MARGIN - cw, y), count, font=DATELINE, fill=ACCENT)
    y += DATELINE.size + 12

    # Double rule under the header.
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=INK, width=3)
    y += 6
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=INK, width=1)
    y += 20

    # ---- Lead story (full width) ----
    kicker, headline, deck = LEAD
    d.text((MARGIN, y), kicker, font=LEAD_KICKER, fill=ACCENT)
    y += LEAD_KICKER.size + 8
    head_lines = wrap(d, headline, LEAD_HEAD, CONTENT_W)
    assert len(head_lines) <= 2, f"lead headline wraps to {len(head_lines)}"
    for line in head_lines:
        d.text((MARGIN, y), line, font=LEAD_HEAD, fill=INK)
        y += LEAD_HEAD.size + 6
    y += 2
    deck_lines = wrap(d, deck, LEAD_DECK, CONTENT_W)
    assert len(deck_lines) <= 3, f"lead deck wraps to {len(deck_lines)}"
    for line in deck_lines:
        d.text((MARGIN, y), line, font=LEAD_DECK, fill=SOFT)
        y += LEAD_DECK.size + 6
    y += 14
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=RULE, width=1)
    y += 18

    # ---- Numbered stories ----
    text_x = MARGIN + 52
    text_w = CONTENT_W - 52
    for number, skicker, shead, sdeck in STORIES:
        row_top = y
        # Number square.
        d.rectangle([MARGIN, row_top + 2, MARGIN + 36, row_top + 38],
                    fill=ACCENT)
        nw = d.textlength(number, font=NUM)
        d.text((MARGIN + (36 - nw) / 2, row_top + 6), number,
               font=NUM, fill=PAPER)
        # Kicker.
        d.text((text_x, row_top), skicker, font=KICKER, fill=ACCENT)
        yy = row_top + KICKER.size + 6
        # Headline.
        hl = wrap(d, shead, HEAD, text_w)
        assert len(hl) <= 2, f"story {number} headline wraps to {len(hl)}"
        for line in hl:
            d.text((text_x, yy), line, font=HEAD, fill=INK)
            yy += HEAD.size + 4
        # Deck.
        dl = wrap(d, sdeck, DECK, text_w)
        assert len(dl) <= 3, f"story {number} deck wraps to {len(dl)}"
        for line in dl:
            d.text((text_x, yy), line, font=DECK, fill=SOFT)
            yy += DECK.size + 4
        y = yy + 12
        d.line([(MARGIN, y), (W - MARGIN, y)], fill=FAINT, width=1)
        y += 18

    # ---- Footer (fixed zone at the bottom) ----
    foot_y = H - 66
    assert y <= foot_y - 6, f"stories run into footer: y={y}"
    d.line([(MARGIN, foot_y - 12), (W - MARGIN, foot_y - 12)],
           fill=INK, width=1)
    fw = d.textlength(FOOTER, font=FOOT)
    assert fw <= CONTENT_W, "footer too wide"
    d.text(((W - fw) / 2, foot_y), FOOTER, font=FOOT, fill=SOFT)
    fw2 = d.textlength(FOOTER2, font=FOOT)
    d.text(((W - fw2) / 2, foot_y + FOOT.size + 6), FOOTER2,
           font=FOOT, fill=SOFT)

    out = Path(__file__).resolve().parent / "news.png"
    img.save(out, "PNG")
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    draw_page()
