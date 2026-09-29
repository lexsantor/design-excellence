# Refresh the installed Design Excellence skill from the governed source, then re-apply the runtime write guard.
# The deny ACE keeps the installed copy read-only for runtime sessions (SKILL.md §7 "Stack modules").
# -Source installs another skill tree (experiment variants); the default is the governed source.
param([string]$Source = (Join-Path $PSScriptRoot '..\design-excellence'))
$ErrorActionPreference = 'Stop'
$src = Resolve-Path $Source
$dst = Join-Path $HOME '.claude\skills\design-excellence'
$user = "$env:USERDOMAIN\$env:USERNAME"

icacls $dst /remove:d $user /T | Out-Null
robocopy $src $dst /MIR /NFL /NDL /NJH /NJS /NP | Out-Null
if ($LASTEXITCODE -ge 8) { throw "robocopy failed ($LASTEXITCODE)" }
icacls $dst /deny "${user}:(OI)(CI)(DE,WD,AD,DC)" | Out-Null

$hash = { param($root) Get-ChildItem $root -Recurse -File | ForEach-Object {
    '{0} {1}' -f (Get-FileHash $_.FullName -Algorithm SHA256).Hash, $_.FullName.Substring($root.Length) } | Sort-Object }
$a = & $hash "$src"; $b = & $hash $dst
if (Compare-Object $a $b) { throw 'installed copy differs from source' }
try { New-Item (Join-Path $dst 'guard-probe.tmp') -ItemType File | Out-Null; throw 'write guard missing' }
catch [System.UnauthorizedAccessException] { }
"installed: $($a.Count) files identical to source; write guard active"
