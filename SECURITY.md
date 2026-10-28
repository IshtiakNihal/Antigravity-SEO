# Security Policy

Antigravity SEO is an autonomous agent framework that runs locally on your workstation inside Google Antigravity. We treat the security of our users and their development environments with the highest priority.

---

## Reporting a Security Vulnerability

If you discover a security issue or vulnerability in Antigravity SEO, please report it responsibly. **Do not open a public issue.**

1. Open a private [GitHub Security Advisory](https://github.com/IshtiakNihal/Antigravity-SEO/security/advisories/new).
2. If you are unable to access the advisory form, open a public GitHub issue titled:
   `"Security Contact Request - [Brief Topic]"` with **no technical details or exploit code**. The maintainer (**Ahmed Ishtiak Nihal**) will contact you privately.

Please include:
* Description of the vulnerability and its potential impact.
* Minimal reproduction steps (command line, target payload, or script).
* Environment details (Operating System, Python version, Antigravity version).
* Suggested remediation if available.

---

## Threat Model & Defenses

Antigravity SEO executes within a local agent harness and interacts with user-supplied URLs. We enforce strict defensive boundaries:

1. **SSRF (Server-Side Request Forgery) Mitigation**:
   * All network fetch operations must pass through [`scripts/url_safety.py`](scripts/url_safety.py).
   * Requests targeting private IP ranges (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`), loopback (`127.0.0.1`, `localhost`), link-local (`169.254.0.0/16`), and cloud instance metadata endpoints (`169.254.169.254`) are blocked prior to connection.

2. **ReDoS & Parser Safety**:
   * All regular expression evaluators (meta tag parsers, schema extractors, entity detectors) enforce strict length limits to prevent catastrophic backtracking.

3. **Zero Secret Leakage**:
   * Antigravity SEO never records, logs, or exports API keys, auth tokens, or session credentials. `.env` files are blocked via `.gitignore`.

---

## Coordinated Disclosure

We follow a **90-day coordinated disclosure policy**:
* **Day 0**: Acknowledgment of receipt.
* **Within 3 Days**: Initial severity triage and reproduction.
* **Within 14 Days**: Remediation candidate tested.
* **Within 30 Days**: Security patch released to main branch.
