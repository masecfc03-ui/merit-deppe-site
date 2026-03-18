#!/usr/bin/env python3
"""
Generates 5 clean, ATS-friendly, print-to-PDF resume HTML files for Merit Deppe.
Harvard Career Services standards: active verbs, quantified results, one page, clean format.
"""

CONTACT = """
<div class="contact">
  <span>(469) 520-6214</span>
  <span class="sep">|</span>
  <span>meritmdeppe@gmail.com</span>
  <span class="sep">|</span>
  <span>Dallas, TX</span>
  <span class="sep">|</span>
  <span>linkedin.com/in/merit-deppe</span>
</div>
""".strip()

EDUCATION = """
<div class="entry">
  <div class="entry-head">
    <span class="org">Texas A&amp;M University</span>
    <span class="date">May 2025</span>
  </div>
  <div class="entry-sub">B.S. Communication &nbsp;|&nbsp; Certificate in Health Communication &nbsp;|&nbsp; College Station, TX</div>
  <div class="entry-sub">Kappa Delta Sorority — Recruited 76 prospective members, converted 11; selected as lead recruitment representative 4 consecutive years</div>
</div>
""".strip()

CERTS = """
<div class="cert-grid">
  <span class="cert">PTCB Certified Pharmacy Technician (CPhT)</span>
  <span class="cert">APhA Immunization-Certified Pharmacy Technician</span>
  <span class="cert">Texas State Board of Pharmacy — Registered Technician</span>
  <span class="cert">CNPR — Certified National Pharmaceutical Representative (In Progress)</span>
  <span class="cert">Adult &amp; Pediatric First Aid / CPR / AED — American Red Cross</span>
</div>
""".strip()

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Inter', 'Calibri', Arial, sans-serif;
  font-size: 10.5pt;
  color: #111;
  background: #fff;
  max-width: 8.5in;
  margin: 0 auto;
  padding: 0.6in 0.7in;
  line-height: 1.45;
}

