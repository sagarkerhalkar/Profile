# Sagar Kerhalkar Global Portfolio V7.1

## Complete A-to-Z Run, Edit, Debug, Test, Build, Secure, Deploy, Back Up and Roll Back Guide

**Owner:** Sagar Kerhalkar  
**Professional title:** IT Infrastructure & DevOps Leader  
**Location:** Bhopal, India  
**Website:** `https://sagarkerhalkar.com`  
**Email:** `sagarhatta@gmail.com`  
**Mobile:** `+91 81059 77226`  
**Repository:** `https://github.com/sagarkerhalkar/Profile`  
**Target hosting:** Cloudflare Pages + Pages Functions + Workers KV

---

## 1. What V7 contains

V7 is a recruiter-focused infrastructure and DevOps leadership portfolio. It includes:

- a medium-sized, exactly two-line hero headline
- a professional observability-console visual
- a lightweight 3D portrait presentation
- six equal-size animated 3D orbit labels around the portrait: `Automation`, `Observability`, `Cloud`, `CI/CD`, `AI`, `DevOps`
- animated DevOps infinity symbol
- animated signal chart, tooling ribbon, platform list and tool cards
- dark and light themes
- responsive layouts for desktop, laptop, tablet, iPad and mobile widths
- four selected GitHub engineering projects
- experience, education, languages and certifications
- private owner-only profile editor
- international SVG contact directory for mobile, email, website, LinkedIn and GitHub
- phone and contact details in the portrait caption, contact section and footer
- generated direct-download CV PDF
- controlled two-page A4 CV layout
- automated Python, JavaScript, HTTP, responsive and PDF tests
- GitHub Actions CI and test-gated Cloudflare deployment workflow

The motion design uses CSS, SVG and small JavaScript interactions. It does not depend on heavy background video, WebGL or a large animation framework.

---

## 2. Approved hero and tooling content

### Hero headline

```text
Building reliable infrastructure
for always-on digital operations.
```

The two lines are separate HTML elements. The browser is not allowed to turn the topic into three or four lines.

### Supporting statement

```text
Engineering reliable digital operations with measurable outcomes.
```

### Platforms & Tooling

```text
Windows
Linux
Unix
Cloud
H/W Networking
```

### Core DevOps / Infrastructure Tools

```text
Docker
GitHub
CI/CD Tools
Monitoring Tools
Linux
PowerShell
Bash
Python
Kubernetes
System Administration
AI-assisted Automation
```

---

## 3. Project structure

```text
Sagar_Global_Profile_Redesign_v7_1/
├── index.html
├── 404.html
├── _headers
├── robots.txt
├── sitemap.xml
├── .nojekyll
├── .gitignore
├── README.md
├── README_A_TO_Z.md
├── TEST_REPORT.md
├── requirements-dev.txt
├── START_LOCAL_TEST.ps1
├── RUN_LOCAL_TESTS.ps1
├── BUILD_RELEASE.ps1
├── wrangler.toml.example
│
├── assets/
│   ├── site.css
│   ├── site.js
│   ├── profile.json
│   ├── admin.css
│   ├── admin.js
│   ├── cv.css
│   ├── cv.js
│   ├── sagar-portrait-v7.webp
│   ├── sagar-avatar-v7.webp
│   ├── portfolio-og-v7.jpg
│   └── Sagar_Kerhalkar_IT_Infrastructure_DevOps_Leader_CV.pdf
│
├── cv/
│   └── index.html
├── admin/
│   └── index.html
├── projects/
│   └── systemhealthmonitor/
│       └── index.html
│
├── functions/
│   ├── api/profile.js
│   ├── api/admin/login.js
│   ├── api/admin/logout.js
│   ├── api/admin/profile.js
│   └── lib/auth.js
│
├── scripts/
│   └── generate_cv_pdf.py
├── tests/
│   ├── validate.py
│   ├── http_smoke.py
│   └── browser_matrix.py
├── tools/
│   └── generate-admin-secrets.mjs
└── .github/workflows/
    ├── ci.yml
    └── deploy-cloudflare.yml
```

---

## 4. Software required on Windows

Install these tools:

```text
Git
Python 3.10 or newer
Node.js 20 or newer
Chrome, Edge or Chromium
```

Recommended:

```text
Visual Studio Code
PowerShell 5.1 or PowerShell 7
```

Check versions:

```powershell
git --version
python --version
py --version
node --version
npm --version
```

At least one of `python` or `py` must work.

---

## 5. Extract V7 safely

Do not replace the live site first. Extract V7 into a separate folder.

```powershell
$Zip = "$env:USERPROFILE\Downloads\Sagar_Global_Profile_Redesign_v7_1.zip"
$Folder = "C:\Temp\Sagar_Global_Profile_Redesign_v7_1"

Remove-Item $Folder -Recurse -Force -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Path $Folder -Force | Out-Null
Expand-Archive -Path $Zip -DestinationPath $Folder -Force
Set-Location $Folder
Get-ChildItem
```

Expected important files:

```powershell
Test-Path .\index.html
Test-Path .\assets\site.css
Test-Path .\assets\site.js
Test-Path .\assets\profile.json
Test-Path .\assets\Sagar_Kerhalkar_IT_Infrastructure_DevOps_Leader_CV.pdf
Test-Path .\cv\index.html
Test-Path .\admin\index.html
```

