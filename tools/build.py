# -*- coding: utf-8 -*-
"""Static site generator for 33128.com. Run: python3 tools/build.py  (writes HTML into repo root)."""
import os, json, datetime, html
from guides import GUIDES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://33128.com"
INTEREST_URL = "https://web.works/contact"
TODAY = datetime.date.today().isoformat()

NAV = [("index.html", "Home"), ("courthouses.html", "Courthouses"), ("guides/index.html", "Guides"),
       ("tools.html", "Tools"), ("videos.html", "Videos"), ("downtown.html", "Downtown 33128"), ("support.html", "Support")]

def head(title, desc, path, pre, extra_ld=None, ogtype="website"):
    url = DOMAIN + "/" + path.replace("index.html", "")
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": "33128.com", "url": DOMAIN + "/",
           "description": "Independent guide to Miami's 33128 courthouse district."}]
    if extra_ld: ld.append(extra_ld)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#0b1f3a">
<meta property="og:type" content="{ogtype}"><meta property="og:site_name" content="33128.com">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{DOMAIN}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{pre}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{pre}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,800&family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/css/style.css">
<script>try{{if(localStorage.getItem("consent")==="essential"){{(window.adsbygoogle=window.adsbygoogle||[]).requestNonPersonalizedAds=1}}}}catch(e){{}}</script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>
<script src="{pre}assets/js/config.js"></script>
<script type="application/ld+json">{json.dumps(ld if len(ld) > 1 else ld[0])}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

def header(pre):
    links = "".join(f'<a href="{pre}{h}">{t}</a>' for h, t in NAV)
    return f"""<div class="interest"><a href="{INTEREST_URL}" target="_blank" rel="noopener"><span class="u">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership</span><span class="pill">Contact →</span></a></div>
<header class="site-head"><div class="wrap head-in">
<a class="brand" href="{pre}index.html" aria-label="33128.com home"><span><span class="mark">33<b>128</b></span><small>Courthouse District Guide</small></span></a>
<nav class="nav" aria-label="Main">{links}<a class="cta" href="{pre}free-case-review.html">Free Case Review</a></nav>
<div style="display:flex;gap:8px"><button class="icon-btn" data-theme-toggle aria-label="Toggle dark mode">◐</button><button class="icon-btn menu-btn" aria-label="Menu" aria-expanded="false">☰</button></div>
</div></header>
<main id="main">
"""

def footer(pre):
    g = "".join(f'<a href="{pre}guides/{x["slug"]}.html">{x["title"].split(":")[0]}</a>' for x in GUIDES[:6])
    return f"""</main>
<footer class="site-foot"><div class="wrap">
<div class="foot-grid">
<div><div class="brand"><span class="mark" style="color:#fff">33<b>128</b></span></div>
<p style="margin-top:10px">An independent, plain-English guide to Miami's 33128 courthouse district — the courts, the paperwork and the people who can help.</p>
<p><a href="{pre}free-case-review.html" class="btn btn-primary" style="display:inline-flex;color:#fff">Free Case Review</a></p>
<small data-updated></small></div>
<div><h4>Explore</h4><a href="{pre}courthouses.html">Courthouse directory</a><a href="{pre}guides/index.html">All guides</a><a href="{pre}tools.html">Free tools</a><a href="{pre}videos.html">Video library</a><a href="{pre}downtown.html">Downtown 33128</a><a href="{pre}about.html">About 33128</a></div>
<div><h4>Popular guides</h4>{g}</div>
<div><h4>Get involved</h4><a href="{pre}for-attorneys.html">For attorneys</a><a href="{pre}support.html#donate">Donate</a><a href="{pre}support.html#sponsor">Sponsor / Advertise</a><a href="{pre}contests.html">Contests &amp; prizes</a><a href="{pre}careers.html">Careers &amp; talent</a><a href="{pre}contact.html">Contact</a><a href="{INTEREST_URL}" target="_blank" rel="noopener">Buy / partner on this domain</a></div>
</div>
<div class="foot-legal">
<p><strong>Not legal advice.</strong> 33128.com is an independent information resource. It is not a law firm, not a lawyer referral service regulated by The Florida Bar, and is not affiliated with, endorsed by or operated by any court, clerk, government agency or the U.S. Postal Service. Submitting a form does not create an attorney–client relationship. Always confirm addresses, hours and deadlines with official sources.</p>
<p>© <span data-year></span> 33128.com · <a style="display:inline" href="{pre}privacy.html">Privacy</a> · <a style="display:inline" href="{pre}terms.html">Terms</a> · <a style="display:inline" href="{pre}disclaimer.html">Disclaimer &amp; Trademark Notice</a> · <a style="display:inline" href="{pre}sitemap.xml">Sitemap</a></p>
</div></div></footer>
<a class="btn btn-primary float-cta" href="{pre}free-case-review.html">⚖ Free case review</a>
<button class="icon-btn to-top" aria-label="Back to top" style="background:var(--card)">↑</button>
<div class="cookie" role="dialog" aria-label="Cookie notice"><strong>Cookies &amp; ads.</strong> We use cookies for essential functions and to show ads from Google, which may use cookies to personalize ads. <a href="{pre}privacy.html#cookies">Learn more</a>.
<div class="acts"><button class="btn btn-teal" data-consent="all">Accept all</button><button class="btn btn-ghost" data-consent="essential">Essential only</button></div></div>
<script src="{pre}assets/js/main.js" defer></script>
</body></html>
"""

def ad(slot): return f'<div class="ad-slot wrap" data-slot="{slot}"></div>'

def page_hero(title, sub, crumbs, pre):
    c = " › ".join([f'<a href="{pre}index.html">Home</a>'] + crumbs)
    return f'<section class="page-hero"><div class="wrap"><div class="crumbs">{c}</div><h1>{title}</h1><p>{sub}</p></div></section>'

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f: f.write(content)

def page(path, title, desc, body, extra_ld=None, ogtype="website"):
    pre = "../" * path.count("/")
    write(path, head(title, desc, path, pre, extra_ld, ogtype) + header(pre) + body(pre) + footer(pre))

# ---------------------------------------------------------------- shared blocks
ISSUES = [("injury", "🚗", "Accident / injury"), ("family", "👪", "Divorce / custody"), ("criminal", "🛡", "Criminal / DUI"),
          ("bankruptcy", "💳", "Debt / bankruptcy"), ("housing", "🏠", "Eviction / landlord–tenant"), ("probate", "📜", "Wills / probate"),
          ("real-estate", "🏢", "Real estate / deeds"), ("traffic", "🚦", "Traffic ticket"), ("employment", "💼", "Work / employment"),
          ("civil", "⚖", "Contract / small claims"), ("business", "📈", "Business / LLC"), ("other", "❓", "Something else")]

