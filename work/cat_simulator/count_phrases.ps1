$content = Get-Content -Path "C:\Users\Mariyaa\Desktop\скрипты\LLM\work\cat_simulator\4_EXAMPLES_AUTHOR__DATASET.md"
$current = ''
$count = 0
foreach ($line in $content) {
  if ($line -match '^## Узел:') {
    if ($current -and $count -gt 0) {
      Write-Host "$current : $count"
    }
    $current = $line
    $count = 0
  }
  elseif (($line.Trim() -ne '') -and ($line -notmatch '^#') -and ($line -notmatch '^---') -and ($line -notmatch '^\|') -and ($line -notmatch '^BotSlug') -and ($line -notmatch '^Автор') -and ($line -notmatch '^Дата') -and ($line -notmatch '^Исключённые')) {
    $count++
  }
}
if ($current -and $count -gt 0) {
  Write-Host "$current : $count"
}
