

School_Inspector
========================

Below you will find basic setup and deployment instructions for the school_inspector
project. To begin you should have the following applications installed on your
local development system:

- Python >= 3.3 (3.4 recommended)
- `pip >= 1.5 <http://www.pip-installer.org/>`_
- `virtualenv >= 1.11 <http://www.virtualenv.org/>`_
- `virtualenvwrapper >= 3.0 <http://pypi.python.org/pypi/virtualenvwrapper>`_
- Postgres >= 9.1
- git >= 1.7

The deployment uses SSH with agent forwarding so you'll need to enable agent
forwarding if it is not already by adding ``ForwardAgent yes`` to your SSH config.


Getting Started
------------------------

If you need Python 3.4 installed, you can use this PPA::

    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt-get update
    sudo apt-get install python3.4-dev

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

Create the Postgres database and run the initial syncdb/migrate::

    createdb -E UTF-8 school_inspector
    python manage.py syncdb --migrate

You should now be able to run the development server::

    python manage.py runserver
