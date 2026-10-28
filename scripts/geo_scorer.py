#!/usr/bin/env python3
"""
GEO (Generative Engine Optimization) Scorer
Evaluates HTML/Markdown text for AI citability, entity density, structured tables, and anti-AI tone.
Returns a GEO Citability Score from 0 to 100.
"""

import sys
import re

AI_FLUFF_WORDS = [
    r"\bdelve into\b",
    r"\ba testament to\b",
    r"\brevolutionary game-changer\b",
    r"\bseamlessly blends?\b",
    r"\blook no further\b",
    r"\bin today's fast-paced\b",
    r"\bin conclusion\b",
    r"\bembark on\b"
]

def calculate_geo_score(html_content):
    score = 0
    feedback = []
    
    # 1. Structured Table (25 points)
    if "<table" in html_content.lower() or "|---" in html_content:
        score += 25
        feedback.append("Structured HTML/Markdown data table present (+25)")
    else:
        feedback.append("Missing structured HTML data table (0/25)")
        
    # 2. Entity Density: Numbers, units, specifications (35 points)
    entity_patterns = [
        r"\b\d+\s*(?:mah|wh|w|v|rpm|vpm|db|mm|g|kg)\b",
        r"\b(?:bluetooth|type-c|usb-c|pd\s*3\.0|qc\s*3\.0|anc|ldac|lhdc|ip\d{2}|ipx\d)\b",
        r"\b\d+\s*(?:months?|years?)\s*(?:official\s*)?warranty\b"
    ]
    matches_count = 0
    for pat in entity_patterns:
        matches_count += len(re.findall(pat, html_content, re.IGNORECASE))
        
    if matches_count >= 8:
        score += 35
        feedback.append(f"High entity density ({matches_count} verifiable spec matches) (+35)")
    elif matches_count >= 4:
        score += 20
        feedback.append(f"Moderate entity density ({matches_count} matches) (+20)")
    else:
        score += 10
        feedback.append(f"Low entity density ({matches_count} matches) (+10)")
        
    # 3. Anti-AI Tone (20 points)
    fluff_found = []
    for pat in AI_FLUFF_WORDS:
        if re.search(pat, html_content, re.IGNORECASE):
            fluff_found.append(pat.replace(r"\b", ""))
            
    if not fluff_found:
        score += 20
        feedback.append("Clean anti-AI commercial tone, zero robotic clichés (+20)")
    else:
        score += 5
        feedback.append(f"AI clichés detected: {', '.join(fluff_found)} (+5)")
        
    # 4. Q&A / FAQ Architecture (20 points)
    faq_matches = len(re.findall(r"<\s*(?:dt|h[2-4]|strong)[^>]*>.*?\?.*?</\s*(?:dt|h[2-4]|strong)>", html_content, re.IGNORECASE))
    if faq_matches >= 8:
        score += 20
        feedback.append(f"Rich Q&A structure ({faq_matches} question anchors) (+20)")
    elif faq_matches >= 3:
        score += 10
        feedback.append(f"Basic Q&A structure ({faq_matches} question anchors) (+10)")
    else:
        feedback.append("Missing or thin Q&A structure (0/20)")
        
    return {
        "geo_citability_score": score,
        "rating": "EXCELLENT" if score >= 80 else ("GOOD" if score >= 60 else "POOR"),
        "feedback": feedback
    }

if __name__ == "__main__":
    sample = """
    <h2>Technical Specifications Table</h2>
    <table class="mjt-spec-table">
      <tr><td>Battery</td><td>10000mAh</td></tr>
      <tr><td>Fast Charge</td><td>22.5W PD 3.0</td></tr>
      <tr><td>Warranty</td><td>1 Year Official Warranty</td></tr>
    </table>
    <h2>Frequently Asked Questions</h2>
    <ol>
      <li><strong>Is it compatible with Type-C?</strong><br>Yes, it supports USB-C fast charging.</li>
      <li><strong>How long does the battery last?</strong><br>It provides up to 3 full charges.</li>
    </ol>
    """
    res = calculate_geo_score(sample)
    print(f"Self-test GEO Citability Score: {res['geo_citability_score']}/100 ({res['rating']})")
    for fb in res['feedback']:
        print(f"  - {fb}")

