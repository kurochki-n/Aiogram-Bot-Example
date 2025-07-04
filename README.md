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
   git clone git@github.com:kurochki-n/Aiogram-Bot-Example.git
   cd Aiogram-Bot-Example
   ```
2. **Создайте и настройте .gitignore и файл окружения:**
   - Переименуйте `.gitignore.example` в `.gitignore`
   - Переименуйте `.env.example` в `.env`
   - Укажите значения переменных:
     ```env
     BOT_TOKEN=токен-вашего-бота
     CHANNEL_ID=айди-вашего-канала
     ```
3. **Установите зависимости с помощью пакетного менеджера [uv](https://github.com/astral-sh/uv):**
   ```bash
   uv sync
   ```
4. **Запустите бота:**
   ```bash
   uv run main.py
   ```

## Переменные окружения
- `BOT_TOKEN` — токен вашего Telegram-бота
- `CHANNEL_ID` — ID или канала для проверки подписки

## Основная структура проекта
```
Aiogram-Bot-Example/
├── main.py                  # Точка входа
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
└── README.md                # Документация
```

## Используемые технологии
- [aiogram 3.x](https://github.com/aiogram/aiogram)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [pydantic](https://github.com/pydantic/pydantic)

## Расширение и кастомизация
Вы можете легко добавить новые команды, состояния, клавиатуры и middleware, а также адаптировать логику под свои задачи.

---

> **Удачи в разработке!**
