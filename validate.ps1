# validate.ps1 - structural check on every SKILL.md before install / commit / publish.
# Asserts: frontmatter block present; name and description fields exist; name == folder name;
# description is non-trivial. Prints [PASS]/[FAIL] per skill, exits nonzero on any failure.

$ErrorActionPreference = 'Stop'
$repo = $PSScriptRoot
$fail = 0
$skillFiles = Get-ChildItem -Path (Join-Path $repo 'plugins') -Recurse -Filter 'SKILL.md' -File
$count = $skillFiles.Count

foreach ($md in $skillFiles) {
    $dir = $md.Directory.Name
    $txt = Get-Content $md.FullName -Raw
    if ($txt -notmatch '(?s)^\s*---\s*\r?\n.*?\r?\n---') { Write-Host "[FAIL] $dir : no YAML frontmatter block"; $fail++; continue }
    if ($txt -notmatch '(?m)^name:\s*(.+)$')            { Write-Host "[FAIL] $dir : missing name"; $fail++; continue }
    $name = $Matches[1].Trim()
    if ($name -ne $dir)                                  { Write-Host "[FAIL] $dir : name '$name' != folder name"; $fail++; continue }
    if ($txt -notmatch '(?m)^description:\s*(.+)$')      { Write-Host "[FAIL] $dir : missing description"; $fail++; continue }
    $desc = $Matches[1].Trim()
    if ($desc.Length -lt 20)                             { Write-Host "[FAIL] $dir : description too short ($($desc.Length) chars)"; $fail++; continue }
    Write-Host "[PASS] $dir"
}

Write-Host ""
Write-Host "total skills found: $count (expected 33)"
if ($count -ne 33) { Write-Host "[WARN] skill count != 33" }
if ($fail -gt 0) { Write-Host "VALIDATION FAILED: $fail problem(s)"; exit 1 }
Write-Host "ALL PASSED"
exit 0
