<h1 align="center">Antigravity SEO</h1>

<p align="center">
  <b>The open-source SEO, GEO, AEO & Ecommerce Optimization Skill for Google Antigravity.</b><br />
  Rank higher in Google Search, win AI Overviews, and get cited by ChatGPT, Perplexity, Gemini, and Copilot.
</p>

<p align="center">
  <a href="#quick-install">Install</a> ·
  <a href="#features">Features</a> ·
  <a href="#commands">Commands</a> ·
  <a href="#architecture">Architecture</a> ·
  <a href="#ecommerce-excellence">Ecommerce</a> ·
  <a href="#geo--aeo">GEO & AEO</a> ·
  <a href="#contributing">Contributing</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Google%20Antigravity-Skill-4285F4?style=flat&logo=google" alt="Google Antigravity Skill" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT" />
  <img src="https://img.shields.io/badge/Schema.org-Compliant-blue" alt="Schema.org" />
  <img src="https://img.shields.io/badge/Anti--AI%20Tone-Enforced-orange" alt="Anti-AI Tone" />
  <img src="https://img.shields.io/badge/GEO%20Ready-ChatGPT%20%7C%20Gemini%20%7C%20Perplexity-purple" alt="GEO Ready" />
</p>

---

## What is Antigravity SEO?

**Antigravity SEO** is a complete, modular, battle-tested SEO framework designed specifically for **Google Antigravity** (and compatible with Claude Code / Cursor agent systems). Inspired by modern AI search architectures and engineered for high-converting ecommerce stores, enterprise publishers, and agency audits.

Traditional SEO alone is no longer enough. Modern organic acquisition requires **Four Core Pillars**:
1. **Traditional Technical SEO:** Clean crawlability, canonicals, sitemaps, single-H1 heading hierarchy, and PageSpeed.
2. **Ecommerce Catalog Integrity:** Price completeness, unique SKU management, leaf categories, and conversion trust badges.
3. **GEO (Generative Engine Optimization):** High entity density and structured HTML tables so ChatGPT Search, Perplexity, and Gemini cite your products and answers.
4. **AEO (Answer Engine Optimization):** Structured 10-FAQ clusters with upfront 1–2 sentence direct factual answers optimized for Google AI Overviews and Featured Snippets.

---

## Quick Install

### Method 1: Automatic Installer (Recommended)

#### For Windows (PowerShell):
```powershell
irm https://raw.githubusercontent.com/IshtiakNihal/Antigravity-SEO/main/install.ps1 | iex
```

#### For Linux / macOS (Bash):
```bash
curl -fsSL https://raw.githubusercontent.com/IshtiakNihal/Antigravity-SEO/main/install.sh | bash
```

### Method 2: Manual Clone
Clone directly into your Antigravity global configuration:
```bash
git clone https://github.com/IshtiakNihal/Antigravity-SEO.git ~/.gemini/config/skills/antigravity-seo
```

Once installed, the `antigravity-seo` skill is immediately available to your Antigravity agent across any workspace!

---

## Commands & Capabilities

In Antigravity, you can activate this skill by prompting your agent naturally or typing:

| Command / Trigger | Action | Output Deliverable |
|---|---|---|
| `/seo audit <url>` | Full-site or single-page technical audit | Pass/Fail score across 9 categories & blocker list |
| `/seo ecommerce <url or catalog>` | Catalog integrity & shopping visibility check | Price, SKU, variation, and schema report |
| `/seo geo <url>` | Generative Engine Optimization analysis | Citability score (0–100) and entity density breakdown |
| `/seo aeo <topic or url>` | Answer Engine Optimization builder | 10 high-intent FAQs with upfront direct answers |
| `/seo schema <url>` | Schema.org JSON-LD generation & validation | Validated `Product`, `Offer`, `BreadcrumbList`, `FAQPage` |
| `/seo titles <keywords>` | High-CTR Title & Meta Description engineering | Commercial meta templates with exact price and warranty hooks |
| `/seo sitemap <domain>` | XML Sitemap discovery & health check | Partition status and lastmod consistency report |
| `/seo humanize <text>` | Anti-AI content audit | Fluff-word purifier and factual density enhancer |