def lead_form(pre, compact=False):
    choices = "".join(f'<label><input type="radio" name="issue" value="{v}" required> {i} {t}</label>' for v, i, t in ISSUES)
    return f"""<form class="form-card" data-form="case-review" data-multistep data-subject="Free case review lead" data-ok="Thank you! Your case summary was received. A team member will review it and you can expect a response within one business day. If you are facing a deadline today, call the court clerk as well.">
<div class="steps-bar" aria-hidden="true"><span></span><span></span><span></span></div>
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="step"><h3>1 · What do you need help with?</h3><div class="choice-grid">{choices}</div>
<div class="step-nav"><span></span><button class="btn btn-primary" data-next>Next →</button></div></div>
<div class="step"><h3>2 · A few quick details</h3>
<div class="row"><div class="field"><label for="urg">How urgent is it?</label><select id="urg" name="urgency" required><option value="">Choose…</option><option>Court date or deadline within 7 days</option><option>Within 30 days</option><option>No deadline yet</option><option>Just researching</option></select></div>
<div class="field"><label for="cty">County</label><select id="cty" name="county" required><option value="">Choose…</option><option>Miami-Dade</option><option>Broward</option><option>Palm Beach</option><option>Monroe</option><option>Other Florida county</option><option>Outside Florida</option></select></div></div>
<div class="row"><div class="field"><label for="hasl">Do you already have a lawyer?</label><select id="hasl" name="has_lawyer" required><option value="">Choose…</option><option>No</option><option>Yes, looking for a second opinion</option></select></div>
<div class="field"><label for="lang">Preferred language</label><select id="lang" name="language"><option>English</option><option>Español</option><option>Kreyòl ayisyen</option><option>Português</option><option>Other</option></select></div></div>
<div class="field"><label for="desc">Briefly describe what happened</label><textarea id="desc" name="description" rows="4" required minlength="20" placeholder="Dates, what happened, what you'd like to achieve. Avoid sharing sensitive ID or account numbers."></textarea></div>
<div class="step-nav"><button class="btn btn-ghost" data-prev>← Back</button><button class="btn btn-primary" data-next>Next →</button></div></div>
<div class="step"><h3>3 · Where should we reach you?</h3>
<div class="row"><div class="field"><label for="nm">Full name</label><input id="nm" name="name" required autocomplete="name"></div>
<div class="field"><label for="ph">Phone</label><input id="ph" name="phone" type="tel" required autocomplete="tel" pattern="[0-9+()\\-\\s.]{{7,}}"></div></div>
<div class="row"><div class="field"><label for="em">Email</label><input id="em" name="email" type="email" required autocomplete="email"></div>
<div class="field"><label for="bt">Best time to contact</label><select id="bt" name="best_time"><option>Any time</option><option>Morning</option><option>Afternoon</option><option>Evening</option></select></div></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree that 33128.com may share my submission with one or more independent attorneys or legal-service providers who may contact me by phone, text or email about my inquiry. Consent is not a condition of any purchase. I understand this is not legal advice and does not create an attorney–client relationship.</label>
<div class="step-nav"><button class="btn btn-ghost" data-prev>← Back</button><button class="btn btn-primary" type="submit">Get my free review</button></div>
<p style="font-size:.8rem;color:var(--muted);margin-top:10px">🔒 Sent securely. We never sell your information to data brokers.</p></div>
<div class="form-msg" role="status"></div></form>"""

def simple_form(name, subject, fields, button, ok=None):
    f = "".join(fields)
    okattr = f' data-ok="{ok}"' if ok else ""
    return f"""<form class="form-card" data-form="{name}" data-subject="{subject}"{okattr}><input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">{f}<button class="btn btn-primary btn-block" type="submit">{button}</button><div class="form-msg" role="status"></div></form>"""

def fld(label, name, typ="text", req=True, opts=None, rows=None, ph=""):
    rid = "f_" + name
    r = " required" if req else ""
    if opts: inp = f'<select id="{rid}" name="{name}"{r}><option value="">Choose…</option>' + "".join(f"<option>{o}</option>" for o in opts) + "</select>"
    elif rows: inp = f'<textarea id="{rid}" name="{name}" rows="{rows}"{r} placeholder="{ph}"></textarea>'
    else: inp = f'<input id="{rid}" name="{name}" type="{typ}"{r} placeholder="{ph}">'
    return f'<div class="field"><label for="{rid}">{label}</label>{inp}</div>'

def row(*x): return '<div class="row">' + "".join(x) + "</div>"

def newsletter(pre):
    return f"""<div class="news reveal"><div><h3>The 33128 Brief</h3><p style="margin:0;color:#cfdaee">One email a month: court changes, new guides, deadline reminders. No spam.</p></div>
<form data-form="newsletter" data-subject="Newsletter signup" data-ok="You're subscribed — welcome to The 33128 Brief."><input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off"><label class="sr" for="nl">Email</label><input id="nl" type="email" name="email" placeholder="you@email.com" required><button class="btn btn-primary" type="submit">Subscribe</button><div class="form-msg" role="status" style="flex-basis:100%"></div></form></div>"""

COURTS = [
 ("Wilkie D. Ferguson, Jr. U.S. Courthouse", "400 N. Miami Avenue", "33128", "federal jury", "🏛", ["U.S. District Court, Southern District of Florida (headquarters)", "Federal civil and criminal cases", "Federal jury service for the Miami division", "U.S. Probation Office"], "(305) 523-5100", "https://www.flsd.uscourts.gov/"),
 ("C. Clyde Atkins U.S. Courthouse", "301 N. Miami Avenue", "33128", "federal bankruptcy", "🏛", ["U.S. Bankruptcy Court, Southern District of Florida (headquarters)", "Federal district court functions"], "(305) 523-5100", "https://www.flsb.uscourts.gov/"),
 ("Lawson E. Thomas Courthouse Center", "175 NW 1st Avenue", "33128", "county family probate", "⚖", ["Family Court Division (divorce, paternity, support)", "Domestic-violence filings — mezzanine", "Probate & Mental Health — 14th floor (new filings, wills for deposit, certified copies)"], "305-275-1155", "https://www.miamidadeclerk.gov/"),
 ("Miami-Dade County Courthouse East", "22 NW 1st Street", "33128", "county records", "📁", ["County Recorder's Office — 1st floor", "Deeds, mortgages, liens and other official records"], "305-275-1155", "https://www.miamidadeclerk.gov/"),
 ("Osvaldo N. Soto Miami-Dade Justice Center", "20 NW 1st Avenue", "33128", "county criminal", "⚖", ["County court proceedings including pretrial and special sets"], "305-275-1155", "https://www.miamidadeclerk.gov/"),
 ("Miami-Dade Children's Courthouse", "155 NW 3rd Street", "33128", "county family", "🧒", ["Juvenile delinquency and dependency matters", "Clerk office — Suite 3318"], "305-275-1155", "https://www.miamidadeclerk.gov/"),
 ("Stephen P. Clark Government Center", "111 NW 1st Street", "33128", "county government", "🏢", ["Miami-Dade County administration and commission chambers", "Clerk services location", "Government Center Metrorail/Metromover station below"], "311 (county services)", "https://www.miamidade.gov/"),
 ("Miami-Dade County Courthouse (historic)", "73 W. Flagler Street", "33130 · nearby", "county civil", "🏛", ["Circuit & County civil — new suits filed in Room 137", "Court registry deposits — Room 138", "Certified copies & file requests — Room 133"], "305-275-1155", "https://www.miamidadeclerk.gov/"),
 ("Richard E. Gerstein Justice Building", "1351 NW 12th Street", "33125 · nearby", "county criminal", "⚖", ["State criminal cases", "Certain traffic and misdemeanor matters"], "305-275-1155", "https://www.miamidadeclerk.gov/"),
 ("James Lawrence King Federal Justice Building", "99 NE 4th Street", "33132 · nearby", "federal", "🏛", ["Federal justice offices in the Miami courthouse complex"], "(305) 523-5100", "https://www.flsd.uscourts.gov/"),
]

def court_cards():
    out = []
    for n, a, z, tags, ico, svcs, ph, url in COURTS:
        li = "".join(f"<li>{s}</li>" for s in svcs)
        q = (a + " Miami FL " + z.split(" ")[0]).replace(" ", "+")
        out.append(f"""<article class="card court reveal" data-tags="{tags}"><div class="ico">{ico}</div><h3>{n}</h3>
<div class="addr">{a}, Miami, FL <span class="zip">{z}</span></div><ul>{li}</ul>
<p style="margin-top:10px;font-size:.9rem">📞 {ph} · <a href="https://www.google.com/maps/search/?api=1&query={q}" target="_blank" rel="noopener">Map</a> · <a href="{url}" target="_blank" rel="noopener">Official site ↗</a></p></article>""")
    return "".join(out)

VIDEOS = [("grnUvCNAfGA", "Jury Service Overview", "U.S. Courts — what to expect if you're called for jury duty (3:33)."),
          ("iKpiwpajm6I", "Court Shorts: Jury Service", "U.S. Courts — federal judges explain the role of the jury.")]
TOPIC_SEARCH = [("Florida small claims court explained", "Small claims"), ("Florida eviction process tenant rights", "Eviction"),
                ("Chapter 7 vs Chapter 13 bankruptcy explained", "Bankruptcy"), ("Florida probate process explained", "Probate"),
                ("what to do after a car accident Florida PIP", "Car accidents"), ("how to represent yourself in court Florida", "Self-help"),
                ("Downtown Miami history walking tour", "Downtown Miami"), ("Miami Metromover ride Government Center", "Getting around")]

def video_cards(n=None):
    v = VIDEOS if n is None else VIDEOS[:n]
    return "".join(f'<div class="card reveal" style="padding:14px"><div class="yt" data-id="{i}" data-title="{t}"></div><h3 style="margin-top:12px">{t}</h3><p>{d}</p></div>' for i, t, d in v)

