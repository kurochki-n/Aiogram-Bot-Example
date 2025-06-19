# Telegram Бот на aiogram

## Описание

Этот проект — пример реализации Telegram-бота на базе [aiogram 3.x](https://docs.aiogram.dev/).

## Основные возможности
- Обработка команд и сообщений пользователей
- Обработка команд и сообщений администраторов бота
- Проверка подписки на канал
- Проверка прав администратора
- Использование FSM (Finite State Machine) для управления состояниями
- Кастомные inline и reply клавиатуры
- Легкая локализация сообщений

## Быстрый старт

1. **Склонируйте репозиторий:**
   ```bash
   git clone <repo-url>
   cd aiogram-bot-example
   ```
2. **Создайте и настройте файл окружения:**
   - Переименуйте `.env.example` в `.env`
   - Укажите значения переменных:
     ```env
     BOT_TOKEN=ваш_токен_бота
     CHANNEL_ID=@your_channel_or_id
     ```
3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Запустите бота:**
   ```bash
   python __main__.py
   ```

## Переменные окружения
- `BOT_TOKEN` — токен вашего Telegram-бота
- `CHANNEL_ID` — ID или username канала для проверки подписки

## Структура проекта
```
aiogram-bot-example/
├── __main__.py              # Точка входа
├── config_reader.py         # Загрузка конфигурации из .env
├── handlers/                # Хендлеры команд и сообщений
│   ├── admin_router.py      # Админ-команды
│   ├── user_router.py       # Пользовательские команды
│   ├── keyboards.py         # Клавиатуры
│   ├── localization.py      # Локализация сообщений
│   └── states.py            # Состояния FSM
├── middlewares/             # Промежуточные обработчики
│   ├── check_sub.py         # Проверка подписки
│   ├── check_is_admin.py    # Проверка прав администратора
│   └── callback_answer.py   # Пример middleware для callback
├── utils/                   # Вспомогательные функции
│   └── tools.py             # Получение списка админов
├── requirements.txt         # Зависимости
└── README.md                # Документация
```

## Пример команд
- `/command` — стартовое сообщение
- Сообщения с текстом `text` — переход в другое состояние
- Inline и reply клавиатуры для взаимодействия

## Используемые технологии
- [aiogram 3.x](https://github.com/aiogram/aiogram)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [pydantic](https://github.com/pydantic/pydantic)

## Расширение и кастомизация
Вы можете легко добавить новые команды, состояния, клавиатуры и middleware, а также адаптировать логику под свои задачи.

---

> **Удачи в разработке!**
