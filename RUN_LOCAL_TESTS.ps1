param(
  [switch]$InstallDependencies,
  [switch]$InstallBrowserTools
)

$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot

$Python = if (Get-Command python -ErrorAction SilentlyContinue) { 'python' } elseif (Get-Command py -ErrorAction SilentlyContinue) { 'py' } else { throw 'Python 3.10+ is required.' }
if (-not (Get-Command node -ErrorAction SilentlyContinue)) { throw 'Node.js 20+ is required.' }

if ($InstallDependencies -or $InstallBrowserTools) {
  & $Python -m pip install -r .\requirements-dev.txt
  & $Python -m playwright install chromium firefox webkit
}

Write-Host "[1/7] Python syntax" -ForegroundColor Cyan
& $Python -m py_compile .\scripts\generate_cv_pdf.py .\tests\validate.py .\tests\browser_matrix.py .\tests\http_smoke.py

Write-Host "[2/7] JavaScript and Cloudflare Function syntax" -ForegroundColor Cyan
$JavaScriptFiles = @(
  '.\assets\site.js',
  '.\assets\cv.js',
  '.\assets\admin.js',
  '.\functions\api\profile.js',
  '.\functions\api\admin\login.js',
  '.\functions\api\admin\logout.js',
  '.\functions\api\admin\profile.js',
  '.\functions\lib\auth.js',
  '.\tools\generate-admin-secrets.mjs'
)
foreach ($File in $JavaScriptFiles) { node --check $File }

Write-Host "[3/7] Generate controlled two-page A4 CV" -ForegroundColor Cyan
& $Python .\scripts\generate_cv_pdf.py

Write-Host "[4/7] Static, profile and PDF validation" -ForegroundColor Cyan
& $Python .\tests\validate.py

Write-Host "[5/7] Local HTTP delivery" -ForegroundColor Cyan
& $Python .\tests\http_smoke.py

Write-Host "[6/7] Responsive browser matrix" -ForegroundColor Cyan
& $Python .\tests\browser_matrix.py

Write-Host "[7/7] Final validation after browser run" -ForegroundColor Cyan
& $Python .\tests\validate.py

Write-Host "ALL PORTFOLIO V7 TESTS PASSED" -ForegroundColor Green
