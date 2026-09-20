# SocialMediaComp

Competition-style leaderboard of high-reach social accounts and communities
(TikTok, Instagram, Facebook, Reddit), with **cited sources for every row** and a
line-by-line verification log.

Live site (GitHub Pages, enabled): `https://buffedlizard55-lab.github.io/SocialMediaComp/`

## What this is

- **40 entries** in `data/master-list.json`
  - Batch 1 (1–20): TikTok, Instagram, Reddit — merged via PR #1
  - Batch 2 (21–40): adds **Facebook** coverage plus food, K-pop, magic, cricket,
    photography, DIY and education topics
- Cohort labels (`creator` / `celebrity` / `brand` / `community`) and countries on every row
- Official education links + observed growth patterns in `data/strategies.json`
- Per-entry verification log: `docs/VERIFICATION.md`
- Static GitHub Pages UI: `index.html` (filter by platform/cohort, search, sortable metric)

## What this is not

- Not live follower counts
- Not proof of organic vs paid growth
- Not a how-to for buying engagement (against platform rules and out of scope)

## Verify

Every row has a `profile_url` and a `source_url`; open both for manual review.
`docs/VERIFICATION.md` documents exactly which table row each figure was read from,
and flags every irregularity found (Q1–Q7).

## Remaining work

See `docs/NEXT_SESSION.md`.