.print-btn {
  position: fixed; top: 12px; right: 12px;
  background: #1a56db; color: #fff;
  border: none; border-radius: 6px;
  padding: 8px 18px; font-size: 13px; font-weight: 600;
  cursor: pointer; z-index: 99;
  font-family: inherit;
}
.print-btn:hover { background: #1245b8; }

h1.name {
  font-size: 22pt;
  font-weight: 700;
  letter-spacing: -0.3px;
  color: #111;
  margin-bottom: 3px;
}

.tagline {
  font-size: 10pt;
  font-weight: 600;
  color: #1a56db;
  letter-spacing: 1.2px;
  text-transform: uppercase;
  margin-bottom: 6px;
}

.contact {
  font-size: 9.5pt;
  color: #444;
  margin-bottom: 10px;
}
.contact .sep { margin: 0 6px; color: #bbb; }

hr.divider {
  border: none;
  border-top: 2px solid #111;
  margin: 6px 0 10px;
}

h2.section {
  font-size: 9.5pt;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  color: #111;
  border-bottom: 1px solid #111;
  padding-bottom: 2px;
  margin: 12px 0 6px;
}

.summary {
  font-size: 10pt;
  color: #222;
  line-height: 1.55;
  margin-bottom: 2px;
}

.entry { margin-bottom: 8px; }

.entry-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.org {
  font-weight: 700;
  font-size: 10.5pt;
  color: #111;
}

.role {
  font-weight: 600;
  font-size: 10pt;
  color: #1a56db;
  margin-top: 1px;
}

.date {
  font-size: 9.5pt;
  color: #555;
  white-space: nowrap;
  margin-left: 8px;
}

.entry-sub {
  font-size: 9.5pt;
  color: #444;
  margin-top: 1px;
}

ul.bullets {
  margin: 4px 0 0 14px;
  padding: 0;
  list-style: disc;
}
ul.bullets li {
  font-size: 10pt;
  color: #222;
  margin-bottom: 2.5px;
  line-height: 1.45;
}
ul.bullets li strong { color: #111; }

.cert-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 4px 16px;
}
.cert {
  font-size: 9.5pt;
  color: #222;
  padding-left: 10px;
  position: relative;
}
.cert::before {
  content: "▸";
  position: absolute;
  left: 0;
  color: #1a56db;
  font-size: 8pt;
  top: 1px;
}

@media print {
  .print-btn { display: none !important; }
  body { padding: 0.5in 0.6in; }
  @page { size: letter; margin: 0; }
  a { color: inherit !important; text-decoration: none !important; }
}
""".strip()

def page(title, tagline, summary, experience_html):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Merit Deppe — {title}</title>
<style>{CSS}</style>
</head>
<body>
<button class="print-btn" onclick="window.print()">⬇ Save as PDF</button>

<h1 class="name">MERIT DEPPE</h1>
<div class="tagline">{tagline}</div>
{CONTACT}
<hr class="divider">

<h2 class="section">Professional Summary</h2>
<p class="summary">{summary}</p>

<h2 class="section">Experience</h2>
{experience_html}

<h2 class="section">Education</h2>
{EDUCATION}

<h2 class="section">Certifications &amp; Credentials</h2>
{CERTS}

</body>
</html>"""


# ═══════════════════════════════════════════════════
#  PHARMA SALES
# ═══════════════════════════════════════════════════
pharma_summary = (
    "Healthcare professional with 4+ years of patient-facing clinical experience "
    "entering pharmaceutical sales with clinical credentials most entry-level candidates "
    "lack. PTCB-certified with deep working knowledge of formulary structures, prior "
    "authorization workflows, and payer systems. Demonstrated ability to drive measurable "
    "volume outcomes through patient education and objection management. Texas A&amp;M "
    "Communication graduate; CNPR in progress."
)
pharma_exp = """
<div class="entry">
  <div class="entry-head">
    <span class="org">CVS Health</span>
    <span class="date">Jan 2024 – Present</span>
  </div>
  <div class="role">Immunizer &amp; Pharmacy Technician — Dallas, TX</div>
  <ul class="bullets">
    <li>Delivered one-on-one patient consultations on vaccine indications, contraindications, and post-care — structurally identical to pharmaceutical rep product detailing with HCPs</li>
    <li><strong>Drove 20+ dose increase in flu season vaccination volume</strong> through proactive patient education and evidence-based hesitancy management</li>
    <li>Administered <strong>45+ vaccines</strong> in a single flu season; counseled patients on mechanism, benefit-risk profile, and adherence expectations</li>
    <li>Navigated formulary restrictions, prior authorization denials, and benefit investigations in real time — core payer-side knowledge for pharmaceutical sales conversations</li>
  </ul>
</div>
<div class="entry">
  <div class="entry-head">
    <span class="org">Las Colinas Pharmacy (Independent)</span>
    <span class="date">Mar 2021 – Dec 2024</span>
  </div>
  <div class="role">Pharmacy Technician — Irving, TX</div>
  <ul class="bullets">
    <li>Built and maintained <strong>3+ year longitudinal patient relationships</strong> through consistent, personalized communication — foundational territory management skill</li>
    <li>Educated patients on complex medication regimens, drug interactions, and adherence strategies directly applicable to HCP product detailing</li>
    <li>Resolved insurance disputes, PA denials, and coverage gaps independently across patients, prescribers, and payers simultaneously</li>
    <li>Operated in an independent pharmacy environment with higher case complexity than chain retail, developing autonomous clinical problem-solving skills</li>
  </ul>
</div>
<div class="entry">
  <div class="entry-head">
    <span class="org">Golf Ranch</span>
    <span class="date">Aug 2019 – Mar 2020</span>
  </div>
  <div class="role">Sales Associate — Richardson, TX</div>
  <ul class="bullets">
    <li>Upsold premium packages through needs assessment and benefit-led recommendations; managed POS and provided customer service in a fast-paced retail environment</li>
  </ul>
</div>"""

# ═══════════════════════════════════════════════════
#  MEDICAL DEVICE
# ═══════════════════════════════════════════════════
device_summary = (
    "Healthcare professional with 4+ years inside clinical environments — pharmacies, "
    "immunization clinics, and patient care settings. Proven ability to communicate "
    "technical product information, navigate HCP workflow, and build lasting clinical "
    "relationships. Texas A&amp;M Communication graduate with Health Communication "
    "Certificate. PTCB-certified. Targeting entry-level medical device sales where "
    "clinical credibility and a competitive drive deliver immediate territory value."
)
device_exp = """
<div class="entry">
  <div class="entry-head">
    <span class="org">CVS Health</span>
    <span class="date">Jan 2024 – Present</span>
  </div>
  <div class="role">Immunizer &amp; Pharmacy Technician — Dallas, TX</div>
  <ul class="bullets">
    <li>Execute clinical procedures requiring technical precision and protocol compliance — direct parallel to medical device handling and sterile technique in OR/clinical settings</li>
    <li>Educate patients on product mechanism, expected outcomes, risks, and post-procedure care — mirrors device rep product detailing with HCPs and clinical staff</li>
    <li><strong>Grew immunization program volume 20+ doses above prior year</strong> through education-first patient engagement — the same model that drives device adoption</li>
    <li>Built rapid credibility alongside pharmacists and nurses within clinical team hierarchies; consistently trusted with independent clinical responsibilities</li>
  </ul>
</div>
<div class="entry">
  <div class="entry-head">
    <span class="org">Las Colinas Pharmacy (Independent)</span>
    <span class="date">Mar 2021 – Dec 2024</span>
  </div>
  <div class="role">Pharmacy Technician — Irving, TX</div>
  <ul class="bullets">
    <li>Managed complex, high-stakes patient interactions requiring clinical accuracy, rapid rapport-building, and precise multi-system documentation</li>
    <li>Coordinated across patients, prescribers, and insurers simultaneously — multi-stakeholder management directly applicable to device account navigation</li>
    <li>Built a <strong>3+ year repeat-engagement reputation</strong> through service reliability — the foundation of any sustainable device sales territory</li>
  </ul>
</div>
<div class="entry">
  <div class="entry-head">
    <span class="org">Texas A&amp;M University — Orientation Program</span>
    <span class="date">2022</span>
  </div>
  <div class="role">Orientation Camp Counselor — College Station, TX</div>
  <ul class="bullets">
    <li>Selected as peer educator and group facilitator for incoming students; demonstrated leadership, inclusion, and structured program delivery under high visibility</li>
  </ul>
</div>"""

# ═══════════════════════════════════════════════════
#  SPECIALTY PHARMACY
# ═══════════════════════════════════════════════════
specialty_summary = (
    "PTCB-certified pharmacy technician with 4+ years of specialty-adjacent clinical "
    "experience: complex prior authorization management, insurance exception resolution, "
    "payer navigation, and longitudinal patient counseling on high-cost therapy regimens. "
    "Understands the specialty pharmacy access model from the inside — PA workflows, "
    "formulary exceptions, and chronic disease patient management. CNPR in progress. "
    "Entering specialty pharmacy sales with clinical fluency that takes most reps years to develop."
)
specialty_exp = """
<div class="entry">
  <div class="entry-head">
    <span class="org">CVS Health</span>
    <span class="date">Jan 2024 – Present</span>
  </div>
  <div class="role">Immunizer &amp; Pharmacy Technician — Dallas, TX</div>
  <ul class="bullets">
    <li>Resolved coverage barriers in real time: formulary exceptions, benefit investigations, coordination of benefits, and step therapy requirements</li>
    <li>Managed high-complexity patient interactions under volume pressure requiring clinical accuracy, rapid trust-building, and precise documentation</li>
    <li><strong>Grew vaccination program 20+ doses above prior year</strong> through patient education-first engagement model directly applicable to specialty adherence support</li>
  </ul>
</div>
<div class="entry">
  <div class="entry-head">
    <span class="org">Las Colinas Pharmacy (Independent)</span>
    <span class="date">Mar 2021 – Dec 2024</span>
  </div>
  <div class="role">Pharmacy Technician — Irving, TX</div>
  <ul class="bullets">
    <li>Supported <strong>chronic disease patient adherence over 3+ year relationships</strong> — exactly mirrors the long-term patient management model in specialty pharmacy</li>
    <li>End-to-end access management: prescriber communication, insurance navigation, patient counseling, and resolution documentation — all independent</li>
    <li>Operated in an independent pharmacy environment with higher case complexity than chain retail, closely mirroring specialty pharmacy's operating model</li>
    <li>Navigated prior authorizations, denial appeals, and formulary exceptions across multiple payers with zero escalation to pharmacist required</li>
  </ul>
</div>"""

# ═══════════════════════════════════════════════════
#  ACCOUNT MANAGER
# ═══════════════════════════════════════════════════
account_summary = (
    "Healthcare professional with 4+ years of relationship-first account management in "
    "clinical settings — managing patient accounts, resolving multi-stakeholder access issues, "
    "and building long-term trust across a complex and diverse client base. Texas A&amp;M "
    "Communication graduate with Health Communication Certificate. Recognized for autonomous "
    "problem-solving, interpersonal precision, and consistent performance in high-volume "
    "environments."
)
account_exp = """
<div class="entry">
  <div class="entry-head">
    <span class="org">CVS Health</span>
    <span class="date">Jan 2024 – Present</span>
  </div>
  <div class="role">Patient Relations &amp; Immunization Specialist — Dallas, TX</div>
  <ul class="bullets">
    <li>Serve as primary patient account contact — coordinating between patients, clinical staff, and insurers to resolve access and coverage issues at scale</li>
    <li><strong>Grew immunization program 20+ doses above prior year</strong> through proactive account engagement and structured patient education</li>
    <li>Maintain quality across a high-volume patient panel while managing concurrent pharmacy operations and clinical responsibilities</li>
  </ul>
</div>
<div class="entry">
  <div class="entry-head">
    <span class="org">Las Colinas Pharmacy (Independent)</span>
    <span class="date">Mar 2021 – Dec 2024</span>
  </div>
  <div class="role">Pharmacy Technician &amp; Patient Account Lead — Irving, TX</div>
  <ul class="bullets">
    <li>Managed full patient account lifecycle: onboarding, ongoing education, issue resolution, and <strong>long-term retention over a 3+ year tenure</strong></li>
    <li>Resolved complex, multi-party issues across patients, insurers, and prescribers — independently and without escalation</li>
    <li>Contributed to a repeat-visit culture through service consistency and personalized relationship management</li>
  </ul>
</div>
<div class="entry">
  <div class="entry-head">
    <span class="org">Kappa Delta Sorority, Texas A&amp;M — Panhellenic Recruitment</span>
    <span class="date">2021 – 2025</span>
  </div>
  <div class="role">Lead Recruitment Representative — College Station, TX</div>
  <ul class="bullets">
    <li>Selected as lead representative for competitive multi-round recruitment 4 consecutive years; managed <strong>76 prospective relationships, converted 11 to members</strong></li>
    <li>Demonstrated consultative persuasion, rapport-building, and structured account development across a multi-week, high-stakes process</li>
  </ul>
</div>"""

# ═══════════════════════════════════════════════════
#  CLINICAL LIAISON
# ═══════════════════════════════════════════════════
clinical_summary = (
    "Clinical healthcare professional with 4+ years of patient-facing experience and a "
    "rare dual credential: B.S. Communication + Certificate in Health Communication from "
    "Texas A&amp;M, paired with PTCB certification and immunization credentials. Formally "
    "trained in message framing, health literacy models, and behavior change theory. "
    "Experienced in adapting clinical education to diverse patient populations in real time. "
    "Targeting clinical liaison or healthcare education roles where strategic communication "
    "bridges clinical expertise and patient or provider understanding."
)
clinical_exp = """
<div class="entry">
  <div class="entry-head">
    <span class="org">CVS Health</span>
    <span class="date">Jan 2024 – Present</span>
  </div>
  <div class="role">Immunizer &amp; Patient Education Specialist — Dallas, TX</div>
  <ul class="bullets">
    <li>Delivered structured patient education on vaccine science, benefit-risk, and post-care — adapted in real time to each patient's health literacy level and emotional state</li>
    <li>Navigated vaccine hesitancy using empathy-first, evidence-based communication aligned with APhA and motivational interviewing frameworks</li>
    <li><strong>Administered 45+ vaccines in a single flu season</strong>; grew program volume 20+ doses above prior year through education-first engagement</li>
    <li>Coordinated with clinical team to ensure accurate, consistent patient messaging across the full care team</li>
  </ul>
</div>
<div class="entry">
  <div class="entry-head">
    <span class="org">Las Colinas Pharmacy (Independent)</span>
    <span class="date">Mar 2021 – Dec 2024</span>
  </div>
  <div class="role">Patient Education &amp; Pharmacy Technician — Irving, TX</div>
  <ul class="bullets">
    <li>Primary patient education resource for a chronic disease population — medication counseling, insurance navigation, and adherence support over <strong>3+ year relationships</strong></li>
    <li>Built longitudinal educational relationships that supported sustained health behavior change across multi-year timeframes</li>
  </ul>
</div>
<div class="entry">
  <div class="entry-head">
    <span class="org">Texas A&amp;M University — Orientation Program</span>
    <span class="date">2022</span>
  </div>
  <div class="role">Orientation Camp Counselor — College Station, TX</div>
  <ul class="bullets">
    <li>Facilitated peer education and structured group communication for incoming students; selected for leadership, inclusion skills, and program delivery under a spotlight</li>
  </ul>
</div>"""

# ═══════════════════════════════════════════════════
#  BUILD ALL FILES
# ═══════════════════════════════════════════════════
import os
base = "/Users/masonmathis/.openclaw/workspace/merit-deppe"

files = [
    ("pharma-resume.html",    "Pharmaceutical Sales Representative",  "PHARMA SALES REPRESENTATIVE",    pharma_summary,    pharma_exp),
    ("device-resume.html",    "Medical Device Sales Representative",   "MEDICAL DEVICE SALES",           device_summary,    device_exp),
    ("specialty-resume.html", "Specialty Pharmacy Sales",              "SPECIALTY PHARMACY SALES",       specialty_summary, specialty_exp),
    ("account-resume.html",   "Healthcare Account Manager",            "HEALTHCARE ACCOUNT MANAGER",     account_summary,   account_exp),
    ("clinical-resume.html",  "Clinical Liaison / Healthcare Educator","CLINICAL LIAISON",               clinical_summary,  clinical_exp),
]

for fname, title, tagline, summary, exp in files:
    html = page(title, tagline, summary, exp)
    path = os.path.join(base, fname)
    with open(path, "w") as f:
        f.write(html)
    print(f"✅ {fname}")

print(f"\nAll 5 resumes built in {base}/")
