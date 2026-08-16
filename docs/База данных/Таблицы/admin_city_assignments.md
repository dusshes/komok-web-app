### Таблица `admin_city_assignments` (Закрепление администраторов за городами)
* `admin_id` (INT, Primary Key, Foreign Key -> users.id, ON DELETE CASCADE) — ссылка на администратора.
* `city_id` (INT, Primary Key, Foreign Key -> cities.id, ON DELETE CASCADE) — ссылка на город.

*Примечание: Составной первичный ключ (`admin_id`, `city_id`) обеспечивает уникальность записи.*
