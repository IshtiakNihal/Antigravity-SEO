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
from meta_generator import generate_meta


class TestAntigravitySEO(unittest.TestCase):

    def test_catalog_audit_valid(self):
        product = {
            "id": 101,
            "name": "QCY Crossky C30 Earphones",
            "sku": "MJ-101",
            "price": 2850,
            "brands": ["QCY"],
            "images": [{"id": 1, "alt": "QCY C30"}]
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
        <h3>FAQ</h3>
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
            "name": "QCY Pulse PB10H Power Bank",
            "image": "https://example.com/pb10h.webp",
            "description": "10000mAh 22.5W Power Bank with 3 built-in cables.",
            "offers": {
                "@type": "Offer",
                "price": "1950",
                "priceCurrency": "BDT",
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
                <loc>https://minjotech.com/product-sitemap1.xml</loc>
                <lastmod>2026-10-28T14:00:00+00:00</lastmod>
            </sitemap>
        </sitemapindex>"""
        parsed = parse_sitemap_xml(sample_index)
        self.assertEqual(parsed["type"], "index")
        self.assertEqual(parsed["count"], 1)
        self.assertEqual(parsed["entries"][0]["loc"], "https://minjotech.com/product-sitemap1.xml")

    def test_meta_generator(self):
        meta = generate_meta(
            brand="LDNIO",
            model="Q17 100W GaN Desktop Charger",
            category="Charger",
            price="3990",
            warranty="12 Months Official",
            site_name="MinjoTech BD"
        )
        self.assertEqual(meta["title_status"], "OPTIMAL")
        self.assertEqual(meta["meta_description_status"], "OPTIMAL")
        self.assertTrue("Price in Bangladesh" in meta["title"] or "Price in BD" in meta["title"])
        self.assertIn("3990", meta["meta_description"])
        self.assertIn("12 Months Official", meta["meta_description"])


if __name__ == "__main__":
    unittest.main()