Every command should return `True`.

---

## 6. Start the portfolio locally

### Recommended helper command

```powershell
cd C:\Temp\Sagar_Global_Profile_Redesign_v7_1
powershell -ExecutionPolicy Bypass -File .\START_LOCAL_TEST.ps1
```

### Select another port

```powershell
powershell -ExecutionPolicy Bypass -File .\START_LOCAL_TEST.ps1 -Port 8090
```

### Manual equivalent

```powershell
cd C:\Temp\Sagar_Global_Profile_Redesign_v7_1
python -m http.server 8080 --bind 127.0.0.1
```

Or:

```powershell
py -m http.server 8080 --bind 127.0.0.1
```

Keep the PowerShell window open.

Open:

```text
Homepage:     http://127.0.0.1:8080/
CV page:      http://127.0.0.1:8080/cv/
Private edit: http://127.0.0.1:8080/admin/
Case study:   http://127.0.0.1:8080/projects/systemhealthmonitor/
Direct PDF:   http://127.0.0.1:8080/assets/Sagar_Kerhalkar_IT_Infrastructure_DevOps_Leader_CV.pdf
```

Stop the server:

```text
Ctrl + C
```

Do not test by double-clicking `index.html`. Use an HTTP server so JSON, paths and browser security behavior match deployment more closely.

---

## 7. Local private editor

Local test login:

```text
Username: sagar
Password: Profile@2026
```

This password is only for local testing. It is visible in client-side JavaScript and must not be treated as production security.

Local edits are saved in browser storage:

```text
sk_profile_preview_v7
```

Theme storage key:

```text
sk_theme_v7
```

Reset the local profile preview in DevTools Console:

```javascript
localStorage.removeItem('sk_profile_preview_v7');
location.reload();
```

Reset the theme:

```javascript
localStorage.removeItem('sk_theme_v7');
location.reload();
```

The public navigation does not link to `/admin/`.

---

## 8. Edit profile data directly

Default data file:

```text
assets/profile.json
```

Validate after editing:

```powershell
python -m json.tool .\assets\profile.json > $null
```

PowerShell alternative:

```powershell
Get-Content .\assets\profile.json -Raw | ConvertFrom-Json | Out-Null
Write-Host "PASS profile.json" -ForegroundColor Green
```

Do not add comments or trailing commas to JSON.

Important protected content:

```text
heroTitleLine1 = Building reliable infrastructure
heroTitleLine2 = for always-on digital operations.
orbitLabels = Automation, Observability, Cloud, CI/CD
```

---

## 9. Install test dependencies

Run once:

```powershell
cd C:\Temp\Sagar_Global_Profile_Redesign_v7_1
python -m pip install -r .\requirements-dev.txt
python -m playwright install chromium firefox webkit
```

Or use the all-in-one test command:

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_LOCAL_TESTS.ps1 -InstallDependencies
```

The browser installation can require several hundred megabytes.

---

## 10. Run every automated test

```powershell
cd C:\Temp\Sagar_Global_Profile_Redesign_v7_1
powershell -ExecutionPolicy Bypass -File .\RUN_LOCAL_TESTS.ps1
```

The script performs seven gates:

```text
1. Python syntax
2. JavaScript and Cloudflare Function syntax
3. Two-page A4 PDF generation
4. Static, content and PDF validation
5. Local HTTP 200 checks
6. Responsive browser matrix
7. Final validation
```

Expected final output:

```text
ALL PORTFOLIO V7 TESTS PASSED
```

---

## 11. Run individual debug tests

### Python syntax

```powershell
python -m py_compile `
  .\scripts\generate_cv_pdf.py `
  .\tests\validate.py `
  .\tests\http_smoke.py `
  .\tests\browser_matrix.py
