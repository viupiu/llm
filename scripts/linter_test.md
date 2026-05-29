# Test Rules File

## Словарь: valid_dict
apple
=>яблоко

* [dict(valid_dict)] *
[dict(valid_dict)] *
ERROR: Rule does not start with '*' .

[@cmb({один})]
ERROR: cmb requires at least two arguments.

{{{тройные}}}
ERROR: Triple braces are forbidden.

{кот/кот}
ERROR: Duplicate alternatives inside inline dictionary: кот

{вернус~/вернусь}
ERROR: Redundant alternative already covered by stem: вернусь

{~/нет}
ERROR: Standalone tilde is forbidden.

мужик~у
ERROR: Tilde inside word is forbidden.

коти{к/шка}
ERROR: Inline dictionary cannot be attached to word fragment.

{котик/котишка}~
ERROR: Tilde must belong to dictionary element, not to dictionary block.

Ответы:
ERROR: Forbidden section in rules file.

---
ERROR: Horizontal separators are forbidden.

[dict(undefined_dict)]
ERROR: Reference to undefined dictionary: undefined_dict

{{потом}}
ERROR: Double braces used for a single element.

[@cmb({да/ага})]
ERROR: Alternatives inside cmb must use double braces.
