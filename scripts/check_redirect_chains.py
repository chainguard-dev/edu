"""Follow every redirect on a running copy of the production nginx image.

Usage: python3 scripts/check_redirect_chains.py BASE_URL [ALIASES_FILE]

BASE_URL is where the image is listening, such as http://localhost:8080.
ALIASES_FILE defaults to public/_aliases, the generated nginx map.

Each rule in the map gives one start URL: the alias itself for an alias rule,
the path for an exact rule, and the literal text before the first regex
metacharacter for a hand-written regex rule. That is a sample of each
hand-written rule, not full coverage of its pattern. Every start URL is
requested with a query string, and the chain is followed to its end.

The check fails when a chain:
- loops, or runs past MAX_HOPS (DOCS-186)
- carries a Location with more than one "?" (DOCS-187)
- redirects to http:// on this site, a downgrade from HTTPS

Chains that end in 404 are listed but do not fail the check. Some already
exist on production and need their own content fixes.

Standard library only, so CI needs no pip install.
"""

import http.client
import re
import sys
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

MAX_HOPS = 10
QUERY = "utm_source=redirect-check"
RULE = re.compile(r'^"(~?)([^"]+)"\s+\S+;$')
REGEX_METACHARACTERS = re.compile(r"[.+*?()|\[\]{}^$\\]")


def start_url(is_regex, key):
    """Return a request path that the rule should match."""
    if not is_regex:
        return key
    pattern = key.removeprefix("^")
    alias = re.fullmatch(r"(.*)\(/\.\*\)\?\$", pattern)
    if alias:
        # A generated alias rule: unescape the literal alias.
        return re.sub(r"\\(.)", r"\1", alias.group(1))
    literal = REGEX_METACHARACTERS.split(pattern, maxsplit=1)[0]
    return literal or None


def load_start_urls(aliases_file):
    urls = set()
    with open(aliases_file) as rules:
        for line in rules:
            match = RULE.match(line.strip())
            if not match:
                raise SystemExit(f"unrecognized line in {aliases_file}: {line.strip()}")
            url = start_url(match.group(1) == "~", match.group(2))
            if url and url.startswith("/"):
                urls.add(url)
    return sorted(urls)


def head(base, path):
    """Return (status, Location) for one HEAD request."""
    parts = urllib.parse.urlsplit(base)
    connection = http.client.HTTPConnection(parts.netloc, timeout=30)
    try:
        connection.request("HEAD", path)
        response = connection.getresponse()
        return response.status, response.getheader("Location") or ""
    finally:
        connection.close()


def follow(base, start):
    """Follow one chain. Return (start, problem or None, final status, hops)."""
    path = f"{start}?{QUERY}"
    seen = []
    hops = []
    for _ in range(MAX_HOPS):
        if path in seen:
            return start, "loop", None, hops
        seen.append(path)
        status, location = head(base, path)
        if status not in (301, 302, 307, 308):
            return start, None, status, hops
        hops.append(location)
        if location.count("?") > 1:
            return start, "doubled query string", None, hops
        target = urllib.parse.urlsplit(location)
        if target.hostname not in (None, "localhost"):
            return start, None, "external", hops
        if target.scheme == "http":
            return start, "redirect downgraded to http://", None, hops
        path = urllib.parse.urlunsplit(("", "", target.path, target.query, ""))
    return start, f"more than {MAX_HOPS} hops", None, hops


def main():
    base = sys.argv[1]
    aliases_file = sys.argv[2] if len(sys.argv) > 2 else "public/_aliases"
    starts = load_start_urls(aliases_file)
    with ThreadPoolExecutor(max_workers=16) as pool:
        results = list(pool.map(lambda start: follow(base, start), starts))

    problems = [r for r in results if r[1]]
    not_found = [r for r in results if r[2] == 404]
    print(f"Followed {len(results)} redirect chains from {aliases_file}.")

    if not_found:
        print(f"\n{len(not_found)} chains end in 404 (reported, not failing):")
        for start, _, _, hops in not_found:
            print(f"  {start} -> {hops[-1] if hops else '(no redirect)'}")

    if problems:
        print(f"\n{len(problems)} chains are broken:")
        for start, problem, _, hops in problems:
            print(f"  {start}: {problem}")
            for hop in hops:
                print(f"      -> {hop}")
        sys.exit(1)
    print("\nNo loops, doubled query strings, or downgraded redirects.")


if __name__ == "__main__":
    main()