# ---------------------------------------------------------------- pages
def p_home(pre):
    gcards = "".join(f'<a class="card reveal" href="{pre}guides/{g["slug"]}.html"><span class="tag t">{g["cat"]}</span><span class="tag">{g["read"]} min</span><h3>{g["title"].split(":")[0]}</h3><p>{g["desc"][:120]}…</p><span class="more">Read guide →</span></a>' for g in GUIDES[:6])
    issue_cards = "".join(f'<a class="card reveal" href="{pre}free-case-review.html?issue={v}"><div class="ico">{i}</div><h3>{t}</h3><p>Free review →</p></a>' for v, i, t in ISSUES[:8])
    return f"""
<section class="hero"><div class="wrap hero-grid">
<div><span class="eyebrow">📍 Downtown Miami · Government Center · Miami-Dade</span>
<div class="big" aria-hidden="true">33128</div>
<h1>Miami's courthouse district, explained in plain English.</h1>
<p class="lead">Seven courthouses and government centers share one tiny ZIP code. Find the right building, understand your deadline, and get matched with a lawyer — free.</p>
<div class="hero-actions"><a class="btn btn-primary" href="{pre}free-case-review.html">⚖ Get a free case review</a><a class="btn btn-light" href="{pre}courthouses.html">Find my courthouse</a></div>
<div class="trust"><div><b>7</b>court &amp; civic buildings in 33128</div><div><b>12</b>in-depth guides</div><div><b>5</b>free interactive tools</div><div><b>$0</b>to use, always</div></div></div>
<div class="hero-card"><h3>Which building do I need?</h3>
<label for="finder-select">My matter is about…</label>
<select id="finder-select"><option value="">Choose a matter…</option><option value="federal">Federal case or federal jury duty</option><option value="bankruptcy">Bankruptcy</option><option value="family">Divorce, custody, child support, domestic violence</option><option value="probate">Probate, wills, guardianship</option><option value="recorder">Recording a deed or official record</option><option value="juvenile">Juvenile or dependency</option><option value="civil">Civil lawsuit / small claims filing</option><option value="criminal">State criminal case</option><option value="county">County government offices</option></select>
<div id="finder-out" class="result" style="background:rgba(255,255,255,.1);color:#fff;margin-top:14px;min-height:60px">Pick a matter to see the building and address.</div></div>
</div></section>

{ad("top")}

<section><div class="wrap"><div class="sec-head"><span class="kicker">Free case review</span><h2>What's your situation?</h2><p>Tell us in two minutes. We route it to an independent attorney who handles exactly that kind of case in South Florida.</p></div>
<div class="grid g4">{issue_cards}</div></div></section>

<section class="sec-alt"><div class="wrap">
<div class="lead-band reveal"><div><span class="kicker" style="color:#fff">Free · Confidential · No obligation</span><h2>Facing a court date or a deadline?</h2>
<ul><li>Missed deadlines are one of the most common ways people lose cases they could have won.</li><li>Many injury and some employment lawyers charge nothing unless you recover money.</li><li>English · Español · Kreyòl · Português</li></ul></div>
<div>{lead_form(pre)}</div></div></div></section>

<section><div class="wrap"><div class="sec-head"><span class="kicker">Guides</span><h2>Start with the basics</h2><p>Original, plain-language explainers on the matters handled inside 33128 — written for people, not lawyers.</p></div>
<div class="grid g3">{gcards}</div><p style="margin-top:24px"><a class="btn btn-ghost" href="{pre}guides/index.html">All 12 guides →</a></p></div></section>

{ad("mid")}

<section class="sec-alt"><div class="wrap"><div class="sec-head"><span class="kicker">33128 by the numbers</span><h2>A tiny ZIP with outsized influence</h2><p>Public data for ZIP 33128 (American Community Survey estimates and local sources).</p></div>
<div class="stat-row"><div class="stat reveal"><b>~0.43</b><span>square miles of land</span></div><div class="stat reveal"><b>~9,000</b><span>residents</span></div><div class="stat reveal"><b>~98%</b><span>of homes renter-occupied</span></div><div class="stat reveal"><b>85</b><span>Walk Score — among Miami's most walkable</span></div></div>
<p style="margin-top:18px;color:var(--muted);font-size:.9rem">Tip of the day: <span data-tip>Arrive 45 minutes early — security lines peak between 8:15 and 9:15 a.m.</span></p></div></section>

<section><div class="wrap"><div class="sec-head"><span class="kicker">Tools</span><h2>Free tools that save you a phone call</h2></div>
<div class="grid g4">
<a class="card reveal" href="{pre}tools.html#deadline"><div class="ico">📅</div><h3>Deadline calculator</h3><p>Count calendar or court business days, skipping weekends and holidays.</p></a>
<a class="card reveal" href="{pre}tools.html#checklist"><div class="ico">✅</div><h3>Court-day checklist</h3><p>A printable list tailored to your hearing type.</p></a>
<a class="card reveal" href="{pre}tools.html#cost"><div class="ico">💵</div><h3>Legal cost estimator</h3><p>Model hourly fees, costs and retainers.</p></a>
<a class="card reveal" href="{pre}tools.html#injury"><div class="ico">🩹</div><h3>Injury claim illustrator</h3><p>Understand how insurers think about claim value.</p></a></div></div></section>

<section class="sec-alt"><div class="wrap"><div class="sec-head"><span class="kicker">Watch</span><h2>Video explainers</h2></div><div class="grid g2">{video_cards()}</div>
<p style="margin-top:20px"><a class="btn btn-ghost" href="{pre}videos.html">Open the video library →</a></p></div></section>

<section><div class="wrap grid g3">
<a class="card reveal" href="{pre}for-attorneys.html"><div class="ico">🤝</div><h3>Attorneys: receive cases</h3><p>Exclusive South Florida leads by practice area and language.</p><span class="more">Partner with us →</span></a>
<a class="card reveal" href="{pre}support.html"><div class="ico">💛</div><h3>Support this guide</h3><p>Donations keep every guide and tool free for the public.</p><span class="more">Donate or sponsor →</span></a>
<a class="card reveal" href="{pre}contests.html"><div class="ico">🏆</div><h3>Win a prize</h3><p>Enter the 33128 Civic Explainer Contest.</p><span class="more">See contests →</span></a></div></section>

<section style="padding-top:0"><div class="wrap">{newsletter(pre)}</div></section>

<section class="sec-alt"><div class="wrap"><div class="sec-head"><span class="kicker">FAQ</span><h2>Common questions</h2></div>
<details><summary>Is 33128.com an official court website?</summary><p>No. We are an independent guide. We link to official court and clerk websites so you can verify everything.</p></details>
<details><summary>Is the case review really free?</summary><p>Yes. There's no charge to submit your situation. Attorneys who contact you set their own fees, and many offer free initial consultations.</p></details>
<details><summary>What is ZIP code 33128?</summary><p>33128 is the ZIP code of Miami's Government Center district in downtown Miami — home to federal and county courthouses, the county's main government center and the Government Center Metrorail station.</p></details>
<details><summary>Can the clerk's office give me legal advice?</summary><p>No. Clerks can explain procedures and accept filings but can't advise you on strategy. That's what attorneys and legal-aid programs are for.</p></details>
</div></section>
"""

