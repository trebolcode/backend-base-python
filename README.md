# Basic Backend Started

Hello, this repository contains data to get started with Python project.

## What do you need to have installed?

Python must be installed:

[Python Install](https://www.python.org/)

This project uses Docker, so it is necessary to have it installed as well:

[Docker Install](https://docs.docker.com/desktop/)

## What is included in the installation?

| Tech    | Information                                    |
| ------- | ---------------------------------------------- |
| Python  | [Documentation](https://www.python.org/doc/)   |
| Uvicorn | [Documentation](https://www.uvicorn.org/)      |
| FastAPI | [Documentation](https://fastapi.tiangolo.com/) |

## Configurate .env file

| Variable           | Values        |
| ------------------ | ------------- |
| DATABASE_HOSTNAME= | postgres      |
| DATABASE_PORT=     | 5432          |
| DATABASE_PASSWORD= | trebolcode123 |
| DATABASE_NAME=     | trebolcode_db |
| DATABASE_USERNAME= | postgres      |
| POSTGRES_PASSWORD= | trebolcode123 |
| POSTGRES_DB=       | trebolcode_db |

## How to start?

It is necessary to build the project using:

`docker-compose -f Developer.yml build`

Then, to execute the project you can use:

`docker-compose -f Developer.yml up`

For only one time you need create tables in database:

`docker exec -it dev_basic_api bash`

Execute file create_tables.py:

`python3 create_tables.py`

And now you can open on the local host on port 8000.

[Local Host](http://localhost:8000/)

If you want to finish it, just press CTRL+D.

## Endpoints

Welcome

Items

### Version 0.2.0
