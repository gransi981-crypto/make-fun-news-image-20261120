# make-fun-news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/gransi981-crypto/make-fun-news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/gransi981-crypto/make-fun-news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A one-page newspaper front page that sums up Friday 20 November 2026's world news in a single image: Russia's biggest barrage of the war on Kyiv, with missiles falling inside Poland and NATO jets scrambling; the AI-stock sell-off pushing the S&P 500 into correction on its sixth straight down day; Trump defending his ties to Putin and Xi after the Shenzhen trilateral summit; plus the day's other stories — a magnitude 6.7 quake in Peru, Cyclone Akvan making landfall in Odisha, Houthi missiles aimed at Riyadh intercepted, Kerch Bridge rail traffic resuming, Hungary lifting its veto on Ukraine's EU talks, and Kenya counting down to an Ebola-free declaration — in the columns and ticker. Every story on the page was checked against same-day reporting in more than one outlet before it was drawn. The image is drawn at build time by `render.py` (Pillow) from same-day reporting verified in multiple outlets; the graded program `main.py` only copies the finished PNG to `/output/entry.png`.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=pab8n0ew&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
