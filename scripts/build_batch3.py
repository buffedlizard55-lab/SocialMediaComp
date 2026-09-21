#!/usr/bin/env python3
"""One-off builder for batch 3 (entries 41-60) of the master list.

Reads data/master-list.json, appends 20 verified batch-3 entries
(YouTube, X, Twitch coverage + pets/makeup/gaming niche entries),
updates meta and data/strategies.json, writes back.

Every figure below was read during the 2026-09-21 session from the cited
source page (Wikipedia list tables, Wikipedia article infoboxes, or Guinness
World Records official record pages). See docs/VERIFICATION.md, batch 3.

Run from repo root: python3 scripts/build_batch3.py
"""
import json

PATH = "data/master-list.json"
STRAT = "data/strategies.json"

WIKI_YT = "https://en.wikipedia.org/wiki/List_of_most-subscribed_YouTube_channels"
WIKI_X = "https://en.wikipedia.org/wiki/List_of_most-followed_X_accounts"
WIKI_TWITCH = "https://en.wikipedia.org/wiki/List_of_most-followed_Twitch_channels"
WIKI_MARK = "https://en.wikipedia.org/wiki/Markiplier"
WIKI_NIKKIE = "https://en.wikipedia.org/wiki/Nikkie_de_Jager"
GWR_DOG = "https://www.guinnessworldrecords.com/world-records/450698-most-followers-for-a-dog-on-instagram"
GWR_CAT = "https://www.guinnessworldrecords.com/world-records/465511-most-followers-for-a-cat-on-instagram"

YT_NOTE = "Wikipedia most-subscribed YouTube list, retrieved 21 September 2026 (top-100 table)"
X_NOTE = "Wikipedia most-followed X accounts list, as of August 2026 (totals rounded down to nearest 0.1M per table note)"
TWITCH_NOTE = "Wikipedia most-followed Twitch channels list, as of 2 August 2026 (rank 3)"

