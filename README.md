Release notes
========

Users list with custom template tags, CSV import on Python3, Django 1.9.
All the features implemented according to trial task spec, including extra features like Excel export and Excel file (in repo).


Extra features
========

Added CSV export and csv file with example export. Added fixture to load test users. Tests on main template tags, model fields validation.

INSTALL
========

1) Install python2.7

2) Make new virtualenv with python2.7:

`virtualenv -p python2 ./env/`

3) Clone project to virtualenv:

```
cd env
git clone https://github.com/moonsly/users_csv_task.git ./code
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

or load ready-to-use fixtures with admin creds - admin / q1w2e3r4 :

`python ./manage.py loaddata exos_task/fixtures/users_fixture.json`

7) Run tests:

```
$ python ./manage.py test exos_task/tests/ -v2

Creating test database for alias 'default' (':memory:')...
Operations to perform:
  Synchronize unmigrated apps: staticfiles, messages
  Apply all migrations: admin, contenttypes, exos_task, auth, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying exos_task.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying sessions.0001_initial... OK
test1_birthdays_bizzfuzz (exos_task.tests.tests_main.MainTests) ... ok
test2_incorrect_date (exos_task.tests.tests_main.MainTests) ... ok
test3_incorrect_date_format (exos_task.tests.tests_main.MainTests) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.056s

OK
Destroying test database for alias 'default' (':memory:')...
```

8) Start server in debug mode:

`python ./manage.py runserver 0.0.0.0:8080`

9) Enter localhost:8080/users , see current users list, add/delete/edit users, export them to CSV.


## Demo screens
exos_1.png  exos_2_edit.png  exos_3_form_validation.png  exos_4_user_view.png  exos_5_add_new_user.png

![title](https://github.com/moonsly/users_csv_task/raw/master/screens/exos_1.png "General users list")

![title](https://github.com/moonsly/users_csv_task/raw/master/screens/exos_2_edit.png "Edit user")

![title](https://github.com/moonsly/users_csv_task/raw/master/screens/exos_3_form_validation.png "Edit user form validation")

![title](https://github.com/moonsly/users_csv_task/raw/master/screens/exos_4_user_view.png "View user")

![title](https://github.com/moonsly/users_csv_task/raw/master/screens/exos_5_add_new_user.png "Add new user")


