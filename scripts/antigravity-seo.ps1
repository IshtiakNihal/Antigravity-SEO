# Antigravity SEO launcher for Windows PowerShell
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$ArgsList
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$runtime = Join-Path $scriptDir "runtime.py"

if (-not (Test-Path $runtime)) {
    Write-Error "Antigravity SEO runtime is missing. Reinstall Antigravity SEO."
    exit 2
}

$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    $pythonCmd = Get-Command py -ErrorAction SilentlyContinue
}

if (-not $pythonCmd) {
    Write-Error "Python 3 is required but was not found on your PATH."
    exit 2
}

& $pythonCmd.Source $runtime @ArgsList
exit $LASTEXITCODE

