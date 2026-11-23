# Phase-wise Build Prompts — 33128.com

Use these prompts in order to rebuild or extend the site with any AI coding assistant. Phases 1–8 are already implemented in this repo. Phases 9–10 are the growth roadmap.

---

## Phase 1: Foundation and brand
> Build a static, dependency-free website for **33128.com**, positioned as "33128 · Miami Courthouse District Guide." Generate it from a Python script (`tools/build.py`) into the repo root for GitHub Pages (main branch, root). Design tokens: navy #0b1f3a, teal #0fb5ae, coral #ff6b4a, paper #faf7f2. Fonts: Fraunces for headings, Inter for body. Support light/dark themes. Mobile-first, accessible (skip link, focus rings, reduced motion), with print styles.
> On top of **every** page, add a full-width bar reading "Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership," linked to https://web.works/contact. Never display the URL text itself.

## Phase 2: AdSense readiness
> Put `<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>` in the `<head>` of every page. Add `ads.txt` with `google.com, pub-6620975821265271, DIRECT, f08c47fec0942fa0`. Rely on Auto ads, plus optional manual slots (top, mid, article, sidebar) configured in `assets/js/config.js` and hidden when empty. Add a cookie banner where "Essential only" sets `requestNonPersonalizedAds=1`. Write Privacy (with Google's required advertising-cookie language), Terms, Disclaimer, About and Contact pages. Provide original long-form content, clear navigation, and no deceptive ad placement.

## Phase 3: Core content
> Write 12 original guides (600–900 words each, with tables and callouts, plus a TOC sidebar, related guides and an in-article ad slot). Topics: courthouse visit, jury duty, small claims ($8,000 limit), traffic tickets, eviction, family court, probate, Chapter 7 vs 13, car accidents (PIP, 14-day rule, 2-year limitation, modified comparative negligence), recording a deed, choosing a lawyer, and the first 72 hours after an arrest. Add Article JSON-LD and a dated "not legal advice" disclaimer to each.

## Phase 4: Courthouse directory and finder
> Build `courthouses.html` with cards for every 33128 court building plus three nearby ones. Each card shows address, services, phone, a map link and the official site. Add filter chips, live search and a "Which building do I need?" finder (also in the home hero).

## Phase 5: Interactive tools
> Build `tools.html` with: (1) a deadline calculator (calendar vs. business days, auto-computed US federal holidays, weekend roll-forward); (2) a court-day checklist builder with print; (3) a legal cost estimator; (4) an injury-claim illustrator using the multiplier method with a contingency fee. Results show live, and each tool carries an estimate disclaimer.

## Phase 6: Lead generation (main revenue engine)
> Build a 3-step lead form with a progress bar: issue (12 practice areas), urgency/county/lawyer status/language/description, then contact details plus explicit TCPA-style consent. Support `?issue=` preselect. Put the form on the home page and on `free-case-review.html`, and add a CTA in every guide and a floating mobile CTA. Add a B2B `for-attorneys.html` with pay-per-lead, sponsor and partner tiers and an intake form.
> Route **all** forms through AJAX (FormSubmit) to a private inbox whose address is assembled at runtime from an encoded string. The email must never appear in HTML, text or `mailto:` links.

## Phase 7: Community and funding
> Build `support.html` with donation tiers (payment links set in config.js, pledge form fallback), a use-of-funds table, and sponsorship packages. Also build `contests.html` (3 contests, official rules, entry form), `careers.html` (6 roles, application form), a `videos.html` lite-YouTube library (privacy-enhanced embeds, topic playlists, suggestion form), and `downtown.html` (neighborhood data, transit, a business-listing form). Add a newsletter on the home page.

## Phase 8: SEO, performance and automation
> Add canonical URLs, Open Graph/Twitter meta, a 1200×630 OG image, WebSite/Organization/Article JSON-LD, `sitemap.xml` with lastmod, `robots.txt`, a web manifest, a favicon and a 404 page. Add a GitHub Actions workflow `auto-refresh.yml` that runs daily: it rebuilds pages, updates sitemap dates and the "content checked" stamp, rotates the tip of the day, and commits.
> Add a trademark/copyright disclosure: "33128" is used descriptively as a USPS ZIP code, no affiliation with courts/USPS, and nominative use of third-party names.

## Phase 9: Growth (next)
> Translate the top 6 guides into Spanish (`/es/`) and Haitian Creole (`/ht/`) with hreflang tags. Add more practice-area landing pages (workers' comp, immigration, employment, landlord). Add a courthouse holiday-closure calendar. Add GA4 or Plausible with `generate_lead` conversion events. Create AdSense ad units and paste their slot IDs into `config.js`.

## Phase 10: Scale monetization
> Connect a lead-distribution CRM (e.g., webhook to Google Sheets or LeadsPedia). Add Stripe Payment Links for donations. Sell sponsor slots per guide category. Launch The 33128 Brief newsletter with sponsor slots. Publish contest winners monthly to generate fresh content and backlinks.
