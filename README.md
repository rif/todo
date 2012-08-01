TODO
=====

Simple TODO task list manager written in django.

Features:
- clean user interface
- ajax creation/editing/deleting of tasks
- REST api

Examples:

*List tasks*
curl -X GET -u <username>:<password> http://localhost:8000/api/tasks

*Create a task*

curl -X POST --data 'title=test;priority=1' -u <username>:<password> http://localhost:8000/api/tasks

*Edit a task*

curl -X PUT --data 'title=test;priority=10' -u <username>:<password> http://localhost:8000/api/task/1/

*Get a task*

curl -X GET -u <username>:<password> http://localhost:8000/api/task/4/

