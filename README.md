# Django 3 by Exaple - Antonio Melé [packt]
Based on book of Antonio Melé -  Django By Exaple

## Useful commands:
* Python and Django version check
    ```shell
    $ python
    Python 3.9.4
    >>> import django
    >>> django.VERSION
    (3, 0, 14, 'final', 0)
    ```
  
* Creating virtual enviroment
    ```shell
    $ python -m venv venv
    $ source venv/bin/activate
    (venv) $
    ```
  
* Creating new Django project
    ```shell
    (venv) $ cd mysite
    (venv) ~/mysite$ python manage.py migrate
    ```
  
* Running local server
    ```shell
    (venv) ~/mysite$ python manage.py runserver localhost:8000
    ```
    
* Creating new app
    ```shell
    (venv) ~/mysite$ python manage.py startapp blog
    ```
  
* Interactive Django shell
  ```shell
  (venv) ~/mysite$ python manage.py shell
  ```
  
## Usefull links
* Path converters: `path("/<int:pk>/<slug:slug>/<int:year>")` \
https://docs.djangoproject.com/en/3.2/topics/http/urls/#path-converters
  
* Regex Path: `re_path(r"^confirm-email/(?P<key>[-:\w]+)/$"` \
https://docs.djangoproject.com/en/3.2/topics/http/urls/#using-regular-expressions
  
* URL Namespace `blog:post_list`, `blog:post_detail` \
https://docs.djangoproject.com/en/3.2/topics/http/urls/#url-namespaces

* URL resolvers `reverse('news-archive')` \
https://docs.djangoproject.com/en/3.2/ref/urlresolvers/
  
* Template language: \
https://docs.djangoproject.com/en/3.2/ref/templates/language/
  
* Template build in tags: \
https://docs.djangoproject.com/en/3.2/ref/templates/builtins/
  
* Class-based views: \
https://docs.djangoproject.com/en/3.2/topics/class-based-views/intro/
  

## Chapter 1
1. Instaling Django
2. Creating first project
3. Schema project for blog app
4. Creating admin site for blog model
5. QuerySet and managers
6. Setting up list view and detail view
7. Creating template views
8. Adding pagination
9. Class-based views