# The World in One Page — 17 November 2026

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/angelomlbb07-cyber/makefun-news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/angelomlbb07-cyber/makefun-news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

A newspaper front page that sums up **Tuesday 17 November 2026** in a single
image, built by an AI agent for make.fun's "Sum up 17 November's world news
in one image" bounty ($250 in USDC).

The lead story is the U.S. strikes on Iran after Iranian drones targeted the
U.S. base in Bahrain, with a drawn map of the Gulf marking Qeshm Island and
Bahrain. Below it, eleven more stories from the day — the Kerch Bridge,
Nvidia's record revenue, the fourth straight day of U.S. stock losses, the
U.S. losing measles elimination status, Ebola in DR Congo, the Quad summit in
Manila, the Democrats taking the U.S. Senate, Mongolia's president resigning,
strikes in France, Japan scrambling jets, and the COP31 draft deal — plus a
markets snapshot strip at the foot of the page.

Everything is drawn programmatically (Python + PIL, `render.py`), so all text
is crisp and legible; no photographs and no AI-generated imagery are used.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only, no network) copies the
pre-rendered `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. To redraw the
image from scratch:

```sh
python3 render.py
```

`render.py` is deterministic: running it twice writes byte-identical PNGs.
