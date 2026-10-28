#!/usr/bin/env python3
"""
URL Safety & SSRF Mitigation Engine
Validates user-supplied and page-derived URLs to block private, loopback,
link-local, cloud metadata, and multicast addresses.
"""

import sys
import socket
import ipaddress
import urllib.parse

BLOCKED_IP_NETWORKS = [
    ipaddress.ip_network("0.0.0.0/8"),
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("127.0.0.0/8"),
    ipaddress.ip_network("169.254.0.0/16"),       # Link-local & AWS/GCP/Azure metadata (169.254.169.254)
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16"),
    ipaddress.ip_network("224.0.0.0/4"),          # Multicast
    ipaddress.ip_network("240.0.0.0/4"),          # Reserved
    ipaddress.ip_network("::1/128"),              # IPv6 loopback
    ipaddress.ip_network("fc00::/7"),             # IPv6 Unique Local
    ipaddress.ip_network("fe80::/10"),            # IPv6 Link-local
]

def is_safe_url(url_string):
    """
    Validates a URL against protocol and network security boundaries.
    Returns (is_safe: bool, reason: str).
    """
    if not url_string or not isinstance(url_string, str):
        return False, "Empty or invalid URL"

    try:
        parsed = urllib.parse.urlparse(url_string.strip())
    except Exception as e:
        return False, f"URL parse failure: {str(e)}"

    scheme = (parsed.scheme or "").lower()
    if scheme not in ("http", "https"):
        return False, f"Disallowed scheme: '{scheme}'. Only HTTP and HTTPS are permitted."

    hostname = (parsed.hostname or "").strip().rstrip(".")
    if not hostname:
        return False, "Missing hostname in URL"

    # Explicit localhost check
    if hostname.lower() in ("localhost", "ip6-localhost", "ip6-loopback"):
        return False, "Localhost access is strictly prohibited"

    # DNS resolution check
    try:
        addr_info = socket.getaddrinfo(hostname, None)
    except socket.gaierror:
        return False, f"DNS resolution failed for host: '{hostname}'"

    for entry in addr_info:
        ip_str = entry[4][0]
        try:
            ip_obj = ipaddress.ip_address(ip_str)
        except ValueError:
            return False, f"Invalid resolved IP format: {ip_str}"

        for blocked_net in BLOCKED_IP_NETWORKS:
            if ip_obj in blocked_net:
                return False, f"Access blocked to private/internal IP: {ip_str}"

    return True, "URL is safe"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        safe, reason = is_safe_url(target)
        print(f"URL: {target}")
        print(f"Safe: {safe}")
        print(f"Reason: {reason}")
        sys.exit(0 if safe else 1)
    else:
        test_cases = [
            ("https://google.com", True),
            ("https://example.com/blog/article", True),
            ("http://127.0.0.1:8080/admin", False),
            ("http://localhost/secret", False),
            ("http://169.254.169.254/latest/meta-data/", False),
            ("ftp://ftp.example.com", False)
        ]
        for url, expected in test_cases:
            safe, reason = is_safe_url(url)
            assert safe == expected, f"Failed for {url}: got {safe}, expected {expected} ({reason})"
        print("All self-test cases passed successfully!")

