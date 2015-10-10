#!yaml|gpg

environment: production

# FIXME: Change to match production domain name
domain: schools.codefordurham.com

# FIXME: Update to the correct project repo
repo:
  url: https://github.com/codefordurham/school-navigator.git
  branch: master

# Addtional public environment variables to set for the project
env:
  NEW_RELIC_APP_NAME: school navigator production

# Uncomment and update username/password to enable HTTP basic auth
# Password must be GPG encrypted.
# http_auth:
#   username: |-
#    -----BEGIN PGP MESSAGE-----
#    -----END PGP MESSAGE-----

# Private environment variables.
# Must be GPG encrypted.
secrets:
  "DB_PASSWORD": |-
    -----BEGIN PGP MESSAGE-----
    Version: GnuPG v1

    hQEMA8VrrxEeDTagAQf+Kc1MxLnTBC8KGm9jED2BR6izZGWgQZY1IkxQ6sCRGtVk
    IlLZzi11hxtdcYYRZkMKmWA9qB/VXwXlTE68rqMX1bFEcsFmqMRn2g15XKJZZZdq
    2zcXSKja8EahWJW1NZgclMjX8nW0PQRV/W2MZLF+DYP33TBF6qCLJELaxHHM6NrV
    xCDHc0p7S0uKpbibh0iCvUAFOxDEw0kS9LiDjXsR44VWsiJu7KyQJ4UMkGvd1K6y
    05kH9OKUQkGPZfScKXFzziQT6Unyz1HAi6bzwU3NfHbKRRl8cLyxQ9l88hmUkW8j
    JUVjY6J/wp0tTTul7JH8gu/BkHNNEAlJkzw5qXt9ENJbAflrZFgZLN9w/t0MpI2p
    q259YqzMPshXmYbsKU/wv8JfQpkfmsZunt5u64GICAHUJrfOGprzARKBOspBS1NS
    KYE+SToQ+sEUSQLAWan8vl118oD/MGgpb4CVCg==
    =q8OE
    -----END PGP MESSAGE-----
  "SECRET_KEY": |-
    -----BEGIN PGP MESSAGE-----
    Version: GnuPG v1

    hQEMA8VrrxEeDTagAQf8CrMCSWsvgkjGGGa6R3ag8D8DzhcnLXMZxDuW3wjlH87/
    DhOuWgvV62aUAyuTB9ic8kWMASeOHhDvMxKloBzdgxL4UXSj2VYnmYD38epzen37
    Uw3M3leXHlAdZ6uDSIh3mhyjtBbrmZ4/t1Fu4IcV7IBiP2LblBZDm0Sav+blP1P4
    A78ZtryFlEQYUq8Wp/G/8Sy6Ow7Hl/ztlkLb/wNrgZUGL90v+iqd8Ko5ORDs1e64
    A+40+6c/kHD8+kkqrPpuo/2fDyRrIInry/IaoAbdqKV9wPPxpykFwJ7UxqwhLga1
    8uMw84+NnFKH+id466RptxDdho8YaLh4zku20mV79NJ7AcnxBODhV3YcoEd92F/D
    Mj+5phXeweMuxGimcSg94WDGYWVQ3GPQgmPccF04YJIQUES73gUufQrZ2oYNjbc9
    8h40e76F23Pc2tsXlh6BwEll3GhvG9Dn3F6A0A49Ur6IDspj1gs/x1gtXgTlxdky
    e35VfrwwyimlWITE
    =5jpW
    -----END PGP MESSAGE-----
  "BROKER_PASSWORD": |-
    -----BEGIN PGP MESSAGE-----
    Version: GnuPG v1

    hQEMA8VrrxEeDTagAQgAzpY5Kyk/R/XAsedrF0OemRX4HoIPuYjFDu2U0jG/azA0
    OTgLxEM7QiDqHI4duaBpfaYrl5woznvFleraY/zA7G04Roqwxh9ENOvEKwWKF9SK
    0nlM2OkrmjKHxuX41+lObHI5SsULTuS+BSRUvVNJX2dSYD/vo9jSRlo3qaoLIUjJ
    AJiC0ktvhEuDpEU5RHa2Tia5MWtTlIgShRB2mFpPpi+27y5UoDwoIww35T8qMIyA
    PsyTjHSNtfYqoXyMGRP8XTEwvmhwr1DUe/7Rvg/hhbSIA4bzibktuNv5gYDlU25q
    rwgnjUdy23uHhCC5mk5Efn0eaMrAm4vOzCAagGmI/NJbAVfzLZnTHzd8cUyxPcbt
    /d218FatITr3ll9e7geUaQuS79Hyn6/W/qQcqbtgSvrYba5BqiQ9+DETQmEi4S2p
    E/iNQR+ITUonXjvCwhzaB/PPLpyUejOGn3XcQQ==
    =qI05
    -----END PGP MESSAGE-----
  "NEW_RELIC_LICENSE_KEY": |-
    -----BEGIN PGP MESSAGE-----
    Version: GnuPG v1

    hQEMA8VrrxEeDTagAQf/UtpBRj35bkhvPKLfjSeycyp3wp9ml+FJRnBHyFjcfKF9
    Mn+NFPBv+Lflqc1y5RqIuApsr45XfGXbnJWOeLoRIMPVAEpr68cJ7LXKJrPNtsvh
    L+5uMK3xLAWHpmJSdmZ6ymZBvh7foxGrK6XcnQo+FHO6xW0Lj7mKSehjlpNSf4Gu
    TK25Ah5KlEFKrQPrKKasqH7gf9kbOmViKmSlXE1g+rQ2nmxF2MqUe+O+s7V1wGqh
    +4m/VRmlQO5Qn9W1rfmMQlijEo6EVB50OaAwSUTFGLLcBPqw4c1+L0wX+a4ElQo2
    Jgnh+KhPFbT5SzKwfpPYLykUFu0OFJYsPLdFRETBkdJjAdeCdYdVoTjBHsiMavVv
    H2ayX1t+uj8RBluhRHnmSU1Viv1zqXT0/xnOs3THtb6Y+L0lra8JHh1GIu8X9rEa
    bjSgtwVr1ewZZ35WXsWLC78HZGsjMNhyOREbwZv00Mw8Pu93
    =typs
    -----END PGP MESSAGE-----

# Private deploy key. Must be GPG encrypted.
# github_deploy_key: |-
#    -----BEGIN PGP MESSAGE-----
#    -----END PGP MESSAGE-----

# Uncomment and update ssl_key and ssl_cert to enabled signed SSL/
# Must be GPG encrypted.
ssl_key: |-
  -----BEGIN PGP MESSAGE-----
  Version: GnuPG v1

  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
  NrJHRi2FU6c3CRczug==
  =bmS/
  -----END PGP MESSAGE-----

ssl_cert: |-
  -----BEGIN PGP MESSAGE-----
  Version: GnuPG v1

  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
  =kSgC
  -----END PGP MESSAGE-----
