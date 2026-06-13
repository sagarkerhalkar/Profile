from pathlib import Path
import json, base64, mimetypes
from playwright.sync_api import sync_playwright
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/Sagar_Kerhalkar_IT_Infrastructure_DevOps_Leader_CV.pdf'
profile=json.loads((ROOT/'assets/profile.json').read_text(encoding='utf-8'))
html=(ROOT/'cv/index.html').read_text(encoding='utf-8')
css=(ROOT/'assets/cv.css').read_text(encoding='utf-8')
js=(ROOT/'assets/cv.js').read_text(encoding='utf-8')
img=(ROOT/profile['avatarImage']).read_bytes()
data_uri='data:image/webp;base64,'+base64.b64encode(img).decode()
profile_inline=dict(profile);profile_inline['avatarImage']=data_uri;profile_inline['profileImage']=data_uri
html=html.replace('<link rel="stylesheet" href="../assets/cv.css">',f'<style>{css}</style>')
html=html.replace('<script src="../assets/cv.js"></script>',f'<script>window.__PROFILE_DATA__={json.dumps(profile_inline)};</script><script>{js}</script>')
with sync_playwright() as p:
    exe='/usr/bin/chromium' if Path('/usr/bin/chromium').exists() else p.chromium.executable_path
    b=p.chromium.launch(headless=True,executable_path=exe)
    page=b.new_page(viewport={'width':1280,'height':900})
    page.set_content(html,wait_until='load')
    page.wait_for_selector('.cv-sheet:nth-child(2)')
    page.emulate_media(media='print')
    page.pdf(path=str(OUT),format='A4',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'},prefer_css_page_size=True)
    b.close()
r=PdfReader(str(OUT))
if len(r.pages)!=2: raise SystemExit(f'Expected exactly 2 pages, got {len(r.pages)}')
text='\n'.join((x.extract_text() or '') for x in r.pages)
for required in ['Sagar Kerhalkar','Professional Experience','Professional Certifications','Selected Engineering Projects']:
    if required.casefold() not in text.casefold(): raise SystemExit(f'Missing PDF text: {required}')
print(f'PASS generated {OUT.name}: {len(r.pages)} A4 pages, {OUT.stat().st_size} bytes')
