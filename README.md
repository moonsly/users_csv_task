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

2) Make new virtualenv with python3:

`virtualenv -p python3 ./env/`

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

``

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