def p_courts(pre):
    return page_hero("Courthouse Directory · 33128", "Every courthouse and civic building inside ZIP 33128 — plus the three nearby buildings people confuse with them.", ["Courthouses"], pre) + f"""
<section><div class="wrap">
<div class="grid g2" style="margin-bottom:28px;align-items:start"><div class="tool"><h3>Which building do I need?</h3><label for="finder-select">My matter is about…</label>
<select id="finder-select"><option value="">Choose a matter…</option><option value="federal">Federal case or federal jury duty</option><option value="bankruptcy">Bankruptcy</option><option value="family">Divorce, custody, child support, domestic violence</option><option value="probate">Probate, wills, guardianship</option><option value="recorder">Recording a deed or official record</option><option value="juvenile">Juvenile or dependency</option><option value="civil">Civil lawsuit / small claims filing</option><option value="criminal">State criminal case</option><option value="county">County government offices</option></select><div id="finder-out" class="result">Pick a matter to see the building.</div></div>
<div class="tool"><h3>Search the directory</h3><label for="court-search">Building, service or street</label><input id="court-search" placeholder="e.g. probate, Flagler, bankruptcy"><p style="margin-top:12px;color:var(--muted);font-size:.92rem">Getting there: Government Center Metrorail station is at 111 NW 1st St. The free Metromover Inner Loop stops at the Wilkie D. Ferguson, Jr. station for the federal courthouse.</p></div></div>
<div class="filter-bar"><button class="chip on" data-filter="all">All</button><button class="chip" data-filter="federal">Federal</button><button class="chip" data-filter="county">County</button><button class="chip" data-filter="family">Family</button><button class="chip" data-filter="probate">Probate</button><button class="chip" data-filter="criminal">Criminal</button><button class="chip" data-filter="civil">Civil</button><button class="chip" data-filter="records">Records</button><button class="chip" data-filter="jury">Jury</button></div>
<div class="grid g2">{court_cards()}</div>
<div class="callout warn" style="margin-top:28px"><strong>Always verify before you go.</strong> Courts relocate divisions, change hours and close for holidays and emergencies. Your notice, summons or the official clerk website is the final word.</div>
</div></section>
{ad("mid")}
<section class="sec-alt"><div class="wrap">{lead_band_small(pre)}</div></section>
"""

def lead_band_small(pre, issue=""):
    q = f"?issue={issue}" if issue else ""
    return f"""<div class="lead-band reveal"><div><h2>Not sure what to do next?</h2><p>Describe your situation once. We'll route it to an independent attorney who handles it every day.</p></div><div style="text-align:center"><a class="btn btn-light" href="{pre}free-case-review.html{q}" style="font-size:1.1rem">⚖ Start my free case review</a><p style="font-size:.85rem;margin-top:10px;color:#fff">2 minutes · confidential · no obligation</p></div></div>"""

def p_guides_index(pre):
    cats = sorted(set(g["cat"] for g in GUIDES))
    chips = '<button class="chip on" data-filter="all">All</button>' + "".join(f'<button class="chip" data-filter="{c.lower().replace(" ", "-")}">{c}</button>' for c in cats)
    cards = "".join(f'<a class="card reveal" data-tags="{g["cat"].lower().replace(" ", "-")}" href="{g["slug"]}.html"><span class="tag t">{g["cat"]}</span><span class="tag">{g["read"]} min read</span><h3>{g["title"]}</h3><p>{g["desc"]}</p><span class="more">Read →</span></a>' for g in GUIDES)
    return page_hero("Guides", "Original, plain-English explainers for the matters handled inside Miami's 33128 courthouse district.", ["Guides"], pre) + f'<section><div class="wrap"><div class="filter-bar">{chips}</div><div class="grid g3">{cards}</div></div></section>{ad("mid")}<section class="sec-alt"><div class="wrap">{lead_band_small(pre)}</div></section>'

def guide_page(g):
    def body(pre):
        import re
        heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', g["body"])
        toc = "".join(f'<a href="#{i}">{html.unescape(re.sub("<.*?>", "", t))}</a>' for i, t in heads)
        related = [x for x in GUIDES if x["slug"] != g["slug"]][:3]
        rel = "".join(f'<a class="card" href="{x["slug"]}.html" style="padding:16px"><h3 style="font-size:1rem">{x["title"].split(":")[0]}</h3></a>' for x in related)
        parts = g["body"].split("</h2>", 3)
        content = g["body"]
        if len(parts) == 4:  # insert in-article ad slot after 3rd section heading content
            idx = content.find("<h2", content.find("</h2>", content.find("</h2>") + 1) + 1)
            if idx > 0: content = content[:idx] + '<div class="ad-slot" data-slot="article"></div>' + content[idx:]
        return page_hero(g["title"], g["desc"], [f'<a href="index.html">Guides</a>', g["cat"]], pre) + f"""
<div class="wrap article"><article class="body"><div class="meta">By the 33128.com editorial team · Updated {datetime.date.today().strftime("%B %Y")} · {g["read"]} min read</div>
{content}
<div class="callout" style="margin-top:2em"><strong>Disclaimer:</strong> This guide is general information about Florida and federal procedures, not legal advice. Laws, fees and court procedures change; verify with the court or an attorney licensed in Florida.</div>
<div style="margin-top:28px">{lead_band_small(pre, g["issue"])}</div></article>
<aside><div class="sticky"><div class="toc"><strong>On this page</strong>{toc}</div>
<a class="btn btn-primary btn-block" href="{pre}free-case-review.html?issue={g["issue"]}">⚖ Free case review</a>
<div class="ad-slot" data-slot="sidebar"></div>
<div><strong style="font-size:.9rem">Related guides</strong><div class="grid" style="gap:10px;margin-top:8px">{rel}</div></div></div></aside></div>"""
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"], "dateModified": TODAY,
          "author": {"@type": "Organization", "name": "33128.com"}, "publisher": {"@type": "Organization", "name": "33128.com"},
          "mainEntityOfPage": DOMAIN + "/guides/" + g["slug"] + ".html"}
    page(f'guides/{g["slug"]}.html', g["title"] + " | 33128.com", g["desc"], body, ld, "article")

def p_tools(pre):
    return page_hero("Free Legal Tools", "Calculators and checklists that answer the questions people usually wait on hold to ask.", ["Tools"], pre) + f"""
<section><div class="wrap grid" style="gap:28px">
<div class="tool reveal" id="deadline"><span class="kicker">Tool 1</span><h2>Deadline calculator</h2><p style="color:var(--muted)">Count forward from the day you were served or the day of an order. "Business days" skips weekends and U.S. federal holidays and rolls a deadline that lands on a closed day to the next business day.</p>
<form id="deadline-form"><div class="row">{fld("Start date (day served / order date)", "start", "date")}{fld("Number of days", "days", "number", ph="e.g. 20")}</div>
<div class="field"><label for="f_mode">Counting method</label><select id="f_mode" name="mode"><option value="calendar">Calendar days (e.g., 20 days to answer a civil complaint)</option><option value="court">Business days (e.g., 5 days to answer an eviction)</option></select></div>
<button class="btn btn-teal" type="submit">Calculate deadline</button></form><div id="deadline-out" class="result">Enter a date to see your estimated deadline.</div></div>
{ad("mid")}
<div class="tool reveal" id="checklist"><span class="kicker">Tool 2</span><h2>Court-day checklist builder</h2>
<form id="check-form"><div class="field"><label for="purpose">What are you going to court for?</label><select id="purpose" name="purpose"><option value="hearing">A hearing or trial (civil / small claims)</option><option value="jury">Jury duty</option><option value="family">Family court</option><option value="traffic">Traffic matter</option><option value="recorder">Recording a document</option></select></div></form><div id="check-out"></div></div>
<div class="tool reveal" id="cost"><span class="kicker">Tool 3</span><h2>Legal cost estimator</h2>
<form id="cost-form"><div class="row">{fld("Hourly rate ($)", "rate", "number", ph="350")}{fld("Estimated hours", "hours", "number", ph="15")}</div><div class="row">{fld("Court costs & filing fees ($)", "fees", "number", ph="400")}{fld("Retainer paid ($)", "retainer", "number", False, ph="2500")}</div></form>
<div id="cost-out" class="result"></div></div>
<div class="tool reveal" id="injury"><span class="kicker">Tool 4</span><h2>Injury claim illustrator</h2><p style="color:var(--muted)">See how the "multiplier method" works — a teaching tool, not a prediction.</p>
<form id="pi-form"><div class="row">{fld("Medical bills ($)", "med", "number", ph="12000")}{fld("Lost wages ($)", "wages", "number", False, ph="3000")}</div>
<div class="row">{fld("Property damage ($)", "prop", "number", False, ph="5000")}<div class="field"><label for="mult">Severity multiplier</label><select id="mult" name="mult"><option value="1.5">1.5 — minor, full recovery</option><option value="2.5" selected>2.5 — moderate</option><option value="3.5">3.5 — significant</option><option value="5">5 — severe / permanent</option></select></div></div>
<div class="field"><label for="fee">Contingency fee %</label><select id="fee" name="fee"><option>0</option><option selected>33.33</option><option>40</option></select></div></form>
<div id="pi-out" class="result"></div><p style="margin-top:14px"><a class="btn btn-primary" href="{pre}free-case-review.html?issue=injury">Get a real evaluation — free</a></p></div>
<div class="tool reveal"><span class="kicker">Tool 5</span><h2>Which courthouse?</h2><p>Use the interactive finder on the <a href="{pre}courthouses.html">courthouse directory</a> or the home page.</p></div>
</div></section>"""

