# Django and ReactJS example project

https://github.com/sochi-team/hospital

## Usage

Start dev provisions (psql) using docker:

```sh
$ ./dev-provision.sh up -d
Starting hospital_postgres_1 ... done
Starting hospital_adminer_1  ... done
$
```

Setup:

```sh
$ ./setup.sh
...
```

### Server

Go to the `server` directory.

Activate python venv:

```sh
$ source ./.env/bin/activate
(.env) $ which python
/Users/fedorenkomi/playground/hospital/server/.env/bin/python
(.env) $
```

Start django dev server in `server/hospital` directory:

```sh
$ python manage.py runserver
...
```

### Polls

http://localhost:8000/polls 
http://localhost:8000/admin user:admin password:7415
