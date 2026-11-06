#!/usr/bin/env python3
"""Check a built site for the mistakes that fail silently.

Usage: python3 scripts/check_site.py public

Fails on broken internal links, invalid structured data, missing page
metadata, hreflang pairs that do not point back at each other, and sitemap
entries that do not exist.
"""
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlparse

SITE_HOST = "liriansu.com"
# Served from other repositories' GitHub Pages under the same domain.
PROJECT_PAGES = ("/mymenu/", "/static/", "/slides/")
SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"


def attr(tag, name):
    match = re.search(rf'\b{name}=(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+))', tag)
    return html.unescape(next(g for g in match.groups() if g is not None)) if match else None


def resolve(root, path):
    path = unquote(path)
    target = root / path.lstrip("/")
    return target.is_file() or (target / "index.html").is_file()


def site_path(url, base):
    """Return the path of an internal URL, or None for an external one."""
    parsed = urlparse(url)
    if parsed.scheme or parsed.netloc:
        return parsed.path or "/" if parsed.netloc == SITE_HOST else None
    if parsed.path.startswith("/"):
        return parsed.path
    return str(Path(base).parent / parsed.path) if parsed.path else None


def check_page(root, url_path, source, errors):
    head = source.split("</head>")[0]
    tags = re.findall(r"<(?:link|meta)\b[^>]*>", head)

    def fail(message):
        errors.append(f"{url_path}: {message}")

    if not re.search(r"<html[^>]*\blang=", source):
        fail("missing <html lang>")
    if not re.search(r"<title>[^<]+</title>", head):
        fail("missing <title>")
    if "/404.html" in url_path:
        return None
    description = next((attr(t, "content") for t in tags if attr(t, "name") == "description"), None)
    if not description:
        fail("missing meta description")
    canonical = next((attr(t, "href") for t in tags if attr(t, "rel") == "canonical"), None)
    if not canonical or not canonical.startswith("https://"):
        fail(f"bad canonical {canonical!r}")
    for block in re.findall(r'<script type=["\']?application/ld\+json["\']?>(.*?)</script>', source, re.S):
        try:
            json.loads(block)
        except ValueError as error:
            fail(f"invalid JSON-LD: {error}")
    alternates = {attr(t, "hreflang"): attr(t, "href") for t in tags if attr(t, "hreflang")}
    return canonical, alternates


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "public")
    errors = []
    pages = {}

    for file in sorted(root.rglob("*.html")):
        source = file.read_text(encoding="utf8", errors="replace")
        url_path = "/" + file.relative_to(root).as_posix()
        if re.search(r'http-equiv=["\']?refresh', source):
            continue  # alias redirect pages
        result = check_page(root, url_path, source, errors)
        if result:
            pages[result[0]] = result[1]
        for match in re.finditer(r'<(?:a|link|img|script)\b[^>]*>', source):
            url = attr(match.group(0), "href") or attr(match.group(0), "src")
            if not url or url.startswith(("#", "mailto:", "data:", "javascript:")):
                continue
            path = site_path(url, url_path)
            if path and not path.startswith(PROJECT_PAGES) and not resolve(root, path):
                errors.append(f"{url_path}: broken link {url}")

    for canonical, alternates in pages.items():
        if alternates and alternates.get("x-default") is None:
            errors.append(f"{canonical}: hreflang without x-default")
        if alternates and canonical not in alternates.values():
            errors.append(f"{canonical}: hreflang without self reference")
        for lang, url in alternates.items():
            if canonical not in pages.get(url, {}).values():
                errors.append(f"{canonical}: hreflang {lang} -> {url} does not point back")

    for sitemap in root.rglob("sitemap.xml"):
        for loc in ET.parse(sitemap).getroot().iter(f"{SITEMAP_NS}loc"):
            path = urlparse(loc.text).path
            if not resolve(root, path):
                errors.append(f"{sitemap.relative_to(root)}: {loc.text} does not exist")
            elif not path.endswith(".xml") and loc.text not in pages:
                errors.append(f"{sitemap.relative_to(root)}: {loc.text} is not a canonical page")
    robots = root / "robots.txt"
    if not robots.is_file() or "Sitemap:" not in robots.read_text(encoding="utf8"):
        errors.append("robots.txt: missing, or has no Sitemap line")

    for error in sorted(set(errors)):
        print(error)
    print(f"checked {len(pages)} pages, {len(set(errors))} problems")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
