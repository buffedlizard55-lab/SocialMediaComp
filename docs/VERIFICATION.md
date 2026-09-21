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

---

# Batch 4 (2026-09-21) — entries 61–80

## Method (batch 4, 2026-09-21)

1. Twenty new rows were planned around the project's gaps: organic or unusual growth,
   pets, gaming, makeup, and topics the top-celebrity lists do not cover. A row was
   written only after the specific table cell, infobox line, or record block was read
   from a page fetched in this session.
2. Wikipedia list tables were fetched in chunks and the row was read before the JSON
   was written. Article infoboxes were used only when the account is below the list
   floor (YouTube top 100 is stated to be above 50 million) or when the list does not
   cover the niche. Those rows are `verified_list: false` and flagged.
3. Handles and profile URLs were copied from the link on the cited page. Where a second
   page was read (a Wikipedia article, or the Guinness news post), its URL is stored as
   `article_url` and linked in the UI. It is not a substitute for `source_url`.
4. Duplicate check: `scripts/build_batch4.py` refuses a `(platform, handle)` already
   in entries 1–60, assigns ids 61–80, and re-reads the file after writing to confirm
   the locked figures. `scripts/validate.py` checks contiguity, hosts, cohorts,
   verification types, optional article URLs, and likes figures.
   Two prose corrections were applied after that write, without changing any
   metric: entry 75's country string was ordered Morocco then Germany (Q19), and
   entry 76's notes no longer call 10.5 billion likes the highest total (Q26).
   `data/snapshots/2026-09-21-master-list.json` is a copy of the corrected file,
   not a second scrape.
5. No follower number was estimated, rounded by us, or taken from a blog, Social Blade
   page, or search snippet of a non-official site. Search-indexed text was used only
   for the Guinness record page, which served a cookie wall (same method as Q13), and
   that row is flagged.
6. TikTok Creator Academy (`https://www.tiktok.com/creator-academy`) returned HTTP 403
   from the fetch tool. No new TikTok "official tactic" was written. YouTube's Help
   page on recommendations was fetched in full and is the only new official-tactics source.

## Sources fetched this session (2026-09-21)

| Source | URL | What was read |
| --- | --- | --- |
| Wikipedia — most-followed TikTok accounts | https://en.wikipedia.org/wiki/List_of_most-followed_TikTok_accounts | Top-50 table, as of 7 September 2026. Followers rounded down to the nearest 0.1 million (page note). |
| Wikipedia — most-subscribed YouTube channels | https://en.wikipedia.org/wiki/List_of_most-subscribed_YouTube_channels | Top-100 table. No rank column. Lead says MrBeast 517 million as of September 2026; a stale sentence still says 500 million as of 12 June 2026 (Q10, reconfirmed). |
| Wikipedia — most-followed Twitch channels | https://en.wikipedia.org/wiki/List_of_most-followed_Twitch_channels | Table as of 2 August 2026. Ranks 1–15 read. |
| Wikipedia — most-followed Instagram accounts | https://en.wikipedia.org/wiki/List_of_most-followed_Instagram_accounts | Lead: as of June 2026. No rank column. @kingjames row read from the table. |
| Wikipedia — most-followed Facebook pages | https://en.wikipedia.org/wiki/List_of_most-followed_Facebook_pages | Table as of 28 August 2026, ranks 1–15 read. No new Facebook row added (see Q32). |
| Visual Capitalist — largest Reddit communities | https://www.visualcapitalist.com/ranked-largest-communities-on-reddit/ | Full 15-row table, May 2025. Data attributed to Reddit. |
| Wikipedia — Stokes Twins | https://en.wikipedia.org/wiki/Stokes_Twins | Infobox updated 9 August 2026; career section. |
| Wikipedia — Alan Chikin Chow | https://en.wikipedia.org/wiki/Alan_Chikin_Chow | Infobox updated 18 September 2026; lead and career. |
| Wikipedia — Mark Rober | https://en.wikipedia.org/wiki/Mark_Rober | Infobox updated 4 September 2026; lead and career open. |
| Wikipedia — KL Bro Biju | https://en.wikipedia.org/wiki/KL_Bro_Biju | Infobox updated 10 December 2025; lead. |
| Wikipedia — jacksepticeye | https://en.wikipedia.org/wiki/Jacksepticeye | Infobox updated 8 September 2026; lead. |
| Wikipedia — Valkyrae | https://en.wikipedia.org/wiki/Valkyrae | Infobox updated 4 July 2026; lead and 2015–2020 career section. |
| Wikipedia — Jeffree Star | https://en.wikipedia.org/wiki/Jeffree_Star | Infobox updated 23 April 2026; lead. |
| Wikipedia — KallMeKris | https://en.wikipedia.org/wiki/KallMeKris | Infobox updated 1 September 2026; lead and 2020 start. |
| Wikipedia — IShowSpeed | https://en.wikipedia.org/wiki/IShowSpeed | Infobox updated 19 September 2026; lead. |
| Wikipedia — Spencer X | https://en.wikipedia.org/wiki/Spencer_X | Infobox updated 24 July 2026; lead and career. |
| Wikipedia — Younes Zarou | https://en.wikipedia.org/wiki/Younes_Zarou | Infobox updated 9 July 2026; full short article. |
| Wikipedia — Doug the Pug | https://en.wikipedia.org/wiki/Doug_the_Pug | Lead read. Not added (Q31). |
| Wikipedia — Huda Kattan | https://en.wikipedia.org/wiki/Huda_Kattan | Lead and career open. No follower figure. Not added (Q31). |
| Guinness record — most Instagram followers for a pig | https://www.guinnessworldrecords.com/world-records/465669-most-followers-for-a-pig-on-instagram | Cookie wall on direct fetch. Who/What/When/Where read from search-indexed text of this URL (Q16). |
| Guinness news — Merlin | https://www.guinnessworldrecords.com/news/2026/3/meet-merlin-the-adorable-mini-pig-who-amassed-a-following-by-talking-with-buttons | Fetched in full. Confirms @merlinthepig, 1.1 million, button communication, Mina Alali. |
| YouTube Help — recommendation system | https://support.google.com/youtube/answer/16533387?hl=en | Fetched in full. Official tactics only. Not a follower source. |

