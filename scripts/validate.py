#!/usr/bin/env python3
"""Structural validation for data/master-list.json.

Checks (fail loudly, exit 1):
  - JSON parses; entries is a list
  - ids are contiguous 1..N
  - added_batch matches id ranges (1-20 / 21-40 / 41-60 / 61-80)
  - no duplicate (platform, handle) pairs
  - required fields present and non-empty on every entry
  - metric_value is a positive number
  - profile_url / source_url are https and point at plausible hosts for the platform
  - cohort is one of the documented values
  - batch 3+ entries carry verification_type; verification_type is a known value
  - optional article_url, if present, is https on a trusted host
  - likes_billions, if present, is a positive number

Run from repo root: python3 scripts/validate.py
"""
import json
import sys
from urllib.parse import urlparse

PATH = "data/master-list.json"
REQUIRED = [
    "id", "platform", "handle", "owner", "topic", "metric_label", "metric_value",
    "snapshot_note", "profile_url", "source_name", "source_url", "growth_notes",
    "verified_list", "cohort", "added_batch",
]
COHORTS = {"creator", "celebrity", "brand", "community"}
VERIFICATION_TYPES = {"list_table", "wiki_article_infobox", "guinness_record"}

HOST_OK = {
    "TikTok": ("tiktok.com", "en.wikipedia.org", "visualcapitalist.com"),
    "Instagram": ("instagram.com", "en.wikipedia.org", "visualcapitalist.com", "guinnessworldrecords.com"),
    "Facebook": ("facebook.com", "en.wikipedia.org", "visualcapitalist.com"),
    "Reddit": ("reddit.com", "en.wikipedia.org", "visualcapitalist.com"),
    "YouTube": ("youtube.com", "www.youtube.com", "en.wikipedia.org"),
    "X": ("x.com", "en.wikipedia.org"),
    "Twitch": ("twitch.tv", "en.wikipedia.org"),
}
ARTICLE_HOSTS = ("en.wikipedia.org", "guinnessworldrecords.com", "visualcapitalist.com", "support.google.com")


def norm(host: str) -> str:
    host = host.lower()
    return host[4:] if host.startswith("www.") else host


def main():
    with open(PATH, encoding="utf-8") as f:
        data = json.load(f)
    entries = data["entries"]
    errors = []

    if data["meta"].get("entry_count") != len(entries):
        errors.append(f"meta.entry_count {data['meta']['entry_count']} != {len(entries)}")

    seen_pairs = {}
    for i, e in enumerate(entries, start=1):
        ctx = f"entry {e.get('id', '?')} ({e.get('handle', '?')})"
        if e.get("id") != i:
            errors.append(f"{ctx}: id {e.get('id')} out of order at position {i}")
        for field in REQUIRED:
            if field not in e:
                errors.append(f"{ctx}: missing required field '{field}'")
            elif e[field] in (None, "") and field != "verified_list":
                errors.append(f"{ctx}: empty required field '{field}'")
        if not isinstance(e.get("metric_value"), (int, float)) or e.get("metric_value", 0) <= 0:
            errors.append(f"{ctx}: metric_value must be a positive number")
        if e.get("cohort") not in COHORTS:
            errors.append(f"{ctx}: cohort '{e.get('cohort')}' not in {sorted(COHORTS)}")
        if e.get("country") is not None and not isinstance(e.get("country"), str):
            errors.append(f"{ctx}: country must be a string or null")
        if i <= 20:
            expected_batch = 1
        elif i <= 40:
            expected_batch = 2
        elif i <= 60:
            expected_batch = 3
        elif i <= 80:
            expected_batch = 4
        else:
            expected_batch = None
        if expected_batch is None:
            errors.append(f"{ctx}: id {i} is past the last documented batch (80)")
        elif e.get("added_batch") != expected_batch:
            errors.append(f"{ctx}: added_batch {e.get('added_batch')} != expected {expected_batch}")
        if e.get("verified_list") not in (True, False):
            errors.append(f"{ctx}: verified_list must be boolean")
        for url_field in ("profile_url", "source_url"):
            u = e.get(url_field, "")
            if not u.startswith("https://"):
                errors.append(f"{ctx}: {url_field} not https: {u}")
                continue
            host = norm(urlparse(u).netloc)
            allowed = HOST_OK.get(e.get("platform"), tuple())
            if allowed and host not in allowed:
                errors.append(f"{ctx}: {url_field} host '{host}' unexpected for platform {e['platform']} ({allowed})")
        pair = (e.get("platform"), str(e.get("handle", "")).lower())
        if pair in seen_pairs:
            errors.append(f"{ctx}: duplicate (platform, handle) with entry {seen_pairs[pair]}")
        seen_pairs[pair] = e.get("id")
        if (e.get("added_batch") or 0) >= 3:
            if e.get("verification_type") not in VERIFICATION_TYPES:
                errors.append(f"{ctx}: verification_type '{e.get('verification_type')}' not in {sorted(VERIFICATION_TYPES)}")
        article = e.get("article_url")
        if article:
            if not isinstance(article, str) or not article.startswith("https://"):
                errors.append(f"{ctx}: article_url not https: {article}")
            else:
                ahost = norm(urlparse(article).netloc)
                if ahost not in ARTICLE_HOSTS:
                    errors.append(f"{ctx}: article_url host '{ahost}' not in {ARTICLE_HOSTS}")
        likes = e.get("likes_billions")
        if likes is not None and (not isinstance(likes, (int, float)) or likes <= 0):
            errors.append(f"{ctx}: likes_billions must be a positive number when present")

    n_flagged = sum(1 for e in entries if e.get("irregularity"))
    print(f"entries: {len(entries)}  flagged: {n_flagged}")
    by_platform = {}
    for e in entries:
        by_platform[e["platform"]] = by_platform.get(e["platform"], 0) + 1
    print("platforms: " + ", ".join(f"{k}={v}" for k, v in sorted(by_platform.items())))

    if errors:
        print("\nFAIL:")
        for err in errors:
            print(" -", err)
        sys.exit(1)
    print("OK: all structural checks passed.")


if __name__ == "__main__":
    main()
