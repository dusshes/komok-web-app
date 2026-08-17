### Таблица `cities` (Города)
* `id` (SERIAL, Primary Key)
* `name` (VARCHAR(100), Not Null) — наименование города.
* `country_id` (INT, Foreign Key -> countries.id, ON DELETE CASCADE) — ссылка на страну.

Наполнение:
- "Дананг"
