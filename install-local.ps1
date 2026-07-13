# install-local.ps1 - make all plugin skills auto-activate in every repo on this machine.
# Junctions each skill dir into ~/.claude/skills (directory junctions need no admin on Windows);
# falls back to a recursive copy if a junction cannot be created.
# Re-run any time after editing skills; the Desktop package stays the single source of truth.

$ErrorActionPreference = 'Stop'
$repo = $PSScriptRoot
$dest = Join-Path $env:USERPROFILE '.claude\skills'
New-Item -ItemType Directory -Force -Path $dest | Out-Null

# A skill dir is any directory that directly contains a SKILL.md.
$skillDirs = Get-ChildItem -Path (Join-Path $repo 'plugins') -Recurse -Filter 'SKILL.md' -File |
    ForEach-Object { $_.Directory }

$n = 0
foreach ($s in $skillDirs) {
    $link = Join-Path $dest $s.Name
    if (Test-Path $link) {
        $item = Get-Item $link -Force
        if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) { $item.Delete() }
        else { Remove-Item $link -Recurse -Force }
    }
    try {
        New-Item -ItemType Junction -Path $link -Target $s.FullName | Out-Null
        Write-Host ("junction  {0}" -f $s.Name)
    } catch {
        Copy-Item -Recurse -Force $s.FullName $link
        Write-Host ("copy      {0}" -f $s.Name)
    }
    $n++
}
Write-Host ""
Write-Host ("installed {0} skills -> {1}" -f $n, $dest)
if ($n -ne 33) { Write-Host ("[WARN] expected 33 skills, installed {0}" -f $n) }
