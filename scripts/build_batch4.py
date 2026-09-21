#!/usr/bin/env python3
"""One-off builder for batch 4 (entries 61-80) of the master list.

Every figure below was read on 2026-09-21 from the cited page (Wikipedia list
table, Wikipedia article infobox, Visual Capitalist ranking table, or a
Guinness World Records record page). See docs/VERIFICATION.md, batch 4.

Run from repo root: python3 scripts/build_batch4.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "data" / "master-list.json"
STRAT = ROOT / "data" / "strategies.json"
SNAP = ROOT / "data" / "snapshots" / "2026-09-21-master-list.json"

WIKI_TT = "https://en.wikipedia.org/wiki/List_of_most-followed_TikTok_accounts"
WIKI_YT = "https://en.wikipedia.org/wiki/List_of_most-subscribed_YouTube_channels"
WIKI_TW = "https://en.wikipedia.org/wiki/List_of_most-followed_Twitch_channels"
WIKI_IG = "https://en.wikipedia.org/wiki/List_of_most-followed_Instagram_accounts"
VC = "https://www.visualcapitalist.com/ranked-largest-communities-on-reddit/"
GWR_PIG = "https://www.guinnessworldrecords.com/world-records/465669-most-followers-for-a-pig-on-instagram"
GWR_NEWS = "https://www.guinnessworldrecords.com/news/2026/3/meet-merlin-the-adorable-mini-pig-who-amassed-a-following-by-talking-with-buttons"
YT_HELP = "https://support.google.com/youtube/answer/16533387?hl=en"

TT_NOTE = "Wikipedia TikTok list, table as of 7 September 2026 (followers rounded down to the nearest 0.1 million)"
YT_NOTE = "Wikipedia most-subscribed YouTube list, top-100 table read 21 September 2026 (table has no rank column; page as-of dates are mixed — see Q10)"
TW_NOTE = "Wikipedia most-followed Twitch channels list, as of 2 August 2026"
IG_NOTE = "Wikipedia most-followed Instagram accounts list, as of June 2026"
VC_NOTE = "Visual Capitalist ranking of largest Reddit communities, May 2025 (data from Reddit)"

BATCH4 = [
    {
        "platform": "Twitch",
        "handle": "KaiCenat",
        "owner": "Kai Cenat",
        "topic": "Gaming / special-event livestreams",
        "cohort": "creator",
        "country": "United States",
        "metric_label": "Followers (millions)",
        "metric_value": 21.4,
        "snapshot_note": TW_NOTE + " (rank 1)",
        "profile_url": "https://www.twitch.tv/KaiCenat",
        "source_name": "Wikipedia: List of most-followed Twitch channels",
        "source_url": WIKI_TW,
        "growth_notes": "Rank 1 on the Twitch table: 21.4 million followers. Streamed categories on that row: special events, various games, chatting. English. The page lead says he is the most-followed channel and the first to reach 20 million followers. A separate lead sentence dated September 2025 still says 20 million; the table value is used (Q25).",
        "verified_list": True,
        "verification_type": "list_table",
        "added_batch": 4,
        "irregularity": "Page lead still contains a September 2025 sentence (Kai Cenat '20 million'; Pokimane '9.4 million') that disagrees with the 2 August 2026 table. Table value used. See Q25.",
    },
    {
        "platform": "Twitch",
        "handle": "Ibai",
        "owner": "Ibai Llanos",
        "topic": "Gaming / special-event livestreams (Spanish)",
        "cohort": "creator",
        "country": "Spain",
        "metric_label": "Followers (millions)",
        "metric_value": 20.4,
        "snapshot_note": TW_NOTE + " (rank 2)",
        "profile_url": "https://www.twitch.tv/ibai",
        "source_name": "Wikipedia: List of most-followed Twitch channels",
        "source_url": WIKI_TW,
        "growth_notes": "Rank 2: 20.4 million followers. Same category pattern as rank 1 (special events, various games, chatting) but Spanish-language, Spain. Shows event-style streaming is not an English-only path. No extra claims about specific events were added; the table does not name them.",
        "verified_list": True,
        "verification_type": "list_table",
        "added_batch": 4,
    },
    {
        "platform": "Twitch",
        "handle": "Jynxzi",
        "owner": "Nicholas Stewart (Jynxzi)",
        "topic": "Gaming (Clash Royale, Rainbow Six Siege)",
        "cohort": "creator",
        "country": "United States",
        "metric_label": "Followers (millions)",
        "metric_value": 11.2,
        "snapshot_note": TW_NOTE + " (rank 12)",
        "profile_url": "https://twitch.tv/jynxzi",
        "source_name": "Wikipedia: List of most-followed Twitch channels",
        "source_url": WIKI_TW,
        "growth_notes": "Rank 12: 11.2 million. Unlike the top rows, the table lists only two games (Clash Royale and Rainbow Six Siege), not 'various games, chatting'. Specialist focus can still land in the top 15. Profile URL is the table link (no www). No start date was on the row, so none is stated.",
        "verified_list": True,
        "verification_type": "list_table",
        "added_batch": 4,
        "irregularity": "Table link is https://twitch.tv/jynxzi (no www). Channel page was not opened from this environment (Q6).",
    },
    {
        "platform": "YouTube",
        "handle": "Stokes Twins",
        "owner": "Alan Chen Stokes and Alex Chen Stokes",
        "topic": "Comedy / YouTube Shorts",
        "cohort": "creator",
        "country": "United States / China",
        "metric_label": "Subscribers (millions)",
        "metric_value": 146,
        "snapshot_note": YT_NOTE,
        "profile_url": "https://www.youtube.com/@stokestwins",
        "source_name": "Wikipedia: List of most-subscribed YouTube channels",
        "source_url": WIKI_YT,
        "article_name": "Wikipedia: Stokes Twins (article)",
        "article_url": "https://en.wikipedia.org/wiki/Stokes_Twins",
        "growth_notes": "List row: 146 million, category People, English, joined YouTube 11 April 2008, United States and China. Article (read 21 Sep 2026): joint channel created 11 March 2017; passed 100 million subscribers in November 2024 after multi-language dubbing (eight languages) and a greater Shorts focus, with average daily views rising from about 3–5 million to about 50 million. Infobox on that article: 144 million main-channel subscribers, updated 9 August 2026. List value used.",
        "verified_list": True,
        "verification_type": "list_table",
        "added_batch": 4,
        "irregularity": "List 146M vs article infobox 144M (9 Aug 2026). List join date 11 Apr 2008 vs article joint-channel date 11 Mar 2017 (infobox years active 2008–present). Article also states a six-month monetization suspension in 2021 after a prank that resulted in misdemeanor charges. See Q20.",
    },
    {
        "platform": "YouTube",
        "handle": "Alan's Universe",
        "owner": "Alan Chikin Chow",
        "topic": "Comedy / YouTube Shorts (scripted series)",
        "cohort": "creator",
        "country": "United States",
        "metric_label": "Subscribers (millions)",
        "metric_value": 102,
        "snapshot_note": YT_NOTE + "; article infobox matches 102 million, updated 18 September 2026",
        "profile_url": "https://www.youtube.com/@AlanChikinChow",
        "source_name": "Wikipedia: List of most-subscribed YouTube channels",
        "source_url": WIKI_YT,
        "article_name": "Wikipedia: Alan Chikin Chow (article)",
        "article_url": "https://en.wikipedia.org/wiki/Alan_Chikin_Chow",
        "growth_notes": "List name is Alan's Universe; link is @AlanChikinChow; 102 million; category Entertainment; joined 3 February 2020; United States. Article infobox (updated 18 September 2026) also says 102 million subscribers and 64.1 billion views, genre Comedy, and calls him the highest-ranking YouTube Shorts creator. Article describes Alan's Universe as a high-school drama series with over 1 billion views. No daily rate was computed; the list's as-of date is mixed (Q10).",
        "verified_list": True,
        "verification_type": "list_table",
        "added_batch": 4,
    },
    {
        "platform": "YouTube",
        "handle": "Mark Rober",
        "owner": "Mark Rober",
        "topic": "Science / DIY education",
        "cohort": "creator",
        "country": "United States",
        "metric_label": "Subscribers (millions)",
        "metric_value": 82.6,
        "snapshot_note": YT_NOTE,
        "profile_url": "https://www.youtube.com/channel/UCY1kMZp36IQSyNx_9h4mpCg",
        "source_name": "Wikipedia: List of most-subscribed YouTube channels",
        "source_url": WIKI_YT,
        "article_name": "Wikipedia: Mark Rober (article)",
        "article_url": "https://en.wikipedia.org/wiki/Mark_Rober",
        "growth_notes": "List row: 82.6 million, category Education/Entertainment, English, joined 20 October 2011, United States, channel UCY1kMZp36IQSyNx_9h4mpCg. Article: former NASA engineer (nine years, seven on the Curiosity rover); popular-science and DIY videos. First video, October 2011, received 1.5 million views in one day (article). Infobox: 81.9 million subscribers and 18.7 billion views, updated 4 September 2026. List subscriber figure used.",
        "verified_list": True,
        "verification_type": "list_table",
        "added_batch": 4,
        "irregularity": "List 82.6M vs article infobox 81.9M (4 Sep 2026). List value used. See Q21.",
    },
    {
        "platform": "YouTube",
        "handle": "KL BRO Biju Rithvik",
        "owner": "Biju (KL Bro Biju)",
        "topic": "Family lifestyle vlogs (Malayalam, Shorts)",
        "cohort": "creator",
        "country": "India",
        "metric_label": "Subscribers (millions)",
        "metric_value": 88.7,
        "snapshot_note": YT_NOTE,
        "profile_url": "https://www.youtube.com/@KLBROBijuRithvik1",
        "source_name": "Wikipedia: List of most-subscribed YouTube channels",
        "source_url": WIKI_YT,
        "article_name": "Wikipedia: KL Bro Biju (article)",
        "article_url": "https://en.wikipedia.org/wiki/KL_Bro_Biju",
        "growth_notes": "List row: 88.7 million, Malayalam, category Lifestyle Vlogs, joined 21 July 2020, India. Article: family lifestyle vlogs and shorts; channel years active 2020–present. Subscriber figure is the list value, not the article infobox (84.7 million, updated 10 December 2025). The article's 'most subscribed individual YouTuber in Asia' sentence was not checked against the full top-100 table and is not used.",
        "verified_list": True,
        "verification_type": "list_table",
        "added_batch": 4,
        "irregularity": "Family vlog; article says he has children. List 88.7M vs stale infobox 84.7M (10 Dec 2025). Asia-#1 claim on the article was not independently verified and is not used. See Q22.",
    },
    {
        "platform": "YouTube",
        "handle": "UR · Cristiano",
        "owner": "Cristiano Ronaldo",
        "topic": "Sports / entertainment (celebrity channel)",
        "cohort": "celebrity",
        "country": "Portugal",
        "metric_label": "Subscribers (millions)",
        "metric_value": 83.3,
        "snapshot_note": YT_NOTE + "; joined YouTube 8 July 2024 (date is a table column, not a computed rate)",
        "profile_url": "https://www.youtube.com/@cristiano",
        "source_name": "Wikipedia: List of most-subscribed YouTube channels",
        "source_url": WIKI_YT,
        "growth_notes": "List row: 83.3 million, languages Portuguese and English, category Entertainment/Sports, joined 8 July 2024, Portugal, link youtube.com/@cristiano. Same person as entries 11 (Instagram) and 51 (X). The join date is cited so the clock is visible. No daily rate was computed, because the list page's as-of date is mixed (Q10). This is pre-existing fame moving to a new channel, not from-zero organic growth.",
        "verified_list": True,
        "verification_type": "list_table",
        "added_batch": 4,
        "irregularity": "Cross-platform duplicate of entries 11 and 51. Celebrity transfer. Not evidence of organic from-zero growth. See Q24.",
    },
    {
        "platform": "YouTube",
        "handle": "jacksepticeye",
        "owner": "Seán William McLoughlin (jacksepticeye)",
        "topic": "Gaming (Let's Play)",
        "cohort": "creator",
        "country": "Ireland",
        "metric_label": "Subscribers (millions)",
        "metric_value": 31.2,
        "snapshot_note": "Wikipedia article infobox: 31.2 million subscribers, last updated 8 September 2026",
        "profile_url": "https://www.youtube.com/@jacksepticeye",
        "source_name": "Wikipedia: jacksepticeye (article)",
        "source_url": "https://en.wikipedia.org/wiki/Jacksepticeye",
        "growth_notes": "Infobox: 31.2 million subscribers, 17.73 billion views, genres Let's Play / comedy / vlogs, channel youtube.com/@jacksepticeye, updated 8 September 2026. Article lead: started uploading December 2012, reached 1 million subscribers in 2014 and 10 million by 2016. Below the YouTube list page's stated 50-million floor for the top 100, so this is an infobox row, not a list-table row.",
        "verified_list": False,
        "verification_type": "wiki_article_infobox",
        "added_batch": 4,
        "irregularity": "Figure is from the article infobox, not the most-subscribed list. Infobox updated 8 September 2026. See Q23.",
    },
    {
        "platform": "YouTube",
        "handle": "Valkyrae",
        "owner": "Rachell Marie Hofstetter (Valkyrae)",
        "topic": "Gaming (livestreams / vlogs)",
        "cohort": "creator",
        "country": "United States",
        "metric_label": "Subscribers (millions)",
        "metric_value": 4.05,
        "snapshot_note": "Wikipedia article infobox: 4.05 million YouTube subscribers, last updated 4 July 2026",
        "profile_url": "https://www.youtube.com/@Valkyrae",
        "source_name": "Wikipedia: Valkyrae (article)",
        "source_url": "https://en.wikipedia.org/wiki/Valkyrae",
        "growth_notes": "Same infobox (updated 4 July 2026): YouTube 4.05 million subscribers and 969.91 million views; Twitch channel Valkyrae 1.6 million followers. Article: Fortnite breakthrough in 2018; left Twitch on 13 January 2020 for an exclusive YouTube streaming contract; Twitch years active listed as 2015–2020 and 2025–present. YouTube is the row because it is the larger figure on that infobox. She was not in the Twitch top-50 table rows read this session.",
        "verified_list": False,
        "verification_type": "wiki_article_infobox",
        "added_batch": 4,
        "irregularity": "Infobox row, not a ranked-list row. Twitch follower count on the same infobox is 1.6 million and is not a separate entry. Updated 4 July 2026. See Q23 and Q25.",
    },
    {
        "platform": "YouTube",
        "handle": "jeffreestar",
        "owner": "Jeffree Star",
        "topic": "Makeup / beauty",
        "cohort": "creator",
        "country": "United States",
        "metric_label": "Subscribers (millions)",
        "metric_value": 15.6,
        "snapshot_note": "Wikipedia article infobox: 15.6 million subscribers, last updated 23 April 2026",
        "profile_url": "https://www.youtube.com/@jeffreestar",
        "source_name": "Wikipedia: Jeffree Star (article)",
        "source_url": "https://en.wikipedia.org/wiki/Jeffree_Star",
        "growth_notes": "Infobox: 15.6 million subscribers, 2.61 billion views, genres vlog / makeup / beauty, channel youtube.com/@jeffreestar, updated 23 April 2026. Article: founded Jeffree Star Cosmetics in November 2014. Makeup row is a creator-owned cosmetics channel, not only tutorials. Older infobox than the other batch-4 article rows.",
        "verified_list": False,
        "verification_type": "wiki_article_infobox",
        "added_batch": 4,
        "irregularity": "Infobox last updated 23 April 2026 — older than other batch-4 snapshots. Not a ranked-list row. Also owns a cosmetics company. See Q23.",
    },
    {
        "platform": "TikTok",
        "handle": "@kallmekris",
        "owner": "Kristina Lee Halliwell Collins (KallMeKris)",
        "topic": "Short comedy sketches",
        "cohort": "creator",
        "country": "Canada",
        "metric_label": "Followers (millions, rounded down to nearest 0.1M)",
        "metric_value": 50.3,
        "likes_billions": 2.5,
        "snapshot_note": TT_NOTE + " (rank 42)",
        "profile_url": "https://www.tiktok.com/@kallmekris",
        "source_name": "Wikipedia: List of most-followed TikTok accounts",
        "source_url": WIKI_TT,
        "article_name": "Wikipedia: KallMeKris (article)",
        "article_url": "https://en.wikipedia.org/wiki/KallMeKris",
        "growth_notes": "List rank 42: 50.3 million followers, 2.5 billion likes. Article: account registered 9 April 2020, first video the same day; short skits (about 30 seconds to a minute); left hairdressing in April 2020. Article and list agree on 50.3 million as of September 2026. Article text says '40th overall'; the list table rank read this session is 42. YouTube infobox on the same article: 13.1 million subscribers and 3.7 billion views, updated 1 September 2026 (not a separate row).",
        "verified_list": True,
        "verification_type": "list_table",
        "added_batch": 4,
        "irregularity": "List description still says 'hairdresser'; article says she left that job in April 2020 and is known for comedy skits. Article says 40th; table rank is 42. See Q18 and Q27.",
    },
    {
        "platform": "TikTok",
        "handle": "@ishowspeed",
        "owner": "Darren Jason Watkins Jr. (IShowSpeed)",
        "topic": "Gaming / IRL streaming",
        "cohort": "creator",
        "country": "United States",
        "metric_label": "Followers (millions, rounded down to nearest 0.1M)",
        "metric_value": 54.3,
        "likes_billions": 0.43,
        "snapshot_note": TT_NOTE + " (rank 32)",
        "profile_url": "https://www.tiktok.com/@ishowspeed",
        "source_name": "Wikipedia: List of most-followed TikTok accounts",
        "source_url": WIKI_TT,
        "article_name": "Wikipedia: IShowSpeed (article)",
        "article_url": "https://en.wikipedia.org/wiki/IShowSpeed",
        "growth_notes": "List rank 32: 54.3 million followers, 0.43 billion likes; description 'social media personality, rapper, and streamer'; United States. Article (infobox updated 19 September 2026) gives a later TikTok figure of 54.6 million and, on other platforms, YouTube 61.4 million subscribers / 10.9 billion views, Instagram 55.3 million, Twitch 6.2 million, X 4.1 million (@ishowspeedsui). Those are not separate rows. Article: YouTube channel registered 2016; attention grew in 2021; shift toward soccer and entertainment in 2022; world-tour livestreams in 2024. List value used so the likes figure stays on the same row.",
        "verified_list": True,
        "verification_type": "list_table",
        "added_batch": 4,
        "irregularity": "Table order quirk: rank 32 is 54.3M and the next row (rank 33, Bayashi) is 54.5M. Infobox TikTok figure is 54.6M (19 Sep 2026) vs list 54.3M (7 Sep 2026). Other-platform infobox figures are notes only. See Q17 and Q18.",
    },
    {
        "platform": "TikTok",
        "handle": "@spencerx",
        "owner": "Spencer Polanco Knight (Spencer X)",
        "topic": "Beatboxing",
        "cohort": "creator",
        "country": "United States",
        "metric_label": "Followers (millions, rounded down to nearest 0.1M)",
        "metric_value": 53.5,
        "likes_billions": 1.3,
        "snapshot_note": TT_NOTE + " (rank 37)",
        "profile_url": "https://www.tiktok.com/@spencerx",
        "source_name": "Wikipedia: List of most-followed TikTok accounts",
        "source_url": WIKI_TT,
        "article_name": "Wikipedia: Spencer X (article)",
        "article_url": "https://en.wikipedia.org/wiki/Spencer_X",
        "growth_notes": "List rank 37: 53.5 million followers, 1.3 billion likes; description beatboxer and social media personality. Article: created the TikTok account in February 2019 and had ten million followers by that fall; previously a street performer. Infobox (updated 24 July 2026): TikTok 53.6 million, Instagram 1 million at instagram.com/iamspencerx, YouTube 2.61 million subscribers and 170 million views. List value used. Skill-audio format, not a dance trend.",
        "verified_list": True,
        "verification_type": "list_table",
        "added_batch": 4,
        "irregularity": "List 53.5M (7 Sep 2026, rounded down to 0.1M) vs infobox 53.6M (24 July 2026). See Q18.",
    },
    {
        "platform": "TikTok",
        "handle": "@youneszarou",
        "owner": "Younes Zarou",
        "topic": "Short-form video / livestreams",
        "cohort": "creator",
        "country": "Morocco / Germany",
        "metric_label": "Followers (millions, rounded down to nearest 0.1M)",
        "metric_value": 57.6,
        "likes_billions": 1.3,
        "snapshot_note": TT_NOTE + " (rank 27)",
        "profile_url": "https://www.tiktok.com/@youneszarou",
        "source_name": "Wikipedia: List of most-followed TikTok accounts",
        "source_url": WIKI_TT,
        "article_name": "Wikipedia: Younes Zarou (article)",
        "article_url": "https://en.wikipedia.org/wiki/Younes_Zarou",
        "growth_notes": "List rank 27: 57.6 million followers, 1.3 billion likes; description 'social media personality'; country flags on the row are Morocco and Germany. Article: born 26 January 1998 in Frankfurt; TikTok account created 2019, first video 22 August 2019; 2020 livestreams drew over 20,000–30,000 viewers and then over 240,000. Infobox (updated 9 July 2026): TikTok 57.4 million; YouTube 27.5 million subscribers and 23 billion views (channel created 6 May 2021). List value used. The article does not describe a more specific video format than short videos and livestreams, so none is inferred.",
        "verified_list": True,
        "verification_type": "list_table",
        "added_batch": 4,
        "irregularity": "Country field follows the list (Morocco and Germany). The biography article states birth in Frankfurt and, in the sections read, does not state Moroccan nationality. Infobox 57.4M (9 July 2026) vs list 57.6M. Article calls him 26th via a Social Blade citation; list rank read here is 27. See Q18 and Q19.",
    },
    {
        "platform": "TikTok",
        "handle": "@barstoolsports",
        "owner": "Barstool Sports",
        "topic": "Sports media",
        "cohort": "brand",
        "country": "United States",
        "metric_label": "Followers (millions, rounded down to nearest 0.1M)",
        "metric_value": 49.6,
        "likes_billions": 10.5,
        "snapshot_note": TT_NOTE + " (rank 44; brand-account column Yes)",
        "profile_url": "https://www.tiktok.com/@barstoolsports",
        "source_name": "Wikipedia: List of most-followed TikTok accounts",
        "source_url": WIKI_TT,
        "growth_notes": "List rank 44: 49.6 million followers and 10.5 billion likes. Description: blog website and digital media company. Brand-account column is Yes. Charli D'Amelio (entry 2) has the higher likes total on the same table (12.3 billion). Barstool's derived likes-per-follower is higher than the other top-50 rows read this session, including Charli. That ratio is arithmetic on rounded inputs, not a published metric.",
        "verified_list": True,
        "verification_type": "list_table",
        "added_batch": 4,
        "irregularity": "Media-company brand account, not an independent creator. Not the highest likes total (entry 2, Charli D'Amelio, 12.3 billion). Highest derived likes-per-follower among top-50 rows read this session. See Q26.",
    },
    {
        "platform": "Instagram",
        "handle": "@merlinthepig",
        "owner": "Merlin the pig (owner Mina Alali)",
        "topic": "Pets (pig)",
        "cohort": "creator",
        "country": "United States",
        "metric_label": "Followers (millions, exact record count)",
        "metric_value": 1.1,
        "snapshot_note": "Guinness World Records: 1,100,000 Instagram followers. Record 'When' field 1 December 2025; record prose says as of 23 February 2026. See Q16.",
        "profile_url": "https://www.instagram.com/merlinthepig/",
        "source_name": "Guinness World Records: Most followers on Instagram for a pig",
        "source_url": GWR_PIG,
        "article_name": "Guinness World Records news: Meet Merlin (fetched in full)",
        "article_url": GWR_NEWS,
        "growth_notes": "Record data block: Who merlinthepig; What 1,100,000 followers; Where United States (Sacramento); When 1 December 2025. Record prose also says 'as of 23 February 2026'. Official news page, fetched in full, confirms @merlinthepig, 1.1 million followers, and describes a potbellied pig in the US trained to press recorded-speech buttons. Unique pet behavior, far below Instagram top-50 scale. instagram.com was not opened from this environment.",
        "verified_list": False,
        "verification_type": "guinness_record",
        "added_batch": 4,
        "irregularity": "Record page served a cookie wall; Who/What/When read from search-indexed text of that official URL (same method as Q13). Date conflict: When = 1 December 2025 vs prose 'as of 23 February 2026'. News page corroborates the handle and 1.1 million. Live count will differ. See Q16.",
    },
    {
        "platform": "Instagram",
        "handle": "@kingjames",
        "owner": "LeBron James",
        "topic": "Sports (basketball)",
        "cohort": "celebrity",
        "country": "United States",
        "metric_label": "Followers (millions)",
        "metric_value": 154,
        "snapshot_note": IG_NOTE,
        "profile_url": "https://www.instagram.com/kingjames",
        "source_name": "Wikipedia: List of most-followed Instagram accounts",
        "source_url": WIKI_IG,
        "growth_notes": "Table row read 21 September 2026: @kingjames, LeBron James, 154 million, description Basketball player, United States. The list has no rank column. Included because basketball was missing from the Instagram rows. Pre-existing NBA fame; not an organic-from-zero case.",
        "verified_list": True,
        "verification_type": "list_table",
        "added_batch": 4,
        "irregularity": "Celebrity account. Topic-gap row, not an organic-growth case study. See Q30.",
    },
    {
        "platform": "Reddit",
        "handle": "r/Showerthoughts",
        "owner": "r/Showerthoughts",
        "topic": "One-line observations / curiosity",
        "cohort": "community",
        "country": None,
        "metric_label": "Members (millions)",
        "metric_value": 34,
        "snapshot_note": VC_NOTE + " (rank 10)",
        "profile_url": "https://www.reddit.com/r/Showerthoughts/",
        "source_name": "Visual Capitalist: Ranked largest communities on Reddit",
        "source_url": VC,
        "growth_notes": "Rank 10: 34 million members, May 2025. Ties r/science (rank 11, also 34 million, already entry 40) on the same table. Format is one-line observations, a different engagement shape from long discussion threads. Same snapshot age as the other Reddit rows (Q7).",
        "verified_list": True,
        "verification_type": "list_table",
        "added_batch": 4,
        "irregularity": "May 2025 snapshot, same age limit as entries 17–20 and 36–40 (Q7 / Q29). reddit.com was not opened from this environment.",
    },
    {
        "platform": "Reddit",
        "handle": "r/space",
        "owner": "r/space",
        "topic": "Space / science community",
        "cohort": "community",
        "country": None,
        "metric_label": "Members (millions)",
        "metric_value": 28,
        "snapshot_note": VC_NOTE + " (rank 15)",
        "profile_url": "https://www.reddit.com/r/space/",
        "source_name": "Visual Capitalist: Ranked largest communities on Reddit",
        "source_url": VC,
        "growth_notes": "Rank 15 of the 15 communities on the May 2025 Visual Capitalist chart: 28 million members. Fills the space-community gap next to the existing NASA row on X (entry 55). Not a creator account. Same snapshot age as the other Reddit rows.",
        "verified_list": True,
        "verification_type": "list_table",
        "added_batch": 4,
        "irregularity": "May 2025 snapshot (Q7 / Q29). reddit.com was not opened from this environment.",
    },
]

# Expected figures, used as a post-write lock so a typo cannot ship.
EXPECTED = {
    61: ("Twitch", "KaiCenat", 21.4),
    62: ("Twitch", "Ibai", 20.4),
    63: ("Twitch", "Jynxzi", 11.2),
    64: ("YouTube", "Stokes Twins", 146),
    65: ("YouTube", "Alan's Universe", 102),
    66: ("YouTube", "Mark Rober", 82.6),
    67: ("YouTube", "KL BRO Biju Rithvik", 88.7),
    68: ("YouTube", "UR · Cristiano", 83.3),
    69: ("YouTube", "jacksepticeye", 31.2),
    70: ("YouTube", "Valkyrae", 4.05),
    71: ("YouTube", "jeffreestar", 15.6),
    72: ("TikTok", "@kallmekris", 50.3),
    73: ("TikTok", "@ishowspeed", 54.3),
    74: ("TikTok", "@spencerx", 53.5),
    75: ("TikTok", "@youneszarou", 57.6),
    76: ("TikTok", "@barstoolsports", 49.6),
    77: ("Instagram", "@merlinthepig", 1.1),
    78: ("Instagram", "@kingjames", 154),
    79: ("Reddit", "r/Showerthoughts", 34),
    80: ("Reddit", "r/space", 28),
}

STRATEGY_ADDS = {
    "official_resources": [
        {
            "name": "YouTube Help — YouTube's Recommendation System",
            "url": YT_HELP,
            "why": "Official YouTube Help page, fetched 21 September 2026. Two stated goals: help each viewer find videos they want to watch, and maximize long-term satisfaction. Creator guidance on that page: recognizable titles and thumbnails, know the audience, publish time is not known to affect long-term viewership (except Premieres and live), use series/playlists/end screens, quality over upload volume, and judge each video on its own performance.",
        }
    ],
    "official_tactics": [
        {
            "source_name": "YouTube Help — YouTube's Recommendation System",
            "source_url": YT_HELP,
            "fetched": "2026-09-21",
            "points": [
                "The page says recommendations are driven by what viewers watch and enjoy, not by a separate thing creators should try to game.",
                "Two goals are stated: help each viewer find videos they want to watch, and maximize long-term viewer satisfaction.",
                "Signals named on the page include watch history, how much of a video is watched, ignores and 'not interested', search, subscriptions, likes, shares, comments, survey responses, and language.",
                "A consistent title and thumbnail style is described as making videos easier to choose.",
                "Publish time is not known to affect long-term viewership. The page says publishing when the audience is active may bring more immediate views, but no evidence was observed for a long-term effect. Premieres and live streams are the exception: use the audience's active times.",
                "Series, clear next-video prompts, playlists, and end screens are listed as ways to help continued viewing.",
                "Quality over upload frequency. The page says the system does not penalize breaks, and that often posting videos that do not resonate can hurt over time.",
                "Each video is scored on fresh performance. One experiment that misses does not, by itself, block the channel. Repeated misses can.",
            ],
        }
    ],
    "observed_patterns": [
        {
            "pattern": "A recent join date on a top-100 YouTube row is a clock, not a rate",
            "example": "UR · Cristiano joined 8 July 2024 and the table shows 83.3 million subscribers",
            "note": "Strongest dated start in the YouTube rows read this session. It is celebrity transfer (same person as entries 11 and 51), not from-zero organic growth. No daily rate was computed because the list page mixes June 2026 and September 2026 sentences (Q10).",
        },
        {
            "pattern": "Shorts plus a recognizable series",
            "example": "Alan's Universe joined YouTube 3 February 2020; list shows 102 million; article infobox matches and calls it the highest-ranking Shorts channel",
            "note": "Article describes a scripted high-school series (Alan's Universe) with over 1 billion views. Packaging is a series, not one-off trend clips.",
        },
        {
            "pattern": "Dubbing plus Shorts coincided with a documented spike",
            "example": "Stokes Twins article: daily views from about 3–5 million to about 50 million in 2024; passed 100 million subscribers that November; list now shows 146 million",
            "note": "Article also says videos are dubbed into eight languages. List/infobox disagree by 2 million (Q20). A 2021 monetization suspension is on the same article — growth was not a straight line.",
        },
        {
            "pattern": "From-zero short comedy, dated account creation",
            "example": "KallMeKris registered TikTok on 9 April 2020; list rank 42 shows 50.3 million followers and 2.5 billion likes as of 7 September 2026",
            "note": "Article says the skits run about 30 seconds to a minute. Table still describes her as a hairdresser; the article says she left that job in April 2020 (Q27).",
        },
        {
            "pattern": "A skill that does not need language",
            "example": "Spencer X, beatboxing: TikTok created February 2019, ten million by that fall (article); list rank 37 shows 53.5 million and 1.3 billion likes",
            "note": "Same language-free mechanic as silent comedy and cooking, applied to sound. Street-performer background is in the article, not inferred.",
        },
        {
            "pattern": "Livestreams as the growth surface, including non-English",
            "example": "Younes Zarou: first TikTok video 22 August 2019; 2020 livestreams over 240,000 viewers (article); list rank 27 shows 57.6 million and 1.3 billion likes",
            "note": "Article does not name a more specific editing format. Country flags on the list are Morocco and Germany; the biography states birth in Frankfurt only (Q19).",
        },
        {
            "pattern": "Event-style streams lead Twitch; a specialist can still be top 15",
            "example": "Kai Cenat 21.4 million (rank 1) and Ibai 20.4 million (rank 2), both 'special events'; Jynxzi rank 12 at 11.2 million with only Clash Royale and Rainbow Six Siege listed",
            "note": "Table as of 2 August 2026. Page lead says Kai Cenat was first to 20 million followers. Spanish-language event streaming (Ibai) matches the English event row, so the format is not language-locked.",
        },
        {
            "pattern": "Science explainers reach the YouTube top 100 without a celebrity head start",
            "example": "Mark Rober, 82.6 million, category Education/Entertainment, joined 20 October 2011",
            "note": "Article: NASA engineer; first video received 1.5 million views in one day. Infobox is 81.9 million (Q21). List value used.",
        },
        {
            "pattern": "Regional-language family Shorts",
            "example": "KL BRO Biju Rithvik, 88.7 million, Malayalam lifestyle vlogs, joined 21 July 2020",
            "note": "Family channel; children appear (flagged). Figure is the list value, not the December 2025 infobox.",
        },
        {
            "pattern": "Highest derived likes-per-follower in the TikTok top 50 read this session is a media brand",
            "example": "Barstool Sports, rank 44: 49.6 million followers and 10.5 billion likes",
            "note": "Brand-account column is Yes. Charli D'Amelio (entry 2) has the higher likes total on the same table (12.3 billion). Dividing the rounded figures puts Barstool higher per follower (about 212 vs about 77). That ratio is not a published rate and is not a recent engagement rate. Do not copy the brand's volume model as a from-zero plan.",
        },
        {
            "pattern": "Let's Play longevity, below the top-100 floor",
            "example": "jacksepticeye: uploading since December 2012, 1 million in 2014, 10 million by 2016, infobox 31.2 million (8 September 2026)",
            "note": "The YouTube list page says all top-100 channels have passed 50 million, so this niche row cannot come from that table. Infobox used and flagged.",
        },
        {
            "pattern": "Platform switching is a real growth decision, with a smaller number on the old platform",
            "example": "Valkyrae left Twitch for a YouTube exclusive contract on 13 January 2020; infobox shows YouTube 4.05 million and Twitch 1.6 million (4 July 2026)",
            "note": "Not in the Twitch top-50 table read this session. Included because the article dates the switch. Do not treat 4.05 million as comparable to 21.4 million Twitch leaders.",
        },
        {
            "pattern": "Makeup growth on the cited page is a cosmetics company, not only tutorials",
            "example": "jeffreestar, 15.6 million YouTube subscribers, infobox updated 23 April 2026; Jeffree Star Cosmetics founded November 2014",
            "note": "Huda Kattan's article documents a WordPress makeup blog (April 2010) and a cosmetics line (2013) but prints no follower figure, so she is not a row. NikkieTutorials remains entry 58.",
        },
        {
            "pattern": "A trainable unusual pet behavior can set a record without reaching top-50 scale",
            "example": "Merlin the pig, 1,100,000 Instagram followers (Guinness), button communication",
            "note": "Record dates conflict (1 December 2025 vs 23 February 2026 prose). Same pet-ceiling point as Jiffpom and Nala, with a 2025/2026 record instead of a 2019/2020 one. Still not comparable to celebrity accounts.",
        },
        {
            "pattern": "One-line communities and space communities are large, and old",
            "example": "r/Showerthoughts 34 million (rank 10) and r/space 28 million (rank 15), May 2025",
            "note": "Same Visual Capitalist snapshot as the existing Reddit rows. r/Showerthoughts ties r/science at 34 million. Not evidence of 2026 growth.",
        },
    ],
    "cited_clocks": [
        {
            "account": "YouTube UR · Cristiano",
            "clock": "Joined YouTube 8 July 2024; top-100 table shows 83.3 million subscribers",
            "source_url": WIKI_YT,
            "caveat": "Celebrity transfer (entries 11 and 51). List page mixes June 2026 and September 2026 dates (Q10). Not a computed daily rate.",
        },
        {
            "account": "YouTube Alan's Universe (@AlanChikinChow)",
            "clock": "Joined 3 February 2020; list shows 102 million, matching the 18 September 2026 infobox",
            "source_url": WIKI_YT,
            "caveat": "Join date is a table column. No daily rate computed.",
        },
        {
            "account": "YouTube KL BRO Biju Rithvik",
            "clock": "Joined 21 July 2020; list shows 88.7 million",
            "source_url": WIKI_YT,
            "caveat": "Family vlog. Infobox (84.7 million, 10 December 2025) was not used.",
        },
        {
            "account": "YouTube Stokes Twins",
            "clock": "Article: joint channel 11 March 2017; passed 100 million in November 2024; list now shows 146 million",
            "source_url": "https://en.wikipedia.org/wiki/Stokes_Twins",
            "caveat": "List join date is 11 April 2008, which is not the joint-channel date (Q20). 2021 monetization suspension is on the same article.",
        },
        {
            "account": "TikTok @kallmekris",
            "clock": "Account registered 9 April 2020; list shows 50.3 million and 2.5 billion likes as of 7 September 2026",
            "source_url": "https://en.wikipedia.org/wiki/KallMeKris",
            "caveat": "Article says 40th; table rank read this session is 42.",
        },
        {
            "account": "TikTok @spencerx",
            "clock": "TikTok created February 2019; ten million by that fall (article); list shows 53.5 million as of 7 September 2026",
            "source_url": "https://en.wikipedia.org/wiki/Spencer_X",
            "caveat": "The ten-million milestone is from the article, not the list table.",
        },
        {
            "account": "TikTok @youneszarou",
            "clock": "First video 22 August 2019; list shows 57.6 million as of 7 September 2026",
            "source_url": "https://en.wikipedia.org/wiki/Younes_Zarou",
            "caveat": "YouTube infobox (27.5 million subscribers, 23 billion views, 9 July 2026) is a different platform and is not this row's metric.",
        },
        {
            "account": "YouTube jacksepticeye",
            "clock": "Uploading since December 2012; 1 million in 2014; 10 million by 2016; infobox 31.2 million updated 8 September 2026",
            "source_url": "https://en.wikipedia.org/wiki/Jacksepticeye",
            "caveat": "Infobox, not the top-100 list. Milestones are years, not exact dates.",
        },
    ],
    "topics_with_public_demand": [
        "Beatboxing / skill audio that does not need language (Spencer X)",
        "Short scripted comedy from a dated zero start (KallMeKris, April 2020)",
        "YouTube Shorts series (Alan's Universe; Stokes Twins dubbing + Shorts)",
        "Science and DIY explainers (Mark Rober; r/space)",
        "Family Shorts in a regional language (KL BRO, Malayalam)",
        "Event livestreams in more than one language (Kai Cenat, Ibai)",
        "Specialist game channels (Jynxzi; jacksepticeye Let's Plays)",
        "Makeup as tutorials and as a cosmetics company (NikkieTutorials, Jeffree Star; Huda Kattan documented without a follower figure)",
        "Unusual pet skills (Merlin the pig, Guinness 2025/2026 record)",
        "Basketball, separate from football and cricket (LeBron James on Instagram — celebrity, not a from-zero plan)",
        "One-line observation communities (r/Showerthoughts)",
        "Sports-media likes density (Barstool Sports on TikTok — brand account)",
    ],
}


def main():
    data = json.loads(PATH.read_text(encoding="utf-8"))
    n0 = len(data["entries"])
    if n0 != 60:
        raise SystemExit(f"expected 60 entries before batch 4, found {n0}")

    seen = {(e["platform"], e["handle"].lower()) for e in data["entries"]}
    next_id = 61
    for e in BATCH4:
        key = (e["platform"], e["handle"].lower())
        if key in seen:
            raise SystemExit(f"duplicate {key}")
        seen.add(key)
        e["id"] = next_id
        next_id += 1
    if len(BATCH4) != 20 or next_id != 81:
        raise SystemExit("batch 4 is not exactly ids 61-80")

    for e in BATCH4:
        exp = EXPECTED[e["id"]]
        if (e["platform"], e["handle"], e["metric_value"]) != exp:
            raise SystemExit(f"lock mismatch id {e['id']}: {e['platform']} {e['handle']} {e['metric_value']} != {exp}")
        if not e["profile_url"].startswith("https://") or not e["source_url"].startswith("https://"):
            raise SystemExit(f"bad url on {e['id']}")
        if e.get("article_url") and not e["article_url"].startswith("https://"):
            raise SystemExit(f"bad article url on {e['id']}")

    data["entries"].extend(BATCH4)
    m = data["meta"]
    m["entry_count"] = len(data["entries"])
    m["last_updated"] = "2026-09-21"
    m["verification_rule"] = (
        "Every follower/member/subscriber figure is taken from a cited source fetched in the "
        "session shown in docs/VERIFICATION.md: a Wikipedia list table, a Wikipedia article "
        "infobox, a Guinness World Records record page, or the Visual Capitalist Reddit ranking. "
        "Batch 4 (entries 61-80) was read line by line on 2026-09-21. Figures are snapshots; "
        "live counts change. No live platform API scrape was performed."
    )
    m.setdefault("batches", {})
    m["batches"]["batch_4"] = (
        "Entries 61-80, added 2026-09-21. Twenty new rows aimed at organic and unusual growth "
        "cases: Twitch event/specialist streamers, YouTube Shorts and science creators, TikTok "
        "from-zero and skill accounts, a Guinness pet record, basketball and a flagged celebrity "
        "YouTube clock, plus two Reddit topic communities. Each figure was read from the cited "
        "page before it was written. See docs/VERIFICATION.md Q16-Q32."
    )
    m["limitations"] = list(m.get("limitations", [])) + [
        "Batch 4 (2026-09-21): tiktok.com, instagram.com, facebook.com, reddit.com, twitch.tv and the TikTok Creator Academy URL returned errors or were not opened from this environment. YouTube Help (support.google.com) was fetched. New tactics are limited to that Help page plus patterns read off the cited account pages.",
        "Batch 4 did not add Facebook rows. The Wikipedia Facebook table links to articles, not facebook.com slugs, and the new top pages read this session are already-famous brands. Batch-2 slug click-throughs are still owed (Q6).",
        "Batch 4 Guinness pig record has an internal date conflict (When 1 December 2025 vs prose 23 February 2026) and the record page was cookie-walled (Q16).",
        "Batch 4 infobox rows (jacksepticeye, Valkyrae, Jeffree Star) and the Guinness row are not on the same date or the same list as the top-100/top-50 tables. Do not rank them against those tables as if the snapshots matched.",
        "Cited start dates (Ronaldo YouTube join date, KallMeKris, Spencer X, Alan's Universe, KL BRO, Stokes, jacksepticeye) are clocks, not a comparable growth-rate table. A second snapshot is still required before any fastest-growth ranking.",
        "Doug the Pug and Huda Kattan were reviewed and not added: the Doug article does not print a profile slug, and the Huda Kattan article prints no follower figure (Q31).",
    ]
    m["primary_sources"] = [
        {"name": "Wikipedia — most-followed TikTok accounts", "url": WIKI_TT, "note": "Table as of 7 September 2026"},
        {"name": "Wikipedia — most-followed Instagram accounts", "url": WIKI_IG, "note": "Table as of June 2026"},
        {"name": "Wikipedia — most-followed Facebook pages", "url": "https://en.wikipedia.org/wiki/List_of_most-followed_Facebook_pages", "note": "Table as of 28 August 2026"},
        {"name": "Visual Capitalist — largest Reddit communities", "url": VC, "note": "May 2025, data from Reddit"},
        {"name": "Wikipedia — most-subscribed YouTube channels", "url": WIKI_YT, "note": "Top-100 table; page dates are mixed (Q10)"},
        {"name": "Wikipedia — most-followed X accounts", "url": "https://en.wikipedia.org/wiki/List_of_most-followed_X_accounts", "note": "As of August 2026"},
        {"name": "Wikipedia — most-followed Twitch channels", "url": WIKI_TW, "note": "As of 2 August 2026"},
        {"name": "Guinness — most Instagram followers for a dog", "url": "https://www.guinnessworldrecords.com/world-records/450698-most-followers-for-a-dog-on-instagram", "note": "Verified 29 April 2019"},
        {"name": "Guinness — most Instagram followers for a cat", "url": "https://www.guinnessworldrecords.com/world-records/465511-most-followers-for-a-cat-on-instagram", "note": "Verified 13 May 2020"},
        {"name": "Guinness — most Instagram followers for a pig", "url": GWR_PIG, "note": "1,100,000; When 1 December 2025; prose as of 23 February 2026 (Q16)"},
        {"name": "YouTube Help — recommendation system", "url": YT_HELP, "note": "Official tactics, fetched 21 September 2026"},
    ]

    PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    SNAP.parent.mkdir(parents=True, exist_ok=True)
    SNAP.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    strat = json.loads(STRAT.read_text(encoding="utf-8"))
    # Guard against a double-append if someone re-runs after editing the assert.
    names = {o["name"] for o in strat["official_resources"]}
    if "YouTube Help — YouTube's Recommendation System" not in names:
        strat["official_resources"].extend(STRATEGY_ADDS["official_resources"])
    strat["official_tactics"] = STRATEGY_ADDS["official_tactics"]
    existing_patterns = {p["pattern"] for p in strat["observed_patterns"]}
    strat["observed_patterns"].extend(
        p for p in STRATEGY_ADDS["observed_patterns"] if p["pattern"] not in existing_patterns
    )
    existing_topics = set(strat["topics_with_public_demand"])
    strat["topics_with_public_demand"].extend(
        t for t in STRATEGY_ADDS["topics_with_public_demand"] if t not in existing_topics
    )
    strat["cited_clocks"] = STRATEGY_ADDS["cited_clocks"]
    STRAT.write_text(json.dumps(strat, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Reload and lock.
    written = json.loads(PATH.read_text(encoding="utf-8"))
    if len(written["entries"]) != 80:
        raise SystemExit("write failed: entry count")
    for e in written["entries"]:
        if e["id"] in EXPECTED:
            exp = EXPECTED[e["id"]]
            got = (e["platform"], e["handle"], e["metric_value"])
            if got != exp:
                raise SystemExit(f"post-write mismatch {got} != {exp}")
    print("OK: 80 entries; batch 4 ids 61-80 locked; strategies and snapshot written.")


if __name__ == "__main__":
    main()
