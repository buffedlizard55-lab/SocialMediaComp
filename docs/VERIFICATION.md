# Verification log

Rule: **no figure enters `data/master-list.json` unless it was read, line by line, from a
cited source fetched on the date shown.** This file is the audit trail.

## Method (batch 2, 2026-09-20)

1. Each source page below was fetched in full during this session and the specific table
   row for each entry was read before the entry was written.
2. Handles/profile URLs for TikTok and Instagram were taken verbatim from the Wikipedia
   table links (the table links each row to the official profile).
3. Facebook pages: Wikipedia's table links to Wikipedia articles, not to Facebook, so each
   page slug was additionally cross-checked against search-result snippets of the Facebook
   pages themselves (noted per row). `facebook.com` is unreachable directly from the build
   environment, so these slugs are flagged for a manual click-through.
4. Reddit: `reddit.com` and its public JSON endpoints were unreachable from the build
   environment (connection refused), so member counts come from the Visual Capitalist
   ranking, which states its data comes from Reddit
   (`reddit.com/best/communities/1/`). Snapshot date: May 2025.
5. Duplicate check: all 20 new handles were programmatically checked against the 20
   existing entries (no collisions), and ids 21–40 are contiguous.

## Sources fetched this session

| Source | URL | Table date |
| --- | --- | --- |
| Wikipedia — List of most-followed TikTok accounts | https://en.wikipedia.org/wiki/List_of_most-followed_TikTok_accounts | as of 7 September 2026 |
| Wikipedia — List of most-followed Instagram accounts | https://en.wikipedia.org/wiki/List_of_most-followed_Instagram_accounts | as of June 2026 |
| Wikipedia — List of most-followed Facebook pages | https://en.wikipedia.org/wiki/List_of_most-followed_Facebook_pages | as of 28 August 2026 |
| Visual Capitalist — Ranked: Largest Communities on Reddit | https://www.visualcapitalist.com/ranked-largest-communities-on-reddit/ | May 2025 |
| Wikipedia — CZN Burak (article) | https://en.wikipedia.org/wiki/CZN_Burak | retrieved 2026-09-20; confirms chef/restaurateur identity behind entry 25's food topic |

## Batch 2 entries, verified line by line

| # | Platform | Handle | Figure | Source row read | Status |
| --- | --- | --- | --- | --- | --- |
| 21 | TikTok | @kimberly.loaiza | 83.5M followers, 4.3B likes | Wikipedia TikTok table rank 10 (Kimberly Loaiza, Mexico) | ✅ verified |
| 22 | TikTok | @bts_official_bighit | 80.8M followers, 1.8B likes | Wikipedia TikTok table rank 11 (BTS, South Korea, "Band") | ✅ verified — flagged: band official account |
| 23 | TikTok | @domelipa | 75.3M followers, 5.3B likes | Wikipedia TikTok table rank 15 (Dominik Lipa, Mexico) | ✅ verified |
| 24 | TikTok | @vilmeijuga | 73.7M followers, 2.7B likes | Wikipedia TikTok table rank 17 (Meicy Villia, Indonesia, "Social media personality and entrepreneur") | ✅ figure verified — see Q9 for topic-detail caveat |
| 25 | TikTok | @cznburak | 73.3M followers, 1.6B likes | Wikipedia TikTok table rank 18 (CZN Burak, Turkey); food topic verified via his Wikipedia article (chef/restaurateur) | ✅ verified |
| 26 | Instagram | @arianagrande | 363M | Wikipedia Instagram table (Ariana Grande, "Musician and actress", US) | ✅ verified |
| 27 | Instagram | @kimkardashian | 344M | Wikipedia Instagram table (Kim Kardashian, "Media personality", US) | ✅ verified |
| 28 | Instagram | @virat.kohli | 273M | Wikipedia Instagram table (Virat Kohli, "Cricketer", India) | ✅ verified |
| 29 | Instagram | @natgeo | 269M | Wikipedia Instagram table (National Geographic, "Magazine", US, brand †) | ✅ verified — flagged: brand |
| 30 | Instagram | @kevinhart4real | 172M | Wikipedia Instagram table (Kevin Hart, "Comedian and actor", US) | ✅ verified |
| 31 | Facebook | Netflix | 205M | Wikipedia Facebook table rank 1 ("Video on demand service", US); slug `facebook.com/netflix` confirmed by search snippet "Welcome to the Netflix global page!" | ✅ verified — flagged: brand; slug click-through recommended |
| 32 | Facebook | 5-Minute Crafts | 147M | Wikipedia Facebook table rank 5 ("Internet media", Cyprus); slug `facebook.com/5min.crafts/` confirmed by search snippet showing TheSoul Publishing / ADME (CY) LTD page info | ✅ verified — flagged: media company; slug click-through recommended |
| 33 | Facebook | Mr. Bean | 141M | Wikipedia Facebook table rank 6 ("Fictional character", UK); slug `facebook.com/MrBean/` confirmed by search snippet "Welcome to Mr Bean's official Facebook page!" | ✅ verified — flagged: character page |
| 34 | Facebook | Shakira | 126M | Wikipedia Facebook table rank 8 ("Musician", Colombia); slug `facebook.com/shakira` confirmed by search snippet "Shakira's Official Facebook Page" | ✅ verified — see quirk Q2 |
| 35 | Facebook | Will Smith | 113M | Wikipedia Facebook table rank 12 ("Actor", US); slug `facebook.com/WillSmith` and the 113M figure independently corroborated by a search snippet of the page itself | ✅ verified |
| 36 | Reddit | r/todayilearned | 41M members | Visual Capitalist table rank 5 | ✅ verified (May 2025 snapshot) |
| 37 | Reddit | r/Music | 38M members | Visual Capitalist table rank 6 | ✅ verified (May 2025 snapshot) |
| 38 | Reddit | r/movies | 36M members | Visual Capitalist table rank 8 | ✅ verified (May 2025 snapshot) |
| 39 | Reddit | r/memes | 35M members | Visual Capitalist table rank 9 | ✅ verified (May 2025 snapshot) |
| 40 | Reddit | r/science | 34M members | Visual Capitalist table rank 11 | ✅ verified (May 2025 snapshot) |

