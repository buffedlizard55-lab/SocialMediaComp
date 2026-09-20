#!/usr/bin/env python3
"""One-off builder for batch 2 (entries 21-40) of the master list.

Reads data/master-list.json, backfills cohort/country/added_batch on batch 1,
appends 20 verified batch-2 entries, updates meta, writes back.
Run from repo root: python3 scripts/build_batch2.py
"""
import json

PATH = "data/master-list.json"

# Backfill fields for batch-1 ids, verified against the same Wikipedia tables
# fetched on 2026-09-20 (see docs/VERIFICATION.md).
BATCH1 = {
    1: {"cohort": "creator", "country": "Italy / Senegal", "likes_billions": 2.7},
    2: {"cohort": "creator", "country": "United States", "likes_billions": 12.3},
    3: {"cohort": "creator", "country": "United States", "likes_billions": 1.5},
    4: {"cohort": "brand", "country": "China", "likes_billions": 0.46},
    5: {"cohort": "creator", "country": "Philippines / United States", "likes_billions": 2.4},
    6: {"cohort": "creator", "country": "United States", "likes_billions": 5.3},
    7: {"cohort": "creator", "country": "Indonesia", "likes_billions": 1.8},
    8: {"cohort": "creator", "country": "United States", "likes_billions": 1.3},
    9: {"cohort": "brand", "country": "Switzerland (international HQ)", "likes_billions": 3.2},
    10: {"cohort": "brand", "country": "United States"},
    11: {"cohort": "celebrity", "country": "Portugal"},
    12: {"cohort": "celebrity", "country": "Argentina"},
    13: {"cohort": "celebrity", "country": "United States"},
    14: {"cohort": "celebrity", "country": "United States"},
    15: {"cohort": "celebrity", "country": "United States"},
    16: {"cohort": "brand", "country": "United States"},
    17: {"cohort": "community", "country": None},
    18: {"cohort": "community", "country": None},
    19: {"cohort": "community", "country": None},
    20: {"cohort": "community", "country": None},
}

WIKI_TT = "https://en.wikipedia.org/wiki/List_of_most-followed_TikTok_accounts"
WIKI_IG = "https://en.wikipedia.org/wiki/List_of_most-followed_Instagram_accounts"
WIKI_FB = "https://en.wikipedia.org/wiki/List_of_most-followed_Facebook_pages"
VC_REDDIT = "https://www.visualcapitalist.com/ranked-largest-communities-on-reddit/"

TT_NOTE = "Wikipedia TikTok list as of 7 September 2026"
IG_NOTE = "Wikipedia Instagram list as of June 2026"
FB_NOTE = "Wikipedia Facebook pages list as of 28 August 2026"

