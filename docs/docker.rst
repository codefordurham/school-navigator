Mac-specific
------------

Create a virtual machine and run Docker clients::

  docker-machine create development --driver virtualbox --virtualbox-disk-size "10000" --virtualbox-cpu-count 2 --virtualbox-memory "4096"

Setup the environment for the docker client::

  # make sure development VM is running in VirtualBox
  docker-machine ls
  # restart the machine if it is not running
  docker-machine restart development  # only needed if
  # load the machine environment
  eval $(docker-machine env development)


Local Development Setup
-----------------------

Build the app::

  docker-compose build
  docker-compose up
  docker-compose run app /venv/bin/python manage.py migrate
