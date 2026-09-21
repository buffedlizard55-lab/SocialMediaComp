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

---

# Batch 3 (2026-09-21) — entries 41–60

## Method (batch 3, 2026-09-21)

1. Each source page below was fetched in full during this session and the specific table
   row (or infobox line / record-data block) for each entry was read before the entry was
   written. 20 new entries were planned, sourced, and written; ids 41–60 are contiguous.
2. Platform coverage was extended to YouTube, X and Twitch (per `docs/NEXT_SESSION.md`
   item 5), plus topic-gap entries for pets, makeup and gaming (item 3) — the top-50 list
   pages do not cover niche topics, so four niche rows use a different, flagged source
   type (Wikipedia article infobox or Guinness World Records record page).
3. Handles/profile URLs were taken from the cited pages: YouTube channel links and X
   usernames are table columns; Twitch channel links are table columns.
4. Duplicate check: all 20 new (platform, handle) pairs were checked programmatically
   against all existing entries (`scripts/build_batch3.py` asserts this; also enforced by
   `scripts/validate.py`). Same-person rows on *different* platforms are intentional
   (MrBeast entry 3 ↔ 41; Ronaldo entry 11 ↔ 51) and flagged per row — Q15.
5. A structural validator (`scripts/validate.py`) now checks id contiguity, required
   fields, URL/plausibility, cohort values, batch boundaries and verification types.

## Sources fetched this session (2026-09-21)

| Source | URL | Table/figure date |
| --- | --- | --- |
| Wikipedia — List of most-subscribed YouTube channels | https://en.wikipedia.org/wiki/List_of_most-subscribed_YouTube_channels | top-100 table; lead dates MrBeast 517M to September 2026; one stale June-2026 sentence (Q10) |
| Wikipedia — List of most-followed X accounts | https://en.wikipedia.org/wiki/List_of_most-followed_X_accounts | as of August 2026 |
| Wikipedia — List of most-followed Twitch channels | https://en.wikipedia.org/wiki/List_of_most-followed_Twitch_channels | as of 2 August 2026 |
| Wikipedia — Markiplier (article) | https://en.wikipedia.org/wiki/Markiplier | infobox last updated 15 September 2026 |
| Wikipedia — Nikkie de Jager (article; NikkieTutorials redirects here) | https://en.wikipedia.org/wiki/Nikkie_de_Jager | infobox last updated 29 March 2026 |
| Wikipedia — Ninja (gamer) (article, cross-check only) | https://en.wikipedia.org/wiki/Ninja_(gamer) | infobox last updated 6 September 2026 |
| Guinness World Records — Most followers on Instagram for a dog | https://www.guinnessworldrecords.com/world-records/450698-most-followers-for-a-dog-on-instagram | record verified 29 April 2019 (Q13) |
| Guinness World Records — Most followers on Instagram for a cat | https://www.guinnessworldrecords.com/world-records/465511-most-followers-for-a-cat-on-instagram | record verified 13 May 2020 (Q13) |
| ForumDaily (citing WSJ) — kids-channel cohort background | https://www.forumdaily.com/en/deti-iz-semej-russkoyazychnyx-immigrantov-stali-zvyozdami-youtube-i-zarabatyvayut-milliony/ | 2023 (topic detail only, Q12) |
| Time Out — Jiffpom @jiffpom Instagram embed | https://www.timeout.com/usa/news/meet-the-most-famous-dog-on-instagram-jiffpom-113017 | 2017 (slug corroboration only, Q13) |

## Batch 3 entries, verified line by line

