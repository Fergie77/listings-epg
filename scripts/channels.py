"""Writes the channel list for the grabber: every UK channel in iptv-org's sky.com list that has a guide id,
then any channel sky.com doesn't carry from the other lists given (mytelly.co.uk has ITVBe and Sky Max).

Usage: python3 scripts/channels.py epg/sites/sky.com/sky.com.channels.xml epg/sites/mytelly.co.uk/mytelly.co.uk.channels.xml > epg/uk.channels.xml
"""
import sys
import xml.etree.ElementTree as ET

seen_ids = set()
seen_channels = set()  # "ITVBe.uk": a channel already covered, whichever feed
out = ['<?xml version="1.0" encoding="UTF-8"?>', "<channels>"]
for index, path in enumerate(sys.argv[1:]):
    added = 0
    for channel in ET.parse(path).getroot().iter("channel"):
        site_id = channel.get("site_id", "")
        xmltv_id = channel.get("xmltv_id", "")
        if not xmltv_id or xmltv_id in seen_ids:
            continue
        base = xmltv_id.split("@")[0]
        if index == 0:
            # sky.com: UK and Ireland channels only, each guide id once (Sky lists some under two numbers).
            if not site_id.startswith("GB#"):
                continue
        elif not base.endswith(".uk") or base in seen_channels:
            # Later lists only fill in UK channels the first one doesn't have.
            continue
        seen_ids.add(xmltv_id)
        seen_channels.add(base)
        channel.tail = None
        out.append("  " + ET.tostring(channel, encoding="unicode").strip())
        added += 1
    print(f"{path}: {added} channels", file=sys.stderr)
out.append("</channels>")
print("\n".join(out))