BATCH3 = [
    # ---- YouTube (Wikipedia most-subscribed channels table) ----
    {
        "platform": "YouTube", "handle": "MrBeast", "owner": "MrBeast",
        "topic": "Entertainment / challenges", "cohort": "creator",
        "country": "United States",
        "metric_label": "Subscribers (millions)", "metric_value": 517,
        "snapshot_note": YT_NOTE,
        "profile_url": "https://www.youtube.com/user/MrBeast6000",
        "source_name": "Wikipedia: List of most-subscribed YouTube channels",
        "source_url": WIKI_YT,
        "growth_notes": "Most-subscribed channel on YouTube per the list page, which also reports an average gain of about 133,000 subscribers per day (June 2026). Same owner as entry 3 (TikTok) — cross-platform brand building; YouTube is now the larger platform of the two.",
        "verified_list": True, "verification_type": "list_table", "added_batch": 3,
        "irregularity": "Cross-platform duplicate of entry 3 (same owner on TikTok).",
    },
    {
        "platform": "YouTube", "handle": "T-Series", "owner": "T-Series (music label)",
        "topic": "Music label (Hindi)", "cohort": "brand",
        "country": "India",
        "metric_label": "Subscribers (millions)", "metric_value": 315,
        "snapshot_note": YT_NOTE,
        "profile_url": "https://www.youtube.com/user/tseries",
        "source_name": "Wikipedia: List of most-subscribed YouTube channels",
        "source_url": WIKI_YT,
        "growth_notes": "Indian music-label channel at industrial release volume; page prose counts it among only two channels above 300 million subscribers.",
        "verified_list": True, "verification_type": "list_table", "added_batch": 3,
        "irregularity": "Record-label channel, not an independent creator.",
    },
    {
        "platform": "YouTube", "handle": "Cocomelon - Nursery Rhymes", "owner": "Cocomelon",
        "topic": "Nursery rhymes / kids education", "cohort": "brand",
        "country": "United States",
        "metric_label": "Subscribers (millions)", "metric_value": 202,
        "snapshot_note": YT_NOTE,
        "profile_url": "https://www.youtube.com/channel/UCbCmjCuTUZos6Inko4u57UQ",
        "source_name": "Wikipedia: List of most-subscribed YouTube channels",
        "source_url": WIKI_YT,
        "growth_notes": "Animated nursery-rhyme format (category per table: Education); page prose counts it among only three channels above 200 million subscribers. Kids content is co-viewed by children and parents, multiplying watch time.",
        "verified_list": True, "verification_type": "list_table", "added_batch": 3,
        "irregularity": "Studio-produced kids-media brand, not an independent creator.",
    },
    {
        "platform": "YouTube", "handle": "SET India", "owner": "Sony Entertainment Television (SET India)",
        "topic": "TV entertainment (Hindi)", "cohort": "brand",
        "country": "India",
        "metric_label": "Subscribers (millions)", "metric_value": 190,
        "snapshot_note": YT_NOTE,
        "profile_url": "https://www.youtube.com/channel/UCpEhnqL0y41EpW2TvWAHD7Q",
        "source_name": "Wikipedia: List of most-subscribed YouTube channels",
        "source_url": WIKI_YT,
        "growth_notes": "Hindi general-entertainment network clips; the list page reports 28 of the top-100 channels are primarily Hindi, reflecting India's platform scale.",
        "verified_list": True, "verification_type": "list_table", "added_batch": 3,
        "irregularity": "TV-network channel, not an independent creator.",
    },
    {
        "platform": "YouTube", "handle": "Vlad and Niki", "owner": "Vlad and Niki",
        "topic": "Kids / family entertainment", "cohort": "creator",
        "country": "Russia",
        "metric_label": "Subscribers (millions)", "metric_value": 150,
        "snapshot_note": YT_NOTE,
        "profile_url": "https://www.youtube.com/channel/UCvlE5gTbOvjiolFlEm-c_Ow",
        "source_name": "Wikipedia: List of most-subscribed YouTube channels",
        "source_url": WIKI_YT,
        "growth_notes": "Family-produced play/adventure videos; press coverage (WSJ via ForumDaily, 2023) names it one of the three most popular live-action kids' channels on YouTube alongside Like Nastya and Kids Diana Show.",
        "verified_list": True, "verification_type": "list_table", "added_batch": 3,
        "irregularity": "Child creators; kids-channel topic detail is third-party-sourced (see VERIFICATION.md Q12).",
    },
    {
        "platform": "YouTube", "handle": "Kids Diana Show", "owner": "Kids Diana Show",
        "topic": "Kids / family entertainment", "cohort": "creator",
        "country": "Ukraine",
        "metric_label": "Subscribers (millions)", "metric_value": 138,
        "snapshot_note": YT_NOTE,
        "profile_url": "https://www.youtube.com/channel/UCk8GzjMOrta8yxDcKfylJYw",
        "source_name": "Wikipedia: List of most-subscribed YouTube channels",
        "source_url": WIKI_YT,
        "growth_notes": "Kids' play-and-roleplay channel (channel name and press coverage); part of the same live-action kids' cohort as Vlad and Niki and Like Nastya.",
        "verified_list": True, "verification_type": "list_table", "added_batch": 3,
        "irregularity": "Child creator; kids-channel topic detail is third-party-sourced (see VERIFICATION.md Q12).",
    },
    {
        "platform": "YouTube", "handle": "Like Nastya", "owner": "Like Nastya",
        "topic": "Kids / family entertainment", "cohort": "creator",
        "country": "Russia",
        "metric_label": "Subscribers (millions)", "metric_value": 133,
        "snapshot_note": YT_NOTE,
        "profile_url": "https://www.youtube.com/channel/UCJplp5SjeGSdVdwsfb9Q7lQ",
        "source_name": "Wikipedia: List of most-subscribed YouTube channels",
        "source_url": WIKI_YT,
        "growth_notes": "Kids' toy-play/adventure channel; press coverage (WSJ via ForumDaily, 2023) names it one of the three most popular live-action kids' channels on YouTube.",
        "verified_list": True, "verification_type": "list_table", "added_batch": 3,
        "irregularity": "Child creator; kids-channel topic detail is third-party-sourced (see VERIFICATION.md Q12).",
    },
    {
        "platform": "YouTube", "handle": "PewDiePie", "owner": "PewDiePie (Felix Kjellberg)",
        "topic": "Entertainment / lifestyle vlogs (gaming history)", "cohort": "creator",
        "country": "Japan / Sweden",
        "metric_label": "Subscribers (millions)", "metric_value": 109,
        "snapshot_note": YT_NOTE,
        "profile_url": "https://www.youtube.com/PewDiePie",
        "source_name": "Wikipedia: List of most-subscribed YouTube channels",
        "source_url": WIKI_YT,
        "growth_notes": "Described on the list page as a gamer and a former holder of the #1 most-subscribed spot; the longest-running individual-creator benchmark on YouTube.",
        "verified_list": True, "verification_type": "list_table", "added_batch": 3,
    },
    # ---- X (Wikipedia most-followed X accounts table, as of August 2026) ----
    {
        "platform": "X", "handle": "@elonmusk", "owner": "Elon Musk",
        "topic": "Business / tech (platform owner)", "cohort": "celebrity",
        "country": None,
        "metric_label": "Followers (millions, rounded down to nearest 0.1M)", "metric_value": 241.6,
        "snapshot_note": X_NOTE,
        "profile_url": "https://x.com/elonmusk",
        "source_name": "Wikipedia: List of most-followed X accounts",
        "source_url": WIKI_X,
        "growth_notes": "Most-followed account on X per the list page; he is also the platform's owner.",
        "verified_list": True, "verification_type": "list_table", "added_batch": 3,
        "irregularity": "Owns the platform. Wikipedia states he partially acquired followers through changes to the platform code that promote his own posts more favorably — treat this row as NOT evidence of organic growth.",
    },
    {
        "platform": "X", "handle": "@BarackObama", "owner": "Barack Obama",
        "topic": "Politics / public figure", "cohort": "celebrity",
        "country": "United States",
        "metric_label": "Followers (millions, rounded down to nearest 0.1M)", "metric_value": 118.9,
        "snapshot_note": X_NOTE,
        "profile_url": "https://x.com/BarackObama",
        "source_name": "Wikipedia: List of most-followed X accounts",
        "source_url": WIKI_X,
        "growth_notes": "Second most-followed person on X per the list page; scale reflects pre-existing global fame (description: President of the United States 2009-2017).",
        "verified_list": True, "verification_type": "list_table", "added_batch": 3,
    },
    {
        "platform": "X", "handle": "@Cristiano", "owner": "Cristiano Ronaldo",
        "topic": "Sports (football)", "cohort": "celebrity",
        "country": "Portugal",
        "metric_label": "Followers (millions, rounded down to nearest 0.1M)", "metric_value": 114.3,
        "snapshot_note": X_NOTE,
        "profile_url": "https://x.com/Cristiano",
        "source_name": "Wikipedia: List of most-followed X accounts",
        "source_url": WIKI_X,
        "growth_notes": "Third most-followed person on X per the list page; second platform row for the same person (entry 11: 678M on Instagram) — top-tier reach replicated across platforms.",
        "verified_list": True, "verification_type": "list_table", "added_batch": 3,
        "irregularity": "Cross-platform duplicate of entry 11 (same person on Instagram).",
    },
    {
        "platform": "X", "handle": "@realDonaldTrump", "owner": "Donald Trump",
        "topic": "Politics / public figure", "cohort": "celebrity",
        "country": "United States",
        "metric_label": "Followers (millions, rounded down to nearest 0.1M)", "metric_value": 111.8,
        "snapshot_note": X_NOTE,
        "profile_url": "https://x.com/realDonaldTrump",
        "source_name": "Wikipedia: List of most-followed X accounts",
        "source_url": WIKI_X,
        "growth_notes": "Fourth most-followed person on X per the list page (description: President of the United States 2017-2021, 2025-present).",
        "verified_list": True, "verification_type": "list_table", "added_batch": 3,
    },
    {
        "platform": "X", "handle": "@narendramodi", "owner": "Narendra Modi",
        "topic": "Politics / public figure", "cohort": "celebrity",
        "country": "India",
        "metric_label": "Followers (millions, rounded down to nearest 0.1M)", "metric_value": 107.1,
        "snapshot_note": X_NOTE,
        "profile_url": "https://x.com/narendramodi",
        "source_name": "Wikipedia: List of most-followed X accounts",
        "source_url": WIKI_X,
        "growth_notes": "Fifth most-followed person on X per the list page; second India-scale row after cricket (entry 13) and Hindi YouTube channels.",
        "verified_list": True, "verification_type": "list_table", "added_batch": 3,
    },
    {
        "platform": "X", "handle": "@rihanna", "owner": "Rihanna",
        "topic": "Music / business", "cohort": "celebrity",
        "country": "Barbados",
        "metric_label": "Followers (millions, rounded down to nearest 0.1M)", "metric_value": 98.6,
        "snapshot_note": X_NOTE,
        "profile_url": "https://x.com/rihanna",
        "source_name": "Wikipedia: List of most-followed X accounts",
        "source_url": WIKI_X,
        "growth_notes": "Sixth most-followed person on X per the list page caption ('Barbadian singer Rihanna'); musician and businesswoman per the table.",
        "verified_list": True, "verification_type": "list_table", "added_batch": 3,
    },
    {
        "platform": "X", "handle": "@NASA", "owner": "NASA",
        "topic": "Space agency / science communication", "cohort": "brand",
        "country": "United States",
        "metric_label": "Followers (millions, rounded down to nearest 0.1M)", "metric_value": 92.3,
        "snapshot_note": X_NOTE,
        "profile_url": "https://x.com/NASA",
        "source_name": "Wikipedia: List of most-followed X accounts",
        "source_url": WIKI_X,
        "growth_notes": "Highest brand/org account in the X table per its brand-account column; mission/imagery content gives science communication mainstream reach.",
        "verified_list": True, "verification_type": "list_table", "added_batch": 3,
        "irregularity": "Government-agency account.",
    },
    # ---- Niche topic-gap entries (pets, makeup, gaming) ----
    {
        "platform": "Instagram", "handle": "@jiffpom", "owner": "Jiffpom (Jiff the Pomeranian)",
        "topic": "Pets (dog)", "cohort": "creator",
        "country": "United States",
        "metric_label": "Followers (millions, exact record count)", "metric_value": 9.018251,
        "snapshot_note": "Guinness World Records: 9,018,251 Instagram followers, verified 29 April 2019 (most followers on Instagram for a dog)",
        "profile_url": "https://www.instagram.com/jiffpom/",
        "source_name": "Guinness World Records: Most followers on Instagram for a dog",
        "source_url": GWR_DOG,
        "growth_notes": "Record-holding pet account: costumed/performing dog content. Shows the pet-niche ceiling (single-digit millions) versus platform top-50 scale, with high brand-commercial value.",
        "verified_list": False, "verification_type": "guinness_record", "added_batch": 3,
        "irregularity": "Snapshot dated 29 April 2019 (record verification date) — live count will differ. Official GWR page read via search-indexed text because the live page served a cookie-consent wall to the build environment. Profile slug corroborated via a Time Out embed of an @jiffpom post; instagram.com itself unreachable from the build environment (see VERIFICATION.md Q13).",
    },
    {
        "platform": "Instagram", "handle": "@nala_cat", "owner": "Nala Cat",
        "topic": "Pets (cat)", "cohort": "creator",
        "country": "United States",
        "metric_label": "Followers (millions, exact record count)", "metric_value": 4.361519,
        "snapshot_note": "Guinness World Records: 4,361,519 Instagram followers, verified 13 May 2020 (most followers on Instagram for a cat)",
        "profile_url": "https://www.instagram.com/nala_cat/",
        "source_name": "Guinness World Records: Most followers on Instagram for a cat",
        "source_url": GWR_CAT,
        "growth_notes": "Record-holding pet account; shelter-adoption backstory (per GWR/press). Demonstrates that a from-zero niche account (started 2012 per press) can reach millions and hold an official record title.",
        "verified_list": False, "verification_type": "guinness_record", "added_batch": 3,
        "irregularity": "Snapshot dated 13 May 2020 (record verification date) — live count will differ. Official GWR page read via search-indexed text because the live page served a cookie-consent wall to the build environment (see VERIFICATION.md Q13).",
    },
    {
        "platform": "YouTube", "handle": "NikkieTutorials", "owner": "Nikkie de Jager",
        "topic": "Makeup / beauty tutorials", "cohort": "creator",
        "country": "Netherlands",
        "metric_label": "Subscribers (millions)", "metric_value": 15,
        "snapshot_note": "Wikipedia article infobox: 15 million subscribers, last updated 29 March 2026",
        "profile_url": "https://www.youtube.com/@NikkieTutorials",
        "source_name": "Wikipedia: Nikkie de Jager (article)",
        "source_url": WIKI_NIKKIE,
        "growth_notes": "Beauty-tutorial format; the article says she gained online popularity after her 2015 video 'The Power of Makeup' inspired many imitator videos — trend-creation (not just trend participation) as a growth lever.",
        "verified_list": False, "verification_type": "wiki_article_infobox", "added_batch": 3,
        "irregularity": "Figure from the Wikipedia article infobox (not a ranked list page); infobox last updated 29 March 2026. Beauty/makeup topic per the same article (beauty vlogger, make-up artist).",
    },
    {
        "platform": "YouTube", "handle": "Markiplier", "owner": "Markiplier (Mark Edward Fischbach)",
        "topic": "Gaming (Let's Play)", "cohort": "creator",
        "country": "United States",
        "metric_label": "Subscribers (millions)", "metric_value": 38.9,
        "snapshot_note": "Wikipedia article infobox: 38.9 million subscribers, last updated 15 September 2026",
        "profile_url": "https://www.youtube.com/channel/UC7_YxT-KID8kRbqZo7MyscQ",
        "source_name": "Wikipedia: Markiplier (article)",
        "source_url": WIKI_MARK,
        "growth_notes": "Let's Play videos of indie horror games (per the article); Forbes listed him as the third-highest-paid content creator on the platform in 2022 (per the article).",
        "verified_list": False, "verification_type": "wiki_article_infobox", "added_batch": 3,
        "irregularity": "Figure from the Wikipedia article infobox, not a ranked list page. Minor internal drift: infobox 38.9M (15 Sep 2026) vs body text 'over 38.8 million as of August 7, 2026' — infobox (newer) used; see VERIFICATION.md Q11.",
    },
    {
        "platform": "Twitch", "handle": "Ninja", "owner": "Ninja (Richard Tyler Blevins)",
        "topic": "Gaming (live streaming)", "cohort": "creator",
        "country": "United States",
        "metric_label": "Followers (millions)", "metric_value": 19.3,
        "snapshot_note": TWITCH_NOTE + "; matches his article infobox (19.3M, updated 6 September 2026)",
        "profile_url": "https://www.twitch.tv/ninja",
        "source_name": "Wikipedia: List of most-followed Twitch channels",
        "source_url": WIKI_TWITCH,
        "growth_notes": "First Twitch channel to reach 10 million followers (per the list page); now ranked 3rd behind Kai Cenat (21.4M) and Ibai (20.4M) as of 2 August 2026 — platform leadership changes fast, and event-style streamers overtook the earlier solo-gaming wave. Fortnite-driven breakout per his article.",
        "verified_list": True, "verification_type": "list_table", "added_batch": 3,
    },
]

