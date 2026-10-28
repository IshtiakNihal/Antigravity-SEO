#!/usr/bin/env python3
"""
Unit Test Suite for Antigravity SEO Framework
Uses standard unittest library for zero-dependency execution.
"""

import os
import sys
import unittest

# Ensure scripts directory is in sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

from catalog_audit import audit_product
from geo_scorer import calculate_geo_score
from schema_validate import validate_product_schema
from sitemap_checker import parse_sitemap_xml
from meta_generator import generate_ecommerce_meta, generate_saas_meta
from url_safety import is_safe_url


class TestAntigravitySEO(unittest.TestCase):

    def test_catalog_audit_valid(self):
        product = {
            "id": 101,
            "name": "Wireless Noise Cancelling Headphones",
            "sku": "SKU-101",
            "price": 249.99,
            "brands": ["Sony"],
            "images": [{"id": 1, "alt": "Headphones"}]
        }
        res = audit_product(product)
        self.assertEqual(res["status"], "PASS")
        self.assertEqual(len(res["issues"]), 0)

    def test_catalog_audit_zero_price_and_missing_sku(self):
        product = {
            "id": 102,
            "name": "Defective Item",
            "sku": "",
            "price": 0,
            "brands": [],
            "images": []
        }
        res = audit_product(product)
        self.assertEqual(res["status"], "FAIL")
        self.assertTrue(any("Price is 0" in i for i in res["issues"]))
        self.assertTrue(any("SKU is empty" in i for i in res["issues"]))
        self.assertTrue(any("No images" in i for i in res["issues"]))

    def test_catalog_audit_keyword_stuffing_warning(self):
        product = {
            "id": 103,
            "name": "Running Shoes Buy Online Free Shipping",
            "sku": "SHOE-01",
            "price": 89,
            "brands": ["Nike"],
            "images": [{"id": 1, "alt": "Shoes"}]
        }
        res = audit_product(product)
        self.assertTrue(any("Commercial keyword stuffed" in w for w in res["warnings"]))

    def test_geo_scorer_high_citability(self):
        html = """
        <h2>Technical Specifications</h2>
        <table class="spec-table">
          <tr><td>Battery Capacity</td><td>10000mAh</td></tr>
          <tr><td>Fast Charging</td><td>22.5W PD 3.0</td></tr>
          <tr><td>Bluetooth Version</td><td>Bluetooth 5.4</td></tr>
          <tr><td>Noise Cancellation</td><td>ANC 43dB</td></tr>
          <tr><td>Weight</td><td>185g</td></tr>
          <tr><td>Warranty</td><td>12 Months Official Warranty</td></tr>
        </table>
        <h3>Frequently Asked Questions</h3>
        <ol>
          <li><strong>Is it compatible with Type-C?</strong> Yes, full USB-C fast charging support.</li>
          <li><strong>Does it include warranty?</strong> Yes, 12 Months Official Warranty is included.</li>
          <li><strong>What is the battery capacity?</strong> 10000mAh high-density polymer.</li>
        </ol>
        """
        res = calculate_geo_score(html)
        self.assertGreaterEqual(res["geo_citability_score"], 70)
        self.assertIn(res["rating"], ["GOOD", "EXCELLENT"])

    def test_geo_scorer_detects_fluff(self):
        html = """
        <p>In today's fast-paced world, delve into a revolutionary game-changer that is a testament to innovation.</p>
        """
        res = calculate_geo_score(html)
        self.assertLess(res["geo_citability_score"], 40)
        self.assertTrue(any("AI clichés detected" in fb for fb in res["feedback"]))

    def test_schema_validate_valid(self):
        valid_schema = {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": "Sony WH-1000XM5 Headphones",
            "image": "https://example.com/xm5.webp",
            "description": "Industry-leading noise cancelling wireless headphones.",
            "offers": {
                "@type": "Offer",
                "price": "399.99",
                "priceCurrency": "USD",
                "availability": "https://schema.org/InStock"
            }
        }
        res = validate_product_schema(valid_schema)
        self.assertTrue(res["valid"])
        self.assertEqual(len(res["errors"]), 0)

    def test_schema_validate_missing_price(self):
        invalid_schema = {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": "Incomplete Product",
            "offers": {}
        }
        res = validate_product_schema(invalid_schema)
        self.assertFalse(res["valid"])
        self.assertTrue(any("Missing required offer field: 'price'" in err for err in res["errors"]))

    def test_sitemap_index_parsing(self):
        sample_index = """<?xml version="1.0" encoding="UTF-8"?>
        <sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
            <sitemap>
                <loc>https://example.com/product-sitemap.xml</loc>
                <lastmod>2026-10-28T14:00:00+00:00</lastmod>
            </sitemap>
        </sitemapindex>"""
        parsed = parse_sitemap_xml(sample_index)
        self.assertEqual(parsed["type"], "index")
        self.assertEqual(parsed["count"], 1)
        self.assertEqual(parsed["entries"][0]["loc"], "https://example.com/product-sitemap.xml")

    def test_meta_generator_ecommerce(self):
        meta = generate_ecommerce_meta(
            brand="Anker",
            model="Prime 250W Power Bank",
            category="Charging",
            price="179.99",
            currency="$",
            warranty="24 Months",
            site_name="TechHQ"
        )
        self.assertEqual(meta["title_status"], "OPTIMAL")
        self.assertEqual(meta["meta_description_status"], "OPTIMAL")
        self.assertIn("Anker", meta["title"])
        self.assertIn("$179.99", meta["meta_description"])
        self.assertIn("24 Months", meta["meta_description"])

    def test_meta_generator_saas(self):
        meta = generate_saas_meta(
            product_name="FlowGrid",
            primary_benefit="AI Agentic Workflow Orchestration",
            target_audience="Developers",
            site_name="FlowGrid"
        )
        self.assertEqual(meta["title_status"], "OPTIMAL")
        self.assertEqual(meta["meta_description_status"], "OPTIMAL")
        self.assertIn("FlowGrid", meta["title"])
        self.assertIn("free trial", meta["meta_description"])

    def test_url_safety_blocks_ssrf(self):
        safe, _ = is_safe_url("http://127.0.0.1:8080/metrics")
        self.assertFalse(safe)

        safe, _ = is_safe_url("http://169.254.169.254/latest/meta-data/")
        self.assertFalse(safe)

        safe, _ = is_safe_url("http://localhost/admin")
        self.assertFalse(safe)

        safe, _ = is_safe_url("ftp://ftp.example.com")
        self.assertFalse(safe)


if __name__ == "__main__":
    unittest.main()
