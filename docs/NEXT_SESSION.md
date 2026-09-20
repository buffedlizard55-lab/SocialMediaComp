# Work remaining and limitations

## Do next session
1. Enable GitHub Pages in repo Settings → Pages → Deploy from branch `main` / `/docs` or root (`index.html`). This session cannot toggle that setting via git alone.
2. Add live-count refresh only with official APIs and stored secrets (TikTok Research API, Meta Graph API, Reddit OAuth). Without keys, do not scrape.
3. Expand beyond top-50 celebrities to mid-tier *organic* niche accounts (pets, makeup tutorials, indie gaming) once each profile can be opened and screenshotted with date-stamped follower counts.
4. Facebook Pages: add a Wikipedia or CrowdTangle-backed list when a comparable sourced table is confirmed line-by-line.
5. Separate “celebrity/brand” vs “creator-from-zero” cohorts so the leaderboard is not dominated by already-famous people.
6. Document engagement-rate (likes/comments per follower), not only follower totals — totals are a poor proxy for *fast* growth.

## Limitations blocking a fully successful project
- No unauthenticated official bulk APIs; live numbers here are **snapshots from secondary lists**.
- Wikipedia and Visual Capitalist **lag** and round figures.
- Cannot prove “organic” vs purchased/boosted from public totals.
- Arena session cannot merge onto `main` if branch policy forbids switching; PR is opened from the session branch.
- GitHub Pages URL is `https://<owner>.github.io/SocialMediaComp/` only after Pages is enabled.

## Irregularities flagged
- Entries 4, 9, 10, 16 are **brand/platform/event** accounts, not independent creators.
- Reddit figures are **May 2025** Visual Capitalist, not 2026-09-20 live counts.
- TikTok FIFA row used the Wikipedia table (rank 9, 85.4M) from the same fetch as ranks 1–8.