STRATEGY_ADDS = {
    "official_resources": [
        {
            "name": "YouTube Creators",
            "url": "https://www.youtube.com/creators/",
            "why": "Official YouTube education/resources for channel growth."
        },
    ],
    "observed_patterns": [
        {
            "pattern": "Kids / family co-viewing at massive scale",
            "example": "Cocomelon (202M), Vlad and Niki (150M), Kids Diana Show (138M), Like Nastya (133M)",
            "note": "Three of the top-10 YouTube channels are kids' channels (batch 3); children re-watch repeatedly and parents co-view, multiplying watch-time signals. Managed by families/studios, not solo creators."
        },
        {
            "pattern": "Documented per-day growth rate",
            "example": "MrBeast: about 133,000 subscribers per day (Wikipedia YouTube list, June 2026)",
            "note": "The only per-day growth rate stated directly on a cited list page; the kind of delta this project wants to track across snapshots."
        },
        {
            "pattern": "Cross-platform reach compounding",
            "example": "MrBeast 517M YouTube + 140.9M TikTok; Ronaldo 678M Instagram + 114.3M X",
            "note": "The two largest individual followings on the leaderboard both replicate top-tier reach on a second platform; platform-native audiences add rather than substitute."
        },
        {
            "pattern": "Growth-leadership turnover on live platforms",
            "example": "Twitch: Ninja first to 10M followers, now #3; Kai Cenat (21.4M) and Ibai (20.4M) lead with event-style streams",
            "note": "Platform leaders change within ~5 years; formats (special events, collabs) overtook the first solo-gaming wave — momentum requires format renewal."
        },
        {
            "pattern": "Platform-owner advantage is not organic",
            "example": "@elonmusk 241.6M on X",
            "note": "Wikipedia states X's owner partially acquired followers via code changes favoring his own posts; flagged in the leaderboard so the 'organic growth' competition is not skewed by it."
        },
        {
            "pattern": "Trend-creation beats trend-participation (beauty niche)",
            "example": "NikkieTutorials' 'The Power of Makeup' (2015) spawned an imitator format",
            "note": "Starting a replicable format recruits other creators into promoting it; one-off trend participation does not compound."
        },
        {
            "pattern": "Pets: durable niche with a hard ceiling",
            "example": "Jiffpom 9.0M and Nala Cat 4.4M on Instagram (Guinness records, 2019/2020)",
            "note": "Pet accounts convert to merchandise/brand deals but plateau far below platform top-50; credential milestones (records) extend the tail."
        },
        {
            "pattern": "Regional-language volume publishing",
            "example": "T-Series 315M and SET India 190M (Hindi); 28 of YouTube's top 100 are primarily Hindi",
            "note": "High-frequency label/network output aimed at India-scale audiences; same mechanics as batch-1's non-English TikTok creators, applied by studios."
        },
    ],
    "topics_with_public_demand": [
        "Kids / family co-viewing content (Cocomelon, Vlad and Niki, Kids Diana Show, Like Nastya)",
        "Gaming across formats: Let's Play (PewDiePie, Markiplier), live streaming (Ninja on Twitch)",
        "Pets / animals as an evergreen niche (Jiffpom, Nala Cat - Guinness record holders)",
        "Makeup / beauty tutorials (NikkieTutorials)",
        "Politics / public figures on X (Obama, Trump, Modi)",
        "Space / science communication (NASA on X)",
        "Regional-language music and TV volume publishing (T-Series, SET India)",
    ],
}


