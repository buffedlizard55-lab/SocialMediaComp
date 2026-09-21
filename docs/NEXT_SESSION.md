# Work remaining and limitations

Status after the 2026-09-21 batch-3 session: **60 entries** across TikTok, Instagram,
Facebook, Reddit, YouTube, X and Twitch; pets/makeup/gaming topic gaps filled with
record/infobox-sourced niche entries; `scripts/validate.py` structural checker added;
per-entry verification log in `docs/VERIFICATION.md` (Q1–Q15).

## Do next session

1. **Confirm the Pages deployment shows the batch-3 content.** After this PR merges,
   the rebuild takes a minute or two; confirm
   `https://buffedlizard55-lab.github.io/SocialMediaComp/` serves 60 entries and the
   new platform filter (YouTube / X / Twitch).
2. **Manual click-throughs still owed** (environment blocks these domains):
   - Facebook slugs (batch 2): `facebook.com/netflix`, `/5min.crafts/`, `/MrBean/`,
     `/shakira`, `/WillSmith` (VERIFICATION.md Q6).
   - Instagram pet slugs (batch 3): `instagram.com/jiffpom/`, `instagram.com/nala_cat/`
     (Q13) — also confirm the *live* follower counts and record them as fresh snapshots
     with a screenshot date.
   - X profile usernames (batch 3): `x.com/elonmusk`, `/BarackObama`, `/Cristiano`,
     `/realDonaldTrump`, `/narendramodi`, `/rihanna`, `/NASA` — table names were used
     verbatim, but no profile page was fetchable.
3. **More mid-tier niche entries** (the "fastest organic growth" core is still thin):
   makeup (Huda Kattan, James Charles, Jeffree Star), pets (Doug the Pug, Tucker Budzyn,
   Tika the Iggy), gaming (Jacksepticeye, Valkyrae, Kai Cenat — Twitch #1 at 21.4M).
   Wikipedia list pages stop at the global top-50, so expect article-infobox/GWR-style
   sources with per-row age flags, or collect date-stamped screenshots.
4. **Engagement-rate dataset.** TikTok rows have cumulative likes; YouTube rows could get
   public view counts from channel pages if ever reachable. Instagram/Facebook/X/Reddit
   engagement needs official APIs (Meta Graph API, Reddit OAuth, X API) with stored
   secrets. Without keys, do not scrape.
5. **Growth deltas.** Take dated snapshots of `master-list.json`
   (`data/snapshots/2026-09.json` today) and compute per-entry deltas once a second
   snapshot exists. MrBeast's "~133,000 subscribers/day" (cited) shows the kind of number
   this unlocks.
6. **Refresh aging rows.** Reddit rows are May-2025 (Q7); Guinness pet records are
   2019/2020 (Q13); NikkieTutorials infobox is March 2026. Re-verify when the platforms
   are reachable or via authenticated APIs.
7. **Cohort analysis view.** A dedicated section comparing creator vs celebrity vs brand
   vs community medians per platform would directly answer "which cohort grows fastest".
8. **Per-metric sorting.** The single metric sort now mixes subscribers, followers and
   members across 7 platforms (a noted limitation); add sort-by-metric-type grouping.

## Limitations blocking a fully successful project

- No unauthenticated official bulk follower APIs for TikTok/Instagram/Facebook/X; all
  figures are **snapshots from cited secondary sources**, not live counts.
- The build environment's network blocks the social platforms themselves (facebook.com,
  instagram.com, tiktok.com, reddit.com, x.com, twitch.tv), so profile pages cannot be
  opened from here; verification relies on cited list snapshots, infoboxes and record
  pages (VERIFICATION.md Q6, Q13).
- "Organic" growth cannot be proven from public totals; brand/celebrity/character/agency
  rows are flagged, and one row (entry 49, @elonmusk) is explicitly documented by
  Wikipedia as partially platform-engineered (Q14) — a bought/engineered-followers audit
  is out of reach.
- Wikipedia/Visual Capitalist/Guinness figures lag and round; batch-3 niche snapshots
  span 2019–2026 and are not directly comparable in age.
- Fastest-growth ranking requires ≥2 dated snapshots; only one snapshot per entry exists.
- The X list table carries a Wikipedia "[unreliable source?]" template on its sourcing
  note (Q14); treat X figures with extra caution.

## Irregularities flagged to date

Batch 1 (PR #1): entries 4, 9, 10, 16 are brand/platform/event accounts; Reddit figures
are May 2025. Batch 2 (PR #2): quirks Q1–Q9 (page-internal rounding inconsistencies,
Facebook table ordering quirk, band/brand/character accounts, slug verification limits,
Reddit snapshot age, third-party topic detail for entry 24). Batch 3 (this session):
Q10–Q15 (stale YouTube prose, infobox drift, third-party kids-channel detail, Guinness
cookie-wall/search-indexed reads, X list caveats incl. platform-owner flag,
intentional cross-platform duplicates).
