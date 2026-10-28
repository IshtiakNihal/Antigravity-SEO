# Antigravity SEO: Autonomous Agent Instructions

> **Native Agent Framework for Google Antigravity**  
> Also fully compatible with **Cursor**, **Claude Code**, **Gemini CLI**, **OpenAI Codex**, and **Cline**.

---

## Architecture Overview

**Antigravity SEO** is a universal, open-source AI SEO framework containing:
- **26 Sub-Skills** (`skills/`) covering Technical SEO, Core Web Vitals, Schema.org JSON-LD, Generative Engine Optimization (GEO), Answer Engine Optimization (AEO), Content & E-E-A-T, Programmatic SEO, International/Hreflang, E-commerce, Local Business, and Backlinks.
- **19 Autonomous Specialist Agents** (`agents/`) that fan out in parallel during full audits.
- **65 Standalone Python Tools** (`scripts/`) providing deterministic, reproducible data parsing, SSRF-safe fetching, and schema validation.

---

## Agent Roles & Dispatch Map

When performing audits, orchestrate tasks across the specialist agent squad:

| Agent | Role | Focus Area | Primary Command |
|---|---|---|---|
| `seo-technical` | Technical SEO Lead | Crawlability, indexability, canonicals, status codes, robots.txt | `/seo technical <url>` |
| `seo-content` | Content & E-E-A-T Editor | Topic depth, information gain, reading level, anti-AI tone | `/seo content <url>` |
| `seo-schema` | Structured Data Engineer | Schema.org JSON-LD generation, rich snippet validation | `/seo schema <url>` |
| `seo-geo` | AI Search Analyst | Citability scoring, entity density, LLM answer readiness | `/seo geo <url>` |
| `seo-aeo` | Answer Engine Architect | 10-FAQ formula with upfront direct answers for AI Overviews | `/seo aeo <topic>` |
| `seo-sitemap` | Sitemap Architect | XML sitemap discovery, partition validation, lastmod health | `/seo sitemap <url>` |
| `seo-performance`| Core Web Vitals Engineer | LCP, INP, CLS, TTFB, script evaluation, render blocking | `/seo audit <url>` |
| `seo-ecommerce` | Commerce Specialist | Product/Offer schema, unique SKUs, multi-currency, facet limits | `/seo ecommerce <url>` |
| `seo-local` | Local SEO Specialist | Google Business Profile, local citations, NAP consistency | `/seo local <url>` |
| `seo-maps` | Maps Intelligence Analyst| Geo-grid ranking, map pack visibility, local reviews | `/seo maps <query>` |
| `seo-cluster` | Topic Strategist | Semantic clustering, pillar-cluster internal linking | `/seo cluster <keyword>`|
| `seo-competitor`| Competitive Analyst | Competitor comparison tables, feature gap matrices | `/seo competitor-pages` |
| `seo-google` | Google API Analyst | Search Console, PageSpeed Insights, CrUX, Indexing API | `/seo google [cmd]` |
| `seo-backlinks` | Link Analyst | Domain backlink profiles, Common Crawl, Moz, Bing | `/seo backlinks <url>` |
| `seo-drift` | Change Monitor | SQLite snapshot baselines, ranking and content drift | `/seo drift <cmd>` |
| `seo-sxo` | Search Experience Designer| Search Intent alignment, UX conversion, persona flow | `/seo sxo <url>` |
| `seo-agentic` | AI Agent Readiness | llms.txt, WebMCP, accessibility tree, agent browsing | `/seo agentic <url>` |
| `seo-programmatic`| Programmatic Architect | Scalable URL patterns, database-to-page templating | `/seo programmatic` |
| `seo-hreflang` | International SEO | Multi-language tags, regional routing, canonical parity | `/seo hreflang <url>` |

---

## Tool Execution Discipline

1. **Security & SSRF Guard**:
   All HTTP requests must validate target URLs through `scripts/url_safety.py` to prevent SSRF against internal/private IP ranges.
2. **Local-First Privacy**:
   No user data, prompts, or domains are ever transmitted to third-party tracking services. All processing runs locally within the Antigravity session.
3. **Evidence-Based Recommendations**:
   Every recommendation must state:
   - What the finding is based on (exact line, code, or HTTP header).
   - Why it matters for ranking or AI citations.
   - Falsifiable test criteria: how the user can verify the fix worked.
