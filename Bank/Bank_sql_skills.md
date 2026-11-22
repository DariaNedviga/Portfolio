## Навыки Python

- Разработка консольных приложений с использованием функций, циклов и условных конструкций.
- Подключение Python к SQLite и выполнение SQL-запросов.
- Обработка пользовательского ввода и базовая обработка ошибок.
- Форматирование и представление табличных данных с помощью библиотеки `tabulate`.

## Навыки SQL

Запросы используются в CRUD-меню. Ниже – ключевые примеры по навыкам. Полный список запросов находится в файле `Bank.py`.

### Схема данных (основные таблицы)

| Таблица | Ключевые поля |
|---|---|
| `client` | `id`, `manager_id`, `first_name`, `last_name`, `patronymic`, `age`, `phone_number`, `bank_id` |
| `investment` | `id`, `client_id`, `name`, `interest_rate`, `cash_out_possibility`, `maturity` |
| `bank_card` | `id`, `type`, `service_price`, `cash_out_limit`, `accumulation_by_balance`, `contactless_payments`, `miles_accumulation`, `swift` |
| `card_client` | `card_id`, `client_id` |

---

### Вставка с подзапросами для внешних ключей (`INSERT` + `SELECT`)

```sql
INSERT INTO client
VALUES (
    NULL,
    (SELECT id FROM manager WHERE last_name = "{manager}"),
    "{name}", "{surname}", "{patronymic}",
    "{age}", "{phone_number}",
    (SELECT id FROM bank WHERE name = "{bank}")
);
```

---

### Выборка с `JOIN` и сортировкой (`SELECT` + `JOIN` + `ORDER BY`)

Демонстрирует соединение трёх таблиц и динамическую сортировку по имени клиента.

```sql
SELECT
    client.last_name,
    client.first_name,
    client.phone_number,
    bank.name AS bank_name,
    manager.last_name AS manager
FROM client
JOIN bank ON bank.id = client.bank_id
JOIN manager ON manager.id = client.manager_id
ORDER BY client.last_name {order};
```

---

### Удаление с подзапросом (`DELETE` + `SELECT` в `WHERE`)

Удаление записи по составному бизнес-ключу (имя + фамилия) без `id`.

```sql
DELETE FROM client
WHERE id = (
    SELECT id FROM client
    WHERE first_name = "{name}" AND last_name = "{surname}"
);
```

---

### Точечное обновление поля (`UPDATE` + `WHERE id = ...`)

Показывает изменение конкретного атрибута сущности с предварительным чтением старого значения (для информативного вывода).

```sql
UPDATE client
SET last_name = "{surname}"
WHERE id = {id};
```

---

### Выборка с ограничением количества строк (`LIMIT`)

Используется для постраничного вывода или ограничения выборки при просмотре списка вкладов.

```sql
SELECT
    investment.id,
    investment.name,
    investment.interest_rate,
    investment.cash_out_possibility,
    investment.maturity,
    client.first_name AS client_name,
    client.last_name AS client_surname
FROM investment
JOIN client ON client.id = investment.client_id
LIMIT {limit};
```

---

### Выборка с диапазоном (`BETWEEN`)

Фильтрация банковских карт по лимиту снятия наличных в заданном интервале.

```sql
SELECT
    bank_card.id,
    bank_card.type,
    bank_card.service_price,
    bank_card.cash_out_limit,
    bank_card.accumulation_by_balance,
    bank_card.contactless_payments,
    bank_card.miles_accumulation,
    bank_card.swift,
    client.last_name AS client_surname,
    client.first_name AS client_name
FROM card_client
JOIN bank_card ON card_client.card_id = bank_card.id
JOIN client ON card_client.client_id = client.id
WHERE cash_out_limit BETWEEN {between_1} AND {between_2};
```

---

### Простое удаление по `id` (`DELETE` + `WHERE id = ...`)

Базовый вариант удаления сущности, когда первичный ключ известен.

```sql
DELETE FROM investment WHERE id = {id};
```

---

### Вставка с явным списком значений (`INSERT` + `VALUES`)

Используется, когда все значения известны и не требуют подзапросов (например, добавление банковской карты).

```sql
INSERT INTO bank_card
VALUES (
    NULL, "{type}", "{price}", "{limit}", "{acc}",
    "{contact}", "{mile}", "{swift}"
);
```

