# Проект укорачивания url Yacut

### Разработчик:

 - [Мирошниченко Евгений Игоревич](https://github.com/Eugenii1996)

### О проекте:

Проект представляет собой сервис по укорачиваню исходных url до удобочитаемого варианта.
Вам нужно просто вставить свою ссылку в поле с исходным url и получить тот url, который вы хотите, либо сгенерированный автоматически, если у вас нет предпочтений.

Примененные библиотеки:
 - alembic==1.7.5
 - attrs==21.4.0
 - click==8.0.3
 - faker==12.0.1
 - flake8==4.0.1
 - flask-migrate==3.1.0
 - flask-sqlalchemy==2.5.1
 - flask-wtf==1.0.0
 - flask==2.0.2
 - greenlet==1.1.2
 - iniconfig==1.1.1
 - itsdangerous==2.0.1
 - jinja2==3.0.3
 - mako==1.1.6
 - markupsafe==2.0.1
 - mccabe==0.6.1
 - mixer==7.2.2
 - packaging==21.3
 - pluggy==1.0.0
 - py==1.11.0
 - pycodestyle==2.8.0
 - pyflakes==2.4.0
 - pyparsing==3.0.7
 - pytest-env==0.6.2
 - pytest==7.1.1
 - python-dateutil==2.8.2
 - python-dotenv==0.19.2
 - six==1.16.0
 - sqlalchemy==1.4.29
 - tomli==2.0.1
 - werkzeug==2.0.2
 - wtforms==3.0.1

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

Из корневой деректории проекта yacut выполнить команду:

```bash
flask run
```