BATCH2 = [
    # ---- TikTok (Wikipedia table, as of 7 September 2026) ----
    {
        "platform": "TikTok", "handle": "@kimberly.loaiza", "owner": "Kimberly Loaiza",
        "topic": "Music / lifestyle (Spanish-language)", "cohort": "creator", "country": "Mexico",
        "metric_label": "Followers (millions, rounded)", "metric_value": 83.5,
        "likes_billions": 4.3,
        "snapshot_note": TT_NOTE + " (rank 10)",
        "profile_url": "https://www.tiktok.com/@kimberly.loaiza",
        "source_name": "Wikipedia: List of most-followed TikTok accounts", "source_url": WIKI_TT,
        "growth_notes": "Top Spanish-language creator; Latin-market scale shows non-English content can reach the global top tier.",
        "verified_list": True,
    },
    {
        "platform": "TikTok", "handle": "@bts_official_bighit", "owner": "BTS",
        "topic": "K-pop / music", "cohort": "celebrity", "country": "South Korea",
        "metric_label": "Followers (millions, rounded)", "metric_value": 80.8,
        "likes_billions": 1.8,
        "snapshot_note": TT_NOTE + " (rank 11)",
        "profile_url": "https://www.tiktok.com/@bts_official_bighit",
        "source_name": "Wikipedia: List of most-followed TikTok accounts", "source_url": WIKI_TT,
        "growth_notes": "Band official account; fandom-driven engagement.",
        "verified_list": True,
        "irregularity": "Band official account (label-run), not an individual creator.",
    },
    {
        "platform": "TikTok", "handle": "@domelipa", "owner": "Dominik Lipa",
        "topic": "Dance / lifestyle", "cohort": "creator", "country": "Mexico",
        "metric_label": "Followers (millions, rounded)", "metric_value": 75.3,
        "likes_billions": 5.3,
        "snapshot_note": TT_NOTE + " (rank 15)",
        "profile_url": "https://www.tiktok.com/@domelipa",
        "source_name": "Wikipedia: List of most-followed TikTok accounts", "source_url": WIKI_TT,
        "growth_notes": "5.3B likes on 75.3M followers = ~70 likes per follower, one of the highest engagement-density figures in the list.",
        "verified_list": True,
    },
    {
        "platform": "TikTok", "handle": "@vilmeijuga", "owner": "Meicy Villia",
        "topic": "Magic / creative skits", "cohort": "creator", "country": "Indonesia",
        "metric_label": "Followers (millions, rounded)", "metric_value": 73.7,
        "likes_billions": 2.7,
        "snapshot_note": TT_NOTE + " (rank 17)",
        "profile_url": "https://www.tiktok.com/@vilmeijuga",
        "source_name": "Wikipedia: List of most-followed TikTok accounts", "source_url": WIKI_TT,
        "growth_notes": "Unique account: language-free magic/creative skits from Indonesia; same no-language-barrier pattern as Khaby Lame / Zach King.",
        "verified_list": True,
    },
    {
        "platform": "TikTok", "handle": "@cznburak", "owner": "CZN Burak",
        "topic": "Food / cooking", "cohort": "creator", "country": "Turkey",
        "metric_label": "Followers (millions, rounded)", "metric_value": 73.3,
        "likes_billions": 1.6,
        "snapshot_note": TT_NOTE + " (rank 18)",
        "profile_url": "https://www.tiktok.com/@cznburak",
        "source_name": "Wikipedia: List of most-followed TikTok accounts", "source_url": WIKI_TT,
        "growth_notes": "Unique account: cooking/food content — a visual, language-light topic with global reach.",
        "verified_list": True,
    },
    # ---- Instagram (Wikipedia table, June 2026) ----
    {
        "platform": "Instagram", "handle": "@arianagrande", "owner": "Ariana Grande",
        "topic": "Music", "cohort": "celebrity", "country": "United States",
        "metric_label": "Followers (millions)", "metric_value": 363,
        "snapshot_note": IG_NOTE,
        "profile_url": "https://www.instagram.com/arianagrande",
        "source_name": "Wikipedia: List of most-followed Instagram accounts", "source_url": WIKI_IG,
        "growth_notes": "Musician/actress; celebrity audience carried from music career.",
        "verified_list": True,
    },
    {
        "platform": "Instagram", "handle": "@kimkardashian", "owner": "Kim Kardashian",
        "topic": "Beauty / fashion / media personality", "cohort": "celebrity", "country": "United States",
        "metric_label": "Followers (millions)", "metric_value": 344,
        "snapshot_note": IG_NOTE,
        "profile_url": "https://www.instagram.com/kimkardashian",
        "source_name": "Wikipedia: List of most-followed Instagram accounts", "source_url": WIKI_IG,
        "growth_notes": "Media personality; beauty/fashion commerce crossover.",
        "verified_list": True,
    },
    {
        "platform": "Instagram", "handle": "@virat.kohli", "owner": "Virat Kohli",
        "topic": "Sports (cricket)", "cohort": "celebrity", "country": "India",
        "metric_label": "Followers (millions)", "metric_value": 273,
        "snapshot_note": IG_NOTE,
        "profile_url": "https://www.instagram.com/virat.kohli",
        "source_name": "Wikipedia: List of most-followed Instagram accounts", "source_url": WIKI_IG,
        "growth_notes": "Cricketer; shows scale of the Indian market and cricket as a growth topic.",
        "verified_list": True,
    },
    {
        "platform": "Instagram", "handle": "@natgeo", "owner": "National Geographic",
        "topic": "Photography / science media", "cohort": "brand", "country": "United States",
        "metric_label": "Followers (millions)", "metric_value": 269,
        "snapshot_note": IG_NOTE,
        "profile_url": "https://www.instagram.com/natgeo",
        "source_name": "Wikipedia: List of most-followed Instagram accounts", "source_url": WIKI_IG,
        "growth_notes": "Unique account: photography-led brand account; evergreen visual content.",
        "verified_list": True,
        "irregularity": "Brand account (magazine), not an independent creator.",
    },
    {
        "platform": "Instagram", "handle": "@kevinhart4real", "owner": "Kevin Hart",
        "topic": "Comedy", "cohort": "celebrity", "country": "United States",
        "metric_label": "Followers (millions)", "metric_value": 172,
        "snapshot_note": IG_NOTE,
        "profile_url": "https://www.instagram.com/kevinhart4real",
        "source_name": "Wikipedia: List of most-followed Instagram accounts", "source_url": WIKI_IG,
        "growth_notes": "Comedian; personality-driven posting.",
        "verified_list": True,
    },
    # ---- Facebook (Wikipedia table, as of 28 August 2026) ----
    {
        "platform": "Facebook", "handle": "Netflix", "owner": "Netflix (page)",
        "topic": "Streaming / entertainment", "cohort": "brand", "country": "United States",
        "metric_label": "Followers (millions)", "metric_value": 205,
        "snapshot_note": FB_NOTE + " (rank 1)",
        "profile_url": "https://www.facebook.com/netflix",
        "source_name": "Wikipedia: List of most-followed Facebook pages", "source_url": WIKI_FB,
        "growth_notes": "Most-followed Facebook page; global entertainment brand. Page slug verified via search snippet ('Netflix global page').",
        "verified_list": True,
        "irregularity": "Brand account.",
    },
    {
        "platform": "Facebook", "handle": "5-Minute Crafts", "owner": "5-Minute Crafts (TheSoul Publishing)",
        "topic": "DIY / life hacks", "cohort": "brand", "country": "Cyprus",
        "metric_label": "Followers (millions)", "metric_value": 147,
        "snapshot_note": FB_NOTE + " (rank 5)",
        "profile_url": "https://www.facebook.com/5min.crafts/",
        "source_name": "Wikipedia: List of most-followed Facebook pages", "source_url": WIKI_FB,
        "growth_notes": "Unique account: industrial-scale short DIY/life-hack video production; one of the fastest-growing Facebook pages historically. Page slug verified via search snippet (TheSoul Publishing).",
        "verified_list": True,
        "irregularity": "Media-company content studio (TheSoul Publishing), not an individual creator.",
    },
    {
        "platform": "Facebook", "handle": "Mr. Bean", "owner": "Mr. Bean (character page, Banijay Rights)",
        "topic": "Comedy (character)", "cohort": "brand", "country": "United Kingdom",
        "metric_label": "Followers (millions)", "metric_value": 141,
        "snapshot_note": FB_NOTE + " (rank 6)",
        "profile_url": "https://www.facebook.com/MrBean/",
        "source_name": "Wikipedia: List of most-followed Facebook pages", "source_url": WIKI_FB,
        "growth_notes": "Fictional-character page; silent physical comedy travels across languages. Page slug verified via search snippet (official page).",
        "verified_list": True,
        "irregularity": "Fictional-character page run by rights holder (Banijay Rights), not a person or creator.",
    },
    {
        "platform": "Facebook", "handle": "Shakira", "owner": "Shakira",
        "topic": "Music", "cohort": "celebrity", "country": "Colombia",
        "metric_label": "Followers (millions)", "metric_value": 126,
        "snapshot_note": FB_NOTE + " (rank 8)",
        "profile_url": "https://www.facebook.com/shakira",
        "source_name": "Wikipedia: List of most-followed Facebook pages", "source_url": WIKI_FB,
        "growth_notes": "Most-followed female individual on Facebook per the Wikipedia page intro. Page slug verified via search snippet (official page).",
        "verified_list": True,
        "irregularity": "Wikipedia table orders rank 8 (126M) ahead of rank 9 (128M); figure used as published, rank noted.",
    },
    {
        "platform": "Facebook", "handle": "Will Smith", "owner": "Will Smith",
        "topic": "Entertainment", "cohort": "celebrity", "country": "United States",
        "metric_label": "Followers (millions)", "metric_value": 113,
        "snapshot_note": FB_NOTE + " (rank 12)",
        "profile_url": "https://www.facebook.com/WillSmith",
        "source_name": "Wikipedia: List of most-followed Facebook pages", "source_url": WIKI_FB,
        "growth_notes": "Actor; figure independently corroborated by a search snippet of the page itself (113M). Page slug verified.",
        "verified_list": True,
    },
    # ---- Reddit (Visual Capitalist, May 2025) ----
    {
        "platform": "Reddit", "handle": "r/todayilearned", "owner": "r/todayilearned community",
        "topic": "Education / curiosity", "cohort": "community", "country": None,
        "metric_label": "Members (millions, approx.)", "metric_value": 41,
        "snapshot_note": "Visual Capitalist, May 2025 (rank 5)",
        "profile_url": "https://www.reddit.com/r/todayilearned/",
        "source_name": "Visual Capitalist: Ranked largest communities on Reddit", "source_url": VC_REDDIT,
        "growth_notes": "Curiosity-driven 'fact' posts; comment-heavy engagement.",
        "verified_list": True,
    },
    {
        "platform": "Reddit", "handle": "r/Music", "owner": "r/Music community",
        "topic": "Music", "cohort": "community", "country": None,
        "metric_label": "Members (millions, approx.)", "metric_value": 38,
        "snapshot_note": "Visual Capitalist, May 2025 (rank 6)",
        "profile_url": "https://www.reddit.com/r/Music/",
        "source_name": "Visual Capitalist: Ranked largest communities on Reddit", "source_url": VC_REDDIT,
        "growth_notes": "Evergreen music news/streaming links.",
        "verified_list": True,
    },
    {
        "platform": "Reddit", "handle": "r/movies", "owner": "r/movies community",
        "topic": "Movies", "cohort": "community", "country": None,
        "metric_label": "Members (millions, approx.)", "metric_value": 36,
        "snapshot_note": "Visual Capitalist, May 2025 (rank 8)",
        "profile_url": "https://www.reddit.com/r/movies/",
        "source_name": "Visual Capitalist: Ranked largest communities on Reddit", "source_url": VC_REDDIT,
        "growth_notes": "Trailers/news/discussion; steady event-driven spikes.",
        "verified_list": True,
    },
    {
        "platform": "Reddit", "handle": "r/memes", "owner": "r/memes community",
        "topic": "Memes / humor", "cohort": "community", "country": None,
        "metric_label": "Members (millions, approx.)", "metric_value": 35,
        "snapshot_note": "Visual Capitalist, May 2025 (rank 9)",
        "profile_url": "https://www.reddit.com/r/memes/",
        "source_name": "Visual Capitalist: Ranked largest communities on Reddit", "source_url": VC_REDDIT,
        "growth_notes": "High-velocity shareable format.",
        "verified_list": True,
    },
    {
        "platform": "Reddit", "handle": "r/science", "owner": "r/science community",
        "topic": "Science", "cohort": "community", "country": None,
        "metric_label": "Members (millions, approx.)", "metric_value": 34,
        "snapshot_note": "Visual Capitalist, May 2025 (rank 11)",
        "profile_url": "https://www.reddit.com/r/science/",
        "source_name": "Visual Capitalist: Ranked largest communities on Reddit", "source_url": VC_REDDIT,
        "growth_notes": "Rule-moderated discussion; AMAs with researchers.",
        "verified_list": True,
    },
]