```

### JavaScript syntax

```powershell
node --check .\assets\site.js
node --check .\assets\cv.js
node --check .\assets\admin.js
node --check .\functions\api\profile.js
node --check .\functions\api\admin\login.js
node --check .\functions\api\admin\logout.js
node --check .\functions\api\admin\profile.js
node --check .\functions\lib\auth.js
node --check .\tools\generate-admin-secrets.mjs
```

### Static and PDF validation

```powershell
python .\tests\validate.py
```

### HTTP test

```powershell
python .\tests\http_smoke.py
```

### Responsive browser test

```powershell
python .\tests\browser_matrix.py
```

The browser test writes:

```text
test-results.json
test_screenshots/desktop-1440-light.png
test_screenshots/desktop-1440-dark.png
test_screenshots/ipad-768-light.png
test_screenshots/ipad-768-dark.png
test_screenshots/iphone-390-light.png
test_screenshots/iphone-390-dark.png
test_screenshots/iphone-390-console-light.png
test_screenshots/iphone-390-console-dark.png
```

---

## 12. Responsive test matrix

The included matrix tests:

```text
1920 × 1080  wide desktop
1440 × 900   desktop
1366 × 768   laptop
1024 × 768   small laptop / landscape tablet
768 × 1024   iPad / tablet portrait
430 × 932    large iPhone / mobile
390 × 844    iPhone class
375 × 667    iPhone SE class
360 × 800    compact Android class
```

Checks include:

```text
No horizontal overflow
Hero remains exactly two lines
Hero text fits its column
Body text is at least 16 px
Six orbit labels exist
Mobile menu opens and closes
Light/dark theme switches
No browser console/page errors
CV contains two controlled A4 sheets
Admin and project pages render
```

Playwright CI installs and executes Chromium, Firefox and WebKit. WebKit gives Safari-like engine coverage, but final production testing on at least one physical iPhone is still recommended because no emulator can guarantee every physical device, OS version and browser setting.

---

## 13. Manual browser QA

Open Chrome or Edge:

```text
F12 -> Console
```

Reload. There should be no red errors.

Open:

```text
F12 -> Network
```

Reload and confirm `200` for:

```text
/
assets/site.css
assets/site.js
assets/profile.json
assets/sagar-portrait-v7.webp
cv/
admin/
projects/systemhealthmonitor/
assets/Sagar_Kerhalkar_IT_Infrastructure_DevOps_Leader_CV.pdf
```

Responsive mode:

```text
F12 -> Ctrl + Shift + M
```

Verify:

```text
The hero is two lines only
The heading is medium and human-readable
The body text is not tiny
Automation, Observability, Cloud, CI/CD, AI and DevOps orbit the portrait
Orbit words do not cover the face
The DevOps infinity animation is visible
The platform list contains five correct entries
No horizontal scrollbar exists
All buttons are reachable
The CV link downloads a PDF
Light mode remains readable
Reduced-motion mode removes continuous movement
```

---

## 14. Generate the A4 CV PDF

Run:

```powershell
cd C:\Temp\Sagar_Global_Profile_Redesign_v7_1
python .\scripts\generate_cv_pdf.py
```

Generated file:

```text
assets/Sagar_Kerhalkar_IT_Infrastructure_DevOps_Leader_CV.pdf
```

The generator fails if the result is not exactly two pages.

Check page count and A4 dimensions:

```powershell
python -c "from pypdf import PdfReader; p=r'assets/Sagar_Kerhalkar_IT_Infrastructure_DevOps_Leader_CV.pdf'; r=PdfReader(p); print('Pages:',len(r.pages)); print([(float(x.mediabox.width),float(x.mediabox.height)) for x in r.pages])"
```

Expected:

```text
Pages: 2
Approximately 595 × 842 points per page
```

The public `Download A4 CV` button downloads this generated file directly. It does not rely on an uncontrolled five-page browser print result.

The CV page also provides `Print latest` for manual printing.

---

## 15. Build a clean release folder

```powershell
cd C:\Temp\Sagar_Global_Profile_Redesign_v7_1
powershell -ExecutionPolicy Bypass `
  -File .\BUILD_RELEASE.ps1 `
  -OutputFolder "C:\Temp\Sagar_Profile_Release_v7_1"
```

The release build runs all tests unless `-SkipTests` is explicitly passed.

Never use `-SkipTests` for the production release.

Release folder:

```text
C:\Temp\Sagar_Profile_Release_v7_1
```

Test the release itself:

```powershell
cd C:\Temp\Sagar_Profile_Release_v7_1
python -m http.server 8090 --bind 127.0.0.1
```

Open:

```text
http://127.0.0.1:8090/
```

---

## 16. Back up the current live repository

Example repository folder:

```text
D:\Profile
```

Create a timestamped backup:

```powershell
$Repo = "D:\Profile"
$Stamp = Get-Date -Format "yyyyMMdd_HHmmss"
$Backup = "D:\Profile_BACKUP_$Stamp"

