import re
import os

# Создаем директорию
dict_dir = r"docs\reference\dictionaries"
os.makedirs(dict_dir, exist_ok=True)

# Читаем файл
with open(r"docs\reference\COMMON_DICTIONARIES.md", "r", encoding="utf-8") as f:
    content = f.read()

# Паттерн для извлечения словарей
pattern = r'## `([^`]+)`\s*\n\n([\s\S]*?)\n\n```text\n([\s\S]*?)\n```'
matches = re.finditer(pattern, content)

count = 0
for match in matches:
    name = match.group(1)
    desc = match.group(2)
    text = match.group(3)
    
    # Формируем содержимое файла
    file_content = f"#{name}\n\n{desc.strip()}\n\n```text\n{text.strip()}\n```\n"
    
    # Пишем файл
    filepath = os.path.join(dict_dir, f"{name}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(file_content)
    
    count += 1
    print(f"Created: {name}.md")

print(f"\nTotal dictionaries created: {count}")
