# grape

A Flask Service for GRAPE application documentation sweet


### Setup
```
python3 -m venv venv.gr
source venv.gr/bin/activate
pip install -r requirements.txt
pip freeze > requirements.txt
```

#### Config
Edit the `grape.ini` file to specify server specific values.

To autogenerate `grape.ini` secrets, call:
```python -m manage init_config```

#### Environment Specific Databases
This application supports different databases for different environments. To set a specific database for an environment 
set a `[DATABASE_<ENV>]` section in the `grape.ini` file. 

E.g.
```ini
[DATABASE_PRODUCTION]
dialect = postgres
username = postgres
password = admin
host = localhost
port = 5432
database = grape
```

##### Currently Supported Database Environments:
```ini
[DATABASE_DEVELOPMENT]
[DATABASE_TESTING]
[DATABASE_PRODUCTION]
```

## grape Management
The flask service is managed with the manage.py module. Depending on the template options you selected, some features 
may be unavailable.

It can be accessed with either:
```bash
python -m manage --help
```
or
```bash
python manage.py --help
```

```bash
usage: manage.py [-?] {run,db,start_workers,test,test_xml,shell,runserver} ...

positional arguments:
  {run,db,start_workers,test,test_xml,shell,runserver}
    run                 The main entrypoint to running the app :return: None
    db                  Perform database migrations
    start_workers       Start the celery worker(s)
    test                Run unit tests
    test_xml            Runs the unit tests specifically for bamboo CI/CD
    shell               Runs a Python shell inside Flask application context.
    runserver           Runs the Flask development server i.e. app.run()

optional arguments:
  -?, --help            show this help message and exit

```

## Using grape

### Celery
Before calling a celery task, you need to first start a worker with:

- ```python -m manage start_workers```

Then you can submit a task:
- ```curl -X POST "http://<SERVER_ADDR>/api/hello/slow_reverse?to_reverse=example" -H "accept: application/json"```

Submitting a task returns a task ID, which can be used to ask for a result:
- ```curl -X GET "http://<SERVER_ADDR>/api/hello/slow_reverse?task_id=c94e2f89-4b89-4a6b-bd6e-463f19b19aaa" -H "accept: application/json"```

### Globus

Globus endpoints require you to be authenticated, once authenticated you will need to register with Globus

Calling the following will return an auth_url that you should navigate to:
- ```curl -X GET "http://127.0.0.1:5000/api/globus/login" -H "accept: application/json"```

Globus will do it's part in the oauth flow, then redirect the user back to grape with a code 
that can be used to get Globus tokens. grape then issues new tokens that include the globus
information and returns them to the user.

Credits
-------
This package was created with Cookiecutter and the `flask_service` project template. The template was 
created and is maintained by Alexander Berger <alexander.berger@jax.org>.

This application was created by Michael A Gargano <michael.gargano@jax.org>.