robocopy $Repo $Backup /E /XD ".git" "node_modules" ".venv" "__pycache__"
Write-Host "Backup created: $Backup" -ForegroundColor Green
```

Confirm:

```powershell
Test-Path "$Backup\index.html"
Test-Path "$Backup\assets\profile.json"
```

---

## 17. Copy V7 into the Git repository

First create a branch:

```powershell
cd D:\Profile
git status
git pull origin main
git checkout -b portfolio-v7-final
```

Copy the clean release:

```powershell
$Release = "C:\Temp\Sagar_Profile_Release_v7_1"
$Repo = "D:\Profile"
robocopy $Release $Repo /E
```

Review changes:

```powershell
cd D:\Profile
git status
git diff --stat
```

Commit:

```powershell
git add .
git commit -m "Release global portfolio V7 with responsive 3D UI and two-page A4 CV"
git push -u origin portfolio-v7-final
```

Create a pull request, allow CI to pass, review screenshots and PDF artifact, then merge into `main`.

Do not push directly to `main` before testing.

---

## 18. GitHub Actions CI/CD

Included workflows:

```text
.github/workflows/ci.yml
.github/workflows/deploy-cloudflare.yml
```

### CI workflow

The CI workflow runs:

```text
Python compilation
JavaScript and Cloudflare Function syntax
A4 CV generation
Profile/PDF validation
HTTP delivery tests
Chromium, Firefox and WebKit responsive tests
Final validation
Artifact upload
```

### Deployment workflow

The deployment workflow repeats the tests and deploys only after all commands pass.

Required GitHub repository secrets:

```text
CLOUDFLARE_API_TOKEN
CLOUDFLARE_ACCOUNT_ID
CLOUDFLARE_PAGES_PROJECT
```

Add them at:

```text
GitHub repository -> Settings -> Secrets and variables -> Actions
```

---

## 19. Test Cloudflare Pages Functions locally

A Python HTTP server does not execute Cloudflare Pages Functions. Use Wrangler for the API and production-auth flow.

From the project root:

```powershell
npm install --save-dev wrangler
npx wrangler --version
```

Start Pages plus Functions:

```powershell
npx wrangler pages dev . --port 8788 --kv=PROFILE_KV
```

Open:

```text
http://127.0.0.1:8788/
http://127.0.0.1:8788/api/profile
http://127.0.0.1:8788/admin/
```

For a production-like local auth test, use a `.dev.vars` file. Never commit this file.

Example `.dev.vars`:

```text
ADMIN_USERNAME=sagar
AUTH_SALT=generated-value
SESSION_SECRET=generated-value
ADMIN_PASSWORD_HASH=generated-value
```

Add `.dev.vars` to `.gitignore`.

---

## 20. Create production admin secrets

Generate values locally:

```powershell
node .\tools\generate-admin-secrets.mjs "Use-A-Long-Unique-Password-Here"
```

It outputs:

```text
ADMIN_USERNAME
AUTH_SALT
SESSION_SECRET
ADMIN_PASSWORD_HASH
```

Set these in Cloudflare Pages environment variables. Mark sensitive values as encrypted secrets.

Never commit:

```text
Plain production password
AUTH_SALT
SESSION_SECRET
ADMIN_PASSWORD_HASH
Cloudflare API token
.dev.vars
.env
```

Production authentication uses:

```text
HTTP-only cookie
Secure flag
SameSite=Strict
Four-hour session expiry
HMAC-signed session token
Server-side password verification
```

---

## 21. Configure Workers KV

Create a Workers KV namespace in Cloudflare.

In the Pages project, add a binding:

```text
Variable name: PROFILE_KV
KV namespace: your portfolio profile namespace
Environment: Production and Preview as required
```

The public API reads the key:

```text
profile
```

The private editor writes the same key after authenticated save.

If KV is empty, the public API falls back to:

```text
assets/profile.json
```

---

## 22. Manual Cloudflare direct deployment

Build the release first:

```powershell
powershell -ExecutionPolicy Bypass `
  -File .\BUILD_RELEASE.ps1 `
  -OutputFolder "C:\Temp\Sagar_Profile_Release_v7_1"
```

Authenticate Wrangler:

```powershell
npx wrangler login
```

Deploy:

```powershell
npx wrangler pages deploy "C:\Temp\Sagar_Profile_Release_v7_1" `
  --project-name="YOUR_CLOUDFLARE_PAGES_PROJECT" `
  --branch=main
```

Do not deploy the source folder with untested files when a clean release folder is available.

---

## 23. Custom domain

In Cloudflare Pages:

```text
Project -> Custom domains -> Set up a custom domain
```

Use:

```text
sagarkerhalkar.com
www.sagarkerhalkar.com
```

Choose one canonical domain and redirect the other.

After DNS propagation, test:

```powershell
Resolve-DnsName sagarkerhalkar.com
Invoke-WebRequest "https://sagarkerhalkar.com" -UseBasicParsing
Invoke-WebRequest "https://sagarkerhalkar.com/assets/Sagar_Kerhalkar_IT_Infrastructure_DevOps_Leader_CV.pdf" -UseBasicParsing
```

---

## 24. Production smoke test

After deployment, test:

```text
https://sagarkerhalkar.com/
https://sagarkerhalkar.com/cv/
https://sagarkerhalkar.com/admin/
https://sagarkerhalkar.com/projects/systemhealthmonitor/
https://sagarkerhalkar.com/api/profile
https://sagarkerhalkar.com/assets/Sagar_Kerhalkar_IT_Infrastructure_DevOps_Leader_CV.pdf
```

PowerShell status test:

```powershell
$Urls = @(
  'https://sagarkerhalkar.com/',
  'https://sagarkerhalkar.com/cv/',
  'https://sagarkerhalkar.com/admin/',
  'https://sagarkerhalkar.com/projects/systemhealthmonitor/',
  'https://sagarkerhalkar.com/api/profile',
  'https://sagarkerhalkar.com/assets/Sagar_Kerhalkar_IT_Infrastructure_DevOps_Leader_CV.pdf'
)

foreach ($Url in $Urls) {
  try {
    $Response = Invoke-WebRequest $Url -UseBasicParsing -TimeoutSec 20
    Write-Host "PASS $($Response.StatusCode) $Url" -ForegroundColor Green
  } catch {
    Write-Host "FAIL $Url - $($_.Exception.Message)" -ForegroundColor Red
  }
}
```

Also verify:

```text
Admin rejects a wrong password
Admin accepts only the production password
Profile save survives a reload
Public visitors cannot access the authenticated admin API
PDF downloads as exactly two A4 pages
Light and dark modes work
No browser console errors
No horizontal scrolling on a physical phone
```

---

## 25. Security headers

`_headers` provides browser security policy for static Pages responses.

After deployment, inspect:

```powershell
$r = Invoke-WebRequest "https://sagarkerhalkar.com" -UseBasicParsing
$r.Headers
```

Verify expected headers such as content-type protection, referrer policy and frame restrictions.

If a new external asset or service is added, update the Content Security Policy carefully instead of weakening it globally.

---

## 26. Rollback

### Git rollback

Find the last known-good commit:

```powershell
cd D:\Profile
git log --oneline -10
```

Create a rollback commit:

```powershell
git revert COMMIT_SHA
git push origin main
```

### Restore folder backup

```powershell
$Repo = "D:\Profile"
$Backup = "D:\Profile_BACKUP_YYYYMMDD_HHMMSS"

