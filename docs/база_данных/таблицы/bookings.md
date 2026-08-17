### Таблица `bookings` (Бронирование товаров)
* `id` (SERIAL, Primary Key)
* `item_id` (INT, Foreign Key -> items.id, ON DELETE CASCADE) — какая вещь забронирована.
* `user_id` (INT, Foreign Key -> users.id, ON DELETE CASCADE) — строго ссылка на авторизованного клиента, который забронировал товар.
* `booking_status` (VARCHAR(50), Default 'Активна') — статусы: `Активна` (ждет в магазине), `Выкуплена` (товар забрали), `Отменена` (бронь истекла или снята).
* `created_at` (TIMESTAMP, Default NOW())