# Telegram Discount Cards WebApp

Веб-приложение для управления дисконтными картами в Telegram.

## Структура проекта

```
project/
├── index.html          # Основной HTML файл
├── package.json        # Конфигурация npm
├── vercel.json        # Конфигурация Vercel
└── README.md          # Данная инструкция
```

## Как задеплоить на Vercel

### Вариант 1: Через Vercel CLI

1. Установите Vercel CLI:
```bash
npm i -g vercel
```

2. Войдите в аккаунт:
```bash
vercel login
```

3. В корневой папке проекта выполните:
```bash
vercel
```

4. Следуйте инструкциям в терминале.

### Вариант 2: Через GitHub (рекомендуется)

1. Создайте репозиторий на GitHub
2. Загрузите все файлы в репозиторий
3. Зайдите на [vercel.com](https://vercel.com)
4. Нажмите "New Project"
5. Импортируйте ваш GitHub репозиторий
6. Vercel автоматически распознает статический сайт и задеплоит его

### Вариант 3: Через веб-интерфейс Vercel

1. Зайдите на [vercel.com](https://vercel.com)
2. Нажмите "Add New Project"
3. Выберите "Browse All Templates"
4. Загрузите ZIP-архив с файлами проекта

## Настройка в Telegram

После деплоя на Vercel:

1. Получите URL вашего приложения (например: `https://your-app.vercel.app`)
2. Создайте бота в Telegram через [@BotFather](https://t.me/botfather)
3. Настройте Web App для вашего бота:
```
/newapp
/setmenubutton
```

## Возможные проблемы и решения

### 1. Ошибка 404 после деплоя
- Убедитесь, что файл называется `index.html`
- Проверьте наличие `vercel.json` с правильной конфигурацией

### 2. Не работает в iframe
- `vercel.json` содержит настройки для работы в iframe Telegram
- Проверьте заголовки `X-Frame-Options` и `Content-Security-Policy`

### 3. Проблемы с сохранением данных
- Приложение использует Telegram Cloud Storage
- При тестировании вне Telegram данные сохраняются в localStorage

### 4. Ошибки JavaScript
- Проверьте консоль браузера на наличие ошибок
- Убедитесь, что Telegram WebApp SDK загружается корректно

## Особенности

- Адаптивный дизайн для мобильных устройств
- Поддержка темы Telegram
- Сохранение данных в Telegram Cloud Storage
- Fallback на localStorage для тестирования
- Современный UI с анимациями

## Технологии

- HTML5
- CSS3 (с современными возможностями)
- Vanilla JavaScript
- Telegram WebApp API
- Vercel для хостинга

## Лицензия

MIT