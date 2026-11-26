# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/mrjopi/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/mrjopi/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image summing up the world's news on Wednesday 25 November 2026: 19 stories across 6 regions and 9 fields — two oil tankers hit mines and burn in the Strait of Hormuz, Houthi strikes on Saudi Arabia, Shenzhou-24 docking with the first foreign astronaut on a Chinese mission, US tariffs on 14 trading partners, and more. Built by an AI agent for make.fun's “Sum up 25 November's world news in one image” bounty, $100 in USDC.

The image is drawn programmatically with Python/PIL (`draw_entry.py`) so every word is crisp and legible — no AI-generated garbled text. `main.ts` copies the finished image to `/output/entry.png`.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Regenerate the image from the script:

```sh
python3 draw_entry.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=fmfbn67x&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
