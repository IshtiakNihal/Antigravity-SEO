#!/usr/bin/env python3
"""
Meta Title and Description Engineering Generator
Generates high-CTR, commercial title tags and meta descriptions optimized for
search intent, character limits (Title <= 60 chars, Meta Description <= 160 chars),
and clean Anti-AI commercial tone.
"""

import sys
import json
import re

def generate_meta(brand, model, category, price=None, warranty=None, site_name="MinjoTech BD"):
    """
    Generates optimized Title and Meta Description for an ecommerce product.
    """
    # 1. Clean inputs
    brand = (brand or "").strip()
    model = (model or "").strip()
    category = (category or "").strip()
    
    # Title construction
    # Preferred: "[Brand] [Model] [Category] Price in Bangladesh | [Site Name]"
    parts = []
    if brand:
        parts.append(brand)
    if model and model.lower() not in brand.lower():
        parts.append(model)
    if category and category.lower() not in model.lower():
        parts.append(category)
        
    core_name = " ".join(parts).strip()
    
    # Try combinations in order of preference to stay under 60 chars
    candidates = [
        f"{core_name} Price in Bangladesh | {site_name}",
        f"{brand} {model} Price in Bangladesh | {site_name}",
        f"{brand} {model} Price in BD | {site_name}",
        f"{brand} {model} Price in BD",
        f"{core_name} Price in BD"
    ]
    
    title_candidate = candidates[0]
    for c in candidates:
        if len(c) <= 60:
            title_candidate = c
            break
    else:
        # If still over 60, truncate safely
        if len(title_candidate) > 60:
            title_candidate = title_candidate[:57].rsplit(" ", 1)[0] + "..."
            
    # Meta Description construction
    # Template: "Buy official [Brand] [Model] in Bangladesh at ৳[Price]. [Specs/Features]. [Warranty] Official Warranty, 100% authentic, fast home delivery across BD."
    desc_parts = [f"Buy official {brand} {model}".strip()]
    if price:
        desc_parts.append(f"in Bangladesh at ৳{price}.")
    else:
        desc_parts.append("at the best price in Bangladesh.")
        
    if warranty:
        desc_parts.append(f"Includes {warranty} warranty,")
    else:
        desc_parts.append("Includes official warranty,")
        
    desc_parts.append("100% genuine guaranteed with fast delivery nationwide.")
    
    meta_desc = " ".join(desc_parts)
    if len(meta_desc) > 160:
        # Truncate safely at word boundary
        meta_desc = meta_desc[:157].rsplit(" ", 1)[0] + "..."
        
    return {
        "title": title_candidate,
        "title_length": len(title_candidate),
        "title_status": "OPTIMAL" if len(title_candidate) <= 60 else "TRUNCATION_RISK",
        "meta_description": meta_desc,
        "meta_description_length": len(meta_desc),
        "meta_description_status": "OPTIMAL" if len(meta_desc) <= 160 else "TRUNCATION_RISK"
    }

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        b = sys.argv[1]
        m = sys.argv[2]
        c = sys.argv[3] if len(sys.argv) > 3 else "Gadget"
        p = sys.argv[4] if len(sys.argv) > 4 else None
        w = sys.argv[5] if len(sys.argv) > 5 else None
        res = generate_meta(b, m, c, p, w)
        print(json.dumps(res, indent=2))
    else:
        sample = generate_meta(
            brand="QCY",
            model="Pulse PB10H 10000mAh",
            category="Power Bank",
            price="1950",
            warranty="1 Year Official",
            site_name="MinjoTech BD"
        )
        print("Self-test Meta Generation Result:")
        print(json.dumps(sample, indent=2))