robocopy $Backup $Repo /E
```

Review before commit:

```powershell
cd D:\Profile
git status
git diff --stat
```

### Cloudflare rollback

Use the Pages deployment history to promote the last known-good deployment if a production issue appears.

---

## 27. Common troubleshooting

### `python` is not recognized

```powershell
py --version
py -m http.server 8080 --bind 127.0.0.1
```

### Playwright browser missing

```powershell
python -m playwright install chromium firefox webkit
```

### PowerShell blocks scripts

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_LOCAL_TESTS.ps1
```

### Old V5 content appears

Clear site data or run:

```javascript
localStorage.removeItem('sk_profile_preview_v5');
localStorage.removeItem('sk_profile_preview_v7');
localStorage.removeItem('sk_theme_v5');
localStorage.removeItem('sk_theme_v7');
location.reload();
```

Then use:

```text
Ctrl + Shift + R
```

### CV still looks old

Regenerate it:

```powershell
python .\scripts\generate_cv_pdf.py
python .\tests\validate.py
```

Check that this file has a new timestamp:

```powershell
Get-Item .\assets\Sagar_Kerhalkar_IT_Infrastructure_DevOps_Leader_CV.pdf
```

### Admin saves locally but not in production

Check:

```text
PROFILE_KV binding exists
All four admin environment values exist
Functions are deployed
/api/admin/profile returns 200 only after login
```

### Mobile horizontal scroll

Run:

```powershell
python .\tests\browser_matrix.py
```

Open `test-results.json` and inspect `overflow`. Every tested viewport should report `0`.

### Animations feel too strong

The visitor can enable reduced motion at OS/browser level. V7 includes `prefers-reduced-motion` handling.

---

## 28. Final release checklist

```text
[ ] V7 ZIP extracted into a new folder
[ ] Current live repository backed up
[ ] Python and Node versions confirmed
[ ] Dependencies installed
[ ] RUN_LOCAL_TESTS.ps1 passes
[ ] Hero is exactly two lines
[ ] Hero is medium and readable
[ ] Orbit labels contain Automation, Observability, Cloud, CI/CD, AI and DevOps
[ ] Orbit labels do not cover the face
[ ] Platform list is correct
[ ] Core tool list is correct
[ ] Mobile menu works
[ ] Light and dark modes work
[ ] No horizontal overflow at all tested sizes
[ ] CV PDF is exactly two A4 pages
[ ] CV portrait is embedded
[ ] CV has no clipped sections
[ ] Release folder built after tests
[ ] Git branch created
[ ] Pull request CI passes
[ ] Cloudflare secrets configured
[ ] PROFILE_KV binding configured
[ ] Production smoke test passes
[ ] One physical iPhone and one Android phone checked
[ ] Rollback path documented
```

---

## 29. Important accuracy statement

The included tests provide strong automated coverage across defined viewport sizes and browser engines. No developer can honestly guarantee identical behavior on every physical phone, browser version, accessibility setting and network condition without production and real-device testing. The correct production process is:

```text
Build -> test -> review artifacts -> deploy preview -> test real devices -> publish -> monitor -> retain rollback
```

V7 is designed to support that process rather than making an unsupported “works everywhere” claim.

---

# 30. GitHub new-branch publishing — exact safe procedure

The recommended branch name is:

```text
portfolio-v7-international
```

## Method A — automated PowerShell script

Clone the repository once if it is not already on the PC:

```powershell
git clone https://github.com/sagarkerhalkar/Profile.git D:\Profile
```

From the extracted V7.1 folder run:

```powershell
cd C:\Temp\Sagar_Global_Profile_Redesign_v7_1
powershell -ExecutionPolicy Bypass -File .\PUBLISH_NEW_BRANCH.ps1 `
  -RepoPath "D:\Profile" `
  -BranchName "portfolio-v7-international"
```

The script:

1. refuses to run if the repository has uncommitted changes;
2. creates a timestamped backup outside the repository;
3. fetches and fast-forwards `main`;
4. creates a new branch;
5. replaces the old portfolio working tree with V7.1 while preserving `.git`;
6. validates JSON and JavaScript;
7. commits the complete source, Docker files, tests and README;
8. pushes the new branch to GitHub.

Branch URL after push:

```text
https://github.com/sagarkerhalkar/Profile/tree/portfolio-v7-international
```

## Method B — manual Git commands

```powershell
git clone https://github.com/sagarkerhalkar/Profile.git D:\Profile
cd D:\Profile

git fetch origin
git switch main
git pull --ff-only origin main
git switch -c portfolio-v7-international
```

Create a backup:

```powershell
$Stamp = Get-Date -Format "yyyyMMdd_HHmmss"
robocopy D:\Profile "D:\Profile_BACKUP_$Stamp" /E /XD ".git" "node_modules" ".wrangler" "__pycache__" /XF "*.pyc"
```

Delete old working-tree files but preserve `.git`:

