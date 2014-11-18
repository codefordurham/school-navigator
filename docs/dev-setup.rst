Development Setup
=================

Follow these steps to contribute to the School Navigator project!


.. _project-architecture:

Project Architecture
--------------------

The project is divided into two components, the frontend and backend:

* :ref:`Frontend <frontend-setup>`: front facing user interface. Built in AngularJS, HTML, and CSS.
* :ref:`Backend <backend-setup>`: backend API that powers the frontend. Built in Python/Django, PostgreSQL, and PostGIS.

Generally, unless you're working on the REST API, you'll develop the
:ref:`Frontend <frontend-setup>`.


.. _clone-the-repository:

Clone the Repository
--------------------

To get started, you'll first need to clone the GitHub repository so you can
work on the project locally. In a terminal, run:

.. code-block:: bash

    git clone git@github.com:codefordurham/school-navigator.git
    cd school-navigator


.. _frontend-setup:

Frontend Setup
--------------

Once you've cloned the project, open the ``frontend`` directory::

    cd frontend/

Next run a basic HTTP server with Python:

.. code-block:: bash

    # Python <= 2.7
    python -m SimpleHTTPServer
    # Python >= 3.0
    python -m http.server

Now visit http://localhost:8000/ in your browser.


.. _backend-setup:

Backend Setup
-------------

Below you will find basic setup instructions for the school_inspector
project. To begin you should have the following applications installed on your
local development system:

- Python >= 3.4 (3.4 recommended)
- `pip >= 1.5 <http://www.pip-installer.org/>`_
- `virtualenv >= 1.11 <http://www.virtualenv.org/>`_
- `virtualenvwrapper >= 3.0 <http://pypi.python.org/pypi/virtualenvwrapper>`_
- Postgres >= 9.1 
- git >= 1.7


The deployment uses SSH with agent forwarding so you'll need to enable agent
forwarding if it is not already by adding ``ForwardAgent yes`` to your SSH config.


Getting Started
~~~~~~~~~~~~~~~

If you need Python 3.4 installed, you can use this PPA::

    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt-get update
    sudo apt-get install python3.4-dev

Even if you have python3.4 installed, ensure that you have `python3.4-dev`
installed, as it's needed to install several python libraries.

You'll also need to install the postgres dev package::

    sudo apt-get install postgresql-server-X.Y-dev

The tool that we use to deploy code is called `Fabric
<http://docs.fabfile.org/>`_, which is not yet Python3 compatible. So,
we need to install that globally in our Python2 environment::

    sudo pip install fabric==1.8.1

To setup your local environment you should create a virtualenv and install the
necessary requirements::

    mkvirtualenv --python=/usr/bin/python3.4 school_inspector
    $VIRTUAL_ENV/bin/pip install -r $PWD/requirements/dev.txt

Then create a local settings file and set your ``DJANGO_SETTINGS_MODULE`` to use it::

    cp school_inspector/settings/local.example.py school_inspector/settings/local.py
    echo "export DJANGO_SETTINGS_MODULE=school_inspector.settings.local" >> $VIRTUAL_ENV/bin/postactivate
    echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate

Exit the virtualenv and reactivate it to activate the settings just changed::

    deactivate
    workon school_inspector

If you're on Ubuntu 12.04, to get get postgis you need to set up a few more
packages before you can create the db and set up the postgis extension::

   sudo apt-add-repository ppa:ubuntugis/ppa
   sudo apt-get update
   sudo apt-get install postgis postgresql-9.1-postgis-2.0 postgresql-9.1-postgis-2.0-scripts

If your on 12.10 or later::

    sudo apt-get install postgis postgresql-X.Y-postgis-2.0 postgresql-X.Y-postgis-2.0-scripts

Now, create a Postgres user::

    sudo -u postgres createuser --superuser $USER
    sudo -u postgres psql

This will open the psql prompt; there you can set the new user's password::

    \password $USER

Exit the psql prompt and create the database for the app and run the initial
syncdb/migrate::

    createdb -E UTF-8 school_inspector
    psql school_inspector -c "CREATE EXTENSION postgis;"
    python manage.py syncdb

You should now be able to run the development server::

    python manage.py runserver