## Batch 1 backfill (entries 1–20)

No figures changed. Three fields were backfilled on batch-1 rows from the **same already-cited
tables** (re-fetched this session): `cohort`, `country`, and TikTok `likes_billions`
(khaby.lame 2.7, charlidamelio 12.3, mrbeast 1.5, tiktok 0.46, bellapoarch 2.4, addisonre 5.3,
williesalim 1.8, zachking 1.3, fifaworldcup 3.2).

## Irregularities and quirks flagged this session

- **Q1 — TikTok page internal inconsistency:** the article prose says Khaby Lame has
  "162.8 million" followers while the table row says 162.9M. Batch 1 uses the table value
  (162.9). Both numbers come from the same Wikipedia page; treated as rounding drift.
- **Q2 — Facebook table ordering quirk:** rank 8 (Shakira, 126M) is listed before rank 9
  (FC Barcelona, 128M), i.e. the published ranks are not strictly sorted. Figures are used
  as published; we do not rely on Facebook ranks.
- **Q3 — Facebook page intro vs table:** the page intro text cites Cristiano Ronaldo at
  "177 million" while the table shows 174M (28 Aug 2026). We do not use Ronaldo's Facebook
  figure at all (he appears in this project only via Instagram, per batch 1).
- **Q4 — Band account:** @bts_official_bighit is a band/label-run account (flagged in JSON).
- **Q5 — Brand/character pages:** Netflix, 5-Minute Crafts, Mr. Bean, National Geographic are
  not independent creators (flagged in JSON and highlighted in the UI).
- **Q6 — Environment network limits:** `tiktok.com`, `instagram.com`, `facebook.com`, and
  `reddit.com` (including its unauthenticated JSON endpoints) refused connections from the
  build environment, so live-profile cross-checks were impossible; verification relies on
  the cited list snapshots plus search snippets for Facebook slugs.
- **Q7 — Reddit snapshot age:** Reddit member counts are from May 2025 (Visual Capitalist),
  ~16 months old at compile time.
- **Q8 — Facebook page intro vs table (Shakira):** the page intro cites Shakira at
  "123 million" followers while the 28 Aug 2026 table row shows 126M. The table value is
  used in `master-list.json` (entry 34); the intro statement ("most-followed female
  individual") is kept only with an explicit source attribution.
- **Q9 — Entry 24 topic detail is third-party-sourced:** Wikipedia's TikTok table describes
  @vilmeijuga only as "social media personality and entrepreneur". The lifestyle/comedy/slime
  content description and the September-2020 account-creation date come from third-party
  biography pages (Wikitia, celebsline), which are low-authority. The follower figure itself
  is verified from Wikipedia; the topic detail is flagged in the JSON (`irregularity`) and
  should be confirmed by opening the profile manually. An earlier draft of this batch
  mislabeled her content as "magic"; that was caught in review and corrected — retained
  here as an example of the line-by-line check working.

## Batch 1 verification record (PR #1, 2026-09-20)

Entries 1–20 were verified line by line against the same Wikipedia TikTok/Instagram tables
and the Visual Capitalist Reddit table before PR #1 was merged. See the git history of
`data/master-list.json` and PR #1 for that audit trail.
