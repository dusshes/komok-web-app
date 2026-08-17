### Таблица `cityes` (Города)
* `id` (SERIAL, Primary Key)
* `name` (VARCHAR(100)) — наименование города.
* `country_id` (INT, Foreign Key -> countryes.id, ON DELETE CASCADE) - ссылка на страну

Наполнение:
- "Дананг"