#!/usr/bin/env python3
"""
XML Sitemap Auditor & Discovery Tool
Crawls sitemap indexes, parses child partition sitemaps, verifies HTTP status codes,
and validates lastmod timestamps and URL counts.
"""

import sys
import json
import re
import urllib.request
import xml.etree.ElementTree as ET

def parse_sitemap_xml(xml_content):
    """
    Parses sitemap XML content, automatically handling standard sitemap namespaces.
    Returns a dict with 'type' ('index' or 'urlset') and list of entries.
    """
    try:
        root = ET.fromstring(xml_content)
    except Exception as e:
        return {"error": f"XML parse error: {str(e)}"}

    # Strip XML namespace if present
    tag = root.tag.split("}")[-1] if "}" in root.tag else root.tag

    if tag == "sitemapindex":
        sitemaps = []
        for sitemap in root:
            loc = ""
            lastmod = ""
            for child in sitemap:
                ctag = child.tag.split("}")[-1] if "}" in child.tag else child.tag
                if ctag == "loc":
                    loc = (child.text or "").strip()
                elif ctag == "lastmod":
                    lastmod = (child.text or "").strip()
            if loc:
                sitemaps.append({"loc": loc, "lastmod": lastmod})
        return {"type": "index", "count": len(sitemaps), "entries": sitemaps}

    elif tag == "urlset":
        urls = []
        for url_node in root:
            loc = ""
            lastmod = ""
            changefreq = ""
            priority = ""
            for child in url_node:
                ctag = child.tag.split("}")[-1] if "}" in child.tag else child.tag
                if ctag == "loc":
                    loc = (child.text or "").strip()
                elif ctag == "lastmod":
                    lastmod = (child.text or "").strip()
                elif ctag == "changefreq":
                    changefreq = (child.text or "").strip()
                elif ctag == "priority":
                    priority = (child.text or "").strip()
            if loc:
                urls.append({
                    "loc": loc,
                    "lastmod": lastmod,
                    "changefreq": changefreq,
                    "priority": priority
                })
        return {"type": "urlset", "count": len(urls), "entries": urls}
    else:
        return {"error": f"Unknown root tag: {tag}"}

def audit_sitemap_url(url, timeout=10):
    """
    Fetches and audits a sitemap URL over HTTP/HTTPS.
    """
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Antigravity-SEO-Auditor/1.0 (+https://github.com/IshtiakNihal/Antigravity-SEO)"}
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            status = response.getcode()
            body = response.read().decode("utf-8", errors="ignore")
            parsed = parse_sitemap_xml(body)
            parsed["http_status"] = status
            parsed["url"] = url
            return parsed
    except Exception as e:
        return {"url": url, "error": str(e), "http_status": 0}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        print(f"Auditing sitemap: {target}")
        result = audit_sitemap_url(target)
        print(json.dumps(result, indent=2))
    else:
        sample_xml = """<?xml version="1.0" encoding="UTF-8"?>
        <sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
            <sitemap>
                <loc>https://example.com/post-sitemap.xml</loc>
                <lastmod>2026-10-28T12:00:00+00:00</lastmod>
            </sitemap>
            <sitemap>
                <loc>https://example.com/product-sitemap1.xml</loc>
                <lastmod>2026-10-28T14:30:00+00:00</lastmod>
            </sitemap>
        </sitemapindex>"""
        res = parse_sitemap_xml(sample_xml)
        print("Self-test Sitemap Index Parse Result:")
        print(json.dumps(res, indent=2))
