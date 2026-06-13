param(
  [string]$OutputFolder = 'C:\Temp\Sagar_Profile_Release_v7',
  [switch]$SkipTests
)
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot

if (-not $SkipTests) {
  powershell -ExecutionPolicy Bypass -File .\RUN_LOCAL_TESTS.ps1
}

Remove-Item $OutputFolder -Recurse -Force -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Path $OutputFolder -Force | Out-Null
$Items = @('index.html','404.html','assets','cv','admin','projects','functions','_headers','robots.txt','sitemap.xml','.nojekyll')
foreach ($Item in $Items) {
  if (Test-Path $Item) { Copy-Item $Item $OutputFolder -Recurse -Force }
}

$Forbidden = Get-ChildItem $OutputFolder -Recurse -Force | Where-Object { $_.Name -in @('__pycache__','.DS_Store') -or $_.Extension -eq '.pyc' }
if ($Forbidden) { $Forbidden | Remove-Item -Recurse -Force }

Write-Host "Release created: $OutputFolder" -ForegroundColor Green
Write-Host "Generated CV: $OutputFolder\assets\Sagar_Kerhalkar_IT_Infrastructure_DevOps_Leader_CV.pdf" -ForegroundColor Cyan
