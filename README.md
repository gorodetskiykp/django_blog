# django_blog
Учебный проект на Django

# github
https://github.com/gorodetskiykp/django_blog
git clone https://github.com/gorodetskiykp/django_blog.git

# git
https://git-scm.com
git pull - забрать с сайта изменения
git add . - добавить в отслеживание все файлы
git commit -m "Создал новое приложение my_blog"
git push

# IDE
- https://www.jetbrains.com/pycharm/
- https://code.visualstudio.com

# Django
- pip install django
- django-admin startproject blog
- python manage.py runserver
- python manage.py migrate
- python manage.py startapp blog_app
- регистрация приложения в settings INSTALLED_APPS
- python manage.py createsuperuser

# Струкрута приложения
- admin - настройка админки
- models - модели данных - работа с БД
- views - логика работы приложения
- urls - маршрутизация

# Адреса
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin

# Логика работы WEB
1. Браузер отправляет запрос на web-сервер (request)
2. Маршрутизатор смотрит URL-адрес и параметры (urls)
3. Маршрутизатор перенаправил запрос в соответсвующий обработчик (handler, view)
4. Обработчик собирает в БД (models), готовит представление (templates)
5. Обработчик отправляет ответ клиенту (response)
