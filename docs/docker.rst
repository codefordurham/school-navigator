Local Docker Development
========================


Mac-specific
------------

Install `Docker for Mac <https://www.docker.com/docker-mac>`_ .


Initial Local Development Setup
-------------------------------

The default development environment, provided by ``docker-compose.yml``, will provide you with these containers:

* PostgreSQL: v9.3 w/ PostGIS v2.3. ``./pgdata`` is mounted from the host environment to persist data.
* Django: Mounts the current directory into the container and uses ``manage.py runserver`` on port ``8000``.
* Nginx: Serves frontend application on port ``8081`` and proxies other requests to Django app.

Configure environment to use the docker settings file::

  echo "DJANGO_SETTINGS_MODULE=eatsmart.settings.docker" > .env

Build the containers::

  docker-compose build

Bring up the containers in this order::

  docker-compose up -d db proxy
  docker-compose up -d app

Now visit http://localhost:8001 in your browser.


Load DB Dump
~~~~~~~~~~~~

The easiest way to get data is to load a db dump::

  https://s3.amazonaws.com/school-navigator/db-2017-12-26.dump.zip
  unzip db-2017-12-26.dump.zip
  docker exec -i "`docker-compose ps -q db`" pg_restore --data-only --no-acl --no-owner -U "postgres" -d "postgres" < db.dump

You'll see a few errors for ``auth_permission``, ``django_content_type``, and ``django_migrations`` tables, but it will still work.

If you've modified the DB locally and want a fresh start, follow these steps first::

  docker-compose down
  docker volume rm schoolnavigator_pgdata  # remove existing PostgreSQL data
  docker-compose up -d db proxy
  docker-compose up -d app  # this will run manage.py migrate and provide a fresh DB

Now follow the ``pg_restore`` steps above.

To create the database dump (as an admin), you can run::

  ssh durhamschoolnavigator.org 'sudo -u postgres pg_dump -Fc school_navigator_production' > db.dump
