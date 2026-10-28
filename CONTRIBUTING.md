# Contributing to Antigravity SEO

We welcome contributions from developers, SEO engineers, and AI researchers working with Google Antigravity!

---

## Getting Started

1. **Fork the Repository**:
   Create a fork of `https://github.com/IshtiakNihal/Antigravity-SEO` on GitHub.

2. **Clone & Set Up Locally**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Antigravity-SEO.git
   cd Antigravity-SEO

   # Create virtual environment
   python -m venv .venv

   # Activate virtual environment
   # Windows:
   .venv\Scripts\activate
   # macOS / Linux:
   source .venv/bin/activate

   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Run the Test Suite**:
   ```bash
   python -m unittest discover tests -v
   ```
   *All tests must pass prior to opening a pull request.*

---

## Contribution Guidelines

* **Google Antigravity Focus**: All skills and agent definitions must be optimized natively for Google Antigravity and Gemini models (`gemini-1.5-pro`, `gemini-1.5-flash`).
* **Security First**: Any tool making external HTTP requests must integrate with `scripts/url_safety.py` to prevent SSRF vulnerabilities.
* **Deterministic Tests**: Add unit tests in `tests/test_audit.py` for any new parser, score calculation, or validation script.
* **Open Source Attribution**: Maintain academic and professional integrity—never copy proprietary assets or third-party screenshots.

---

## Submitting Pull Requests

1. Create a feature branch: `git checkout -b feature/your-feature-name`.
2. Commit your changes with clear, descriptive commit messages.
3. Push to your fork: `git push origin feature/your-feature-name`.
4. Open a Pull Request against `main`. Complete the checklist in `.github/PULL_REQUEST_TEMPLATE.md`.
