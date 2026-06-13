from pathlib import Path
import json, base64, os
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
SHOTS = ROOT / 'test_screenshots'
SHOTS.mkdir(exist_ok=True)
PROFILE = json.loads((ROOT / 'assets/profile.json').read_text(encoding='utf-8'))
STORAGE_SHIM = "<script>window.__testLocalStorage={_:{'sk_theme_v7':'dark'},getItem(k){return this._[k]??null},setItem(k,v){this._[k]=String(v)},removeItem(k){delete this._[k]},clear(){this._={}}};window.__testSessionStorage={_:{},getItem(k){return this._[k]??null},setItem(k,v){this._[k]=String(v)},removeItem(k){delete this._[k]},clear(){this._={}}};</script>"

def test_js(js):
    return js.replace('localStorage','window.__testLocalStorage').replace('sessionStorage','window.__testSessionStorage')


def data_uri(path: Path, mime='image/webp'):
    return f'data:{mime};base64,' + base64.b64encode(path.read_bytes()).decode()


def inline_home():
    html = (ROOT / 'index.html').read_text(encoding='utf-8')
    css = (ROOT / 'assets/site.css').read_text(encoding='utf-8')
    js = (ROOT / 'assets/site.js').read_text(encoding='utf-8')
    p = dict(PROFILE)
    p['profileImage'] = data_uri(ROOT / PROFILE['profileImage'])
    p['avatarImage'] = data_uri(ROOT / PROFILE['avatarImage'])
    html = html.replace('<link rel="stylesheet" href="assets/site.css">', f'<style>{css}</style>')
    html = html.replace('src="assets/sagar-portrait-v7.webp"', f'src="{p["profileImage"]}"')
    html = html.replace('<script src="assets/site.js"></script>', STORAGE_SHIM + f'<script>window.__PROFILE_DATA__={json.dumps(p)};</script><script>{test_js(js)}</script>')
    return html


def inline_cv():
    html = (ROOT / 'cv/index.html').read_text(encoding='utf-8')
    css = (ROOT / 'assets/cv.css').read_text(encoding='utf-8')
    js = (ROOT / 'assets/cv.js').read_text(encoding='utf-8')
    p = dict(PROFILE)
    p['profileImage'] = data_uri(ROOT / PROFILE['profileImage'])
    p['avatarImage'] = data_uri(ROOT / PROFILE['avatarImage'])
    html = html.replace('<link rel="stylesheet" href="../assets/cv.css">', f'<style>{css}</style>')
    html = html.replace('<script src="../assets/cv.js"></script>', STORAGE_SHIM + f'<script>window.__PROFILE_DATA__={json.dumps(p)};</script><script>{test_js(js)}</script>')
    return html


def inline_admin():
    html = (ROOT / 'admin/index.html').read_text(encoding='utf-8')
    css = (ROOT / 'assets/admin.css').read_text(encoding='utf-8')
    js = (ROOT / 'assets/admin.js').read_text(encoding='utf-8')
    p = dict(PROFILE)
    p['profileImage'] = data_uri(ROOT / PROFILE['profileImage'])
    p['avatarImage'] = data_uri(ROOT / PROFILE['avatarImage'])
    html = html.replace('<link rel="stylesheet" href="../assets/admin.css">', f'<style>{css}</style>')
    html = html.replace('<script src="../assets/admin.js"></script>', STORAGE_SHIM + f'<script>window.__PROFILE_DATA__={json.dumps(p)};</script><script>{test_js(js)}</script>')
    return html


def inline_project():
    html = (ROOT / 'projects/systemhealthmonitor/index.html').read_text(encoding='utf-8')
    css = (ROOT / 'assets/site.css').read_text(encoding='utf-8')
    return html.replace('<link rel="stylesheet" href="../../assets/site.css">', f'<style>{css}</style>')


def launch(browser_type, name):
    if name == 'chromium' and Path('/usr/bin/chromium').exists():
        return browser_type.launch(headless=True, executable_path='/usr/bin/chromium')
    exe = Path(browser_type.executable_path)
    if not exe.exists():
        print(f'SKIP {name} locally: browser executable is not installed. CI installs and runs this engine.')
        return None
    return browser_type.launch(headless=True)


viewports = [
    ('desktop-1920', 1920, 1080),
    ('desktop-1440', 1440, 900),
    ('laptop-1366', 1366, 768),
    ('tablet-1024', 1024, 768),
    ('ipad-768', 768, 1024),
    ('iphone-430', 430, 932),
    ('iphone-390', 390, 844),
    ('iphone-se', 375, 667),
    ('mobile-360', 360, 800),
]

results = []
home = inline_home()

