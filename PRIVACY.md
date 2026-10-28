# Privacy Policy

Antigravity SEO is designed with a strict **local-first, privacy-by-default architecture**.

## What Stays 100% Local

- **Zero Telemetry**: Antigravity SEO does not collect, log, track, or phone home any analytics, telemetry, user identities, or prompt histories.
- **Local Analysis**: All website audits, HTML parsers, technical scrapers, Core Web Vitals evaluations, entity density calculations, and schema validations execute entirely on your machine within your local Google Antigravity session.
- **Local Reports**: All generated Markdown audits, JSON logs, and optimization plans are stored on your local filesystem under your project or Antigravity workspace.

---

## Network Activity & External APIs

### 1. Default Audit Operations
When you run commands like `/seo audit <url>`, `/seo technical <url>`, or `/seo schema <url>`:
- The skill issues standard outbound HTTP/HTTPS requests **only to the target URL** you explicitly supplied.
- No intermediary proxy or tracking server is involved.

### 2. Optional Third-Party Services
If you choose to integrate optional search engine APIs by supplying your own keys, Antigravity SEO contacts only the official vendor endpoints:

| Service / Tool | Destination Endpoint | Data Transmitted | Privacy Policy |
|---|---|---|---|
| **Google Search Console** | `searchconsole.googleapis.com` | Target site URLs, query parameters | [Google Privacy](https://policies.google.com/privacy) |
| **Google PageSpeed Insights** | `pagespeedonline.googleapis.com` | Target URL to test speed & CWV | [Google Privacy](https://policies.google.com/privacy) |
| **Bing Webmaster / IndexNow** | `api.bing.com` / `api.indexnow.org` | Target domain, submitted URLs | [Microsoft Privacy](https://privacy.microsoft.com/) |
| **Moz Link Explorer** | `lsapi.seomoz.com` | Target domain name for backlink metrics | [Moz Privacy](https://moz.com/privacy-policy) |

---

## Security of API Credentials

- All credentials, tokens, and OAuth secrets remain under your local control.
- Never commit `.env` files or hardcode API keys into version control.
