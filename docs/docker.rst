Create a virtual machine and run Docker clients::

  docker-machine create development --driver virtualbox --virtualbox-disk-size "10000" --virtualbox-cpu-count 2 --virtualbox-memory "4096"

Setup the environment for the docker client::

  docker-machine restart development  # only after restart
  eval $(docker-machine env development)

Build the app::

  docker build -t school-navigator:app .
