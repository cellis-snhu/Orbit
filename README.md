# Orbit
Orbit is a tool for managing your daily tasks

# Getting Started

# Run the development server
## Setup a virtual environment

### using `uv` (preferred)
Install [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Setup Virtual Environment

```shell
uv venv my-name --python3.12

uv pip install -r pyproject.toml

uv run flask run
```

### using python `venv`

```sh
python3 -m venv venv

source ./venv/bin/activate

pip install -r pyproject.toml

flask run
```

## Initial Database Setup
### Local SQLite database
To install the local sqlite database used by the dev
configuration run the following commands:
```shell
flask db init

flask db migrate -m 'initial migration'

flask db upgrade
```

### Setup a test user in the database
```shell
flask shell

>>> u = User(username='yourusername', email='yourname@example.com')
>>> u.set_password('testpass')
>>> db.session.add(u)
>>> db.session.commmit()
```

## Setup Production Postgresql database
Setup the initial database container by running
```shell
docker compose up -d
```

After, setup the initial migrations by running:
```shell
flask db migrate -m 'initial migration'

flask db upgrade
```

Lastly, set the `DATABASE_URL` environment variable as below with the correct strings
(the test postgres db is this string below)

```shell
DATABASE_URL=postgresql://postgres:secret@localhost:5432/postgres
```

run flask with
`flask run` or `uv run flask run`

#### Run tests

```shell
uv run python -m pytest
```
