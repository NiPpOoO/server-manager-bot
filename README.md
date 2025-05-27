# Server Manager Bot 🚀

Этот проект позволяет **управлять сервером** через API.

## 📌 Установка
1. Клонируйте репозиторий: git clone https://github.com/denis/server-manager-bot.git

2. Установите зависимости: pip install -r requirements.txt

3. Запустите API: uvicorn main:app --reload

   
## 🚀 API-эндпоинты
| Метод | URL              | Описание               |
|-------|-----------------|------------------------|
| GET   | /server/status  | Проверить статус      |
| POST  | /server/restart | Перезапустить сервер  |
| POST  | /server/shutdown| Выключить сервер      |


