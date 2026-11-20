## SQL: навыки

Запросы используются в трёх модулях: парсер словаря, CRUD-меню, модуль статистики. Полный список в [`arch_queries.md`](https://github.com/DariaNedviga/Portfolio/blob/main/arch_queries.md), здесь ключевые примеры по навыкам.

### Схема данных

| Таблица | Поля |
|---|---|
| `Term` | id, word, latin, definition, extra_info |
| `Link` | id, word, latin, link |
| `Archaeologist` | id, surname, surname_lat, name, years, achievements, extra_info |

---

### Агрегация и условный подсчёт (`COUNT`, `DISTINCT`, `SUM`, `CASE`)

```sql
SELECT DISTINCT COUNT(*),
       SUM((CASE WHEN col IS NOT NULL AND col != '' THEN 1 ELSE 0 END) + ...)
FROM {table};
```

---

### Параметризованная вставка (`INSERT` + placeholders)

```sql
INSERT INTO Term (word, latin, definition, extra_info) VALUES (?, ?, ?, ?);
```

---

### Динамический `SELECT` по имени таблицы  (из фиксированного списка `Term`/`Link`/`Archaeologist`)

```sql
SELECT DISTINCT COUNT(*), SUM({expr_sum}) FROM {table}
```

---

### Точечное обновление и удаление по `id` (`UPDATE`, `DELETE`)

```sql
UPDATE Term SET word=?, latin=?, definition=?, extra_info=? WHERE id=?;
DELETE FROM {table_name} WHERE id=?;
```
