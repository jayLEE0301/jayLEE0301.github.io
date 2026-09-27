#!/usr/bin/env python3
"""Refresh the star counts in the Code panel of index.html.

Repos are discovered from the page itself: every
<span class="repo-star-count" data-repo="owner/name"> is looked up and its
text replaced. The marquee renders each tile twice, so every repo has more
than one span and all of them are updated.

A repo that fails to fetch keeps whatever number the page already had, so a
transient API error degrades to a slightly stale number rather than a blank.
Run from anywhere; paths resolve against the repo root.
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, "index.html")
FINDER = re.compile(r'<span class="repo-star-count" data-repo="([^"]+)">')


def fetch_stars(repo, token):
    request = urllib.request.Request(
        "https://api.github.com/repos/" + repo,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "sjlee.cc-star-sync",
        },
    )
    if token:
        request.add_header("Authorization", "Bearer " + token)
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)["stargazers_count"]


def human(count):
    """Match how GitHub itself abbreviates: 219, 1.2k, 27.8k."""
    if count < 1000:
        return str(count)
    return ("%.1f" % (count / 1000.0)).rstrip("0").rstrip(".") + "k"


def main():
    with open(PAGE, encoding="utf-8") as handle:
        html = handle.read()

    repos = sorted(set(FINDER.findall(html)))
    if not repos:
        sys.exit("No repo-star-count spans found in %s" % PAGE)

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("No GITHUB_TOKEN: falling back to unauthenticated (60/hour).")

    failures = []
    for repo in repos:
        try:
            stars = fetch_stars(repo, token)
        except (urllib.error.URLError, KeyError, ValueError) as error:
            failures.append("%s (%s)" % (repo, error))
            print("%-40s kept existing value" % repo)
            continue

        span = re.compile(
            r'(<span class="repo-star-count" data-repo="%s">)[^<]*(</span>)'
            % re.escape(repo)
        )
        text = human(stars)
        html, replaced = span.subn(lambda m: m.group(1) + text + m.group(2), html)
        print("%-40s %8s  (%d spans)" % (repo, text, replaced))

    with open(PAGE, "w", encoding="utf-8") as handle:
        handle.write(html)

    if failures:
        print("Could not refresh: " + "; ".join(failures), file=sys.stderr)
    # Only a total failure is worth failing the job over; partial results
    # still leave the page correct.
    if len(failures) == len(repos):
        sys.exit("Every lookup failed.")


if __name__ == "__main__":
    main()
