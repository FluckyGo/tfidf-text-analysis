# tfidf-text-analysis
Сервис предоставляет возможность загрузки текстового файла, обработки его с использованием алгоритма TF-IDF и отображения результата в виде таблицы.

**Проект доступен локально по адресу : http://localhost:8000/**

**_Репозиторий проекта:_**
```
https://github.com/FluckyGo/tfidf-text-analysis
```

### Запуск проекта локально:

**_Репозиторий проекта, клонируйте на локальный компьютер_:**
```
https://github.com/FluckyGo/tfidf-text-analysis.git
```

**_В директории проекта на примере .env.example создать .env:_**
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
**_В директории проекта :_**
```
pythom -m venv venv - Создание виртуального окружение

Активация виртуального окружения:

bash/zsh: source venv/bin/activate
cmd.exe: venv\Scripts\activate

pip install requarements.txt - Установка зависимостей проекта

cd backend - Перейти в каталог проекта

python manage.py migrate - Применить миграции

python manage.py createsuperuser - Создать админа, если нужно

python manage.py runserver - Запустить сервис локально

```



**Возможное дальнейшее развитие проекта :**
```
- Отказаться от templates и для frontend использовать SPA React
- Написать тесты на Pytest
- В проекте оставлена возможность использовать Postgresql
- Запуск проекта через Docker

```

### *Бэк написал:*
[FluckyGo](https://github.com/FluckyGo)