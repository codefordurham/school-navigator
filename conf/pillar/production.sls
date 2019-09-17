#!yaml|gpg

environment: production

# FIXME: Change to match production domain name
domain: durhamschoolnavigator.org
letsencrypt: true

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
  "EMAIL_HOST_PASSWORD": |-
    -----BEGIN PGP MESSAGE-----
    Version: GnuPG v1

    hQEMA8VrrxEeDTagAQf9GWBBIUEQb1r93KPllR/mMREBTQYkwdqDpU8Z53XpyidN
    gscU1oqExdic63ig0ChHnLZ+oGwat4TjrqzXF+uru7sEUCqHr2KNUOfxn/nIS83H
    fSFlXG0R1N0gzQgkcpVI171Jl2qLBMG9MLfOROtGAI8jUa1xvzspjHyrkY9YW6pl
    Dn8TnC2wvzVoYM5CbEhUwQ8G8jWW7sKssw1Zr94jeVRWGUgV373D+FdPhbXQJyE/
    jTzbszrwE/5G0JIO/UQlteWeL2w6J9BZUAx07wLRHPEeLi88G8xfbAVGY4FQt6VV
    +jAQkE7ZYVF5Sowz/dR11W6Tn9peVpv/YI2epVtLPNJnAUBVIjsX+sI17O2vHtzu
    ivxmp3+jIaDfxx0cM5haynKEFQaipHdqSIHc8hNoMXLeoy98pH1zS8WC3f0YWoKg
    FOx60IB/mi9NpsG5tW+L1lKg3Wat4m1LRo6IP51CEIJv+Iv2iSD10g==
    =ToBn
    -----END PGP MESSAGE-----

# Private deploy key. Must be GPG encrypted.
# github_deploy_key: |-
#    -----BEGIN PGP MESSAGE-----
#    -----END PGP MESSAGE-----

# Uncomment and update ssl_key and ssl_cert to enabled signed SSL/
# Must be GPG encrypted.

