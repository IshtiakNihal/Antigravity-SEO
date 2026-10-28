# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in Antigravity SEO, please report it responsibly. Do **not** open a public issue.

1. Open a private [GitHub Security Advisory](https://github.com/IshtiakNihal/Antigravity-SEO/security/advisories/new) on this repository. Private vulnerability reporting is enabled on this project.
2. If the advisory form is unavailable to you, open a public issue titled *"Security contact request"* with **no technical details**. The maintainer will reply with a private, secure communication channel.

When reporting, please include:
- A concise description of the vulnerability and its potential security impact.
- A minimal proof-of-concept / reproducer (target URL, CLI command, payload, or test case).
- Affected environment, OS, and Python version.
- Any suggested fix or remediation if available.

---

## Coordinated Disclosure

Antigravity SEO follows a **90-day coordinated disclosure** policy:

| Timeline | Milestone |
|---:|---|
| **Day 0** | Maintainer acknowledges receipt of the vulnerability report. |
| **Day ≤ 3** | Initial triage: severity rating (CVSS v3.1) and verification of reproducibility. |
| **Day ≤ 14** | Remediation / patch candidate prepared and tested. |
| **Day ≤ 30** | Fix released in a patched version; reporter credited in release notes (unless opt-out requested). |
| **Day ≤ 90** | Public security advisory published. |

---

## Supported Versions

| Version Line | Status | Notes |
|---|---|---|
| **v1.x (Current)** |  Fully Supported | Active development; all security patches and functional updates. |
| **Pre-release** | ⚠️ Best-effort | Development branches; upgrade to main. |

---

## Threat Model & Mitigations

Antigravity SEO is an autonomous audit and optimization toolkit that executes inside the user's local Google Antigravity workstation. It accepts user-supplied target domains and URLs, fetches remote web resources, and parses structured data.

### 1. Server-Side Request Forgery (SSRF) & Untrusted Targets
* **Threat**: An audited target URL or redirected location might attempt to pivot into local-network services (`localhost`, `127.0.0.1`, `10.0.0.0/8`, `192.168.0.0/16`, `169.254.169.254` cloud metadata endpoints).
* **Mitigation**: All fetch operations must route through strict URL safety guards (`scripts/url_safety.py`). Private, loopback, multicast, link-local, and reserved IP ranges are blocked prior to HTTP resolution.

### 2. Malicious Content Injection & Regular Expression DoS (ReDoS)
* **Threat**: Malicious target web pages could craft catastrophic backtracking strings to hang parsing agents.
* **Mitigation**: All regex parsers for meta tags, Schema.org JSON-LD, and HTML heading trees enforce input size boundaries and execution timeouts.

### 3. Credential & Environment Protection
* **Threat**: Leaking API keys (Google OAuth, PageSpeed, Bing, Moz) into logs, generated Markdown files, or Git history.
* **Mitigation**: Antigravity SEO strictly prohibits committing credentials or secrets. Environment variables and configuration files (`.env`) are excluded via `.gitignore` and sanitized during all report rendering.
