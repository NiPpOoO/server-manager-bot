# 🚀 Server Manager Bot  

**Server Manager Bot** — это API для управления сервером, его мониторинга и логирования.  

## 📌 Основные возможности  
✅ Получение информации о сервере (CPU, RAM, диск)  
✅ Управление сервером (`restart`, `shutdown`)  
✅ Логирование событий  
✅ Поддержка базы данных PostgreSQL  

---

## 🔧 Установка  
1. **Клонируйте репозиторий:**  
   ```bash
   git clone https://github.com/denis/server-manager-bot.git
2. Установите зависимости: pip install -r requirements.txt

3. Настройте .env с параметрами базы данных: DATABASE_URL=postgresql://user:password@localhost/server_manager_db
SECRET_KEY=super_secret_key
DEBUG=True

4. Запустите API: uvicorn main:app --reload

API-эндпоинты

Метод	URL	Описание
GET	/server/status	Проверить статус
POST	/server/restart	Перезапустить сервер
POST	/server/shutdown	Выключить сервер
API-эндпоинты
