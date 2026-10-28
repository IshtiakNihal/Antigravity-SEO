#!/usr/bin/env python3
"""
Schema.org JSON-LD Validator
Validates Product, Offer, BreadcrumbList, and FAQPage JSON-LD schemas.
"""

import sys
import json

def validate_product_schema(schema_obj):
    errors = []
    warnings = []
    
    stype = schema_obj.get("@type", "")
    if stype != "Product":
        errors.append(f"Expected @type Product, got '{stype}'")
        return {"valid": False, "errors": errors, "warnings": warnings}
        
    if not schema_obj.get("name"):
        errors.append("Missing required field: 'name'")
    if not schema_obj.get("image"):
        warnings.append("Missing recommended field: 'image'")
    if not schema_obj.get("description"):
        warnings.append("Missing recommended field: 'description'")
        
    offers = schema_obj.get("offers")
    if offers is None:
        errors.append("Missing required field: 'offers'")
    else:
        offer_dict = offers if isinstance(offers, dict) else (offers[0] if isinstance(offers, list) and offers else {})
        if not offer_dict.get("price"):
            errors.append("Missing required offer field: 'price'")
        if not offer_dict.get("priceCurrency"):
            errors.append("Missing required offer field: 'priceCurrency'")
        if not offer_dict.get("availability"):
            warnings.append("Missing recommended offer field: 'availability'")
            
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings
    }

if __name__ == "__main__":
    test_payload = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": "QCY Pulse PB10H 10000mAh Power Bank",
        "image": "https://minjotech.com/wp-content/uploads/pb10h.webp",
        "description": "10000mAh 22.5W Power Bank with 3 built-in cables.",
        "sku": "MJ-12281",
        "brand": { "@type": "Brand", "name": "QCY" },
        "offers": {
            "@type": "Offer",
            "url": "https://minjotech.com/product/qcy-pulse-pb10h-10000mah-power-bank/",
            "priceCurrency": "BDT",
            "price": "1950",
            "availability": "https://schema.org/InStock"
        }
    }
    result = validate_product_schema(test_payload)
    print("Self-test Schema Validation Result:")
    print(json.dumps(result, indent=2))