def p_videos(pre):
    search = "".join(f'<a class="card reveal" href="https://www.youtube.com/results?search_query={q.replace(" ", "+")}" target="_blank" rel="noopener"><span class="tag t">{t}</span><h3>{q.capitalize()}</h3><p>Browse explainers on YouTube ↗</p></a>' for q, t in TOPIC_SEARCH)
    return page_hero("Video Library", "Short, trustworthy video explainers on jury service, court procedures and getting around downtown Miami.", ["Videos"], pre) + f"""
<section><div class="wrap"><div class="sec-head"><span class="kicker">Featured</span><h2>From the U.S. Courts</h2></div><div class="grid g2">{video_cards()}</div></div></section>
{ad("mid")}
<section class="sec-alt"><div class="wrap"><div class="sec-head"><span class="kicker">Topic playlists</span><h2>Explore by topic</h2><p>Hand-picked searches to the best explainer videos. Always check that a video is about <em>Florida</em> law before relying on it.</p></div><div class="grid g4">{search}</div></div></section>
<section><div class="wrap">{simple_form("video-suggest", "Video suggestion / creator collaboration", [row(fld("Your name", "name"), fld("Email", "email", "email")), fld("Video URL or channel", "video_url", "url"), fld("Why is it useful?", "note", rows=3, req=False)], "Suggest a video", "Thanks! We review every suggestion.")}</div></section>"""

def p_downtown(pre):
    return page_hero("Downtown 33128", "Living, working and getting around Miami's Government Center district.", ["Downtown 33128"], pre) + f"""
<section><div class="wrap article" style="padding-top:0"><div class="body">
<h2 id="where">Where is 33128?</h2>
<p>33128 covers Miami's <strong>Government Center</strong> district on the western side of downtown — roughly between I-95 and NE/NW 1st Avenue, around Flagler Street and north toward NW 5th Street. It borders Overtown (33136), the Central Business District and Brickell (33130–33131) and Little Havana to the southwest. Downtown Miami as a whole spans several ZIP codes: 33128, 33129, 33130, 33131, 33132 and 33136.</p>
<h2 id="numbers">The neighborhood in numbers</h2>
<div class="table-wrap"><table><tr><th>Metric</th><th>33128</th></tr>
<tr><td>Land area</td><td>About 0.43 sq mi</td></tr><tr><td>Residents</td><td>About 8,000–9,900 depending on the estimate</td></tr>
<tr><td>Median household income</td><td>About $36,000 (below the Florida average)</td></tr><tr><td>Housing tenure</td><td>Roughly 98% renter-occupied</td></tr>
<tr><td>Median age</td><td>About 44</td></tr><tr><td>Walk Score</td><td>85 — one of Miami's most walkable ZIPs</td></tr>
<tr><td>Area codes</td><td>305 / 786 / 645</td></tr></table></div>
<p style="font-size:.85rem;color:var(--muted)">Sources: U.S. Census Bureau ACS estimates as reported by public ZIP data aggregators; Walk Score. Figures vary between sources and years.</p>
<h2 id="transit">Getting around</h2>
<ul><li><strong>Metrorail:</strong> Government Center station connects to the airport (via the Orange Line), Dadeland and Palmetto.</li>
<li><strong>Metromover:</strong> free automated loops (Inner, Omni, Brickell) circulate through downtown — ideal for courthouse hopping.</li>
<li><strong>Brightline:</strong> MiamiCentral station is a short walk east, linking downtown to Fort Lauderdale, West Palm Beach and Orlando.</li>
<li><strong>Parking:</strong> garages surround the government center; budget for event-day pricing when the arena or nearby venues host events.</li></ul>
<h2 id="civic">Civic &amp; cultural landmarks nearby</h2>
<ul><li>HistoryMiami Museum and the main branch of the Miami-Dade Public Library on West Flagler Street.</li>
<li>The historic Miami-Dade County Courthouse (73 W. Flagler St.), a neoclassical landmark completed in 1928.</li>
<li>The Miami River and Riverwalk to the south; Overtown's Lyric Theater to the north.</li></ul>
<h2 id="business">Doing business in 33128</h2>
<p>The district's daily foot traffic — jurors, litigants, attorneys, county employees — sustains a dense mix of law offices, bail bond agencies, process servers, court reporters, notaries, translators, copy shops and quick-service restaurants. Professional-services firms that sell to the legal community are natural sponsors of this guide.</p>
<p><a class="btn btn-teal" href="{pre}support.html#sponsor">List your business / sponsor →</a></p>
</div><aside><div class="sticky"><div class="toc"><strong>On this page</strong><a href="#where">Where is 33128?</a><a href="#numbers">In numbers</a><a href="#transit">Getting around</a><a href="#civic">Landmarks</a><a href="#business">Business</a></div><div class="ad-slot" data-slot="sidebar"></div></div></aside></div></section>
<section class="sec-alt"><div class="wrap"><div class="sec-head"><span class="kicker">Local directory</span><h2>Get your business listed</h2><p>Serving clients near the courthouses? Apply for a free basic listing or a featured placement.</p></div>
{simple_form("business-listing", "Business listing request", [row(fld("Business name", "business"), fld("Category", "category", opts=["Law firm", "Bail bonds", "Process server", "Court reporter", "Notary / translation", "Restaurant / café", "Parking", "Other"])), row(fld("Contact name", "name"), fld("Email", "email", "email")), row(fld("Phone", "phone", "tel"), fld("Website", "website", "url", False)), fld("Listing type", "listing", opts=["Free basic listing", "Featured listing (paid)", "Category sponsor (paid)"]), fld("Notes", "notes", rows=3, req=False)], "Request listing")}</div></section>"""

def p_review(pre):
    return page_hero("Free Case Review", "Two minutes. Confidential. Routed to an independent South Florida attorney who handles your type of case.", ["Free Case Review"], pre) + f"""
<section><div class="wrap grid g2" style="align-items:start;gap:40px">
<div>{lead_form(pre)}</div>
<div><h2>How it works</h2>
<div class="grid" style="gap:14px"><div class="card"><div class="ico">1</div><h3>Tell us what happened</h3><p>Pick your issue and add a short description — no legal jargon needed.</p></div>
<div class="card"><div class="ico">2</div><h3>We route it</h3><p>Your summary goes to an independent attorney or legal-service provider matched by practice area, location and language.</p></div>
<div class="card"><div class="ico">3</div><h3>Get a call back</h3><p>Typically within one business day. Urgent deadlines are flagged first.</p></div></div>
<h3 style="margin-top:28px">Why people use 33128.com</h3>
<ul><li>✔ Free to submit, no obligation to hire</li><li>✔ Attorneys focused on Miami-Dade, Broward and Palm Beach</li><li>✔ Multilingual: English, Español, Kreyòl, Português</li><li>✔ We never sell your data to brokers</li></ul>
<div class="callout warn"><strong>In danger or facing an emergency?</strong> Call 911. If a court hearing is today, contact the clerk's office directly.</div>
<p style="font-size:.85rem;color:var(--muted)">33128.com is not a law firm and does not provide legal advice. Attorneys are independent and responsible for their own services. This is attorney advertising where applicable. Past results do not guarantee future outcomes.</p></div>
</div></section>
<section class="sec-alt"><div class="wrap"><div class="sec-head"><h2>Questions about the review</h2></div>
<details><summary>Does it cost anything?</summary><p>No. Submitting is free. If you decide to hire an attorney, fees are agreed between you and that attorney — and many injury lawyers charge nothing unless they win.</p></details>
<details><summary>Who sees my information?</summary><p>Only our intake team and the attorney(s) or legal-service providers best suited to your issue. See our <a href="{pre}privacy.html">privacy policy</a>.</p></details>
<details><summary>Should I include documents?</summary><p>Not yet. The attorney who contacts you will tell you what to send. Please don't include Social Security, bank or card numbers in the form.</p></details></div></section>"""

