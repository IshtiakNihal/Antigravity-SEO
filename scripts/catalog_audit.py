#!/usr/bin/env python3
"""
Catalog Integrity Auditor
Checks an ecommerce catalog for ৳0/empty prices, missing SKUs, and keyword-stuffed titles.
"""

import sys
import json
import re

def audit_product(product):
    issues = []
    warnings = []
    
    # 1. Price check
    price_val = product.get("price", 0)
    try:
        price_num = float(price_val) if price_val else 0.0
    except (ValueError, TypeError):
        price_num = 0.0
        
    if price_num <= 0:
        issues.append("CRITICAL: Price is 0 or missing")
        
    # 2. SKU check
    sku = product.get("sku", "")
    if not sku or not str(sku).strip():
        issues.append("CRITICAL: SKU is empty")
        
    # 3. Title check
    name = product.get("name", "")
    if "price in bangladesh" in name.lower() or "price in bd" in name.lower():
        warnings.append("WARNING: Keyword stuffed into product title (use SEO title tag instead)")
        
    # 4. Brand check
    brands = product.get("brands", [])
    if not brands:
        warnings.append("WARNING: No brand assigned")
        
    # 5. Image check
    images = product.get("images", [])
    if not images:
        issues.append("CRITICAL: No images uploaded")
        
    return {
        "id": product.get("id"),
        "name": name,
        "sku": sku,
        "price": price_num,
        "status": "PASS" if not issues else "FAIL",
        "issues": issues,
        "warnings": warnings
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            data = json.load(f)
            items = data if isinstance(data, list) else [data]
            results = [audit_product(p) for p in items]
            print(json.dumps(results, indent=2))
    else:
        sample = {
            "id": 12469,
            "name": "Sample Turbo Fan",
            "sku": "MJ-12469",
            "price": 1200,
            "brands": ["Weidasi"],
            "images": [{"id": 1, "alt": "Turbo Fan"}]
        }
        res = audit_product(sample)
        print("Self-test result:")
        print(json.dumps(res, indent=2))
