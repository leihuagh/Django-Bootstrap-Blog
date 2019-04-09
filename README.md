# Django Bootstrap Blog

## Credit by

- [Corey Schafer Playlist](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
- [GitHub](https://github.com/CoreyMSchafer/code_snippets/tree/master/Django_Blog)

## Packages in Global Environment

- python 3.7.3
- virtualenv 6.4.3
- pylint
- autopep8
- flake8

## Packages in Virtual Environment

- Django 2.2
- mysqlclient 1.4.2
- pillow
- Faker
- django-crispy-forms
- requests

## File Structure

### Project

- config

### Apps

- core
- home
- company
- users
- authentication
- blog

## Commands Used in Project

- Start Project

```shell
django-admin startproject config .
```

- Start App

```shell
python manage.py startapp <app name>
```

- Run Server

```shell
python manage.py runserver
```

- Migrations

```shell
python manage.py makemigrations
python manage.py migrate
```

- Create Super User

```shell
python manage.py createsuperuser
```

- Dump Data Example

```shell
python manage.py dumpdata auth.User --format json --indent 4 > texture/users.json
```

- Seed Data Example

```shell
python manage.py loaddata texture/users.json
```

- Collect Static Files

```shell
python manage.py collectstatic
```

## Pagination Variables

```python
<ul>
    <li>{{ <app>.has_previous}}</li>
    <li>{{ <app>.number }}</li>
    <li>{{ <app>.paginator.count }}</li>
    <li>{{ <app>.paginator.page_range }}</li>
    <li>{{ <app>.has_next }}</li>
</ul>
```
