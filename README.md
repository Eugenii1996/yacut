# Проект укорачивания url Yacut

### Разработчик:

 - [Мирошниченко Евгений Игоревич](https://github.com/Eugenii1996)

### О проекте:

Проект представляет собой сервис по укорачиваню исходных url до удобочитаемого варианта.
Вам нужно просто вставить свою ссылку в поле с исходным url и получить тот url, который вы хотите, либо сгенерированный автоматически, если у вас нет предпочтений.

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