```powershell
Get-ChildItem D:\Profile -Force |
  Where-Object { $_.Name -ne ".git" } |
  Remove-Item -Recurse -Force
```

Copy the new source into `D:\Profile`, then run:

```powershell
cd D:\Profile
python -m json.tool .\assets\profile.json > $null
node --check .\assets\site.js
node --check .\assets\cv.js
node --check .\assets\admin.js

git add -A
git status
git commit -m "Add international portfolio V7.1 with Docker, CI/CD and deployment guide"
git push -u origin portfolio-v7-international
```

Create a pull request only after local and GitHub Actions tests pass:

```text
GitHub repository → Pull requests → New pull request
base: main
compare: portfolio-v7-international
```

Do not merge until the preview deployment, A4 CV and responsive screenshots are verified.

---

# 31. Cloudflare Pages deployment to sagarkerhalkar.com

Cloudflare Pages Git integration automatically builds and deploys changes pushed to the connected repository. Use `main` as production and the V7.1 branch as a preview until approval.

## Step 1 — push the branch

Complete section 30 first.

## Step 2 — connect the GitHub repository

In Cloudflare:

```text
Workers & Pages
→ Create application
→ Pages
→ Connect to Git
→ GitHub
→ Select sagarkerhalkar/Profile
```

Recommended project settings:

```text
Project name: sagar-profile
Production branch: main
Framework preset: None
Build command: leave blank
Build output directory: /
Root directory: /
```

The source is static HTML/CSS/JavaScript and does not require a framework build command. Pages Functions are detected from the `functions/` directory.

## Step 3 — configure KV for the private editor

Create a Workers KV namespace in Cloudflare and bind it to the Pages project with this exact variable name:

```text
PROFILE_KV
```

In the Pages project:

```text
Settings
→ Functions
→ KV namespace bindings
→ Add binding
Variable name: PROFILE_KV
KV namespace: select the portfolio namespace
```

Configure both Production and Preview environments when the editor must work in both.

## Step 4 — generate production admin secrets

Never use the local test password as production security.

Generate secrets locally:

```powershell
cd D:\Profile
node .\tools\generate-admin-secrets.mjs "Use-A-New-Long-Unique-Password-Here"
```

The command prints:

```text
ADMIN_USERNAME
AUTH_SALT
SESSION_SECRET
ADMIN_PASSWORD_HASH
```

Add them in Cloudflare Pages:

```text
Settings
→ Environment variables
→ Production
→ Add variable / Encrypt
```

Add the same variables to Preview only if preview admin access is required.

## Step 5 — verify the branch preview

A non-production Git branch receives a preview deployment. Verify:

```text
/
/cv/
/admin/
/projects/systemhealthmonitor/
/assets/Sagar_Kerhalkar_IT_Infrastructure_DevOps_Leader_CV.pdf
/api/profile
```

Verify admin login and save only after KV and secrets are configured.

## Step 6 — merge only after CI and preview approval

Merge the pull request into `main`. Cloudflare Pages then deploys the production branch.

## Step 7 — attach the domain

In the Pages project:

```text
Custom domains
→ Set up a domain
→ sagarkerhalkar.com
→ Continue
```

For an apex domain such as `sagarkerhalkar.com`, the domain must be a Cloudflare zone using Cloudflare nameservers. Do not remove the old working DNS record before the Pages preview has been tested.

Add `www.sagarkerhalkar.com` as a second custom domain if required, then configure one canonical redirect so search engines see only one primary URL.

## Step 8 — production smoke test

```powershell
$Urls = @(
  "https://sagarkerhalkar.com/",
  "https://sagarkerhalkar.com/cv/",
  "https://sagarkerhalkar.com/admin/",
  "https://sagarkerhalkar.com/projects/systemhealthmonitor/",
  "https://sagarkerhalkar.com/api/profile",
  "https://sagarkerhalkar.com/assets/Sagar_Kerhalkar_IT_Infrastructure_DevOps_Leader_CV.pdf"
)
foreach ($Url in $Urls) {
  try {
    $Response = Invoke-WebRequest $Url -UseBasicParsing -TimeoutSec 20
    Write-Host "PASS $($Response.StatusCode) $Url" -ForegroundColor Green
  } catch {
    Write-Host "FAIL $Url — $($_.Exception.Message)" -ForegroundColor Red
  }
}
```

Hard refresh after deployment:

```text
Ctrl + Shift + R
```

---

# 32. Direct Wrangler deployment

Install/login:

```powershell
npm install --global wrangler
wrangler login
```

Local Pages + Functions test:

```powershell
cd D:\Profile
wrangler pages dev . --ip 127.0.0.1 --port 8788 --kv PROFILE_KV
```

Open:

```text
http://127.0.0.1:8788/
```

Direct preview deployment:

```powershell
wrangler pages deploy . `
  --project-name="sagar-profile" `
  --branch="portfolio-v7-international"
```

Production deployment should be made only from tested `main` or through the included test-gated GitHub Actions workflow.

---

# 33. Docker production container

## Important architecture note

The standard Docker image serves the public static portfolio with Nginx. It includes the homepage, project pages, CV page and downloadable A4 PDF.

Cloudflare Pages Functions and Workers KV do not run inside Nginx. Therefore:

```text
Public portfolio in Docker: supported
Static CV/PDF download in Docker: supported
Local browser preview editing: supported on localhost
Production owner editor with Cloudflare KV: use Cloudflare Pages
```

