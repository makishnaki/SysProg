# Заказ 05 — мониторинг доступности сервисов
`services.json` — список внутренних адресов. Напишите **свою** утилиту проверки
сетевых соединений и HTTP-ответов, с журналом времени и тайм-аутами.

Запустите `python lab_services.py`. Это тестовые HTTP-сервисы только на 127.0.0.1.
На 8765 работает `/health` со статусом 200, `/error` отвечает 503,
`/slow` задерживается на 3 секунды. На 8766 — второй здоровый сервис.
8767 намеренно не запущен. Если порты заняты, измените их в обоих файлах.

Проверки: выключите 8766, замените адрес на `/error`, `/slow` и обратно;
различайте недоступный порт, тайм-аут и HTTP 503. Ping не заменяет HTTP-проверку.

## Результаты проверки

1. **Запуск тестового стенда (`lab_services.py`)**
   ![Запуск тестового стенда](https://github.com/makishnaki/SysProg/blob/main/05%20—%20Checking%20services/screenshots/1TerminalStart.png)

2. **Штатная проверка (`/health`)**
   ![Штатная проверка](https://github.com/makishnaki/SysProg/blob/main/05%20—%20Checking%20services/screenshots/2TerminalStart.png)

3. **Ошибка сети при некорректном адресе**
   ![Ошибка сети](https://github.com/makishnaki/SysProg/blob/main/05%20—%20Checking%20services/screenshots/1Proverka.png)

4. **Проверка HTTP 503 (`/error`) и таймаута (`/slow`)**
   ![HTTP 503 и таймаут](https://github.com/makishnaki/SysProg/blob/main/05%20—%20Checking%20services/screenshots/2Proverka.png)

5. **Отключение порта 8766**
   ![Отключение порта 8766](https://github.com/makishnaki/SysProg/blob/main/05%20—%20Checking%20services/screenshots/3Proverka.png)
