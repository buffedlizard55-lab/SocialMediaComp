# Work remaining and limitations

Status after the 2026-09-20 batch-2 session: **40 entries** across TikTok, Instagram,
Facebook and Reddit; Facebook coverage added; cohort/country/likes fields added;
per-entry verification log in `docs/VERIFICATION.md`.

## Do next session

1. **Confirm GitHub Pages is enabled** (repo Settings → Pages → Deploy from branch `main`, root).
   The site only becomes live at `https://buffedlizard55-lab.github.io/SocialMediaComp/`
   after that toggle; it cannot be flipped reliably from inside the repo. If it is already
   enabled, just confirm the URL loads.
2. **Manual click-through of the 5 Facebook page slugs** (`facebook.com/netflix`,
   `/5min.crafts/`, `/MrBean/`, `/shakira`, `/WillSmith`) — they were verified via search
   snippets only because facebook.com refused connections from the build environment
   (see VERIFICATION.md Q6).
3. **Mid-tier organic niche accounts.** The lists are still top-of-funnel celebrities/brands.
   Add pets, makeup-tutorial, and indie-gaming creators whose follower counts can be
   captured with date-stamped screenshots or official APIs — needed for a real
   "fastest organic growth" competition rather than a biggest-total list.
4. **Engagement-rate dataset.** TikTok's public table includes cumulative likes, so a
   likes-per-follower column is computable now for TikTok rows; Instagram/Facebook/Reddit
   engagement needs official APIs (Meta Graph API, Reddit OAuth) with stored secrets.
   Without keys, do not scrape.
5. **YouTube + X coverage.** Wikipedia's "List of most-subscribed YouTube channels" and
   Visual Capitalist's "Most Followed People on X in 2026" both exist and are citable the
   same way; add them as a batch 3 (~20 more entries).
6. **Growth deltas.** A leaderboard competition needs *change over time*. Take dated
   snapshots of `master-list.json` (e.g. `data/snapshots/2026-09.json`) and compute deltas
   per entry once at least two snapshots exist.
7. **Refresh aging rows.** Reddit rows are May-2025 snapshots (VERIFICATION.md Q7); refresh
   when reddit.com is reachable or via an authenticated API.
8. **Cohort analysis page.** The `cohort` filter exists; a dedicated view comparing
   creator vs celebrity vs brand medians would directly answer "which cohort grows fastest".

## Limitations blocking a fully successful project

- No unauthenticated official bulk follower APIs for TikTok/Instagram/Facebook; all figures
  are **snapshots from cited secondary lists**, not live counts.
- The build environment's network blocks tiktok.com, instagram.com, facebook.com and
  reddit.com, so direct profile cross-checks are impossible here (VERIFICATION.md Q6).
- "Organic" growth cannot be proven from public totals; brand/celebrity/character pages are
  flagged but a bought-followers audit is out of reach.
- Wikipedia/Visual Capitalist figures lag and round (Reddit: ±0.5M and ~16 months old).
- Fastest-growth ranking requires ≥2 dated snapshots; only one snapshot per entry exists so far.

## Irregularities flagged to date

Batch 1 (PR #1): entries 4, 9, 10, 16 are brand/platform/event accounts; Reddit figures are
May 2025. Batch 2: see `docs/VERIFICATION.md` quirks Q1–Q7 (page-internal rounding
inconsistencies, Facebook table ordering quirk, band/brand/character accounts, slug
verification limits, Reddit snapshot age).
