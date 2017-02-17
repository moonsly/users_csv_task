Release notes
========

Users list with custom template tags, CSV import on Python3, Django 1.9.


Extra features
========

Added CSV export and csv file with example export. Added fixture to load test users. Tests on main template tags, model fields validation.

INSTALL
========

1) Install python3.5

2) Make new virtualenv with python3:

`virtualenv -p python3 ./env/`

3) Clone project to virtualenv:

```
cd env
git clone https://github.com/moonsly/simple_task_manager.git ./code
```

4) Install dependencies (Django 1.9):

```
cd code
pip install -r ./requirements.txt
```

5) Run migrate to make initial DB structure:

`python ./manage.py migrate`

6) Create superuser to enter django admin:

`python ./manage.py createsuperuser`

or load ready-to-use fixtures with admin creds - admin / q1w2e3r4

8) Start server in debug mode:

`python ./manage.py runserver 0.0.0.0:8080`

9) Enter django admin at /8080, create new users and then tasks on / , mark them Doing/Done, delete, edit, enjoy :)


## Demo screenshots

![title](https://github.com/moonsly/simple_task_manager/raw/master/screenshots/TM1.png "General task list")

![title](https://github.com/moonsly/simple_task_manager/raw/master/screenshots/TM_add.png "Add task menu")

![title](https://github.com/moonsly/simple_task_manager/raw/master/screenshots/TM_edit.png "Edit task")

![title](https://github.com/moonsly/simple_task_manager/raw/master/screenshots/TM_filter_by_owner.png "Filter tasks by owner (only mine)")

![title](https://github.com/moonsly/simple_task_manager/raw/master/screenshots/TM_filter_done.png "Hide done tasks")


