# Проект укорачивания url Yacut

### Разработчик:

 - [Мирошниченко Евгений Игоревич](https://github.com/Eugenii1996)

### О проекте:

На большинстве сайтов адреса страниц довольно длинные. Делиться такими длинными ссылками не всегда удобно, а иногда и вовсе невозможно.
Удобнее использовать короткие ссылки. Например, ссылки http://yacut.ru/lesson и http://yacut.ru/12e07d воспринимаются лучше, 
чем https://yandex.ru/trainer/backend-developer/lesson/12e07d96-31f3-449f-abcf-e468b6a39061/.
Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

Примененные технологии:
 - Python 3
 - Git
 - Pytest
 - Flask
 - Jinja2
 - SQLAlchemy

### Клонирование репозитория и переход в него в командной строке:

```bash
git clone git@github.com:Eugenii1996/yacut.git
```

```bash
cd yacut
```

Cоздать и активировать виртуальное окружение:

```bash
pyhton -m venv venv
```

* Если у вас Linux/MacOS

    ```bash
    source venv/bin/activate
    ```

* Если у вас windows

    ```bash
    source venv/scripts/activate
    ```

### Установка зависимостей из файла requirements.txt:

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

### Запуск проекта:



Из корневой деректории проекта yacut выполнить команды:

* Для запуска интерактивной оболочки flask:

    ```bash
    flask shell
    ```

* Для создания базы данных:

    ```shell
    from opinions_app import db
    db.create_all()
    ```

* Для запуска сервера:

    ```bash
    flask run
    ```