---

## Architecture & Sub-Skills

```text
Antigravity-SEO/
├── skills/
│   ├── seo/                 # Master Orchestrator Skill
│   ├── seo-ecommerce/       # Catalog Integrity & Product Page Optimization
│   ├── seo-geo/             # Generative Engine Optimization (AI Citations)
│   ├── seo-aeo/             # Answer Engine Optimization (AI Overviews & Snippets)
│   ├── seo-schema/          # Schema.org JSON-LD Generation & Validation
│   ├── seo-technical/       # Crawlability, Canonicals & Core Web Vitals
│   ├── seo-content/         # E-E-A-T, Information Gain & Anti-AI Humanizer
│   └── seo-sitemap/         # XML Sitemap Discovery & Partition Monitoring
├── agents/                  # Specialist Agent Definitions
│   ├── seo-technical.md     # Technical SEO Lead
│   ├── seo-ecommerce.md     # Ecommerce Specialist
│   ├── seo-geo.md           # AI Search & Entity Analyst
│   └── seo-aeo.md           # Answer & Featured Snippet Architect
├── scripts/                 # Standalone Python / Node Utility Scripts
│   ├── catalog_audit.py     # Fast catalog scanner for ৳0 prices and missing SKUs
│   ├── geo_scorer.py        # Entity density & citability calculation algorithm
│   ├── schema_validate.py   # Schema.org validator
│   └── sitemap_checker.py   # Sitemap crawler & health auditor
├── tests/                   # Automated pytest suite
├── install.ps1              # Windows 1-click installer
├── install.sh               # Unix 1-click installer
└── README.md
```

---

## Ecommerce Commercial Excellence

E-commerce stores cannot convert visitors if basic commercial facts are broken. Antigravity SEO enforces:

* **Zero-Price Detection:** Immediately flags any product with price `0` or empty price that prevents checkout.
* **SKU Integrity:** Ensures every simple product and child variation has a standardized, unique SKU (`MJ-[ID]`).
* **Title Duplication Prevention:** Separates CMS product names from HTML `<title>` tags, avoiding repetitive spam titles (e.g. `Model Price in BD Price in BD | Store`).
* **Conversion Trust Elements:** Injects verified warranty badges (official brand vs replacement coverage) and estimated delivery timelines.
* **Mobile Viewport Discipline:** Ensures upper buying summary contains 3–5 bullet points, reserving 2-column HTML specification tables for the description tab.

---

## GEO & AEO: The Future of Search

### Generative Engine Optimization (GEO)
AI engines do not read marketing adjectives. They look for:
* **High Entity Density:** Exact dimensions, mAh capacities, wattage ratings, motor RPM, Bluetooth versions, and audio codecs.
* **Structured HTML Tables:** LLMs prioritize 2-column clean `<table>` layouts when synthesizing comparative answers (e.g., *"Compare Model A vs Model B"*).
* **Anti-AI Tone:** Detects and removes generic robotic filler (*"revolutionary"*, *"game-changer"*, *"delve into"*, *"testament to"*).

### Answer Engine Optimization (AEO)
Google's AI Overviews and Featured Snippets favor the **10 FAQ Formula**:
* 10 distinct questions answering genuine buyer objections.
* **Upfront Direct Answer:** Every answer begins with an immediate, factual 1–2 sentence answer before explaining technical details.

---

## Contributing

We welcome contributions from the open-source community! 
1. Fork the repo.
2. Create a feature branch (`git checkout -b feature/amazing-skill`).
3. Commit your changes (`git commit -m 'feat: add new crawler tool'`).
4. Push to the branch (`git push origin feature/amazing-skill`).
5. Open a Pull Request.

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

Maintained with ❤️ by **Ishtiak Nihal** for the global Google Antigravity & AI developer community.
