{% set version=pillar.get("postgresql_version", "9.3") %}

include:
  - locale.utf8

postgresql-apt-repo:
  pkgrepo.managed:
    - name: 'deb http://apt.postgresql.org/pub/repos/apt/ {{ grains['oscodename'] }}-pgdg main'
    - file: /etc/apt/sources.list.d/pgdg.list
    - key_url: https://www.postgresql.org/media/keys/ACCC4CF8.asc

db-packages:
  pkg:
    - installed
    - names:
      - postgresql-{{ version }}
      - libpq-dev
    - require:
      - pkgrepo: postgresql-apt-repo

postgresql:
  pkg:
    - installed
  service:
    - running
    - enable: True

/var/lib/postgresql/configure_utf-8.sh:
  cmd.wait:
    - name: bash /var/lib/postgresql/configure_utf-8.sh
    - user: postgres
    - cwd: /var/lib/postgresql
    - unless: psql -U postgres template1 -c 'SHOW SERVER_ENCODING' | grep "UTF8"
    - require:
      - file: /etc/default/locale
    - watch:
      - file: /var/lib/postgresql/configure_utf-8.sh

  file.managed:
    - name: /var/lib/postgresql/configure_utf-8.sh
    - source: salt://postgresql/default-locale.sh
    - user: postgres
    - group: postgres
    - mode: 755
    - template: jinja
    - context:
        version: "{{ version }}"
    - require:
      - pkg: postgresql

{% if 'postgis' in pillar['postgresql_extensions'] %}
postgis-packages:
  pkg:
    - installed
    - names:
      - postgresql-{{ version }}-postgis-2.1
    - require:
      - pkg: db-packages
{% endif %}
