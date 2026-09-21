# SocialMediaComp

Competition-style leaderboard of high-reach social accounts and communities
(TikTok, Instagram, Facebook, Reddit, YouTube, X, Twitch), with **cited sources for
every row** and a line-by-line verification log.

Live site (GitHub Pages): `https://buffedlizard55-lab.github.io/SocialMediaComp/`

## What this is

- **80 entries** in `data/master-list.json`
  - Batch 1 (1–20): TikTok, Instagram, Reddit — merged via PR #1
  - Batch 2 (21–40): Facebook, plus food, K-pop, cricket, photography, DIY — PR #2
  - Batch 3 (41–60): YouTube, X, Twitch, plus pet / makeup / gaming niche rows — PR #3
  - Batch 4 (61–80): organic and unusual growth cases (Shorts, science, beatbox,
    event streams, a Guinness pig record, dated creator clocks) — this session
- Cohort, country, and a flag on every irregular row
- Official education links and observed patterns in `data/strategies.json`
- Verification log: `docs/VERIFICATION.md` (Q1–Q32)
- Static site: `index.html` (filter, search, notes, clocks, likes density, cohort medians)
- Checks: `python3 scripts/validate.py`
- Snapshot of the file as written on 21 September 2026: `data/snapshots/2026-09-21-master-list.json`

## What this is not

- Not live follower counts. Every figure is a dated snapshot from its cited source.
- Not proof of organic versus paid or platform-engineered growth. Flagged rows exist.
- Not a guide to buying engagement. That is against platform rules and out of scope.

## Verify

Every row has a `profile_url` and a `source_url`. Open both. Where a second page was
read, `article_url` is set and linked from the row notes.
`docs/VERIFICATION.md` records which table cell each figure was read from.

## Remaining work

See `docs/NEXT_SESSION.md`.
