## Навыки Python

- Разработка консольных приложений с использованием функций, циклов и условных конструкций.
- Подключение Python к SQLite и выполнение SQL-запросов.
- Обработка пользовательского ввода и базовая обработка ошибок.
- Форматирование и представление табличных данных с помощью библиотеки `tabulate`.

-------
## Навыки SQL

SQL используется для работы с базой данных банка «Триумф»: управление клиентами, вкладами и банковскими картами.

### Схема данных

| Таблица | Поля |
|---|---|
| `bank` | id, name, address, number_of_employess |
| `manager` | id, first_name, last_name, patronymic, phone, bank_id |
| `client` | id, manager_id, first_name, last_name, patronymic, age, phone_number, bank_id |
| `passport_data` | id, first_name, last_name, patronymic, gender, date_of_birth, place_of_birth, serial_number, address, department_code, issued_by, date_of_issue, client_id |
| `investment` | id, client_id, name, interest_rate, cash_out_possibility, maturity |
| `loan` | id, client_id, name, interest_expense, monthly_payment, total_amount, remainder, maturity_date |
| `bank_card` | id, type, service_price, cash_out_limit, accumulation_by_balance, contactless_payments, miles_accumulation, swift |
| `card_client` | card_id, client_id |

---

### Создание реляционной структуры и связей (`PRIMARY KEY`, `FOREIGN KEY`)

```sql
CREATE TABLE "client" (
    "id" INTEGER NOT NULL UNIQUE,
    "manager_id" INTEGER,
    "first_name" TEXT,
    "last_name" TEXT,
    "patronymic" TEXT,
    "age" INTEGER,
    "phone_number" INTEGER,
    "bank_id" INTEGER,
    PRIMARY KEY("id" AUTOINCREMENT),
    FOREIGN KEY("manager_id") REFERENCES "manager"("id"),
    FOREIGN KEY("bank_id") REFERENCES "bank"("id")
);
```

---

### Добавление данных с подзапросами (`INSERT`, `SELECT`)

```sql
INSERT INTO client VALUES (
    NULL,
    (SELECT id FROM manager WHERE last_name = "{manager}"),
    "{name}", "{surname}", "{patronymic}",
    "{age}", "{phone_number}",
    (SELECT id FROM bank WHERE name = "{bank}")
);
```

---

### Объединение таблиц (`JOIN`)

Получение списка клиентов с названиями банков и фамилиями менеджеров:

```sql
SELECT client.last_name, client.first_name,
       client.phone_number,
       bank.name AS bank_name,
       manager.last_name AS manager
FROM client
JOIN bank ON bank.id = client.bank_id
JOIN manager ON manager.id = client.manager_id
ORDER BY client.last_name;
```

---

### Фильтрация по диапазону (`WHERE`, `BETWEEN`)

```sql
SELECT bank_card.id, bank_card.type,
       bank_card.cash_out_limit
FROM card_client
JOIN bank_card ON card_client.card_id = bank_card.id
JOIN client ON card_client.client_id = client.id
WHERE cash_out_limit BETWEEN {between_1} AND {between_2};
```

---

### Ограничение выборки (`LIMIT`)

```sql
SELECT investment.id, investment.name,
       investment.interest_rate,
       client.first_name AS client_name
FROM investment
JOIN client ON client.id = investment.client_id
LIMIT {limit};
```

---

### Точечное обновление и удаление по `id` (`UPDATE`, `DELETE`)

```sql
UPDATE client
SET last_name = "{surname}"
WHERE id = {id};

DELETE FROM investment
WHERE id == {id};
```
