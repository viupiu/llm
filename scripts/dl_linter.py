import re
import sys
from typing import List, Tuple, Optional

class LintError:
    def __init__(self, line: int, message: str, level: str = "ERROR"):
        self.line = line
        self.message = message
        self.level = level

    def __str__(self):
        return f"{self.level} [строка {self.line}]\n{self.message}"

class DLLinter:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.errors: List[LintError] = []
        self.content: List[str] = []

    def load_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.content = f.readlines()
        except Exception as e:
            print(f"Error reading file: {e}")
            sys.exit(1)

    def _build_dict_ranges(self) -> list[Tuple[int, int]]:
        """Возвращает список (start, end) — диапазоны строк, принадлежащие ## Словарь секциям (0-indexed)."""
        ranges = []
        in_dict = False
        start = 0
        for idx, line in enumerate(self.content):
            if re.match(r'^##\s*Словарь:\s', line):
                in_dict = True
                start = idx
            elif re.match(r'^## ', line):
                if in_dict:
                    ranges.append((start, idx))
                in_dict = False
        if in_dict:
            ranges.append((start, len(self.content)))
        return ranges

    def _is_in_dict_or_rule_section(self, line_num: int) -> bool:
        """line_num — 1-based index. Возвращает True, если строка внутри ## Словарь секции ИЛИ не внутри ## Узел секции (т.е. это словарь/общий текст)."""
        # Проверка: строка в ## Словарь
        in_dict_header = bool(re.match(r'^##\s*Словарь:\s', self.content[line_num - 1]))
        if in_dict_header:
            return True

        # Проверяем, в какой секции находится строка
        in_dict = False
        in_node = False
        for idx in range(line_num - 1):
            line = self.content[idx].strip()
            if re.match(r'^##\s*Словарь:\s', line):
                in_dict = True
                in_node = False
            elif re.match(r'^## Узел:', line):
                in_node = True
                in_dict = False
            elif re.match(r'^## ', line):
                in_dict = False
                in_node = False
        return in_dict

    def add_error(self, line: int, message: str, level: str = "ERROR"):
        self.errors.append(LintError(line, message, level))

    # --- Checks ---

    def check_leading_star(self, line_num: int, text: str):
        # П1. Правило без ведущей *
        # Matches patterns that look like rules but don't start with *
        # A rule is typically a line that isn't empty, isn't a header, isn't a comment, and isn't a dictionary entry
        stripped = text.strip()
        if not stripped or stripped.startswith('#') or stripped.startswith('//') or '=>' in stripped:
            return

        # If it looks like a rule (contains DL constructs) but doesn't start with *
        if (re.search(r'\[dict\(|\[@cmb|\{|\[if', stripped)) and not stripped.startswith('*'):
            self.add_error(line_num, "Rule does not start with '*' .")

    def check_cmb_args(self, line_num: int, text: str):
        # П2. CMB с одним аргументом
        # Find [@cmb(...)] and check number of arguments
        matches = re.finditer(r'\[@cmb\((.*?)\)', text)
        for match in matches:
            args_str = match.group(1)
            # Simple split by comma, but need to handle nested braces
            args = []
            bracket_level = 0
            current_arg = []
            for char in args_str:
                if char == '{': bracket_level += 1
                elif char == '}': bracket_level -= 1
                if char == ',' and bracket_level == 0:
                    args.append("".join(current_arg).strip())
                    current_arg = []
                else:
                    current_arg.append(char)
            args.append("".join(current_arg).strip())
            
            if len([a for a in args if a]) < 2:
                self.add_error(line_num, "cmb requires at least two arguments.")

    def check_triple_braces(self, line_num: int, text: str):
        # П3. Тройные скобки
        if '{{{' in text:
            self.add_error(line_num, "Triple braces are forbidden.")

    def check_inline_duplicates(self, line_num: int, text: str):
        # П4. Дубликаты внутри инлайн-словаря {кот/кот}
        matches = re.finditer(r'\{(.*?)\}', text)
        for match in matches:
            content = match.group(1)
            if '/' in content:
                parts = [p.strip() for p in content.split('/')]
                seen = set()
                for p in parts:
                    if p and p in seen:
                        self.add_error(line_num, f"Duplicate alternatives inside inline dictionary: {p}")
                    seen.add(p)

    def check_stem_coverage(self, line_num: int, text: str):
        # П5. Стем плюс уже покрытая словоформа {вернус~/вернусь}
        matches = re.finditer(r'\{(.*?)\}', text)
        for match in matches:
            content = match.group(1)
            parts = [p.strip() for p in content.split('/')]
            stems = [p for p in parts if p.endswith('~')]
            for stem in stems:
                root = stem[:-1]
                for p in parts:
                    if p != stem and p.startswith(root):
                        self.add_error(line_num, f"Redundant alternative already covered by stem: {p}")

    def check_standalone_tilde(self, line_num: int, text: str):
        # П6. Тильда отдельно от слова {~/нет}, {ты ~}, {общ/~}
        matches = re.finditer(r'\{(.*?)\}', text)
        for match in matches:
            content = match.group(1)
            parts = [p.strip() for p in content.split('/')]
            for p in parts:
                if p == '~' or p == ' ~' or p == '~ ':
                    self.add_error(line_num, "Standalone tilde is forbidden.")

    def check_tilde_inside_word(self, line_num: int, text: str):
        # П7. Тильда внутри слова мужик~у, слов~арь
        # Tilde must be at the start or end of a token
        # This regex looks for tilde that is surrounded by alphanumeric characters on both sides
        if re.search(r'\w~\w', text):
            self.add_error(line_num, "Tilde inside word is forbidden.")

    def check_attached_inline_dict(self, line_num: int, text: str):
        # П8. Приклеенный инлайн-словарь коти{к/шка}
        if re.search(r'\w\{', text):
            self.add_error(line_num, "Inline dictionary cannot be attached to word fragment.")

    def check_tilde_after_braces(self, line_num: int, text: str):
        # П9. Тильда после закрывающей скобки {котик/котишка}~
        if re.search(r'\}~', text):
            self.add_error(line_num, "Tilde must belong to dictionary element, not to dictionary block.")

    def check_forbidden_sections(self, line_num: int, text: str):
        # П10. Запрещённые секции: Ответы:, Условия:, Правила:
        forbidden = ['Ответы:', 'Условия:', 'Правила:']
        for word in forbidden:
            if text.strip() == word:
                self.add_error(line_num, "Forbidden section in rules file.")

    def check_horizontal_separators(self, line_num: int, text: str):
        # П11. Горизонтальные разделители ---
        if text.strip() == '---':
            self.add_error(line_num, "Horizontal separators are forbidden.")

    def check_dictionary_definitions(self):
        # П12. Ссылка на словарь без определения [dict(name)]
        defined_dicts = set()
        # Find all ## Словарь: name
        for line in self.content:
            match = re.search(r'##\s*Словарь:\s*(\w+)', line)
            if match:
                defined_dicts.add(match.group(1))
        
        for line_num, text in enumerate(self.content, 1):
            matches = re.finditer(r'\[dict\((\w+)\)\]', text)
            for match in matches:
                dict_name = match.group(1)
                if dict_name not in defined_dicts:
                    self.add_error(line_num, f"Reference to undefined dictionary: {dict_name}")

    def check_double_braces_single_element(self, line_num: int, text: str):
        # П13. Двойные скобки для одного элемента {{потом}}
        matches = re.finditer(r'\{\{([^\}]*)\}\}', text)
        for match in matches:
            content = match.group(1)
            if '/' not in content:
                self.add_error(line_num, "Double braces used for a single element.")

    def check_single_braces_in_cmb(self, line_num: int, text: str):
        # П14. Одиночные скобки для списка внутри cmb [@cmb({да/ага})]
        matches = re.finditer(r'\[@cmb\((.*?)\)', text)
        for match in matches:
            args_str = match.group(1)
            # Check for {a/b} but not {{a/b}}
            # This is tricky. We look for { containing / but not preceded by {
            # Simple approach: if it contains { and / but not {{
            if '/' in args_str and '{{' not in args_str:
                # Need to be sure the / is inside { }
                if re.search(r'\{[^\{]*\/[^}]*\}', args_str):
                    self.add_error(line_num, "Alternatives inside cmb must use double braces.")

    def check_star_inside_braces(self, line_num: int, text: str):
        # П15. Звёздочка внутри фигурных скобок {*}: {*}, { * }
        # Звёздочка — wildcard правила, не элемент инлайн-списка
        matches = re.finditer(r'\{([^}]*)\}', text)
        for match in matches:
            content = match.group(1).strip()
            if content == '*' or content.strip() == '*':
                self.add_error(line_num, "Wildcard '*' inside braces is forbidden. Remove {*}.")

    def check_double_star_wildcard(self, line_num: int, text: str):
        # П16. Правило вида "* * * ..." или "* * {" — пустой двойной wildcard
        # "* * {*}" и "* * {словарь}" — бессмысленная конструкция, нужно убрать * *
        stripped = text.strip()
        if not stripped or stripped.startswith('#') or stripped.startswith('//') or '=>' in stripped:
            return
        if re.search(r'\*\s+\*\s+\*', stripped):
            self.add_error(line_num, "Consecutive wildcards '* * *' are redundant. Use single '*' with pattern.")
        if re.match(r'\*\s+\*\s+\{[^}]*\}\s*\*', stripped):
            self.add_error(line_num, "Redundant '* *' before inline dictionary. Use '* {паттерн} *'.")

    def check_attached_star(self, line_num: int, text: str):
        # П17. Звёздочка прилипает к слову без пробела: *лево, *лев~, *двер~
        # или слово* * где * прилипает справа
        stripped = text.strip()
        if not stripped or stripped.startswith('#') or stripped.startswith('//'):
            return
        star_matches = re.finditer(r'\*', stripped)
        for m in star_matches:
            pos = m.start()
            # Проверяем символ после *
            if pos + 1 < len(stripped):
                ch_after = stripped[pos + 1]
                if ch_after.isalpha() or ch_after == '~':
                    self.add_error(line_num, f"Wildcard '*' must have a space after it. Found '* followed by '{ch_after}'.")
            # Проверяем символ перед * (но не в конструкциях [@cmb], [dict] и т.д.)
            if pos > 0:
                ch_before = stripped[pos - 1]
                if ch_before.isalpha() or ch_before == '~':
                    # Исключаем случаи вроде [dict(name)] * — тут ]*, ок
                    if ch_before not in (']', ')', '}'):
                        self.add_error(line_num, f"Wildcard '*' must have a space before it. Found '{ch_before}' followed by '*'.")

    def check_double_braces_outside_cmb(self, line_num: int, text: str):
        # П18. Двойные скобки {{...}} вне [@cmb]
        # {{а/б}} разрешены ТОЛЬКО внутри [@cmb]. Вне cmb используйте одинарные {а/б}
        if '{{' not in text:
            return
        # Проверяем, есть ли @@cmb в строке
        if '@cmb' not in text:
            self.add_error(line_num, "Double braces '{{...}}' found outside [@cmb]. Use single braces '{...}' outside combinator.")

    def check_tilde_not_attached(self, line_num: int, text: str):
        # П19. Тильда отдельно от слова в правиле (не внутри {}): "двер ~", "поздравит ~"
        # Проверяем токены из правила (вне скобок/конструкций)
        stripped = text.strip()
        if not stripped or stripped.startswith('#') or stripped.startswith('//'):
            return
        # Ищем паттерн "слово ~" где ~ идёт отдельно через пробел
        if re.search(r'\w+\s+~(?!\w)', stripped):
            # Исключаем контекст внутри []
            outside_brackets = re.sub(r'\[[^\]]*\]', '', stripped)
            if re.search(r'\w+\s+~(?!\w)', outside_brackets):
                self.add_error(line_num, "Tilde '~' is not attached to a word. Use 'слово~' without space.")

    def check_orphan_tilde_token(self, line_num: int, text: str):
        # П20. Тильда как самостоятельный токен вне {} (например "* ~ *")
        # Проверяем после удаления всего внутри [] и {}
        cleaned = re.sub(r'\[[^\]]*\]', '', text)
        cleaned = re.sub(r'\{[^}]*\}', '', cleaned)
        cleaned = cleaned.strip()
        if '~' in cleaned:
            tokens = cleaned.split()
            for tok in tokens:
                if tok == '~' or tok == '~*':
                    self.add_error(line_num, "Standalone tilde '~' token found outside inline dictionary.")

    def run(self):
        self.load_file()
        
        for line_num, text in enumerate(self.content, 1):
            in_dict = self._is_in_dict_or_rule_section(line_num)
            stripped = text.strip()
            
            # Rule-specific checks (leading star, forbidden sections, etc.)
            # Only apply when NOT inside a dictionary section
            if not in_dict:
                self.check_leading_star(line_num, text)
            
            # DL syntax checks - apply everywhere (both rules and dict entries
            # can contain DL constructs)
            self.check_cmb_args(line_num, text)
            self.check_triple_braces(line_num, text)
            self.check_inline_duplicates(line_num, text)
            self.check_stem_coverage(line_num, text)
            self.check_standalone_tilde(line_num, text)
            self.check_tilde_inside_word(line_num, text)
            self.check_attached_inline_dict(line_num, text)
            self.check_tilde_after_braces(line_num, text)
            
            # Structural checks - rules only
            if not in_dict:
                self.check_forbidden_sections(line_num, text)
                self.check_horizontal_separators(line_num, text)
            
            # Brace checks - apply to rules only
            if not in_dict:
                self.check_double_braces_single_element(line_num, text)
                self.check_single_braces_in_cmb(line_num, text)
        
        self.check_dictionary_definitions()
        
        return self.errors

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python dl_linter.py <file_path>")
        sys.exit(1)
    
    target_file = sys.argv[1]
    linter = DLLinter(target_file)
    errors = linter.run()
    
    if errors:
        for error in errors:
            print(error)
        sys.exit(1)
    else:
        print("No syntax errors found.")
        sys.exit(0)
