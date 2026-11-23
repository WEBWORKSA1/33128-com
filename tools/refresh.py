# -*- coding: utf-8 -*-
"""Daily refresh: rebuilds pages (dates, sitemap lastmod) and rotates the tip of the day."""
import json, datetime, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TIPS = [
 "Arrive 45 minutes early — security lines peak between 8:15 and 9:15 a.m.",
 "Take Metrorail to Government Center; the free Metromover Inner Loop stops at the federal courthouse.",
 "Clerks can explain procedures but can't give legal advice — ask an attorney for strategy.",
 "Bring three copies of every document: one for the judge, one for the other side, one for you.",
 "Florida small claims covers disputes of $8,000 or less, excluding costs, interest and attorney's fees.",
 "In a Florida eviction for unpaid rent, tenants generally must deposit rent into the court registry to raise defenses.",
 "To use Florida PIP benefits after a crash, get initial medical treatment within 14 days.",
 "Whoever holds an original will must deposit it with the clerk within 10 days of learning of the death.",
 "Courtrooms are cold — bring a sweater, especially for jury duty.",
 "Verify any Florida lawyer with The Florida Bar's member search before hiring.",
 "Missing a court date can lead to a default judgment or a warrant — calendar every date the day you get it.",
 "Request interpreters and ADA accommodations well before your hearing date.",
]
today = datetime.date.today()
status = {"updated": datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ"),
          "tip": TIPS[today.toordinal() % len(TIPS)]}
os.makedirs(os.path.join(ROOT, "assets/data"), exist_ok=True)
with open(os.path.join(ROOT, "assets/data/status.json"), "w") as f: json.dump(status, f, indent=1)
subprocess.check_call([sys.executable, os.path.join(ROOT, "tools/build.py")], cwd=os.path.join(ROOT, "tools"))
print("refreshed", status)
