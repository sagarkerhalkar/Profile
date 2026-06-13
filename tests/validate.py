from __future__ import annotations

from pathlib import Path
import json
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'index.html', '404.html', '_headers', 'robots.txt', 'sitemap.xml',
    'assets/site.css', 'assets/site.js', 'assets/profile.json',
    'assets/sagar-portrait-v7.webp', 'assets/sagar-avatar-v7.webp',
    'assets/cv.css', 'assets/cv.js',
    'cv/index.html', 'admin/index.html', 'assets/admin.css', 'assets/admin.js',
    'functions/api/profile.js', 'functions/api/admin/login.js',
    'functions/api/admin/logout.js', 'functions/api/admin/profile.js',
    'functions/lib/auth.js', 'projects/systemhealthmonitor/index.html',
    'scripts/generate_cv_pdf.py', 'tests/browser_matrix.py', 'tests/http_smoke.py',
    '.github/workflows/ci.yml', '.github/workflows/deploy-cloudflare.yml',
]
for rel in REQUIRED:
    path = ROOT / rel
    if not path.exists():
        raise SystemExit(f'Missing required file: {rel}')

profile = json.loads((ROOT / 'assets/profile.json').read_text(encoding='utf-8'))
assert profile['portfolioVersion'] == '7.0.0'
assert profile['heroTitleLine1'] == 'Building reliable infrastructure'
assert profile['heroTitleLine2'] == 'for always-on digital operations.'
assert profile['orbitLabels'] == ['Automation', 'Observability', 'Cloud', 'CI/CD', 'AI', 'DevOps']
assert profile['phone'] == '+91 81059 77226'
assert profile['email'] == 'sagarhatta@gmail.com'
assert profile['toolGroups'][0]['tools'] == ['Windows', 'Linux', 'Unix', 'Cloud', 'H/W Networking']
for tool in ['Docker', 'GitHub', 'CI/CD Tools', 'Monitoring Tools', 'Linux', 'PowerShell', 'Bash', 'Python', 'Kubernetes', 'System Administration', 'AI-assisted Automation']:
    assert tool in profile['toolGroups'][1]['tools'], tool
assert any(g['title'] == 'AI & Intelligent Automation' for g in profile['toolGroups'])
assert len(profile['projects']) == 4
assert len(profile['certifications']) >= 5
assert {'English', 'Hindi', 'Marathi'} <= {x['name'] if isinstance(x, dict) else x for x in profile['languages']}
assert any('Nagpur University' in x['institution'] for x in profile['education'])

html = (ROOT / 'index.html').read_text(encoding='utf-8')
css = (ROOT / 'assets/site.css').read_text(encoding='utf-8')
js = (ROOT / 'assets/site.js').read_text(encoding='utf-8')
for token in ['portraitOrbit', 'heroTitleLine1', 'heroTitleLine2', 'Download A4 CV', 'devops-infinity', 'icon-phone', 'icon-mail', 'icon-globe', 'icon-linkedin', 'icon-github', 'contact-directory', 'footer-contact']:
    assert token in html, token
for token in ['@media(prefers-reduced-motion:reduce)', '@keyframes orbitLabelV7', 'width:124px', 'contact-item', 'footer-contact', 'portrait-meta']:
    assert token in css, token
for token in ['renderOrbit', 'linkHref', "tel:${String(value)", 'data-contact-value']:
    assert token in js, token
assert (ROOT / profile['profileImage']).stat().st_size < 1_500_000

pdf = ROOT / 'assets/Sagar_Kerhalkar_IT_Infrastructure_DevOps_Leader_CV.pdf'
if not pdf.exists():
    raise SystemExit('Missing generated A4 CV PDF')
reader = PdfReader(str(pdf))
assert len(reader.pages) == 2, f'Expected exactly 2 CV pages, got {len(reader.pages)}'
for index, page in enumerate(reader.pages, start=1):
    width = float(page.mediabox.width)
    height = float(page.mediabox.height)
    assert abs(width - 595.28) < 2 and abs(height - 841.89) < 2, (index, width, height)
text = '\n'.join((page.extract_text() or '') for page in reader.pages)
for required_text in [
    'Sagar Kerhalkar', 'IT Infrastructure & DevOps Leader',
    'Professional Experience', 'Professional Certifications',
    'Education & Professional Training', 'Selected Engineering Projects',
    'CI/CD', 'Kubernetes', 'Nagpur University', '91 81059 77226',
]:
    assert required_text.casefold() in text.casefold(), required_text
assert 'localhost:' not in text.casefold()
assert pdf.stat().st_size > 300_000, 'CV PDF is unexpectedly small; embedded portrait may be missing.'

print('PASS V7 structure, six equal-size 3D orbit labels, international SVG contact system, AI tooling, responsive CSS and two-page A4 PDF validation.')
