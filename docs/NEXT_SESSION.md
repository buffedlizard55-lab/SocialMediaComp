# Work remaining and limitations

Status after the 2026-09-21 batch-4 session: **80 entries**. Batch 4 added 20 rows
(ids 61–80) from pages fetched that day. Verification log: `docs/VERIFICATION.md`
(Q1–Q32). Structural check: `python3 scripts/validate.py`. First full-file snapshot:
`data/snapshots/2026-09-21-master-list.json`.

The site now shows growth notes, second-source links, cited clocks, official YouTube
Help tactics (page fetched this session), approximate TikTok likes-per-follower, and
per-platform cohort medians. Those views are summaries of stored snapshots. They are
not live rates.

## Do next session

1. **Confirm GitHub Pages rebuilt after this merge.** Open
   `https://buffedlizard55-lab.github.io/SocialMediaComp/` and check that it shows
   80 entries, a Batch filter that includes Batch 4, and the YouTube Help source.
   Pages is already enabled from `main` `/` (last observed status: built). A rebuild
   usually takes a minute or two after the merge.
2. **Manual click-throughs still owed.** This environment cannot open the social
   platforms. Click these and record the date if the live count differs:
   - Facebook slugs from batch 2: `facebook.com/netflix`, `/5min.crafts/`, `/MrBean/`,
     `/shakira`, `/WillSmith` (Q6).
   - Instagram pet slugs: `instagram.com/jiffpom/`, `instagram.com/nala_cat/`,
     `instagram.com/merlinthepig/` (Q13, Q16).
   - Batch 4 profile URLs on TikTok, YouTube, and Twitch. Table links were copied;
     the pages themselves were not opened.
   - X profiles from batch 3, still unopened.
3. **Do not add a row from memory of this log.** Re-fetch the page. Wikipedia lists
   are dynamic. The exclusion table in `docs/VERIFICATION.md` (batch 4) is a reading
   note, not a permission to copy a figure forward.
4. **Safe additions already read, if still wanted after a re-read:**
   - TikTok @espn, rank 22 on the 7 September 2026 table: 61 million followers,
     6.2 billion likes, brand column Yes. Not added. 6.2 billion is below both
     Barstool (10.5 billion, entry 76) and Charli D'Amelio (12.3 billion, entry 2).
   - IShowSpeed YouTube, article infobox 61.4 million subscribers, updated
     19 September 2026. If added, flag it as a cross-platform duplicate of entry 73
     and do not mark it `verified_list`.
   - Pokimane only if she appears in the 2 August 2026 Twitch table or a dated
     infobox. Do not use the September 2025 lead sentence of 9.4 million (Q25).
5. **Still blocked on a missing fact, not on time:**
   - Doug the Pug: the Wikipedia article states 3.9 million Instagram followers in a
     sentence ending "as of 2021" and does not print a profile slug. Do not guess
     `@itsdougthepug` or any other handle.
   - Huda Kattan: the article documents the April 2010 blog and the 2013 cosmetics
     line and prints no follower figure. Do not import a number from a blog.
6. **Second snapshot, then deltas.** Diff a future `data/snapshots/` file against
   `2026-09-21-master-list.json`. Until that file exists, do not rank "fastest
   growth" from follower totals. The cited clocks on the site are start dates a
   source printed. They are not rates. MrBeast's "~133,000 subscribers/day" remains
   the only per-day rate copied from a list page (batch 3).
7. **Refresh aging rows before using them in a comparison.** Reddit rows are May
   2025 (Q7, Q29). Jiffpom is 29 April 2019 and Nala Cat is 13 May 2020 (Q13).
   Merlin's record has two dates (Q16). Jeffree Star's infobox is 23 April 2026.
   NikkieTutorials' infobox is 29 March 2026.
8. **Official tactics still thin.** TikTok Creator Academy returned HTTP 403 this
   session. Instagram and Meta help pages were not re-fetched. Next session should
   fetch those official pages and add only sentences that were actually read.
   Do not write a TikTok algorithm guide from memory.
9. **Engagement beyond cumulative TikTok likes** needs official APIs (YouTube Data
   API, Meta Graph API, Reddit OAuth, X API) with stored secrets. Do not scrape.
10. **Facebook slugs.** The 28 August 2026 table still does not link to
    `facebook.com`. Batch 2's search-snippet method is the bar. Do not invent a slug.
    Q2 and Q32 (intro captions vs table) are still open.

## Limitations blocking a fully successful project

- No public unauthenticated bulk follower API for TikTok, Instagram, Facebook, X,
  Twitch, or Reddit. Every figure is a dated snapshot from a cited secondary source.
- The build environment cannot open those platforms (and TikTok Creator Academy
  returned 403). Profile pages cannot be confirmed from here.
- "Organic" cannot be proven from a public total. Brand, celebrity, character, and
  platform-owner rows are flagged. Entry 49 (@elonmusk) is documented by Wikipedia
  as partly platform-engineered (Q14). Entry 68 (Ronaldo's YouTube channel) is a
  celebrity transfer, not a from-zero case (Q24).
- Snapshot ages on this list run from 2019 (Jiffpom) through 21 September 2026.
  Medians in the UI mix those ages on purpose and are labeled as such. They are not
  a growth ranking.
- One snapshot file exists. A fastest-growth ranking needs two.
- Wikipedia list pages contradict themselves in places (Q1, Q2, Q3, Q10, Q17, Q25,
  Q32). The row value used is recorded. A reviewer should still open the link.
- The X list carries a Wikipedia "[unreliable source?]" template (Q14).
- Guinness record pages cookie-wall this environment (Q13, Q16). Those figures need
  a human click-through.
- Niche pet and makeup accounts that the project wants (Doug the Pug, Huda Kattan,
  Tucker Budzyn, Tika the Iggy) are not on the top-50 lists. They cannot be added
  until a trusted page prints both a handle and a dated count.

## Irregularities to keep visible

Do not clear flags in a cleanup pass. Q1–Q15 are batches 1–3. Q16–Q32 are batch 4
(Merlin date conflict, TikTok sort quirks, list-vs-infobox drift, Younes country,
Stokes date and monetization suspension, Mark Rober drift, KL BRO family channel
and stale infobox, infobox-only rows, Ronaldo YouTube duplicate, stale Twitch lead,
Barstool brand likes, KallMeKris job-title lag, IShowSpeed other platforms,
Reddit snapshot age, LeBron celebrity, Doug/Huda not guessed, Facebook intro vs table).