with sync_playwright() as p:
    available = [('chromium', p.chromium), ('firefox', p.firefox), ('webkit', p.webkit)]
    requested = {x.strip() for x in os.getenv('PORTFOLIO_BROWSERS', 'chromium,firefox,webkit').split(',') if x.strip()}
    for browser_name, browser_type in [x for x in available if x[0] in requested]:
        browser = launch(browser_type, browser_name)
        if not browser:
            continue
        targets = viewports if browser_name == 'chromium' else [('desktop-1440', 1440, 900), ('iphone-390', 390, 844)]
        for name, width, height in targets:
            page = browser.new_page(
                viewport={'width': width, 'height': height},
                device_scale_factor=1,
                is_mobile=width < 600,
                has_touch=width < 600,
            )
            page.set_default_timeout(10000)
            errors = []
            page.on('console', lambda msg: errors.append(msg.text) if msg.type == 'error' else None)
            page.on('pageerror', lambda exc: errors.append(str(exc)))
            page.set_content(home, wait_until='load')
            page.wait_for_selector('.hero-title span:nth-child(2)', state='attached')
            page.wait_for_function("document.querySelector('.hero-title span:nth-child(2)').textContent.length > 0")
            page.evaluate("document.querySelectorAll('.reveal').forEach(x=>x.classList.add('visible'))")
            metrics = page.evaluate("""() => {
                const d=document.documentElement;
                const t=document.querySelector('.hero-title');
                const s=[...t.querySelectorAll('span')];
                return {
                  overflow:d.scrollWidth-d.clientWidth,
                  titleLines:s.map(x=>({scroll:x.scrollWidth,client:x.clientWidth,height:x.getBoundingClientRect().height})),
                  font:parseFloat(getComputedStyle(t).fontSize),
                  orbit:document.querySelectorAll('.orbit-label').length,
                  bodyFont:parseFloat(getComputedStyle(document.body).fontSize),
                  contactItems:document.querySelectorAll('.contact-item').length,
                  contactIcons:document.querySelectorAll('.contact-item svg').length,
                  footerIcons:document.querySelectorAll('.footer-contact svg').length,
                  phoneHref:document.querySelector('[data-link="phone"]')?.getAttribute('href')||''
                };
            }""")
            assert metrics['overflow'] <= 1, (browser_name, name, metrics)
            assert metrics['orbit'] == 6
            assert metrics['contactItems'] == 6, (browser_name, name, metrics)
            assert metrics['contactIcons'] == 6, (browser_name, name, metrics)
            assert metrics['footerIcons'] >= 6, (browser_name, name, metrics)
            assert metrics['phoneHref'].startswith('tel:+918105977226'), (browser_name, name, metrics)
            assert all(x['scroll'] <= x['client'] + 2 for x in metrics['titleLines']), (browser_name, name, metrics)
            assert metrics['font'] >= 20, (browser_name, name, metrics['font'])
            assert metrics['bodyFont'] >= 16
            if width < 600:
                page.click('#menuBtn')
                assert page.locator('#mobileNav').evaluate("e=>e.classList.contains('open')")
                page.click('#menuBtn')
                assert not page.locator('#mobileNav').evaluate("e=>e.classList.contains('open')")
            page.click('#themeBtn')
            assert page.locator('html').get_attribute('data-theme') == 'light'
            assert not errors, (browser_name, name, errors)
            if browser_name == 'chromium' and name in ['desktop-1440', 'ipad-768', 'iphone-390']:
                page.screenshot(path=str(SHOTS / f'{name}-light.png'), full_page=False)
                if name == 'iphone-390':
                    page.locator('.ops-console').screenshot(path=str(SHOTS / 'iphone-390-console-light.png'))
                page.click('#themeBtn')
                page.screenshot(path=str(SHOTS / f'{name}-dark.png'), full_page=False)
                if name == 'iphone-390':
                    page.locator('.ops-console').screenshot(path=str(SHOTS / 'iphone-390-console-dark.png'))
            results.append({'browser': browser_name, 'viewport': name, **metrics})
            page.close()
        browser.close()

    browser = launch(p.chromium, 'chromium')
    assert browser
    for html, selector, label in [
        (inline_cv(), '.cv-sheet:nth-child(2)', 'cv'),
        (inline_admin(), '#loginCard', 'admin'),
        (inline_project(), '.case-hero', 'project'),
    ]:
        page = browser.new_page(viewport={'width': 1280, 'height': 900})
        page.set_default_timeout(10000)
        errors = []
        page.on('pageerror', lambda exc: errors.append(str(exc)))
        page.set_content(html, wait_until='load')
        page.wait_for_selector(selector, state='attached')
        assert not errors, (label, errors)
        page.close()

    page = browser.new_page(viewport={'width': 1280, 'height': 900})
    page.set_default_timeout(10000)
    page.set_content(inline_cv(), wait_until='load')
    page.wait_for_selector('.cv-sheet:nth-child(2)', state='attached')
    dims = page.evaluate("""() => [...document.querySelectorAll('.cv-sheet')].map(x=>({
        scroll:x.scrollHeight,client:x.clientHeight,w:x.getBoundingClientRect().width,h:x.getBoundingClientRect().height
    }))""")
    assert len(dims) == 2
    assert all(x['scroll'] <= x['client'] + 2 for x in dims), dims
    page.close()
    browser.close()

(ROOT / 'test-results.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
print('PASS V7 responsive matrix, six-label 3D orbit, international contact icons, light/dark theme, no overflow, admin, project and two-page CV.')
print('Browser engines executed:', sorted(set(x['browser'] for x in results)))