## Batch 4 entries, verified line by line

| # | Platform | Handle | Figure read | Source row | Status |
| --- | --- | --- | --- | --- | --- |
| 61 | Twitch | KaiCenat | 21.4 million, rank 1 | Twitch table: special events, various games, chatting; English; United States; link `twitch.tv/KaiCenat` | ✅ table value. Lead also says first to 20 million. Stale September 2025 sentence ignored (Q25). |
| 62 | Twitch | Ibai | 20.4 million, rank 2 | Twitch table: Ibai Llanos; special events, various games, chatting; Spanish; Spain; link `twitch.tv/ibai` | ✅ No event names added; the table does not name them. |
| 63 | Twitch | Jynxzi | 11.2 million, rank 12 | Twitch table: Nicholas Stewart; Clash Royale and Rainbow Six Siege; English; United States; link `twitch.tv/jynxzi` (no www) | ✅ No start date on the row, so none stored. |
| 64 | YouTube | Stokes Twins | 146 million | YouTube table: English, category People, joined 11 April 2008, United States and China, link `youtube.com/@stokestwins` | ✅ List value. Article infobox 144 million (9 Aug 2026) not used (Q20). |
| 65 | YouTube | Alan's Universe | 102 million | YouTube table: link `youtube.com/@AlanChikinChow`, Entertainment, joined 3 February 2020, United States | ✅ Infobox on the article also says 102 million, updated 18 September 2026. |
| 66 | YouTube | Mark Rober | 82.6 million | YouTube table: Education/Entertainment, joined 20 October 2011, United States, channel `UCY1kMZp36IQSyNx_9h4mpCg` | ✅ List value. Infobox 81.9 million (4 Sep 2026) not used (Q21). |
| 67 | YouTube | KL BRO Biju Rithvik | 88.7 million | YouTube table: Malayalam, Lifestyle Vlogs, joined 21 July 2020, India, link `youtube.com/@KLBROBijuRithvik1` | ✅ List value. Infobox 84.7 million (10 Dec 2025) not used (Q22). |
| 68 | YouTube | UR · Cristiano | 83.3 million | YouTube table: Portuguese and English, Entertainment/Sports, joined 8 July 2024, Portugal, link `youtube.com/@cristiano` | ✅ Flagged celebrity duplicate of entries 11 and 51 (Q24). No rate computed. |
| 69 | YouTube | jacksepticeye | 31.2 million | Article infobox, updated 8 September 2026; channel `youtube.com/@jacksepticeye`; views 17.73 billion on the same infobox | ✅ Not a top-100 row (Q23). Lead: uploading since December 2012, 1 million in 2014, 10 million by 2016. |
| 70 | YouTube | Valkyrae | 4.05 million subscribers | Article infobox, updated 4 July 2026; channel `youtube.com/@Valkyrae`; views 969.91 million. Same infobox: Twitch 1.6 million | ✅ YouTube figure is the row. Twitch figure is a note, not a second entry (Q23, Q25). |
| 71 | YouTube | jeffreestar | 15.6 million | Article infobox, updated 23 April 2026; channel `youtube.com/@jeffreestar`; views 2.61 billion; genres vlog, makeup, beauty | ✅ Older infobox than the other batch-4 articles (Q23). Cosmetics company founded November 2014, per the lead. |
| 72 | TikTok | @kallmekris | 50.3 million, 2.5 billion likes, rank 42 | TikTok table: Kristina Collins; Canada; description on the table is "social media personality and hairdresser" | ✅ Figure matches the article (50.3 million as of September 2026). Topic uses the article (comedy skits), not the stale table job title (Q27). Article says 40th; table rank is 42 (Q18). Account registered 9 April 2020, per the article. |
| 73 | TikTok | @ishowspeed | 54.3 million, 0.43 billion likes, rank 32 | TikTok table: United States; description social media personality, rapper, and streamer; link `tiktok.com/@ishowspeed` | ✅ List value kept so likes stay on the same row. Infobox 54.6 million (19 Sep 2026) not used (Q18). Rank sits above a 54.5 million row (Q17). |
| 74 | TikTok | @spencerx | 53.5 million, 1.3 billion likes, rank 37 | TikTok table: Spencer X; beatboxer and social media personality; United States | ✅ List value. Article: TikTok created February 2019, ten million by that fall. Infobox 53.6 million (24 July 2026) not used (Q18). |
| 75 | TikTok | @youneszarou | 57.6 million, 1.3 billion likes, rank 27 | TikTok table: social media personality; Morocco and Germany flags; link `tiktok.com/@youneszarou` | ✅ List value. Article infobox 57.4 million (9 July 2026) not used. Country caveat Q19. |
| 76 | TikTok | @barstoolsports | 49.6 million, 10.5 billion likes, rank 44 | TikTok table: brand-account column Yes; "blog website and digital media company"; United States | ✅ Second-highest likes total read (Charli D'Amelio, entry 2, is 12.3 billion). Highest derived likes-per-follower. Brand flag (Q26). |
| 77 | Instagram | @merlinthepig | 1,100,000 followers | GWR record data: Who merlinthepig; What 1,100,000; Where United States (Sacramento); When 1 December 2025 | ✅ Flagged. Prose on the same indexed record says as of 23 February 2026. News page fetched in full confirms the handle and 1.1 million (Q16). |
| 78 | Instagram | @kingjames | 154 million | Instagram table, as of June 2026: LeBron James, basketball player, United States, link `instagram.com/kingjames` | ✅ Celebrity topic-gap row, not an organic case (Q30). Table has no rank column; none stored. |
| 79 | Reddit | r/Showerthoughts | 34 million, rank 10 | Visual Capitalist table, May 2025 | ✅ Ties r/science (entry 40) on the same table. Handle spelling copied from the table. |
| 80 | Reddit | r/space | 28 million, rank 15 | Visual Capitalist table, May 2025 | ✅ Last row of that 15-row chart. |

## Read, and deliberately not added

These figures were on pages fetched this session. They are not in `master-list.json`.

| Candidate | Figure read | Why it is not a row |
| --- | --- | --- |
| TikTok @espn | Rank 22, 61 million followers, 6.2 billion likes, brand column Yes, United States | Sports-media brand. Not added. 6.2 billion likes is below both Barstool (10.5 billion, entry 76) and Charli D'Amelio (12.3 billion, entry 2). |
| TikTok @therock, @willsmith | 79.7 million / 0.68 billion likes; 77.9 million / 0.66 billion likes | Same people as entries 14 and 35. Not added, to avoid another celebrity duplicate. |
| TikTok @realmadrid, @fcbarcelona | 77.1 million / 2.3 billion likes; 72.5 million / 3.1 billion likes; both brand | Club accounts. Sports topic is already covered. |
| TikTok rank 25, Champions League | Row was split across a fetch chunk: 59.2 million, 2.7 billion likes, country cell empty in the text read | Incomplete read of the country cell. Not added. |
| Pokimane | Lead sentence: 9.4 million, "as of September 2025", citing Social Blade | Not in the 2 August 2026 table rows that were read (through rank 15). The 9.4 million sentence is stale next to Kai Cenat's table value of 21.4 million (Q25). |
| Doug the Pug | Article lead: Instagram 3.9 million, and Twitter "over 2.6 million" in a sentence ending "as of 2021" | No profile slug on the page. A handle was not guessed (Q31). |
| Huda Kattan | Article documents a WordPress blog started April 2010 and Huda Beauty founded 2013 | No follower or subscriber figure on the article. Not invented (Q31). |
| James Charles | Article infobox was visible in search and the page was not used | Not added. The article is a dispute record, not a clean growth case. No controversy details are repeated here. |
| Facebook Samsung, Facebook's own page, Real Madrid C.F. | Table: 162 million, 154 million, 135 million, as of 28 August 2026 | Brand or already-famous pages. Table links to Wikipedia articles, not `facebook.com` slugs. No slug was guessed (Q32). |

## Irregularities and quirks flagged this session (batch 4)

- **Q16 — Merlin record date conflict and cookie wall.** Direct fetch of
  `guinnessworldrecords.com/world-records/465669-most-followers-for-a-pig-on-instagram`
  returned a cookie-consent wall, same class of failure as Q13. The record data block
  was read from search-indexed text of that official URL: Who merlinthepig; What
  1,100,000 follower(s); Where United States (Sacramento); When 1 December 2025.
  The same indexed prose says the 1.1 million was "as of 23 February 2026". Both
  dates are stored. The news page
  `guinnessworldrecords.com/news/2026/3/meet-merlin-the-adorable-mini-pig-who-amassed-a-following-by-talking-with-buttons`
  was fetched in full and confirms @merlinthepig, 1.1 million followers, Mina Alali
  (USA), and button communication. `instagram.com` was not opened. Live count will differ.
- **Q17 — TikTok table is not strictly sorted.** On the 7 September 2026 table, rank 32
  (@ishowspeed, 54.3 million) is listed before rank 33 (@bayashi.tiktok, 54.5 million).
  Rank 50 (@laliga, 46.6 million) is listed after rank 49 (@nianaguerrero, 46.5 million).
  Same class of quirk as Q2. Figures used as published. Ranks are not used as a sort key
  in the app.
- **Q18 — List figure vs article infobox, where both were read.** List value is the
  metric when the row also has a likes figure, so both numbers come from one row.
  - @ishowspeed: list 54.3 million (7 September 2026) vs infobox 54.6 million (19 September 2026).
  - @spencerx: list 53.5 million (7 September 2026, rounded down to 0.1 million) vs infobox 53.6 million (24 July 2026).
  - @youneszarou: list 57.6 million vs infobox 57.4 million (9 July 2026). The article calls him 26th via a Social Blade citation retrieved 9 July 2026; the list rank read here is 27.
  - @kallmekris: both say 50.3 million, but the article says "40th overall" and the table rank is 42.
- **Q19 — Younes Zarou country.** The TikTok table shows Morocco and Germany flags.
  The biography article says he was born in Frankfurt on 26 January 1998 and, in the
  sections fetched, does not state Moroccan nationality. Country on the row follows
  the list order: Morocco, then Germany. Manual review of the table's country
  citations is recommended.
- **Q20 — Stokes Twins, three disagreements on pages that were both fetched.**
  List: 146 million, joined YouTube 11 April 2008. Article infobox (9 August 2026):
  144 million main channel, years active 2008–present. Article body: joint channel
  created 11 March 2017. List subscriber figure is used. The article also states
  YouTube suspended monetization for six months in 2021 after a prank that resulted
  in misdemeanor charges, at which time the channel had about 4.8 million followers.
  That interruption is a flag, not a reason to drop the row. TikTok 30.9 million and
  Instagram 4.9 million appear on the infobox without profile URLs, so those platforms
  were not added.
- **Q21 — Mark Rober list vs infobox.** List 82.6 million. Infobox 81.9 million,
  18.7 billion views, updated 4 September 2026. List value used. The 1.5 million views
  in one day is the article's description of the October 2011 first video, not a
  current rate.
- **Q22 — KL BRO.** List 88.7 million. Article infobox 84.7 million, updated
  10 December 2025 (stale relative to the list). List value used. The article says
  the channel is family lifestyle vlogs and that he has children; the row is flagged
  for that. The article's claim that he is the most-subscribed individual YouTuber in
  Asia was not checked against the full top-100 table and is not used.
- **Q23 — Infobox rows are not list rows.** jacksepticeye (31.2 million, 8 September
  2026), Valkyrae (4.05 million, 4 July 2026) and jeffreestar (15.6 million, 23 April
  2026) are below the YouTube list page's statement that every top-100 channel has
  passed 50 million. They are flagged `verified_list: false`. Do not rank them against
  the top-100 table as if the snapshots were the same age. Jeffree Star's infobox is
  the oldest of the three.
- **Q24 — UR · Cristiano is a third row for Cristiano Ronaldo** (entries 11 and 51).
  Included only because the YouTube table prints a join date of 8 July 2024 next to
  83.3 million subscribers. No daily rate was computed. The list page still mixes a
  June 2026 "500 million" sentence with a September 2026 "517 million" sentence (Q10).
  This row is not evidence of from-zero organic growth.
- **Q25 — Twitch lead is stale relative to its own table.** The lead says, as of
  September 2025, Kai Cenat has 20 million and Pokimane has 9.4 million. The table,
  as of 2 August 2026, says Kai Cenat has 21.4 million. Pokimane was not in the table
  rows read (ranks 1–15). She was not added. Valkyrae's 1.6 million Twitch followers
  are from her article infobox (4 July 2026), not from that table.
- **Q26 — Barstool Sports is a brand.** Brand-account column on the TikTok table is
  Yes. 10.5 billion likes is not the highest likes total on that table. Charli
  D'Amelio (entry 2) is 12.3 billion, re-read from the same table this session.
  Dividing rounded likes by rounded followers puts Barstool first among the top-50
  rows read (about 212 per follower, versus about 77 for Charli). That ratio is
  arithmetic in the UI. It is not a published rate. An earlier draft of this note
  called 10.5 billion the highest likes total. That was wrong and was corrected
  before the rows were treated as final.
- **Q27 — KallMeKris table job title is stale.** The table says "social media
  personality and hairdresser". The article says she left hairdressing in April 2020,
  registered the account on 9 April 2020, and is known for short comedy skits. Topic
  on the row follows the article. Follower and likes figures follow the table.
- **Q28 — IShowSpeed other-platform infobox figures are notes, not rows.** Updated
  19 September 2026: YouTube 61.4 million subscribers and 10.9 billion views;
  Instagram 55.3 million (`instagram.com/ishowspeed`); Twitch 6.2 million; X 4.1
  million at `@ishowspeedsui` (not `@ishowspeed`). Adding them would duplicate the
  person. The TikTok list row is the entry because it also has likes.
- **Q29 — New Reddit rows use the May 2025 Visual Capitalist snapshot.** Same age
  limit as Q7. r/Showerthoughts at 34 million ties entry 40 (r/science).
- **Q30 — @kingjames is pre-existing fame.** 154 million, basketball player, United
  States, Instagram list as of June 2026. Added for the basketball topic gap only.
- **Q31 — Reviewed and not added, rather than guessed.** Doug the Pug: the article
  states 3.9 million Instagram followers in a sentence that ends "as of 2021" and
  does not print a profile slug. Huda Kattan: blog (April 2010) and cosmetics line
  (2013) are documented; no follower figure is printed. James Charles was not used
  as a growth case.
- **Q32 — Facebook table re-read; no new Facebook row.** As of 28 August 2026 the
  table still lists Shakira at 126 million (rank 8) before FC Barcelona at 128 million
  (rank 9), which is Q2. A caption says Facebook's own page is third with 155 million;
  the table shows Samsung at rank 3 with 162 million and Facebook at rank 4 with 154
  million. The Ronaldo caption still says 177 million against the table's 174 million
  (Q3). New top pages read (Samsung 162, Real Madrid 135, Coca-Cola 107) are brands.
  The table does not link to `facebook.com`, so no slug was invented.

## Official strategy source (not a follower source)

YouTube Help, "YouTube's Recommendation System",
https://support.google.com/youtube/answer/16533387?hl=en , fetched in full on
2026-09-21. The tactics on the site are paraphrases of that page, with the link.
TikTok Creator Academy was not re-fetched (HTTP 403). Older official URLs already
in `data/strategies.json` were not re-verified this session and are unchanged.

