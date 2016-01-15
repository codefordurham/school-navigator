#!yaml|gpg

environment: production

# FIXME: Change to match production domain name
domain: durhamschoolnavigator.org

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
