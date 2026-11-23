/* 33128.com — site script (no dependencies) */
(function () {
  "use strict";
  var SITE = window.SITE || {};
  var BASE = (document.currentScript && document.currentScript.src.replace(/assets\/js\/main\.js.*$/, "")) || "";

  /* ---------- Private inbox routing (never rendered on the page) ---------- */
  function inbox() {
    // assembled at runtime only; the address never appears in markup
    var p = ["=02bj5C", "bpFWbnB", "UMhN3ay", "92diV2d"];
    var s = p.join("").split("").reverse().join("");
    try { return atob(s); } catch (e) { return ""; }
  }
  function endpoint() { return "https://formsubmit.co/ajax/" + inbox(); }

  /* ---------- Theme ---------- */
  var root = document.documentElement;
  function setTheme(t) { root.setAttribute("data-theme", t); try { localStorage.setItem("theme", t); } catch (e) {} }
  try { var saved = localStorage.getItem("theme"); if (saved) root.setAttribute("data-theme", saved); } catch (e) {}
  document.querySelectorAll("[data-theme-toggle]").forEach(function (b) {
    b.addEventListener("click", function () { setTheme(root.getAttribute("data-theme") === "dark" ? "light" : "dark"); });
  });

  /* ---------- Mobile menu ---------- */
  var nav = document.querySelector(".nav"), mb = document.querySelector(".menu-btn");
  if (mb && nav) mb.addEventListener("click", function () {
    var o = nav.classList.toggle("open"); mb.setAttribute("aria-expanded", o ? "true" : "false");
  });

  /* ---------- Active nav ---------- */
  var here = location.pathname.replace(/index\.html$/, "");
  document.querySelectorAll(".nav a").forEach(function (a) {
    var h = a.getAttribute("href"); if (!h) return;
    var abs = new URL(h, location.href).pathname.replace(/index\.html$/, "");
    if (abs === here || (abs.length > 1 && here.indexOf(abs) === 0 && abs !== "/")) a.setAttribute("aria-current", "page");
  });

  /* ---------- Reveal on scroll ---------- */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }); }, { threshold: .12 });
    document.querySelectorAll(".reveal").forEach(function (el) { io.observe(el); });
  } else document.querySelectorAll(".reveal").forEach(function (el) { el.classList.add("in"); });

  /* ---------- Back to top ---------- */
  var tt = document.querySelector(".to-top");
  if (tt) { window.addEventListener("scroll", function () { tt.classList.toggle("show", scrollY > 700); }, { passive: true });
    tt.addEventListener("click", function () { scrollTo({ top: 0, behavior: "smooth" }); }); }

  /* ---------- Cookie consent ---------- */
  var ck = document.querySelector(".cookie");
  try { if (ck && !localStorage.getItem("consent")) ck.classList.add("show"); } catch (e) {}
  document.querySelectorAll("[data-consent]").forEach(function (b) {
    b.addEventListener("click", function () {
      try { localStorage.setItem("consent", b.getAttribute("data-consent")); } catch (e) {}
      if (ck) ck.classList.remove("show");
    });
  });

  /* ---------- AdSense manual slots (auto ads work without these) ---------- */
  var slots = SITE.adSlots || {};
  document.querySelectorAll(".ad-slot[data-slot]").forEach(function (box) {
    var id = slots[box.getAttribute("data-slot")];
    if (!id) { box.style.display = "none"; return; }
    box.innerHTML = '<span class="lbl">Advertisement</span><ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-6620975821265271" data-ad-slot="' + id + '" data-ad-format="auto" data-full-width-responsive="true"></ins>';
    try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
  });

  /* ---------- Forms (all routed privately) ---------- */
  function serialize(form) {
    var data = {}, fd = new FormData(form);
    fd.forEach(function (v, k) { if (k === "_honey") return; data[k] = data[k] ? data[k] + ", " + v : v; });
    data._subject = "[33128.com] " + (form.getAttribute("data-subject") || "Website form") + (data.name ? " — " + data.name : "");
    data._template = "table"; data._captcha = "false";
    data.page = location.href; data.submitted = new Date().toISOString();
    return data;
  }
  document.querySelectorAll("form[data-form]").forEach(function (form) {
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var msg = form.querySelector(".form-msg");
      var hp = form.querySelector("[name=_honey]");
      if (hp && hp.value) return;
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var btn = form.querySelector("[type=submit]"); if (btn) { btn.disabled = true; btn.dataset.t = btn.textContent; btn.textContent = "Sending…"; }
      fetch(endpoint(), { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(serialize(form)) })
        .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
        .then(function () {
          if (msg) { msg.className = "form-msg ok"; msg.textContent = form.getAttribute("data-ok") || "Thank you — your message was received. We'll be in touch shortly."; }
          form.reset(); if (form.hasAttribute("data-multistep")) goStep(form, 0);
          if (window.gtag) gtag("event", "generate_lead", { form: form.getAttribute("data-form") });
        })
        .catch(function () { if (msg) { msg.className = "form-msg err"; msg.textContent = "Something went wrong sending your message. Please try again in a minute."; } })
        .finally(function () { if (btn) { btn.disabled = false; btn.textContent = btn.dataset.t; } });
    });
  });

  /* ---------- Multi-step lead form ---------- */
  function goStep(form, n) {
    var steps = form.querySelectorAll(".step"), bars = form.querySelectorAll(".steps-bar span");
    steps.forEach(function (s, i) { s.classList.toggle("active", i === n); });
    bars.forEach(function (b, i) { b.classList.toggle("on", i <= n); });
    form.dataset.step = n;
  }
  document.querySelectorAll("form[data-multistep]").forEach(function (form) {
    goStep(form, 0);
    form.addEventListener("click", function (e) {
      var t = e.target.closest("[data-next],[data-prev]"); if (!t) return;
      e.preventDefault();
      var n = +form.dataset.step, cur = form.querySelectorAll(".step")[n];
      if (t.hasAttribute("data-next")) {
        var bad = Array.prototype.find.call(cur.querySelectorAll("input,select,textarea"), function (f) { return !f.checkValidity(); });
        if (bad) { bad.reportValidity(); return; }
        goStep(form, n + 1);
      } else goStep(form, Math.max(0, n - 1));
      form.scrollIntoView({ behavior: "smooth", block: "start" });
    });
    // preselect issue from ?issue=
    var q = new URLSearchParams(location.search).get("issue");
    if (q) { var r = form.querySelector('input[name=issue][value="' + q + '"]'); if (r) r.checked = true; }
  });

  /* ---------- Lite YouTube ---------- */
  document.querySelectorAll(".yt[data-id]").forEach(function (el) {
    var id = el.getAttribute("data-id");
    el.style.backgroundImage = "url(https://i.ytimg.com/vi/" + id + "/hqdefault.jpg)";
    el.setAttribute("role", "button"); el.setAttribute("tabindex", "0");
    function play() {
      if (el.classList.contains("playing")) return;
      el.classList.add("playing");
      el.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" title="' + (el.getAttribute("data-title") || "Video") + '" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>';
    }
    el.addEventListener("click", play);
    el.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); play(); } });
  });

  /* ---------- Courthouse directory filter ---------- */
  var chips = document.querySelectorAll(".chip[data-filter]");
  chips.forEach(function (c) {
    c.addEventListener("click", function () {
      chips.forEach(function (x) { x.classList.remove("on"); }); c.classList.add("on");
      var f = c.getAttribute("data-filter");
      document.querySelectorAll("[data-tags]").forEach(function (card) {
        card.style.display = (f === "all" || card.getAttribute("data-tags").split(" ").indexOf(f) > -1) ? "" : "none";
      });
    });
  });
  var cs = document.getElementById("court-search");
  if (cs) cs.addEventListener("input", function () {
    var v = cs.value.toLowerCase();
    document.querySelectorAll("[data-tags]").forEach(function (card) { card.style.display = card.textContent.toLowerCase().indexOf(v) > -1 ? "" : "none"; });
  });

  /* ---------- Which building? finder ---------- */
  var FINDER = {
    federal: ["Wilkie D. Ferguson, Jr. U.S. Courthouse", "400 N. Miami Ave, 33128 — U.S. District Court (federal civil & criminal cases, federal jury service)."],
    bankruptcy: ["C. Clyde Atkins U.S. Courthouse", "301 N. Miami Ave, 33128 — U.S. Bankruptcy Court, Southern District of Florida."],
    family: ["Lawson E. Thomas Courthouse Center", "175 NW 1st Ave, 33128 — Family Court Division and domestic-violence filings (mezzanine)."],
    probate: ["Lawson E. Thomas Courthouse Center — 14th floor", "175 NW 1st Ave, 33128 — Probate & Mental Health filings, wills for deposit, certified copies."],
    recorder: ["Courthouse East", "22 NW 1st St, 33128 — County Recorder's Office (deeds, mortgages, official records), 1st floor."],
    juvenile: ["Miami-Dade Children's Courthouse", "155 NW 3rd St, 33128 — juvenile and dependency matters."],
    civil: ["Miami-Dade County Courthouse (just outside 33128)", "73 W. Flagler St, 33130 — circuit & county civil; new suits filed in Room 137."],
    criminal: ["Richard E. Gerstein Justice Building (outside 33128)", "1351 NW 12th St, 33125 — state criminal cases; some traffic/misdemeanor matters."],
    county: ["Stephen P. Clark Government Center", "111 NW 1st St, 33128 — Miami-Dade County government offices; Metrorail Government Center station below."]
  };
  var fsel = document.getElementById("finder-select"), fout = document.getElementById("finder-out");
  if (fsel && fout) fsel.addEventListener("change", function () {
    var r = FINDER[fsel.value]; if (!r) { fout.innerHTML = ""; return; }
    fout.innerHTML = '<b class="big">' + r[0] + '</b>' + r[1] + '<br><small>Always confirm room, floor and hours on your notice or the official court website before you go.</small>';
  });

  /* ---------- Deadline calculator ---------- */
  function nthDow(y, m, dow, n) { var d = new Date(y, m, 1); var add = (dow - d.getDay() + 7) % 7; return new Date(y, m, 1 + add + (n - 1) * 7); }
  function lastDow(y, m, dow) { var d = new Date(y, m + 1, 0); return new Date(y, m, d.getDate() - ((d.getDay() - dow + 7) % 7)); }
  function observed(d) { var w = d.getDay(); if (w === 6) return new Date(d.getFullYear(), d.getMonth(), d.getDate() - 1); if (w === 0) return new Date(d.getFullYear(), d.getMonth(), d.getDate() + 1); return d; }
  function holidays(y) {
    var h = [observed(new Date(y, 0, 1)), nthDow(y, 0, 1, 3), nthDow(y, 1, 1, 3), lastDow(y, 4, 1), observed(new Date(y, 5, 19)), observed(new Date(y, 6, 4)), nthDow(y, 8, 1, 1), nthDow(y, 9, 1, 2), observed(new Date(y, 10, 11)), nthDow(y, 10, 4, 4), new Date(y, 10, nthDow(y, 10, 4, 4).getDate() + 1), observed(new Date(y, 11, 25))];
    return h.map(function (d) { return d.toDateString(); });
  }
  function isHoliday(d) { return holidays(d.getFullYear()).indexOf(d.toDateString()) > -1; }
  function isCourtClosed(d) { return d.getDay() === 0 || d.getDay() === 6 || isHoliday(d); }
  var dl = document.getElementById("deadline-form");
  if (dl) dl.addEventListener("submit", function (e) {
    e.preventDefault();
    var start = new Date(dl.start.value + "T12:00:00"), n = parseInt(dl.days.value, 10), mode = dl.mode.value, out = document.getElementById("deadline-out");
    if (isNaN(start) || !n) { out.textContent = "Enter a start date and number of days."; return; }
    var d = new Date(start), c = 0;
    while (c < n) { d.setDate(d.getDate() + 1); if (mode === "court" ? !isCourtClosed(d) : true) c++; }
    var rolled = false; while (isCourtClosed(d)) { d.setDate(d.getDate() + 1); rolled = true; }
    var left = Math.ceil((d - new Date()) / 864e5);
    out.innerHTML = '<b class="big">' + d.toLocaleDateString(undefined, { weekday: "long", year: "numeric", month: "long", day: "numeric" }) + '</b>' +
      (mode === "court" ? "Counting business days (weekends and federal holidays skipped). " : "Counting calendar days; ") +
      (rolled ? "The last day fell on a weekend/holiday, so it rolls to the next business day. " : "") +
      (left >= 0 ? "<strong>" + left + " day(s) from today.</strong>" : "<strong>That date has passed.</strong>") +
      '<br><small>Estimate only — Florida and federal rules have exceptions (service method, local holidays, court orders). Confirm with the clerk or an attorney.</small>';
  });

  /* ---------- Legal cost estimator ---------- */
  var ce = document.getElementById("cost-form");
  if (ce) ce.addEventListener("input", calcCost);
  function calcCost() {
    var rate = +ce.rate.value || 0, hrs = +ce.hours.value || 0, fees = +ce.fees.value || 0, ret = +ce.retainer.value || 0;
    var total = rate * hrs + fees;
    document.getElementById("cost-out").innerHTML = '<b class="big">$' + total.toLocaleString() + '</b>Estimated total (' + hrs + ' h × $' + rate + '/h + $' + fees.toLocaleString() + ' costs).' +
      (ret ? ' After a $' + ret.toLocaleString() + ' retainer you would owe about <strong>$' + Math.max(0, total - ret).toLocaleString() + '</strong> more.' : "") +
      '<br><small>Many injury lawyers work on contingency instead (no hourly fee; a percentage of any recovery).</small>';
  }
  if (ce) calcCost();

  /* ---------- Injury claim illustrator ---------- */
  var pi = document.getElementById("pi-form");
  function calcPI() {
    var med = +pi.med.value || 0, wages = +pi.wages.value || 0, prop = +pi.prop.value || 0, mult = +pi.mult.value || 1.5, fee = +pi.fee.value || 0;
    var econ = med + wages + prop, nonEcon = med * mult, gross = econ + nonEcon, net = gross * (1 - fee / 100);
    document.getElementById("pi-out").innerHTML = '<b class="big">$' + Math.round(gross).toLocaleString() + '</b>Illustrative gross value: economic losses $' + econ.toLocaleString() + ' + pain-and-suffering estimate $' + Math.round(nonEcon).toLocaleString() + ' (medical × ' + mult + ').<br>After a ' + fee + '% contingency fee: about <strong>$' + Math.round(net).toLocaleString() + '</strong> before medical liens and costs.' +
      '<br><small>This is the "multiplier method," a rough teaching heuristic — not a prediction. Fault, insurance limits and Florida\'s comparative-negligence rules can change outcomes dramatically.</small>';
  }
  if (pi) { pi.addEventListener("input", calcPI); calcPI(); }

  /* ---------- Court-day checklist ---------- */
  var CL = {
    base: ["Government-issued photo ID", "Your notice, summons or case number (printed and on your phone)", "Arrive 45 minutes early for security screening", "Leave knives, scissors, pepper spray and other prohibited items at home", "Phone fully charged — set to silent in the courtroom", "Pen and notepad", "Money/card for parking or a Metrorail fare"],
    hearing: ["Three copies of every document you plan to show (judge, other side, you)", "Photos, receipts, contracts, texts — printed and in date order", "Names and contact details of any witnesses", "A one-page timeline of what happened"],
    jury: ["Your jury summons with juror number", "A book or work that doesn't need Wi-Fi", "A sweater — courtrooms are cold", "Your employer's contact details if you need a service certificate"],
    family: ["Financial affidavit and supporting pay stubs/tax returns if required", "Proposed parenting plan, if any", "Child-care arrangements — children often are not allowed in courtrooms"],
    traffic: ["The citation", "Proof of insurance and registration", "Driving-school completion certificate, if you elected it"],
    recorder: ["Original signed document with notary block completed", "Correct recording fees (check current fee schedule)", "Return address / self-addressed envelope"]
  };
  var clf = document.getElementById("check-form");
  if (clf) clf.addEventListener("change", buildCL);
  function buildCL() {
    var items = CL.base.slice(), t = clf.purpose.value; if (CL[t]) items = items.concat(CL[t]);
    document.getElementById("check-out").innerHTML = '<ul class="checklist">' + items.map(function (i, k) { return '<li><label style="font-weight:400"><input type="checkbox" id="c' + k + '">' + i + '</label></li>'; }).join("") + '</ul><button class="btn btn-ghost" type="button" onclick="window.print()">🖨 Print checklist</button>';
  }
  if (clf) buildCL();

  /* ---------- Status / last refreshed ---------- */
  var st = document.querySelector("[data-updated]");
  if (st) fetch(BASE + "assets/data/status.json", { cache: "no-store" }).then(function (r) { return r.json(); }).then(function (j) {
    st.textContent = "Content checked " + new Date(j.updated).toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" });
    var tip = document.querySelector("[data-tip]"); if (tip && j.tip) tip.textContent = j.tip;
  }).catch(function () {});

  /* ---------- Year ---------- */
  document.querySelectorAll("[data-year]").forEach(function (y) { y.textContent = new Date().getFullYear(); });

  /* ---------- Optional donation links (set in config.js) ---------- */
  document.querySelectorAll("[data-pay]").forEach(function (a) {
    var url = (SITE.donate || {})[a.getAttribute("data-pay")];
    if (url) { a.href = url; a.target = "_blank"; a.rel = "noopener"; }
  });
})();