| # | Platform | Handle | Figure | Source row read | Status |
| --- | --- | --- | --- | --- | --- |
| 41 | YouTube | MrBeast | 517M subs | YouTube table row 1 (US, Entertainment; link `youtube.com/user/MrBeast6000`); page prose: "517 million subscribers as of September 2026", "average of 133,000 subscribers per day" (June 2026) | ✅ verified — flagged: cross-platform duplicate of entry 3 |
| 42 | YouTube | T-Series | 315M subs | YouTube table row 2 (India, Music, link `youtube.com/user/tseries`) | ✅ verified — flagged: record-label channel |
| 43 | YouTube | Cocomelon - Nursery Rhymes | 202M subs | YouTube table row 3 (US, Education, channel `UCbCmjCuTUZos6Inko4u57UQ`) | ✅ verified — flagged: studio brand |
| 44 | YouTube | SET India | 190M subs | YouTube table row 4 (India, Entertainment, channel `UCpEhnqL0y41EpW2TvWAHD7Q`) | ✅ verified — flagged: TV network |
| 45 | YouTube | Vlad and Niki | 150M subs | YouTube table row 5 (Russia, Entertainment, channel `UCvlE5gTbOvjiolFlEm-c_Ow`) | ✅ figure verified — kids topic per press (Q12) |
| 46 | YouTube | Kids Diana Show | 138M subs | YouTube table row 7 (Ukraine, Entertainment, channel `UCk8GzjMOrta8yxDcKfylJYw`) | ✅ figure verified — kids topic per press (Q12) |
| 47 | YouTube | Like Nastya | 133M subs | YouTube table row 9 (Russia, Entertainment, channel `UCJplp5SjeGSdVdwsfb9Q7lQ`) | ✅ figure verified — kids topic per press (Q12) |
| 48 | YouTube | PewDiePie | 109M subs | YouTube table row 14 (Japan/Sweden, "Entertainment/Lifestyle Vlogs", link `youtube.com/PewDiePie`); page prose calls him a "Swedish gamer" and a former #1 | ✅ verified |
| 49 | X | @elonmusk | 241.6M followers | X table row 1 (link `x.com/elonmusk`); page lead: "over 241 million followers" + platform-code statement (Q14) | ✅ verified — flagged: platform owner; not organic |
| 50 | X | @BarackObama | 118.9M | X table row 2 (`x.com/BarackObama`) | ✅ verified |
| 51 | X | @Cristiano | 114.3M | X table row 3 (`x.com/Cristiano`) | ✅ verified — flagged: cross-platform duplicate of entry 11 |
| 52 | X | @realDonaldTrump | 111.8M | X table row 4 (`x.com/realDonaldTrump`) | ✅ verified |
| 53 | X | @narendramodi | 107.1M | X table row 5 (`x.com/narendramodi`) | ✅ verified |
| 54 | X | @rihanna | 98.6M | X table row 6 (`x.com/rihanna`); page caption: "Barbadian singer Rihanna is the sixth most-followed person on X" | ✅ verified |
| 55 | X | @NASA | 92.3M | X table row 7 (`x.com/NASA`, brand-account column "Yes") | ✅ verified — flagged: government agency |
| 56 | Instagram | @jiffpom | 9,018,251 (9.02M) | GWR record data: "Who: Jiffpom / What: 9,018,251 follower(s) / When: 29 April 2019" | ✅ verified — see Q13 (search-indexed read; 2019 snapshot) |
| 57 | Instagram | @nala_cat | 4,361,519 (4.36M) | GWR record data: "Who: nala_cat / What: 4,361,519 follower(s) / When: 13 May 2020" | ✅ verified — see Q13 |
| 58 | YouTube | NikkieTutorials | 15M subs | Wikipedia article infobox (channel `youtube.com/@NikkieTutorials`, "Subscribers: 15 million", last updated 29 March 2026); makeup/beauty per article | ✅ verified — infobox source, flagged |
| 59 | YouTube | Markiplier | 38.9M subs | Wikipedia article infobox (channel `UC7_YxT-KID8kRbqZo7MyscQ`, "Subscribers: 38.9 million", last updated 15 September 2026); gaming (Let's Play) per article | ✅ verified — infobox source; 38.9 vs 38.8 drift (Q11) |
| 60 | Twitch | Ninja | 19.3M followers | Twitch table row 3 (`twitch.tv/ninja`, owner Tyler Blevins, US, as of 2 Aug 2026); cross-checked against his article infobox (19.3M, 6 Sep 2026) | ✅ verified |

## Irregularities and quirks flagged this session (batch 3)

- **Q10 — YouTube list page has a stale sentence:** the prose says "As of June 12, 2026,
  … MrBeast, having 500 million subscribers", while the page lead says "517 million … as
  of September 2026" and the table row shows 517. The table value (517) is used.
- **Q11 — Markiplier infobox vs body:** infobox says 38.9M subscribers (last updated
  15 September 2026); the body says "over 38.8 million … as of August 7th, 2026".
  Rounding drift; the newer infobox value is used.
- **Q12 — Kids-channel topic detail is third-party-sourced:** the YouTube table lists
  Vlad and Niki, Kids Diana Show and Like Nastya only by name/category ("Entertainment").
  Their classification as the three most-popular live-action kids' channels comes from
  press coverage (WSJ via ForumDaily, 2023; Daily Mail, 2022). Follower figures are from
  the Wikipedia table; the topic detail is flagged per row.
- **Q13 — Guinness pages and Instagram slugs:** the official GWR record pages were
  fetched but served a cookie-consent wall to the build environment, so the record data
  blocks ("What / When" fields) were read from search-indexed text of those same official
  pages. The record snapshots are dated (Jiffpom 29 April 2019; Nala Cat 13 May 2020) and
  live counts will differ. instagram.com is unreachable from the build environment;
  `@jiffpom` was corroborated via a Time Out page embedding an actual @jiffpom post,
  `@nala_cat` via GWR's own "Who: nala_cat" record field. Manual click-through of both
  profile slugs is recommended.
- **Q14 — X list caveats:** Wikipedia's X table carries an "[unreliable source?]" template
  on its sourcing note ("each total rounded down to the nearest hundred thousand"), and
  the page lead states Musk "partially acquired these followers through changing the code
  of the platform to promote his own posts more favorably". Figures are used as published;
  entry 49 is flagged as not evidence of organic growth.
- **Q15 — Cross-platform duplicates are intentional:** entries 41 (MrBeast/YouTube) and
  51 (Ronaldo/X) duplicate persons already present on other platforms (3, 11). The
  duplicate check keys on (platform, handle), and each duplicate row is flagged in the
  JSON and the UI.
- **X rows have no country column in the source table.** Country values were set only
  where the fetched page itself states them (descriptions: US presidents, Indian PM;
  caption: "Barbadian singer" Rihanna), or from the same person's existing row (Ronaldo,
  per entry 11). @elonmusk's country is left empty rather than guessed.

