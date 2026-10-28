# Antigravity SEO One-Click Installer for Windows
# Installs Antigravity SEO globally into ~/.gemini/config/skills/antigravity-seo

$ErrorActionPreference = 'Stop'

Write-Host "==============================================" -ForegroundColor Cyan
Write-Host "   Installing Antigravity SEO Skill for AGY   " -ForegroundColor Cyan
Write-Host "==============================================" -ForegroundColor Cyan

$TargetDir = Join-Path $env:USERPROFILE ".gemini\config\skills\antigravity-seo"

if (Test-Path $TargetDir) {
    Write-Host "Existing Antigravity SEO installation found at: $TargetDir" -ForegroundColor Yellow
    Write-Host "Updating repository..." -ForegroundColor Yellow
    Set-Location $TargetDir
    git pull origin main
} else {
    Write-Host "Cloning Antigravity SEO into: $TargetDir" -ForegroundColor Green
    git clone https://github.com/IshtiakNihal/Antigravity-SEO.git $TargetDir
}

Write-Host "`nAntigravity SEO Skill installed successfully!" -ForegroundColor Green
Write-Host "The skill is now globally available in Google Antigravity." -ForegroundColor White
Write-Host "You can invoke it by asking Antigravity to run an SEO, GEO, AEO, or Ecommerce audit." -ForegroundColor White
