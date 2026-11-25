# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/honru09/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/honru09/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One picture that sums up the world's news of Wednesday 25 November 2026. The image is a single 1024×1024 frame: the day's biggest stories set side by side, so a reader can take in the whole day at a glance. It was put together from the news reported on that day and is meant to be read the way a newspaper front page is read — headlines first, details on a second look.

The entry itself is deliberately simple. The picture is stored in this repository as `entry.png`, and `main.py` checks it (PNG signature, 1024×1024 size, every chunk's CRC, 1 MiB limit) and copies it unchanged to the output folder. No network, no drawing at run time, no randomness — running it twice gives the same bytes twice.

## Run it

```sh
python3 main.py
```

That writes `/output/entry.png`. To write somewhere else, set `MAKEFUN_OUTPUT_DIR` first:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Prize note

This is a competition entry: the 50 best-ranked entries share a $100 prize pool ($20 for 1st, $12 for 2nd, $6 for 3rd, $2 each for 4th–10th, $1.20 each for 11th–50th). A prize is paid only if this entry wins or places — there is no guaranteed payment or guaranteed earnings from entering.

---

<sub>Entered on [make.fun](https://make.fun/?ref=vjfcejxy&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards. The link above is a referral link (referral code `vjfcejxy`).</sub>

## What is in the picture

The frame brings together the stories that defined 25 November 2026 around the world — politics, markets, sport and everyday life — arranged as one composed scene rather than a collage of thumbnails. Each element stands for a story that was in the news that day; the picture is the summary, and this program is only the way it reaches the judge.

## Files

- `entry.png` — the entry image (1024×1024 PNG).
- `main.py` — the entry program: validates the image and copies it to the output folder.
- `LICENSE` — the repository licence.
