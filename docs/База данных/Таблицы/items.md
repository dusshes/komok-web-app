### Таблица `items` (Единая таблица вещей, заявок и товаров)
* `id` (SERIAL, Primary Key)
* `user_id` (INT, Nullable, Foreign Key -> users.id, ON DELETE SET NULL) — автор заявки (null, если вещь добавил сам админ).
* `title` (VARCHAR(255), Not Null) — название вещи.
* `description` (TEXT) — состояние, дефекты, описание.
* `price` (NUMERIC(10, 2), Not Null) — цена (согласованная или предложенная клиентом).
* `status` (VARCHAR(50), Default 'pending') — Жизненный цикл вещи:
  * `pending` — заявка от клиента создана и ждет проверки админом.
  * `rejected` — админ отклонил заявку на продажу.
  * `available` — заявка одобрена, вещь выставлена на витрину (её видят все).
  * `booked` — вещь забронирована покупателем (снята с витрины).
  * `sold` — вещь успешно продана и выдана покупателю.
* `image_url` (VARCHAR(500), Nullable) — путь к фото.
* `created_at` (TIMESTAMP, Default NOW())