# ssl_key: |-
#   -----BEGIN PGP MESSAGE-----
#   Version: GnuPG v1.4.11 (GNU/Linux)
#
#   hQEMA8VrrxEeDTagAQf+NhoudnPhQIzNrV9WPIgzc8Zf4rnjcj4At/qc75uVn2T0
#   CQeF8Sj1qaaKKhM4Sub+/KpUWCKG/HvwXWlqWFsXjTYRtMnIH/pzYOXalcUdTdZA
#   5ipue9oO5vXphSO2Rp5/rJ0AFUe0h1WTaxKunt23HiT1X59dtr8BtWvfS75pMjCf
#   JQdRQqsWK46AiAcLD/r1EefGD2mZSY2AV1mrKiF4HUxMLqUG2XMgReGUAYA+EmJq
#   PpFY8o48b/rw0EDcLVUkfR+DsAvqPHwDYJwixtLZlbAE8x8QjRUTFuu35NHkHkWy
#   hIgeMeKSLwgqCh+3/BZuTQkNFmRM7PisDttcBFzefdLqAQn4XMjaLIE1DMJIccdE
#   lHIWTT4adIWM8I3N38Nruo2MAjZbxAHyEOshmP0S1A0xxRWJY05VBs66JoZJ7iBk
#   7rSyhwp9PBpyQktOLrQ1NcMT7tefXEEcc7iKPDQAtSpiKoZSVaF1iJbX/wJoHNPp
#   SQtXmQ+A4lEXU16SAZgVqg462PbbXQCzgBfBFTK40t2JExTVbTlAJj4eIpLfe7Ne
#   I1dEr9WBZ1SVe4iUa15xQgc6fqE4GKIN/kWUjjLwpNb8NSEcg2xECV8s2CJaTRcB
#   zuCPJLSeUAcnmAi3XKwvpZmucr5/qzoC235xTya1z8wTWh4cjF2JTkQYsLjIByr+
#   AYiDncdr2MUKCNEMXYNrs7f0l/tvD5NgxwS7YaXV3oRi7VSAvMSu8eBOc0Z5MHAK
#   0kRy7gWrBwfqzpB/qDqWQADFnffYaqId9xnfjekVYPgxWsggMKicAFKSL3FbVx51
#   meJer+rmtxCoTgmve9ZoghwWDWOGrrOeOkC7UA3pEfHHtF1ve/pajLNe4LrEJJcs
#   mCj5TJ2Yz7uU4wdPZVmFS1xVS5SiSKJ84CbgXDP0eSefo4R8t9rBshoBGmgVoLZU
#   BwYGxPMBrQ+VVtBlHswM8qFgrVWtjJByYVJ3YSIVXYzkJPW9jyB1oObW69enAFp0
#   cPzNpeZ+U1c0NakfdF+0iE3RL2I1G3ZFiOtMp2O0WDnDqHhdIYEOGWbY38li8Fa+
#   9gJS07rSruFN5F4Gdq0rwvclu9PGp5Ztb+45PtVempPmSiezrcrAr+wTr0NNkALX
#   EHzuIt1L6ka/afxfGqWYkRIKDAkeJ60eK9/FtnzboNbrnIJGP3K9UBG6RMy+zyKp
#   x7QeLkNGfRJprFKLQuEBMxgNCWj1wgjab60WFVfeYPcGV+hzkJ7aGFlHdYHxIlYL
#   ieIipO4beNGdedWWdy7ejz6TsP38qfIKhPudaZWZYYA2MTvmlj0c785AbW1HLRnz
#   o6OukmodLpCfQQR7dcg1MevlTiDsirZjvmjh8BaNqGC6NgEclRjqS8ML3rle4tCK
#   D2Pz29KGhhVRLn3a5OR5vJKDj6Qdk/5rawidp7Sj9OsKzuGks3Tix8km8MgNqI67
#   Bq/nYTgitZIEtMuly180G1eyaYUppOtwzID0ALVNuA7Nlcy5bCEk1BPgecNN4vfW
#   u4Gzr6oTGQmEXbjxSBVf+fMU3iM7UZlctgyaNmEXvz/+kfZ6rz4bBnctRxcheiCX
#   gGfMWIxFeau/9oRSe6pvCL9CQfrng5w7pbHThzN79qmXfCQ/0Yt34LRVBmknmuUf
#   zrD3hopVzWRD5GuNiAUzLQDNOBuG4YE+veLxIkrrmmA2Gvnwee1+sV+EnbkSvOso
#   XMCegecMe+3E7V/1C5ZTvGwhYCpfFbslGlzzTbtnp4A4HCsZF6IHH18yjdKSsbqd
#   yf9wk1LTvXIGqXEtWCio+DZ5diVhrSYcUwBhhUj2l3x19HrUseLB3IYLv0y4tipO
#   E53H14sqFk62fpuTRADQFEWGFxVg5p9ab0N+s7J6uY2jEPLFPs6lG418WHR9jUeJ
#   AzV01fogCkTYrJCVuskq4hAB5EeZZ6M3/lITptuBN8770yt9BncwL0J+88Y04RVk
#   1VU6py/1jD1qHQOEtjxFQklifoqMm0HMJ6CM4iBsQHpZIvPHoH/0Q8ekXIldIs09
#   g063OwYat8OTRxBBMaehrSIp4LdSAjJ4gAsNxmxvyWHgRsOU34abw1O5//zXdxUh
#   z9+3DBIGIOGC6WEb3a45JPRTn9opWSOR2EKyMIvI881cYoVeA9o2F4KmpdpPPfvU
#   U5rf9uxFO12J2yljR1jz5/E=
#   =wLsF
#   -----END PGP MESSAGE-----
#
# ssl_cert: |-
#   -----BEGIN PGP MESSAGE-----
#   Version: GnuPG v1.4.11 (GNU/Linux)
#
#   hQEMA8VrrxEeDTagAQf/a7GS2Ji0KdIA5IjEZZZs1aqYiRmHizof3pa5RBK0tqIi
#   vlbbYd2uR5uQHolYo8D2ZNmH9dxyNJTY18V2lE/5x0rtyCyJueX2FVu0JuVEJaEz
#   O4/eIbD5Qjloa7SkpICBHGAsQXw/CE/NwjcKvZpP8cN64xWEEYTxQw/L9qu7RkZ4
#   Pqv9k4sLhTGvJl4z3HwWqZrNHADp/0LsUd8JQcSZNOBZxtsI318lncr71zwV/98h
#   60qIBpGcusfkhT5kKPiGBh9MG1IZT472nkUt8XWxJi6h+h2xLm0tyDSZlndwRpc/
#   T1dqo7aiC+Jj+hh2qPAK4+nOq58JW6IsNK5kyO/RR9LrAWQ/mvohB4HlomQhP9Cu
#   2l4OsEj/5fv/qw31/HEv3CzEaQj1qeiGC8YxjdHwFtcqaddHQcrI69zQw/+mJkut
#   TudqV3JzDzo/lYOm9m0EfPND6jeaJoQoaVshNTU7uh3Si0XdySYua9CK0bfEehVf
#   r0zrIJLScTR+GxWukt4VBuNKCQox2Tkfeowe9rVuiE1Y80lUHv8Qae0q29M+4opP
#   aNhb1KvCHobAPpiRnz0g5/tkO+e/2iNR5BEBtMvottLJDbpTGgP2BD3yJwoprDO3
#   5pjXUS8//SkNasov9PMddJteQYzJfu17JWgJlBs4Sjzf0JgbNwFFP7uNWv3s8aFf
#   WYP7X7nnsFdSlGJ9bj6DD+veAToXx+JQnRO5oxml0x7VdLlhfQP5oeGE4nVqTGF1
#   U0QQK5lqwGn8Jmpm1tKgxqK3pMycP8dK/HwagRBAEuAyP1+XOzDpLG/ME3sje+t1
#   0ezjq9RRMJpLTbQZZDIpMlLF0e9PxofewaEco0RG9RoAQzqsge/+zsFL/7RI8mqd
#   rod4t+OCYN2g2d2lswHF4MdfJA3dYn3KsO3Pe+oes/MjdpEYmZhV5Ck6F9EVZuCs
#   ClXcvipWzeuO9uWB80Hl9RcSk2hBh7csUJPvACoWgcsL6eacdgSKoA3i+0cYhq/m
#   4Wwo2oqXAR3KWp+uWqESTLBqsLMg6CkQrwD0Ud7saQT1cA25xt3jJzhPl0qLemcE
#   Wt98V3lfJYCq3ptgX2H2OLVRwQYZHvpHhOTxEeeQ9IOqkX86qKb9YUZFeUfcGDXN
#   hu60FQSa2sNc0Gln5eA38+F5isMLCuy/hyrV84b0uQxTK1/MawB/k/06bUP0NeCB
#   fBSMiAOYVkoDbc2L8V4MGqLDEdtubeCFZxd42lYcenY0AqE4U2ovxIsH7IeexKYO
#   1SNXyqWwjKOZk5fqoacPWbYIhI6yznH3bYR/nftK/zGabUfoix+A3zIEkXoMMQkj
#   cHQc67T0mX7bjT9TQhIuMKCbUPqOO/c4U2zGm6uotAFpTa+6IC4Y8pDx7fdUk0fU
#   3+6rV7BdBlXY9AMBu74dYO3xikWkeKF9hrrcRjm3nNdQmPsYErIDgMzAHfetGI3z
#   V+Jwew/HQ1h5rt83pI1JTMnHW3WGHqhNwISt6JXhgjtel7W7YBJzXStc15hGYnIv
#   jQo9lk1Si0Cskjnp8vUVNWPCCZRNfO9bJ+q6+fbaSGNmQwv7MAQsN6sYFQDhNy9b
#   K3RXD9MapjPR1mkzjoX5DoLm60riktH3bZfVucjmhA0az0DsSz4UCphH1IPhtap2
#   peZzgN5NddoxzOljt3FyEGLphyU85eP1OMpyyw0okb9QU4K/V1iPxpnRiBQiEXjp
#   bsgZtIlhLvbt8bf8yuxVs3xnlMMK5Si9LEbYduYmOBy08KLS8pxfeuZ1ZgxpEF/x
#   3Z5tKWaPGROSr1GpzFH3OIEwOg0YLCAW6kWVBNKx6+F2f6eRRv8CWCKpDFnHhahZ
#   Q7sDfmJTSvKya5IEd9IZJQ3hGeMMRFV8Odza8lYoGzu0AANQJj47ADuX9XleZFEf
#   SA0qzVzIUupL1nL1jJdpGhJZzVBcAWX8ygsrEDNQRq23XaO4nMtwodP314H+zSlR
#   9Mz+vO1zhjhk7mY6bzem3uC67QnS+gQiVB5ljho/n5vHzkfQbwjblDkXdLIjTYF8
#   NgB2gr+Y2H6tzPYBoh904/XXwQvyyDNfFN1wQrRa39h3Y//T/KYyKAp0URMDG0aH
#   xtDk0uSOjW633sKdHGWwXIDGGIKFGoVMpwBllFc2s3kxqhgUjMBLRFNncP2Bb4ru
#   JKxRjTzi3Q2o8JHzvY+Q6/fM3wYKPtB28P3PCujion7gO4SwK0PzUUOoOUCcYhrl
#   oo3/ygT7W6c+XfzoJPNpuHr93ibybBI50Og23Pe0RciubK1tBHStdtRfxnGhoK26
#   mgsoGldCkNX0cEv892NLc8mNfyHgY76uk2v0HS7esEteLPccMcM3PS31kxEQkQtS
#   aHvP+oke5zEgmCWhOMUOUUauIM4tcCMiSP+Nv196adU0b2gs4/pRgU5K6Ke1H1k4
#   TvWJuP0GzN/svBXFZRgUCmfYP5k4wCVt7kFcPP1Q7pL+YaByejYDdBWtAiqJ246O
#   SGzWjjGEA+OI+ShRv7c1GRO4ZPqb/khp1cO+5u4RCAgxscxD+znQFaCuoD66yIxu
#   JfZW9BYujeX1AzC3ZLXvX4IHIIjrxt3gUXeY8cTgUSt5ZdeEF9EXAsLLptkflVs7
#   ghkTzAofQl2n+PSduSK7mXKbBkom2Q/sZ5FdoFwKJSIArs8RkXBsGv0yEZg9Q1qt
#   hlvbvAI390XFRH88G1C3WXJRGPtk2wg8wVGBHkf4DhHEim2It4hVYMk5YeNpjOz4
#   oJ1vHWcIzjj7EL5VZXTNDK8uYzr9v8gXBRBAYbkWLjgmsVQvM5jBlVKWZmqxD5eK
#   AErxp+7w5WeBsdn2YENHzeL4x5JX8m1jyQ0V5EEql3tQp1PhAalXqciIVLFGFz2O
#   KTrIkd9tfRvaw/MqEOoCPPbl7W3B4OT2xfOwAOwsGX1eWBEcTgRo2sk6k/hNIh9o
#   TFDceFeEy7PIMkponiF4LmZ8glR2Yn5uqkMi0tPJrnENSF19ds02FkZAq+AD6ik+
#   u6X0Eur5VMZoWQ6q3RTcfdkZeTpjZO2R4Ma7NSwCaKArwLZmzeIBegSv67RnJvEY
#   RcvCEYuEhl/fD/1MscIq91vpaJfn8l2+hmxG/b/4JMjhOjgdlXvm9Jo4aQJ+Eq8E
#   uHdk0RDBgx7ef9yFogIbUmh1cLNR/TRqi7PXX68lrLQ27uA0Er3IzWaMO/g5C234
#   cgRJKBTpKpS5jCG+lzTxg0mVM4guF7yiBYOhtc7DI6zbj8FWjHxnXd9ChtxQSHHy
#   KiwjG3SZMZvcmkDMOW5MGjFaEyXwpgCZaXK8Xz8htMleLEKeUlV5rhkv8uVeRZxD
#   O+jXcqnB3vbcId8sDRhIMCv9W9lIlrUo2bYjQVcPc2w4MhRWzhisX4KtNQMc5NuT
#   XxQlcOJLCSFoIQsJdQk2HZIZT7IVLn2fAJN2Nz5jYqs1wyQetFbalaBlZmfGtXQu
#   gxCb4bJdRIUXtDzopCmlysnGcwgxLlW3Ms0Nye/YKpqEjqmJDHf6GcbSSTTxfmEw
#   /ay015kiHlIwW6iIAEyumSjUq2rHXaA99wFnRJ+LL88EdAN29QQvqhCb4zn9cUE9
#   zNcErYy9OaZodjbCkQBbsI7WwRBGROACxMMMzTgPnnvV38+fqckp93ANnmgEDDnJ
#   HDORmC3NcAtVUFJzgQirbp0eByu9GfITRiYTJLjk1o6/4IQ/Ly8IfJDMYGEzLtY1
#   yIY7lOsy/IadXKLe6eZTU+OhFeRk7TaH44DtaU+iqMrqV4hTIfsWDLaSbTO4R6nz
#   zHApTBFD47XOjLfXbyg6T+5Kxp3ryNJg1PWSlVbvXRyK5hfZp95lVqHSCW4=
#   =DdYV
#   -----END PGP MESSAGE-----