def main():
    with open(PATH, encoding="utf-8") as f:
        data = json.load(f)
    n0 = len(data["entries"])
    assert n0 == 40, f"expected 40 entries, found {n0}"

    # Duplicate guards: handles must be unique within a platform, ids contiguous.
    seen = {(e["platform"], e["handle"].lower()) for e in data["entries"]}
    next_id = n0 + 1
    for e in BATCH3:
        key = (e["platform"], e["handle"].lower())
        assert key not in seen, f"duplicate {key}"
        seen.add(key)
        e["id"] = next_id
        next_id += 1
    assert len(BATCH3) == 20 and next_id == 61

    data["entries"].extend(BATCH3)
    m = data["meta"]
    m["entry_count"] = len(data["entries"])
    m["last_updated"] = "2026-09-21"
    m["verification_rule"] = (
        "Every follower/member/subscriber figure is taken from a cited source fetched in the "
        "session shown in docs/VERIFICATION.md: a Wikipedia list table (batches 1-3), a Wikipedia "
        "article infobox or a Guinness World Records record page (batch-3 niche entries, flagged "
        "per row), or an official platform URL. Figures are snapshots; live counts change. No live "
        "API scrape was performed."
    )
    m["batches"]["batch_3"] = (
        "Entries 41-60, added 2026-09-21. Adds YouTube (10), X (7) and Twitch (1) coverage plus "
        "pets/makeup/gaming niche entries verified from Wikipedia article infoboxes and Guinness "
        "World Records record pages."
    )
    m["limitations"] = [
        lim for lim in m["limitations"]
        if "Batch 2:" not in lim
    ] + [
        "Batch 2 network note (2026-09-20): tiktok.com, instagram.com, facebook.com and reddit.com were unreachable from the build environment then; figures come from the cited list snapshots (see docs/VERIFICATION.md Q6). The same limits still applied on 2026-09-21 (x.com, twitch.tv and instagram.com not directly fetchable; Guinness pages fetchable but cookie-walled, Q13).",
        "Batch 3 niche entries use dated snapshots of different ages (Wikipedia infoboxes updated Mar-Sep 2026; Guinness records verified 2019/2020) — ages are flagged per row and are not directly comparable.",
        "Wikipedia's X list table carries an 'unreliable source?' template on its sourcing note; figures are used as published (Q14).",
        "YouTube list page has a stale sentence (MrBeast '500 million' as of June 2026) next to the table's 517M; the table value is used (Q10).",
    ]
    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    with open(STRAT, encoding="utf-8") as f:
        strat = json.load(f)
    strat["official_resources"].extend(STRATEGY_ADDS["official_resources"])
    strat["observed_patterns"].extend(STRATEGY_ADDS["observed_patterns"])
    strat["topics_with_public_demand"].extend(STRATEGY_ADDS["topics_with_public_demand"])
    with open(STRAT, "w", encoding="utf-8") as f:
        json.dump(strat, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"OK: {len(data['entries'])} entries now; appended ids 41-60; strategies updated.")


if __name__ == "__main__":
    main()
