---
name: seo-schema
description: Schema.org structured data engineering skill. Generates and validates JSON-LD markup for Product, Offer, BreadcrumbList, FAQPage, ItemPage, and Organization.
---

# Schema.org Structured Data Engineering

Generates and validates Google-compliant JSON-LD structured data.

## Standard Product Schema Payload
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "[Product Name]",
  "image": "[Primary Image URL]",
  "description": "[Meta Description]",
  "sku": "[Unique SKU]",
  "brand": {
    "@type": "Brand",
    "name": "[Brand Name]"
  },
  "offers": {
    "@type": "Offer",
    "url": "[Product Permalink]",
    "priceCurrency": "BDT",
    "price": "[Approved Price]",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition"
  }
}
```
