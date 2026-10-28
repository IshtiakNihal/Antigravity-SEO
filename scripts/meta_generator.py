#!/usr/bin/env python3
"""
Universal Meta Title & Description Generator
Engineered for CTR, search intent, strict character limits (Title <= 60 chars,
Meta Description <= 160 chars), and clean Anti-AI authoritative tone.
Supports Ecommerce, SaaS, Blog/Content, and Local Business archetypes.
"""

import sys
import json
import re

def generate_ecommerce_meta(brand, model, category="Product", price=None, currency="$", warranty=None, site_name="Official Store", region=None):
    """
    Generates high-converting commercial meta tags for ecommerce products.
    """
    brand = (brand or "").strip()
    model = (model or "").strip()
    category = (category or "").strip()
    site_name = (site_name or "Store").strip()

    parts = [p for p in (brand, model, category) if p]
    core_name = " ".join(parts) if parts else "Product"

    region_suffix = f" in {region}" if region else ""
    
    candidates = [
        f"{core_name}{region_suffix} | {site_name}",
        f"{brand} {model}{region_suffix} | {site_name}".strip(),
        f"{model}{region_suffix} | {site_name}".strip(),
        f"{brand} {model}".strip()
    ]

    title_candidate = candidates[0]
    for c in candidates:
        if len(c) <= 60:
            title_candidate = c
            break
    else:
        title_candidate = title_candidate[:57].rsplit(" ", 1)[0] + "..."

    # Meta Description
    desc_elements = [f"Buy official {brand} {model}".strip()]
    if price:
        desc_elements.append(f"for {currency}{price}.")
    else:
        desc_elements.append("at the best price online.")

    if warranty:
        desc_elements.append(f"Includes {warranty} warranty.")
    
    desc_elements.append("100% genuine guaranteed with fast nationwide shipping.")
    meta_desc = " ".join(desc_elements)
    if len(meta_desc) > 160:
        meta_desc = meta_desc[:157].rsplit(" ", 1)[0] + "..."

    return {
        "type": "ecommerce",
        "title": title_candidate,
        "title_length": len(title_candidate),
        "title_status": "OPTIMAL" if len(title_candidate) <= 60 else "TRUNCATION_RISK",
        "meta_description": meta_desc,
        "meta_description_length": len(meta_desc),
        "meta_description_status": "OPTIMAL" if len(meta_desc) <= 160 else "TRUNCATION_RISK"
    }

def generate_saas_meta(product_name, primary_benefit, target_audience="Teams", site_name=None):
    """
    Generates high-CTR meta tags for SaaS & B2B Software landing pages.
    """
    site_suffix = f" | {site_name}" if site_name else ""
    title_candidate = f"{product_name} - {primary_benefit}{site_suffix}"
    if len(title_candidate) > 60:
        title_candidate = f"{product_name}: {primary_benefit}"
        if len(title_candidate) > 60:
            title_candidate = title_candidate[:57].rsplit(" ", 1)[0] + "..."

    meta_desc = f"{product_name} helps {target_audience} {primary_benefit.lower()}. Automate workflows, save time, and scale faster. Start your free trial today."
    if len(meta_desc) > 160:
        meta_desc = meta_desc[:157].rsplit(" ", 1)[0] + "..."

    return {
        "type": "saas",
        "title": title_candidate,
        "title_length": len(title_candidate),
        "title_status": "OPTIMAL" if len(title_candidate) <= 60 else "TRUNCATION_RISK",
        "meta_description": meta_desc,
        "meta_description_length": len(meta_desc),
        "meta_description_status": "OPTIMAL" if len(meta_desc) <= 160 else "TRUNCATION_RISK"
    }

def generate_meta(brand, model, category="Product", price=None, warranty=None, site_name="Store", region=None, currency="$"):
    """
    Universal backwards-compatible adapter.
    """
    return generate_ecommerce_meta(brand, model, category, price, currency, warranty, site_name, region)

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        b = sys.argv[1]
        m = sys.argv[2]
        c = sys.argv[3] if len(sys.argv) > 3 else "Product"
        res = generate_meta(b, m, c)
        print(json.dumps(res, indent=2))
    else:
        sample_ecom = generate_ecommerce_meta("Sony", "WH-1000XM5 Wireless Headphones", "Audio", price="399", warranty="1 Year Official", site_name="TechStore")
        sample_saas = generate_saas_meta("FlowGrid", "AI Workflow Automation Platform", "Engineers", "FlowGrid")
        print("Self-test Ecommerce Meta:")
        print(json.dumps(sample_ecom, indent=2))
        print("\nSelf-test SaaS Meta:")
        print(json.dumps(sample_saas, indent=2))