def p_attorneys(pre):
    return page_hero("For Attorneys & Legal-Service Providers", "Receive pre-qualified South Florida inquiries from people standing at the courthouse door.", ["For attorneys"], pre) + f"""
<section><div class="wrap grid g3">
<div class="card tier reveal"><h3>Pay-per-lead</h3><div class="price">Custom</div><ul><li>Exclusive or shared leads</li><li>Filter by practice area, county, language</li><li>Real-time email delivery</li></ul></div>
<div class="card tier pop reveal"><h3>Practice-area sponsor</h3><div class="price">Monthly</div><ul><li>Exclusive branding on one guide category</li><li>First right on matching leads</li><li>Featured profile in the directory</li></ul></div>
<div class="card tier reveal"><h3>District partner</h3><div class="price">Annual</div><ul><li>Site-wide presence in your practice area</li><li>Newsletter features</li><li>Co-authored guides (with clear attribution)</li></ul></div></div></section>
<section class="sec-alt"><div class="wrap grid g2" style="align-items:start;gap:40px"><div><h2>Why 33128 traffic converts</h2><p>Visitors arrive with a summons, a hearing date or a fresh accident — the highest-intent moment in the legal journey. Every inquiry includes issue type, urgency, county, language and a written description.</p>
<ul><li>Practice areas: injury, family, criminal, bankruptcy, landlord–tenant, probate, real estate, employment, business.</li><li>Compliant intake: express written consent captured on every lead.</li><li>Florida Bar advertising rules respected: no guarantees, clear disclaimers.</li></ul></div>
{simple_form("attorney-partner", "Attorney partnership inquiry", [row(fld("Your name", "name"), fld("Firm", "firm")), row(fld("Email", "email", "email"), fld("Phone", "phone", "tel")), row(fld("Florida Bar number", "bar_number", req=False), fld("Primary practice area", "practice", opts=["Personal injury", "Family", "Criminal defense", "Bankruptcy", "Landlord–tenant", "Probate / estates", "Real estate", "Employment", "Business", "Immigration", "Other"])), fld("Counties served", "counties", opts=["Miami-Dade", "Miami-Dade + Broward", "Tri-county (incl. Palm Beach)", "Statewide"]), fld("Monthly lead volume wanted", "volume", opts=["1–10", "11–30", "31–100", "100+"]), fld("Anything else?", "notes", rows=3, req=False)], "Request partner info")}</div></section>"""

def p_support(pre):
    tiers = [("Supporter", "$5", "/month", ["Keeps one guide updated", "Name on supporters wall (optional)"], "monthly5"),
             ("Advocate", "$25", "/month", ["Funds a new guide each quarter", "Quarterly impact report", "Supporters wall"], "monthly25"),
             ("Champion", "$100", "one-time", ["Sponsors a translation into Spanish or Kreyòl", "Thank-you in the newsletter"], "once100")]
    tcards = "".join(f'<div class="card tier reveal{" pop" if i == 1 else ""}"><h3>{n}</h3><div class="price">{p}<small style="font-size:1rem;color:var(--muted)"> {per}</small></div><ul>{"".join(f"<li>{x}</li>" for x in b)}</ul><a class="btn btn-primary btn-block" data-pay="{k}" href="#pledge">Give {p}</a></div>' for i, (n, p, per, b, k) in enumerate(tiers))
    return page_hero("Support 33128.com", "Donations, sponsorships and partnerships keep every guide and tool free for the public.", ["Support"], pre) + f"""
<section id="donate"><div class="wrap"><div class="sec-head"><span class="kicker">Donate</span><h2>Keep court information free</h2><p>Your support pays for research, updates when courts change procedures, translations, hosting, marketing to reach people who need it, and hiring writers and developers.</p></div>
<div class="grid g3">{tcards}</div>
<div class="grid g2" style="margin-top:30px;align-items:start;gap:30px" id="pledge"><div><h3>Where your money goes</h3>
<div class="table-wrap"><table><tr><th>Use</th><th>Share</th></tr><tr><td>Research &amp; content updates</td><td>40%</td></tr><tr><td>Translations &amp; accessibility</td><td>20%</td></tr><tr><td>Outreach &amp; promotion</td><td>15%</td></tr><tr><td>Hiring talent (writers, devs, designers)</td><td>15%</td></tr><tr><td>Contests &amp; prizes</td><td>10%</td></tr></table></div>
<p style="font-size:.85rem;color:var(--muted)">33128.com is not a registered charity; contributions are not tax-deductible.</p></div>
{simple_form("donation-pledge", "Donation / support pledge", [row(fld("Name", "name"), fld("Email", "email", "email")), row(fld("Amount (USD)", "amount", "number"), fld("Frequency", "frequency", opts=["One-time", "Monthly", "Annual"])), fld("Earmark (optional)", "earmark", opts=["Wherever needed most", "Operations", "Translations", "Promotion & marketing", "Hiring talent", "Contests & prizes"], req=False), fld("Message", "message", rows=3, req=False)], "Pledge my support", "Thank you! We'll send secure payment instructions to your email.")}</div></div></section>
{ad("mid")}
<section id="sponsor" class="sec-alt"><div class="wrap"><div class="sec-head"><span class="kicker">Sponsor &amp; advertise</span><h2>Reach people at the courthouse door</h2><p>Law firms, bail bond agencies, court reporters, translators, parking operators and downtown businesses can sponsor guides, tools, the newsletter or contests.</p></div>
<div class="grid g4"><div class="card"><div class="ico">📘</div><h3>Guide sponsor</h3><p>Branded placement on one guide or category.</p></div><div class="card"><div class="ico">🧮</div><h3>Tool sponsor</h3><p>"Powered by" on a calculator.</p></div><div class="card"><div class="ico">✉</div><h3>Newsletter</h3><p>Feature slot in The 33128 Brief.</p></div><div class="card"><div class="ico">🏆</div><h3>Contest sponsor</h3><p>Fund prizes; get naming rights.</p></div></div>
<div style="margin-top:28px">{simple_form("sponsorship", "Sponsorship / advertising inquiry", [row(fld("Name", "name"), fld("Company", "company")), row(fld("Email", "email", "email"), fld("Phone", "phone", "tel", False)), row(fld("Interest", "interest", opts=["Guide sponsor", "Tool sponsor", "Newsletter", "Contest sponsor", "Site-wide partnership", "Buy / partner on the 33128.com domain"]), fld("Monthly budget", "budget", opts=["Under $250", "$250–$1,000", "$1,000–$5,000", "$5,000+"])), fld("Goals", "goals", rows=3, req=False)], "Send sponsorship inquiry")}</div></div></section>
<section><div class="wrap grid g2"><a class="card reveal" href="{pre}contests.html"><div class="ico">🏆</div><h3>Contests &amp; prizes</h3><p>Run by the community, funded by supporters and sponsors.</p></a><a class="card reveal" href="{pre}careers.html"><div class="ico">🧑‍💻</div><h3>Careers &amp; talent</h3><p>We hire writers, translators, designers and developers.</p></a></div></section>"""

def p_contests(pre):
    return page_hero("Contests &amp; Prizes", "Help make court information clearer — and win.", ["Contests"], pre) + f"""
<section><div class="wrap grid g3">
<div class="card reveal"><span class="tag">Open</span><h3>Civic Explainer Contest</h3><p>Create a 60–120 second video or one-page graphic explaining one court process (jury duty, small claims, eviction deadlines…).</p><p><strong>Prizes:</strong> $500 · $250 · $100 + featured placement.</p></div>
<div class="card reveal"><span class="tag">Open</span><h3>Plain-Language Rewrite</h3><p>Take a confusing legal term or form instruction and rewrite it so a 12-year-old understands it.</p><p><strong>Prize:</strong> $100 monthly winner.</p></div>
<div class="card reveal"><span class="tag t">Students</span><h3>Law Student Guide Fellowship</h3><p>Florida law students draft a guide with attorney review and byline credit.</p><p><strong>Award:</strong> $750 stipend per published guide.</p></div></div></section>
<section class="sec-alt"><div class="wrap grid g2" style="align-items:start;gap:40px"><div><h2>Official rules (summary)</h2><ol><li>Open to legal residents of the United States aged 18+. Void where prohibited.</li><li>No purchase or donation necessary to enter or win.</li><li>Entries must be original; you keep copyright and grant 33128.com a non-exclusive license to display your entry.</li><li>Judging: clarity (40%), accuracy (40%), creativity (20%) by an independent panel.</li><li>Winners are notified by email and announced in the newsletter. Prize amounts may change based on sponsor funding and are confirmed when each round opens.</li><li>No trademarks, logos or copyrighted material from third parties.</li></ol></div>
{simple_form("contest-entry", "Contest entry", [row(fld("Full name", "name"), fld("Email", "email", "email")), fld("Contest", "contest", opts=["Civic Explainer Contest", "Plain-Language Rewrite", "Law Student Guide Fellowship"]), fld("Link to your entry", "entry_url", "url"), fld("Short description", "description", rows=3), '<label class="check"><input type="checkbox" required name="rules" value="agreed"> I confirm I am 18+, the entry is my original work, and I accept the official rules.</label><br>'], "Submit entry", "Entry received — good luck! We'll confirm by email.")}</div></section>"""

