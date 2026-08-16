### Таблица `users` (Пользователи и Администраторы)
* `id` (SERIAL, Primary Key)
* `email` (VARCHAR(150), Unique, Not Null) — для авторизации.
* `name` (VARCHAR(100)) — имя пользователя.
* `oauth_provider` (VARCHAR(50), Nullable) — 'google', 'vk' или null.
* `oauth_id` (VARCHAR(100), Nullable) — ID в соцсети.
* `is_admin` (BOOLEAN, Default False) — флаг администратора.
* `created_at` (TIMESTAMP, Default NOW())