## Install Docker Desktop

After installation verify:

```powershell
docker --version
docker compose version
```

## Build the image

```powershell
cd D:\Profile
docker build --pull --no-cache -t sagar-global-portfolio:v7.1 .
```

List the image:

```powershell
docker image ls sagar-global-portfolio
```

## Run the container

```powershell
docker run -d `
  --name sagar-global-portfolio `
  --restart unless-stopped `
  -p 8080:80 `
  sagar-global-portfolio:v7.1
```

Open:

```text
http://127.0.0.1:8080/
```

## Container health and logs

```powershell
docker ps
docker inspect --format='{{json .State.Health}}' sagar-global-portfolio
docker logs --tail 100 sagar-global-portfolio
Invoke-WebRequest http://127.0.0.1:8080/healthz -UseBasicParsing
```

Expected health response:

```text
ok
```

## Docker Compose

Start:

```powershell
cd D:\Profile
docker compose up -d --build
```

Status:

```powershell
docker compose ps
docker compose logs --tail 100
```

Stop without deleting the image:

```powershell
docker compose down
```

Rebuild after code changes:

```powershell
docker compose down
docker compose build --pull --no-cache
docker compose up -d
```

## Docker smoke test

```powershell
$Urls = @(
  "http://127.0.0.1:8080/healthz",
  "http://127.0.0.1:8080/",
  "http://127.0.0.1:8080/cv/",
  "http://127.0.0.1:8080/projects/systemhealthmonitor/",
  "http://127.0.0.1:8080/assets/Sagar_Kerhalkar_IT_Infrastructure_DevOps_Leader_CV.pdf"
)
foreach ($Url in $Urls) {
  $Response = Invoke-WebRequest $Url -UseBasicParsing -TimeoutSec 20
  Write-Host "PASS $($Response.StatusCode) $Url" -ForegroundColor Green
}
```

## Docker image export/import

Export for another campus/server:

```powershell
docker save sagar-global-portfolio:v7.1 -o D:\Backup\sagar-global-portfolio-v7.1.tar
```

Import on another Docker server:

```powershell
docker load -i D:\Backup\sagar-global-portfolio-v7.1.tar
docker run -d --name sagar-global-portfolio --restart unless-stopped -p 8080:80 sagar-global-portfolio:v7.1
```

## Docker rollback

Keep the previous image tag:

```powershell
docker tag sagar-global-portfolio:v7.1 sagar-global-portfolio:approved
```

Before an update:

```powershell
docker tag sagar-global-portfolio:approved sagar-global-portfolio:rollback
```

Rollback:

```powershell
docker rm -f sagar-global-portfolio
docker run -d `
  --name sagar-global-portfolio `
  --restart unless-stopped `
  -p 8080:80 `
  sagar-global-portfolio:rollback
```

---

# 34. Docker CI/CD gate

The V7.1 GitHub Actions CI runs on every branch push and pull request. It now performs:

```text
Python syntax
JavaScript syntax
Cloudflare Function syntax
A4 CV generation
PDF page-count validation
Static content validation
HTTP smoke tests
Responsive browser tests
Docker image build
Docker container health check
Homepage, CV and PDF container smoke tests
Artifact upload
```

The deployment workflow remains restricted to `main`, and deploys only after tests pass.

Check status:

```text
GitHub repository
→ Actions
→ Portfolio V7.1 CI
```

Do not merge when any check is red.

---

# 35. Production backup and rollback

## Git rollback

Find recent commits:

```powershell
git log --oneline -10
```

Create a rollback branch without rewriting history:

```powershell
git switch -c rollback-portfolio-v7 <GOOD_COMMIT_SHA>
git push -u origin rollback-portfolio-v7
```

Test that branch as a Cloudflare preview before changing production.

## Cloudflare rollback

Use the Pages deployment history to select the last known-good production deployment and roll back. Keep the previous deployment until mobile, A4 PDF, admin login and custom-domain tests pass.

## Local backup

```powershell
$Stamp = Get-Date -Format "yyyyMMdd_HHmmss"
robocopy D:\Profile "D:\Profile_FULL_BACKUP_$Stamp" /E /XD ".git" "node_modules" ".wrangler" "__pycache__" /XF "*.pyc"
```

---

# 36. Final release checklist

```text
[ ] New Git branch pushed
[ ] README.md visible on branch root
[ ] GitHub Actions green
[ ] Docker image builds
[ ] Docker health check is healthy
[ ] Cloudflare branch preview opens
[ ] Homepage checked in dark and light modes
[ ] Mobile menu checked
[ ] 360, 390, 430, 768, 1024, 1366, 1440 and 1920 widths checked
[ ] Chromium test passed
[ ] Firefox CI test passed
[ ] WebKit/Safari-like CI test passed
[ ] Direct A4 CV download opens
[ ] CV is exactly two A4 pages
[ ] Admin login works through Cloudflare Functions
[ ] Profile save persists in PROFILE_KV
[ ] Email, phone, website, LinkedIn and GitHub links work
[ ] Custom domain HTTPS works
[ ] No console errors
[ ] No horizontal overflow
[ ] Old production deployment retained for rollback
```

---

<!-- CLOUDFLARE_KV_ADMIN_SETUP_START -->

