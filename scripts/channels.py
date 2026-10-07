"""Writes the channel list for the grabber: every UK channel in iptv-org's sky.com list that has a guide id.

Usage: python3 scripts/channels.py epg/sites/sky.com/sky.com.channels.xml > epg/uk.channels.xml
"""
import sys
import xml.etree.ElementTree as ET

tree = ET.parse(sys.argv[1])
seen = set()
out = ['<?xml version="1.0" encoding="UTF-8"?>', "<channels>"]
for channel in tree.getroot().iter("channel"):
    site_id = channel.get("site_id", "")
    xmltv_id = channel.get("xmltv_id", "")
    # UK and Ireland channels only, each guide id once (Sky lists some channels under two numbers).
    if not site_id.startswith("GB#") or not xmltv_id or xmltv_id in seen:
        continue
    seen.add(xmltv_id)
    channel.tail = None
    out.append("  " + ET.tostring(channel, encoding="unicode").strip())
out.append("</channels>")
print("\n".join(out))
print(f"{len(seen)} channels", file=sys.stderr)
