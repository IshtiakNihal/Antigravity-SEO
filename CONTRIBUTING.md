# Contributing to Antigravity SEO

Thank you for your interest in contributing to **Antigravity SEO**! We welcome developers, technical SEOs, prompt engineers, and AI researchers from all backgrounds.

---

## How to Get Involved

### 1. Reporting Bugs
Before creating an issue, search the [Issues tab](https://github.com/IshtiakNihal/Antigravity-SEO/issues) to verify if the issue has already been reported.

When submitting a bug report:
- Use the **Bug Report** issue template.
- Include your Operating System, Antigravity CLI / IDE version, and Python version.
- Provide the exact command executed (e.g. `/seo technical https://example.com`).
- Include relevant terminal logs or error tracebacks.

### 2. Suggesting Enhancements & New Skills
- Open a **Feature Request** issue to propose new audits, agent roles, or search engine adaptations (e.g. Apple Intelligence, DuckDuckGo AI).
- Clearly explain the problem it solves and how you envision the command syntax.

### 3. Pull Request Guidelines

1. **Fork the Repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Antigravity-SEO.git
   cd Antigravity-SEO
   git checkout -b feature/your-awesome-feature
   ```

2. **Set Up Development Environment**:
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate

   pip install -r requirements.txt
   ```

3. **Run the Test Suite**:
   ```bash
   python -m unittest discover tests
   # or
   pytest tests/
   ```
   *Ensure all unit tests pass before submitting code.*

4. **Code Quality Standards**:
   - Write clean, modular Python with descriptive docstrings.
   - Enforce SSRF protection via `scripts/url_safety.py` for any new web-scraping features.
   - Maintain zero telemetry and local execution integrity.

5. **Submit Your Pull Request**:
   - Open a PR against the `main` branch.
   - Fill out the provided PR template describing your changes, test evidence, and any relevant issue numbers.

---

## Governance & Recognition

All contributors will be recognized in the repository's contributors list! Please adhere to our [Code of Conduct](CODE_OF_CONDUCT.md).
