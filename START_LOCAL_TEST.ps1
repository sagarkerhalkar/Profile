param([int]$Port = 8080)
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
$Python = if (Get-Command python -ErrorAction SilentlyContinue) { 'python' } elseif (Get-Command py -ErrorAction SilentlyContinue) { 'py' } else { throw 'Python 3.10+ is required.' }
Write-Host "Portfolio V7 local server" -ForegroundColor Green
Write-Host "Homepage: http://127.0.0.1:$Port/" -ForegroundColor Cyan
Write-Host "CV:       http://127.0.0.1:$Port/cv/" -ForegroundColor Cyan
Write-Host "Admin:    http://127.0.0.1:$Port/admin/" -ForegroundColor Cyan
Write-Host "Project:  http://127.0.0.1:$Port/projects/systemhealthmonitor/" -ForegroundColor Cyan
Write-Host "Press Ctrl+C to stop." -ForegroundColor Yellow
& $Python -m http.server $Port --bind 127.0.0.1
