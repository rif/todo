TODO
=====

Simple TODO task list manager written in django.

Features
----------
- clean user interface
- ajax creation/editing/deleting of tasks
- REST api

Examples
------------
*List tasks*

curl -X GET -u user:pass http://localhost:8000/api/tasks/

*Create a task*

curl -X POST --data 'title=test;priority=1' -u user:pass http://localhost:8000/api/tasks/

*Edit a task*

curl -X PUT --data 'title=test;priority=10' -u user:pass http://localhost:8000/api/tasks/1

*Get a task*

curl -X GET -u user:pass> http://localhost:8000/api/tasks/4

*Delete a task*

curl -X DELETE -u user:pass> http://localhost:8000/api/tasks/4

Installation
-------------

mkvirtualenv --no-site-packages todo

git clone git://github.com/rif/todo.git

cd todo/

pip install -r pip_requirements.txt

./manage.py migrate

./manage.py collectstatic

./manage.py runserver

