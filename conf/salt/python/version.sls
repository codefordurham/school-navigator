include:
  - python

python-pkgs:
  pkg:
    - installed
    - names:
      - python{{ pillar['python_version'] }}
      - python{{ pillar['python_version'] }}-dev
    - require:
      - pkgrepo: deadsnakes
