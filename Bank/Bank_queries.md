# Все SQL-запросы проекта
**2025, Банк «Триумф»**
**СУБД: SQLite**

---

## 1. DML: вставка данных (INSERT)

Демонстрирует: `INSERT` с подзапросами для внешних ключей, `INSERT` с явным списком значений.

### 1.1. Клиент (с подзапросами для `manager_id` и `bank_id`)
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

### 1.2. Вклад (с подзапросом для `client_id` по трём полям)
```sql
INSERT INTO investment
VALUES (
    NULL,
    (SELECT id FROM client
     WHERE last_name = "{client_surname}"
       AND first_name = "{client_name}"
       AND phone_number = "{client_phone}"),
    "{name}", {interest}, {cash_out}, {maturity}
);
```

### 1.3. Банковская карта (прямая вставка всех полей)
```sql
INSERT INTO bank_card
VALUES (
    NULL, "{type}", "{price}", "{limit}", "{acc}",
    "{contact}", "{mile}", "{swift}"
);
```

---

## 2. DML: чтение данных (SELECT)

Демонстрирует: `JOIN` нескольких таблиц, алиасы, динамическую сортировку, `LIMIT`, `BETWEEN`.

### 2.1. Список клиентов с банком и менеджером
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

### 2.2. Список вкладов с данными клиента (с `LIMIT`)
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

### 2.3. Банковские карты с лимитом в диапазоне (`BETWEEN`)
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

### 2.4. Чтение одного поля перед обновлением (пример для `last_name`)
```sql
SELECT last_name FROM client WHERE id = {id};
```
> Аналогичные `SELECT` используются для `first_name`, `age`, `name`, `interest_rate`, `cash_out_possibility`, `maturity`, `type`, `service_price`, `cash_out_limit`, `accumulation_by_balance` и т.д.

---

## 3. DML: изменение данных (UPDATE)

Демонстрирует: `UPDATE` с `SET` и `WHERE` по первичному ключу.

### 3.1. Обновление поля клиента (пример: фамилия)
```sql
UPDATE client SET last_name = "{surname}" WHERE id = {id};
```

### 3.2. Обновление поля вклада (пример: название)
```sql
UPDATE investment SET name = "{name}" WHERE id = {id};
```

### 3.3. Обновление поля банковской карты (пример: тип)
```sql
UPDATE bank_card SET type = "{type}" WHERE id = {id};
```
> Аналогичные `UPDATE` выполняются для остальных полей каждой сущности (`first_name`, `age`, `interest_rate`, `cash_out_possibility`, `maturity`, `client_id`, `service_price`, `cash_out_limit` и др.).

---

## 4. DML: удаление данных (DELETE)

Демонстрирует: `DELETE` по первичному ключу и `DELETE` с подзапросом по бизнес-ключу.

### 4.1. Удаление по `id` (пример: вклад)
```sql
DELETE FROM investment WHERE id = {id};
```

### 4.2. Удаление клиента по имени и фамилии (через подзапрос)
```sql
DELETE FROM client
WHERE id = (
    SELECT id FROM client
    WHERE first_name = "{name}" AND last_name = "{surname}"
);
```