def main():
    with open(PATH, encoding="utf-8") as f:
        data = json.load(f)

    existing = {e["id"]: e for e in data["entries"]}
    if max(existing) != 20 or len(existing) != 20:
        raise SystemExit("Expected exactly entries 1..20 in master list")

    for eid, extra in BATCH1.items():
        existing[eid].setdefault("cohort", extra["cohort"])
        existing[eid].setdefault("country", extra["country"])
        if "likes_billions" in extra:
            existing[eid].setdefault("likes_billions", extra["likes_billions"])
        existing[eid].setdefault("added_batch", 1)

    used = {e["handle"].lower() for e in data["entries"]}
    for i, entry in enumerate(BATCH2, start=21):
        if entry["handle"].lower() in used:
            raise SystemExit(f"Duplicate handle: {entry['handle']}")
        entry_with_id = {"id": i, "added_batch": 2, **entry}
        data["entries"].append(entry_with_id)
        used.add(entry["handle"].lower())

    data["meta"]["entry_count"] = len(data["entries"])
    data["meta"]["batches"] = {
        "batch_1": "Entries 1-20, merged via PR #1 (2026-09-20).",
        "batch_2": "Entries 21-40, added this session (2026-09-20). Adds Facebook coverage and food/K-pop/magic/cricket/photography topics.",
    }
    data["meta"]["limitations"].extend([
        "Batch 2: tiktok.com, instagram.com, facebook.com and reddit.com were unreachable from the build environment (network-blocked), so figures come from the cited list snapshots, not live fetches; see docs/VERIFICATION.md.",
        "Facebook profile URLs (slugs) were cross-checked with search-result snippets of the pages themselves, not opened directly; flagged for manual review.",
        "Wikipedia's Facebook table has an internal ordering quirk (rank 8 = 126M listed before rank 9 = 128M); figures are used as published.",
    ])

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"OK: {len(data['entries'])} entries written")


if __name__ == "__main__":
    main()
