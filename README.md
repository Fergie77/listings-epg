# The Listings: TV guide

Builds a UK TV guide (XMLTV) twice a day from sky.com (and mytelly.co.uk for the few channels sky.com lacks), using the [iptv-org/epg](https://github.com/iptv-org/epg) grabber, and publishes it with GitHub Pages for The Listings app:

- https://fergie77.github.io/listings-epg/guide.xml.gz
- https://fergie77.github.io/listings-epg/guide.xml

The channel list is every UK channel in iptv-org's sky.com list (`scripts/channels.py`). To run it now, use **Actions → Grab the guide → Run workflow**.