def p_careers(pre):
    roles = [("Legal content writer (Florida)", "Freelance · remote", "Write and update plain-English guides; JD or paralegal background preferred."),
             ("Spanish / Haitian Creole translator", "Freelance · remote", "Translate guides and tools; legal-translation experience preferred."),
             ("Front-end developer", "Contract · remote", "Build interactive tools in vanilla JS; accessibility-first."),
             ("Video creator", "Per project", "Short explainer videos for YouTube and social."),
             ("Partnerships &amp; sales", "Commission", "Sign law-firm and local-business sponsors."),
             ("Community moderator", "Part-time · remote", "Run contests, respond to suggestions, curate videos.")]
    cards = "".join(f'<div class="card reveal"><span class="tag t">{t}</span><h3>{r}</h3><p>{d}</p></div>' for r, t, d in roles)
    return page_hero("Careers &amp; Talent", "Help build the most useful courthouse-district guide in the country.", ["Careers"], pre) + f"""
<section><div class="wrap"><div class="grid g3">{cards}</div></div></section>
<section class="sec-alt"><div class="wrap">{simple_form("talent-application", "Talent application", [row(fld("Full name", "name"), fld("Email", "email", "email")), row(fld("Role", "role", opts=[r for r, _, _ in roles] + ["Other"]), fld("Portfolio / LinkedIn URL", "portfolio", "url", False)), row(fld("Languages", "languages", req=False), fld("Availability", "availability", opts=["Full-time", "Part-time", "Per project"])), fld("Why you?", "pitch", rows=4)], "Apply now", "Application received — thank you! We'll be in touch if there's a fit.")}</div></section>"""

def p_about(pre):
    return page_hero("About 33128.com", "Why a ZIP code became a public guide — and what \"33128\" means.", ["About"], pre) + f"""
<section><div class="wrap article" style="padding-top:0"><div class="body">
<h2 id="mission">Our mission</h2><p>Every weekday, thousands of people walk into the courthouses of ZIP 33128 — jurors, parents in custody disputes, families settling an estate, tenants facing eviction, small-business owners chasing an unpaid invoice. Most have never been to court before. 33128.com exists to make that first visit less confusing: where to go, what to bring, which deadline matters and who can help.</p>
<h2 id="meaning">What does 33128 mean?</h2>
<p><strong>In geography and commerce</strong>, 33128 is the U.S. ZIP code for Miami's Government Center district — home to the headquarters of the U.S. District Court and U.S. Bankruptcy Court for the Southern District of Florida, the county's family, probate, juvenile and recording offices, and the Stephen P. Clark Government Center. Very few ZIP codes anywhere concentrate this much judicial activity in under half a square mile.</p>
<p><strong>In the economy</strong>, it's a renter-heavy, walkable urban core whose daytime population (lawyers, jurors, litigants, county staff) far exceeds its ~9,000 residents — the kind of high-intent foot traffic that powers law offices, bail bonds, court reporting and quick-service retail.</p>
<p><strong>In technology and AI</strong>, the digits read naturally as "33 · 128": 128 is 2<sup>7</sup>, the bit-length of AES-128 encryption and a common context-window size (128K tokens) for modern language models. We like the coincidence: this site is about turning complex information into something compact and usable.</p>
<p><strong>For people</strong>, it's a place where life-changing decisions happen — which is why plain language matters here more than almost anywhere.</p>
<h2 id="how">How we make money</h2><p>We keep the site free through advertising (Google AdSense), sponsorships clearly labeled as such, partnerships with independent attorneys who receive inquiries submitted through our case-review form with the user's consent, and voluntary donations. Advertisers do not influence our guides.</p>
<h2 id="editorial">Editorial standards</h2><ul><li>Guides are written in plain English and link to primary sources (courts, clerks, statutes).</li><li>We date every update and correct errors promptly — <a href="{pre}contact.html">report one here</a>.</li><li>Sponsored content is always labeled.</li></ul>
</div><aside><div class="sticky"><a class="btn btn-primary btn-block" href="{pre}free-case-review.html">⚖ Free case review</a><div class="ad-slot" data-slot="sidebar"></div></div></aside></div></section>"""

def p_contact(pre):
    return page_hero("Contact", "Questions, corrections, partnerships or press — we read everything.", ["Contact"], pre) + f"""
<section><div class="wrap grid g2" style="align-items:start;gap:40px">
{simple_form("contact", "Contact form", [row(fld("Name", "name"), fld("Email", "email", "email")), fld("Topic", "topic", opts=["General question", "Report a correction", "Advertising / sponsorship", "Attorney partnership", "Domain / website acquisition", "Press", "Other"]), fld("Message", "message", rows=6)], "Send message", "Thanks — your message was received. We usually reply within one or two business days.")}
<div><h2>Before you write</h2><ul><li><strong>Need legal help?</strong> Use the <a href="{pre}free-case-review.html">free case review</a> — it's faster.</li><li><strong>Court questions</strong> (your case number, hearing time): contact the court clerk directly; we can't access court records.</li><li><strong>Interested in this website, the domain, sponsorship, advertising or a partnership?</strong> <a href="{INTEREST_URL}" target="_blank" rel="noopener">Contact the owner here</a>.</li></ul>
<div class="callout">We never ask for payment by gift card, wire transfer or cryptocurrency. If someone claims to be from 33128.com and does, it's a scam.</div></div></div></section>"""

def legal_page(title, inner):
    return lambda pre: page_hero(title, "Last updated " + datetime.date.today().strftime("%B %d, %Y") + ".", [title], pre) + f'<section><div class="wrap article" style="padding-top:0;grid-template-columns:1fr"><div class="body" style="max-width:820px">{inner}</div></div></section>'

PRIVACY = """
<p>This policy explains what 33128.com ("we") collects and how it's used.</p>
<h2>Information you give us</h2><p>When you submit a form (case review, contact, sponsorship, donation pledge, contest entry, application or newsletter), we receive the information you enter. Case-review submissions are shared, with your express consent, with one or more independent attorneys or legal-service providers so they can contact you. We do not sell your information to data brokers.</p>
<h2>Form processing</h2><p>Forms are delivered through a third-party form-processing service that transmits submissions to our private inbox. That service processes data under its own privacy policy.</p>
<h2 id="cookies">Cookies and advertising</h2><p>We use Google AdSense to display ads. Third-party vendors, including Google, use cookies to serve ads based on a user's prior visits to this website or other websites. Google's use of advertising cookies enables it and its partners to serve ads to users based on their visit to this site and/or other sites on the Internet. You may opt out of personalized advertising by visiting <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a> or <a href="https://www.aboutads.info/choices/" target="_blank" rel="noopener">www.aboutads.info</a>. See also <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">how Google uses information from sites that use its services</a>.</p>
<p>Choosing "Essential only" in our cookie banner requests non-personalized ads. We store your theme and consent choices in your browser's local storage.</p>
<h2>Embedded content</h2><p>Videos are embedded from YouTube using privacy-enhanced mode and load only when you click play.</p>
<h2>Children</h2><p>This site is not directed to children under 13, and we do not knowingly collect their information.</p>
<h2>Your choices</h2><p>You may ask us to access or delete information you submitted by using the <a href="contact.html">contact form</a>. California, Virginia, Colorado and other state residents may have additional rights under applicable law.</p>
<h2>Security</h2><p>Our site is served over HTTPS. No method of transmission is 100% secure; please don't submit Social Security, bank or card numbers.</p>
<h2>Changes</h2><p>We may update this policy and will revise the date above.</p>"""

