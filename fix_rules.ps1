$path = "C:\Users\Mariyaa\Desktop\скрипты\LLM\work\greeting_bot\3_RULES_AUTHOR__RULES_AND_DICTIONARIES.md"
$content = Get-Content -LiteralPath $path -Encoding UTF8
$output = @()
$inNode = $false

foreach ($line in $content) {
  # Remove trailing whitespace
  $line = $line.TrimEnd()
  
  # Skip --- lines
  if ($line -match '^\s*---\s*$') { continue }
  
  # Skip "Ответы:" lines
  if ($line -match '^\s*Ответы:\s*$') { continue }
  
  # Skip "Условия:" lines  
  if ($line -match '^\s*Условия:\s*$') { continue }
  
  # Skip "Правила:" lines
  if ($line -match '^\s*Правила:\s*$') { continue }
  
  # Remove leading * from that_anchor lines (add leading *)
  if ($line -match '^[[:space:]]*%that_anchor=') {
    $line = $line.TrimStart()
    $output += $line
    continue
  }
  
  $output += $line
}

# Now do content-level replacements
$result = $output -join "`n"

# Fix triple braces to double: {{{ to {{ except where already {{
$result = [regex]::Replace($result, '\{\{\{', '{{{')  # safety
$result = [regex]::Replace($result, '\{\{\{([^}]*)\}\}\}', '{{`1}}')  # {{{x}}} -> {{x}}

# Fix bare { that starts a line -> add leading *
$result = [regex]::Replace($result, '(?m)^([{]\w)', '* `1')

Set-Content -LiteralPath $path -Value $result -Encoding UTF8 -NoNewline
