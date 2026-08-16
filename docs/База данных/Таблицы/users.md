### Таблица `users` (Пользователи и Администраторы)
* `id` (SERIAL, Primary Key)
* `email` (VARCHAR(150), Unique, Not Null) — для авторизации.
* `password_hash` (VARCHAR(255), Nullable) — хэш пароля (null, если вход только через OAuth).
* `name` (VARCHAR(100)) — имя пользователя.
* `oauth_provider` (VARCHAR(50), Nullable) — 'google', 'vk' или null.
* `oauth_id` (VARCHAR(100), Nullable) — ID в соцсети.
* `is_admin` (BOOLEAN, Default False) — флаг администратора.
* `country_id` (INT, Nullable, Foreign Key -> countries.id, ON DELETE SET NULL) — страна проживания.
* `city_id` (INT, Nullable, Foreign Key -> cities.id, ON DELETE SET NULL) — город проживания.
* `whatsapp` (VARCHAR(50), Nullable) — телефон для WhatsApp.
* `telegram` (VARCHAR(100), Nullable) — никнейм в Telegram.
* `zalo` (VARCHAR(50), Nullable) — телефон/ID Zalo (популярно во Вьетнаме).
* `max` (VARCHAR(100), Nullable) — никнейм/ID в сервисе Max.
* `preferred_contact` (VARCHAR(20), Default 'email') — предпочтительный способ связи ('email', 'whatsapp', 'telegram', 'zalo', 'max').
* `payout_details` (TEXT, Nullable) — реквизиты, куда перечислять выручку с продаж.
* `created_at` (TIMESTAMP, Default NOW())

