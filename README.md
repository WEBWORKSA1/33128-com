# 33128.com — Miami Courthouse District Guide

A static, AdSense-ready website that is also a legal lead-generation site, hosted on **GitHub Pages (main branch, root)**.

- `tools/build.py` generates every HTML page. Guide content lives in `tools/guides.py`.
- `tools/refresh.py` runs daily via `.github/workflows/auto-refresh.yml`. It rebuilds the pages, updates sitemap dates and rotates the tip of the day.
- `assets/js/config.js` holds AdSense manual slot IDs and donation payment links.
- `RESEARCH.md` covers the meaning of 33128, the concept decision and the 25-site benchmark.
- `PROMPTS.md` contains the phase-wise build prompts.

Edit content in `tools/`, then run `python3 tools/refresh.py`.

**Custom domain:** point 33128.com DNS at GitHub Pages (four A records 185.199.108–111.153, plus `www` CNAME → webworksa1.github.io), then set the custom domain under Settings → Pages.

© 33128.com. "33128" is used descriptively as a U.S. ZIP code; see `disclaimer.html`.
