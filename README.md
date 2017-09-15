
Test application
=============

This application use REST API to work with users' accounts.

How to install
--------

* This project based on Django==1.9, Python==2.7

* Clone project from github:

        $ git clone https://github.com/dasap89/db2_blog.git
        $ cd db2_blog

* Create virtual environment inside repo:

        $ virtualenv env --python=python2.7
        $ source env/bin/activate

* Install packages from requirements.txt using pip:

        $ pip install -r requirements.txt

* Run migrations:

        $ python manage.py migrate

* Load fixtures:

        $ python manage.py loaddaata fixtures/data.json

* Run application or go to "How to use":

        $ python manage.py runserver


How to use
--------

Go to localhost:8000
