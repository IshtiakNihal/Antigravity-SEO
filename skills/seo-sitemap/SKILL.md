---
name: seo-sitemap
description: XML Sitemap discovery and health monitoring skill. Verifies sitemap index routing, partition boundaries, and lastmod timestamp hygiene.
---

# XML Sitemap Discovery & Health Monitoring

Monitors XML sitemaps ensuring that new and updated URLs are discovered by search engine crawlers without delay.

## Sitemap Health Checks
1. Primary sitemap index responds with HTTP 200 and valid `text/xml` MIME type.
2. Child sitemaps do not exceed 50,000 URLs or 50MB uncompressed size.
3. Every published canonical URL is present in exactly one sitemap partition.
4. `lastmod` timestamps accurately reflect real editorial updates.
