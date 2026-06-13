param(
  [string]$RepoPath = "D:\Profile",
  [string]$BranchName = "portfolio-v7-international"
)
$ErrorActionPreference = "Stop"
$Source = $PSScriptRoot

if (-not (Test-Path (Join-Path $RepoPath ".git"))) {
  throw "Not a Git repository: $RepoPath. Clone it first with: git clone https://github.com/sagarkerhalkar/Profile.git D:\Profile"
}

Set-Location $RepoPath
if (git status --porcelain) {
  throw "The repository has uncommitted changes. Commit or stash them before running this script."
}

$Stamp = Get-Date -Format "yyyyMMdd_HHmmss"
$Backup = "${RepoPath}_BACKUP_${Stamp}"
Write-Host "Creating backup: $Backup" -ForegroundColor Cyan
robocopy $RepoPath $Backup /E /XD ".git" "node_modules" ".wrangler" "__pycache__" /XF "*.pyc" | Out-Null
if ($LASTEXITCODE -gt 7) { throw "Backup failed with robocopy code $LASTEXITCODE" }

Write-Host "Updating local main branch..." -ForegroundColor Cyan
git fetch origin
git switch main
git pull --ff-only origin main

if (git show-ref --verify --quiet "refs/heads/$BranchName") {
  throw "Local branch already exists: $BranchName. Choose another name or delete it intentionally."
}
if (git ls-remote --exit-code --heads origin $BranchName 2>$null) {
  throw "Remote branch already exists: $BranchName. Choose another branch name."
}

git switch -c $BranchName

Write-Host "Removing old working-tree files while preserving .git..." -ForegroundColor Yellow
Get-ChildItem $RepoPath -Force | Where-Object { $_.Name -ne ".git" } | Remove-Item -Recurse -Force

Write-Host "Copying Portfolio V7.1 source..." -ForegroundColor Cyan
$ExcludeDirs = @(".git", ".wrangler", "node_modules", "__pycache__", "test_screenshots", "pdf_renders")
$ExcludeFiles = @("*.pyc", "test-results.json", "quick-*.png", "Sagar_Global_Profile_Redesign_*.zip", "Sagar_Profile_Release_*.zip")
$Args = @($Source, $RepoPath, "/E")
foreach ($d in $ExcludeDirs) { $Args += @("/XD", (Join-Path $Source $d)) }
foreach ($f in $ExcludeFiles) { $Args += @("/XF", $f) }
robocopy @Args | Out-Null
if ($LASTEXITCODE -gt 7) { throw "Copy failed with robocopy code $LASTEXITCODE" }

Set-Location $RepoPath
python -m json.tool .\assets\profile.json > $null
node --check .\assets\site.js
node --check .\assets\cv.js
node --check .\assets\admin.js

git add -A
git status --short
git commit -m "Add international portfolio V7.1 with Docker, CI/CD and deployment guide"
git push -u origin $BranchName

Write-Host "Branch pushed successfully:" -ForegroundColor Green
Write-Host "https://github.com/sagarkerhalkar/Profile/tree/$BranchName" -ForegroundColor Green
Write-Host "Backup retained at: $Backup" -ForegroundColor Cyan
