{% import 'project/_vars.sls' as vars with context %}
{% set version=pillar.get("postgresql_version", "9.3") %}

{% if 'postgis' in pillar['postgresql_extensions'] %}
postgis-packages:
  pkg:
    - installed
    - names:
      - postgresql-{{ version }}-postgis-2.1
    - require:
      - pkg: postgresql
    - require_in:
      - file: manage
      - postgres_database: database-{{ pillar['project_name'] }}
{% endif %}

{% for extension in pillar.get('postgresql_extensions', []) %}
create-{{ extension }}-extension:
  cmd.run:
    - name: psql -U postgres {{ pillar['project_name'] }}_{{ pillar['environment'] }} -c "CREATE EXTENSION postgis;"
    - unless: psql -U postgres {{ pillar['project_name'] }}_{{ pillar['environment'] }} -c "\dx+" | grep postgis
    - user: postgres
    - require:
      - pkg: postgis-packages
      - postgres_database: database-{{ pillar['project_name'] }}
    - require_in:
      - virtualenv: venv
{% endfor %}