## Cloudflare Workers KV and Production Admin Setup

This section applies to:

```text
Cloudflare Pages project: sagar-profile-pages
GitHub branch: portfolio-v7-international
Production domain: https://sagarkerhalkar.com
Local repository: D:\Profile
```

### A. Create the KV namespace from the Cloudflare dashboard

1. Open **Workers KV**.
2. Click **+ Create** in the top-right corner.
3. Enter:

```text
sagar-profile-kv
```

4. Click **Create**.

### B. Bind KV to the Pages project

Open:

```text
Workers & Pages
â†’ sagar-profile-pages
â†’ Settings
â†’ Bindings
â†’ Add binding
â†’ KV namespace
```

Set:

```text
Variable name: PROFILE_KV
KV namespace: sagar-profile-kv
```

Save the binding for **Production**. Add it to **Preview** too when preview deployments need the admin editor.

The variable name must be exactly `PROFILE_KV`, because the Pages Functions use `env.PROFILE_KV`.

### C. CLI alternative for creating KV

When the dashboard is confusing, run:

```powershell
cd D:\Profile
npx.cmd wrangler kv namespace create PROFILE_KV
```

Wrangler prints the namespace ID. Copy that ID.

Create or update `wrangler.toml`:

```toml
name = "sagar-profile-pages"
pages_build_output_dir = "."
compatibility_date = "2026-06-14"

[[kv_namespaces]]
binding = "PROFILE_KV"
id = "PASTE_THE_NAMESPACE_ID_HERE"
```

Do not leave the placeholder ID.

Verify namespaces:

```powershell
npx.cmd wrangler kv namespace list
```

Deploy after adding the binding:

```powershell
npx.cmd wrangler pages deploy . --project-name=sagar-profile-pages --branch=portfolio-v7-international --commit-dirty=true
```

### D. Generate production admin values

Choose a strong private password. Do not send it in chat and do not commit it.

```powershell
cd D:\Profile
node .\tools\generate-admin-secrets.mjs "YOUR_PRIVATE_PASSWORD"
```

The command prints:

```text
ADMIN_USERNAME=sagar
AUTH_SALT=generated-value
SESSION_SECRET=generated-value
ADMIN_PASSWORD_HASH=generated-value
```

Keep the PowerShell window open while copying the values.

### E. Add Cloudflare variables and encrypted secrets

Open:

```text
Workers & Pages
â†’ sagar-profile-pages
â†’ Settings
â†’ Variables and Secrets
â†’ Add
```

Add the normal variable:

```text
ADMIN_USERNAME = sagar
```

Add these as encrypted secrets:

```text
AUTH_SALT
SESSION_SECRET
ADMIN_PASSWORD_HASH
```

Paste only each generated value. Do not include the variable name or `=` sign inside the value box.

### F. Redeploy

```powershell
cd D:\Profile
npx.cmd wrangler pages deploy . --project-name=sagar-profile-pages --branch=portfolio-v7-international --commit-dirty=true
```

### G. Test the public API

```powershell
Invoke-WebRequest "https://sagarkerhalkar.com/api/profile" -UseBasicParsing
```

Expected result:

```text
StatusCode : 200
```

### H. Test production admin login

Open:

```text
https://sagarkerhalkar.com/admin/
```

Use:

```text
Username: sagar
Password: the private password used when generating the hash
```

Change one small field, save it, refresh, and confirm the change remains.

### I. Error meanings

```text
503 Admin auth not configured
```

One or more of these values is missing:

```text
ADMIN_USERNAME
AUTH_SALT
SESSION_SECRET
ADMIN_PASSWORD_HASH
```

```text
401 Unauthorized
```

The username or password is incorrect.

```text
Login works but saved changes disappear
```

`PROFILE_KV` is missing, has the wrong binding name, or the site was not redeployed after binding.

### J. PowerShell npm/npx execution-policy issue

If PowerShell blocks `npm.ps1` or `npx.ps1`, use the Windows command wrappers:

```powershell
npm.cmd --version
npx.cmd wrangler --version
```

### K. Production smoke test

```powershell
$Urls = @(
    "https://sagarkerhalkar.com/",
    "https://sagarkerhalkar.com/cv/",
    "https://sagarkerhalkar.com/admin/",
    "https://sagarkerhalkar.com/projects/systemhealthmonitor/",
    "https://sagarkerhalkar.com/api/profile",
    "https://sagarkerhalkar.com/assets/Sagar_Kerhalkar_IT_Infrastructure_DevOps_Leader_CV.pdf"
)

foreach ($Url in $Urls) {
    try {
        $Response = Invoke-WebRequest $Url -UseBasicParsing -TimeoutSec 30
        Write-Host "PASS $($Response.StatusCode) $Url" -ForegroundColor Green
    }
    catch {
        Write-Host "FAIL $Url - $($_.Exception.Message)" -ForegroundColor Red
    }
}
```

### L. Security rules

- Never commit production passwords.
- Never commit `AUTH_SALT`, `SESSION_SECRET`, or `ADMIN_PASSWORD_HASH`.
- Local password `Profile@2026` is only for local testing.
- Production password is the private password used in the generator command.
- Always redeploy after changing bindings or secrets.

<!-- CLOUDFLARE_KV_ADMIN_SETUP_END -->
