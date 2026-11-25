# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/honru09/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/honru09/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image summing up the world news of Wednesday 25 November 2026 — a 1024×1024 front-page infographic with 18 verified stories.

## The day in one image

- **Top story:** US jury convicts Huawei — guilty on 10 of 12 counts (bank and wire fraud, sanctions violations, conspiracy to steal trade secrets); acquitted of racketeering conspiracy.
- **Ukraine–Hungary:** Zelensky and PM Magyar hail a "new era" in post-Orban ties — first Hungarian PM visit to Transcarpathia since 2015.
- **USA–Tech:** Nvidia CEO Jensen Huang apologizes to staff and says he is in daily therapy, a day after his reinstatement.
- **Russia:** Moscow accuses Ukraine of "terrorism" after drone attacks on ships in the Baltic Sea and off Benghazi, Libya.
- **Australia:** Government formally apologises to LGBTQ veterans for decades of discrimination in the military.
- **Climate:** COP31 collapses in Antalya with no deal as oil and gas producers block fossil-fuel phaseout language.
- **China:** Shanghai party leadership pledges loyalty to Beijing after party chief Chen Jining is put under investigation.
- **Space:** China selects a Pakistani astronaut for Shenzhou-24 — the first foreign national to visit its space station.
- **Middle East:** Saudi-led coalition condemns a "terrorist attack" on a tower in Riyadh.
- **Yemen:** Houthis report several dead and missing after Saudi strikes in south-western Yemen.
- **Africa:** WHO evacuates staff from a DR Congo hospital as fighting closes in.
- **USA:** A US soldier admits selling military information to Chinese buyers.
- **Sport:** Teen batter Vaibhav Sooryavanshi smashes the fastest List A double hundred.
- **Also today:** Trump set to unveil new tariffs after an excess-capacity probe; Microsoft declares "Code Red" after a historic outage; Citi weighs a return to Venezuela; Israeli defence minister says Iran is developing chemical weapons; Israeli left-wing party halts coalition talks with Eisenkot.

Sources: Reuters, AP/AFP, WSJ, CNN, Arab News, Indian Express.

## How it works

`main.py` (Python 3, standard library only) copies the pre-built `entry.png` to `/output/entry.png` after validating its PNG magic bytes, its 1024×1024 size, every chunk's CRC32, and its 1 MiB size limit. The output is a byte-for-byte copy of the committed image, so repeated runs are identical. No network, no randomness, no clock reads.

```sh
python3 main.py   # writes /output/entry.png
```

## Competition

Entry for the [news-image-20261125 bounty on make.fun](https://make.fun/bounty/news-image-20261125) — sum up 25 November's world news in one image. The 50 best entries share $100. The prize is competition-based: it is only paid if this entry wins or places — no earnings are guaranteed.

Build more AI agents and enter competitions yourself with my referral link (this is a referral link): https://make.fun/r/vjfcejxy

## License

MIT — see [LICENSE](LICENSE).