TERMS = """
<h2>Use of the site</h2><p>33128.com provides general legal information for educational purposes. By using it you agree to these terms.</p>
<h2>No legal advice; no attorney–client relationship</h2><p>Content is not legal advice. Using the site or submitting a form does not create an attorney–client relationship with us or with any attorney. We are not a law firm and are not a lawyer referral service under Florida Bar rules; attorneys who contact you are independent and solely responsible for their services.</p>
<h2>Accuracy</h2><p>We work to keep information accurate, but laws, court locations, fees and procedures change. Verify with official sources before acting. Tools produce estimates only.</p>
<h2>User submissions</h2><p>You agree to submit accurate information and not to submit unlawful, infringing or harmful content. Contest entries are governed by the contest rules.</p>
<h2>Donations and sponsorships</h2><p>Donations are voluntary, generally non-refundable and not tax-deductible. Sponsorships are governed by separate written agreements.</p>
<h2>Third-party links and ads</h2><p>We are not responsible for third-party websites, ads or services.</p>
<h2>Limitation of liability</h2><p>To the fullest extent permitted by law, 33128.com is not liable for any damages arising from use of the site. The site is provided "as is."</p>
<h2>Governing law</h2><p>These terms are governed by the laws of the State of Florida.</p>"""

DISCLAIMER = """
<h2>Legal information disclaimer</h2><p>33128.com is an independent publication. It is <strong>not</strong> affiliated with, endorsed by or operated by the U.S. Courts, the U.S. District or Bankruptcy Court for the Southern District of Florida, the Miami-Dade Clerk of the Court and Comptroller, Miami-Dade County, the City of Miami, The Florida Bar, the U.S. Postal Service or any government agency. Building names and addresses are used for identification and navigation only.</p>
<h2>Attorney advertising</h2><p>Portions of this site may constitute attorney advertising. Any results described do not guarantee similar outcomes. Choosing a lawyer is an important decision that should not be based solely on advertisements.</p>
<h2 id="trademark">Trademark &amp; copyright disclosure regarding "33128"</h2>
<ul><li>"33128" is a United States ZIP code — a public geographic designation assigned by the U.S. Postal Service. It is used on this website <strong>descriptively</strong>, to identify the geographic area this guide covers. 33128.com claims no exclusive trademark rights in the number "33128" itself, and nothing here implies endorsement by the U.S. Postal Service or any owner of a mark containing those digits.</li>
<li>We do not use, and do not intend to use, any third-party trademark, logo or trade dress that incorporates "33128." Any third-party names (courts, agencies, programs, platforms) are the property of their respective owners and are referenced for identification only (nominative use).</li>
<li>The site name, original text, guides, tool code, design and graphics of 33128.com are © 33128.com, all rights reserved, except where noted. Public-domain government information (such as addresses and court rules) is not claimed.</li>
<li>Embedded videos remain the property of their creators and are displayed through YouTube's standard embed functionality.</li>
<li>If you believe content on this site infringes your rights, please use the <a href="contact.html">contact form</a> with details and we will respond promptly.</li></ul>
<h2>Advertising</h2><p>Ads are served by Google AdSense and are labeled. We do not endorse advertised products or services.</p>"""

def p_404(pre):
    return f'<section class="hero"><div class="wrap" style="text-align:center"><div class="big">404</div><h1>That page isn\'t on the docket.</h1><p class="lead" style="margin:0 auto">Try the courthouse directory or a guide instead.</p><div class="hero-actions" style="justify-content:center"><a class="btn btn-light" href="/courthouses.html">Courthouses</a><a class="btn btn-primary" href="/free-case-review.html">Free case review</a></div></div></section>'

def build():
    org = {"@context": "https://schema.org", "@type": "Organization", "name": "33128.com", "url": DOMAIN + "/", "logo": DOMAIN + "/assets/img/favicon.svg"}
    page("index.html", "33128 · Miami Courthouse District Guide — Courts, Deadlines & Free Case Review", "Independent plain-English guide to Miami's 33128 courthouse district: find the right courthouse, calculate deadlines, read Florida legal guides and get a free case review.", p_home, org)
    page("courthouses.html", "Courthouse Directory for ZIP 33128, Miami | 33128.com", "Addresses, services and directions for every courthouse in Miami's 33128 Government Center district — federal, bankruptcy, family, probate, recorder and more.", p_courts)
    page("guides/index.html", "Florida Legal Guides for Miami | 33128.com", "Plain-English guides on jury duty, small claims, evictions, divorce, probate, bankruptcy, car accidents and more in Miami-Dade.", p_guides_index)
    for g in GUIDES: guide_page(g)
    page("tools.html", "Free Legal Tools: Deadline Calculator, Court Checklist & Cost Estimators | 33128.com", "Free interactive tools: court deadline calculator, court-day checklist, legal cost estimator and injury claim illustrator.", p_tools)
    page("videos.html", "Court & Jury Video Library | 33128.com", "Video explainers on jury service, court procedures and getting around downtown Miami.", p_videos)
    page("downtown.html", "Downtown Miami 33128: Neighborhood Guide, Data & Transit | 33128.com", "What ZIP 33128 covers, neighborhood data, Metrorail and Metromover tips, landmarks and doing business near Miami's courthouses.", p_downtown)
    page("free-case-review.html", "Free Case Review — Miami & South Florida | 33128.com", "Describe your legal issue in two minutes and get routed to an independent South Florida attorney. Free, confidential, no obligation.", p_review)
    page("for-attorneys.html", "Legal Leads & Sponsorship for Florida Attorneys | 33128.com", "Receive high-intent South Florida legal inquiries by practice area, county and language. Sponsorship and partnership options.", p_attorneys)
    page("support.html", "Donate, Sponsor or Advertise | 33128.com", "Support free court information for Miami: donate, sponsor a guide or tool, or advertise to people at the courthouse door.", p_support)
    page("contests.html", "Contests & Prizes | 33128.com", "Enter the Civic Explainer Contest, Plain-Language Rewrite and Law Student Guide Fellowship.", p_contests)
    page("careers.html", "Careers & Talent | 33128.com", "Join 33128.com as a legal writer, translator, developer, video creator or partnerships lead.", p_careers)
    page("about.html", "About 33128.com & the Meaning of 33128", "Our mission, editorial standards, how we're funded, and what 33128 means in geography, commerce, the economy and technology.", p_about)
    page("contact.html", "Contact 33128.com", "Contact 33128.com for questions, corrections, partnerships, advertising or press.", p_contact)
    page("privacy.html", "Privacy Policy | 33128.com", "How 33128.com collects, uses and protects information, including cookies and Google AdSense.", legal_page("Privacy Policy", PRIVACY))
    page("terms.html", "Terms of Use | 33128.com", "Terms of use for 33128.com.", legal_page("Terms of Use", TERMS))
    page("disclaimer.html", "Disclaimer & Trademark/Copyright Notice | 33128.com", "Legal disclaimer, attorney-advertising notice and trademark/copyright disclosure regarding 33128.", legal_page("Disclaimer &amp; Trademark Notice", DISCLAIMER))
    # 404 uses absolute paths (served at any depth by GitHub Pages)
    write("404.html", head("Page not found | 33128.com", "Page not found.", "404.html", "/").replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">') + header("/") + p_404("/") + footer("/"))
    # sitemap
    urls = ["", "courthouses.html", "guides/", "tools.html", "videos.html", "downtown.html", "free-case-review.html", "for-attorneys.html", "support.html", "contests.html", "careers.html", "about.html", "contact.html", "privacy.html", "terms.html", "disclaimer.html"] + [f'guides/{g["slug"]}.html' for g in GUIDES]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{DOMAIN}/{u}</loc><lastmod>{TODAY}</lastmod><changefreq>{'weekly' if u in ('', 'guides/') else 'monthly'}</changefreq><priority>{'1.0' if u == '' else '0.8' if u.startswith('guides') or u == 'free-case-review.html' else '0.6'}</priority></url>\n" for u in urls) + "</urlset>\n"
    write("sitemap.xml", sm)
    print("built", len(urls), "urls")

if __name__ == "__main__":
    build()
