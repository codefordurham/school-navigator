#!yaml|gpg

environment: production

# FIXME: Change to match production domain name
domain: 54.172.183.193

# FIXME: Update to the correct project repo
repo:
  url: https://github.com/codefordurham/school-navigator.git
  branch: upgrade-template

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

    hQEMA3hX3TDeS0RrAQf7B39vlF2xsM8h4UrKdXnblVHJ8+mL2EtGM3WJH2/ZKP75
    lJfRF7lOrBpqC1FVtz73wr/SEDX5mY0/EE6m0MKgbC8kgjyxSamqyECCXC6EfTor
    Pkj9oQaqWq/EoVq5WlfX7tkAFMZ8URhaSgtHjofffBmRMJrZT/XKAgTqg07pqcuM
    m/rdQvUW1NI5rPz/JFSTBc68CB+kAsOlcK0q43gX+75bYAw+McRtfKOhOInkZ4hB
    C+ghA+LTS2I/mbYtUtmL15FaD3hTg4XFr+EVqp1SJKmb+fQjDBcfDjxFVANrldL8
    B5/qc9C7jktRxlXUo+2kg/soOIG/2pNYzOkXyuVWptJbAc5UhTPkFMml/tqIa3/+
    a1InUbzHgVs1hTqdOmpQMz5uEYMPpWhAddNreg3sUVvU7ln2iD3TT32TZ5Fm4tXS
    6ItQuWYvWx9alrrk8Q9E+xSZTol7PeOt0kkTew==
    =xF0K
    -----END PGP MESSAGE-----
  "SECRET_KEY": |-
    -----BEGIN PGP MESSAGE-----
    Version: GnuPG v1

    hQEMA3hX3TDeS0RrAQf/fZqg0zNVv5U+WGxJsbOu03PTKQVdw98dRyh4vCsW4r2D
    81h0NI1/nnkyzfUdOVJ52yov6y7eEOlS2rwDs3AwwQEs1YwpnRBTDP0MVG8tKmrS
    HW28rnsZ44S6svUNX5DA9r1j2KmXXMXQoXdIaBONSmPWnB3Ez6K0Nkj9yCOCv4ub
    vPCPT5zNgsgPXYwrNW0BvMqFA4iuIB8hGeehuExLE8ljcmKxay19OhZ3LecC70HW
    6a6yYviWKd0veMdcrfRJQk7eJb/g5psbFYkT0AHfSraVxcNe8/dicE7cM/YIWFuE
    22qpFZxnG7PHIZHhmye+P4Gg6sgx8yCZ44fhdubGk9J7AQZ395c3YxeMleOzGLjl
    tqkpe8eEKZWv2O3dVnQVeWbAiyWmuFLls44++/iIU++TtrEcD9gpJcLj9QMb6acO
    pWQJlGK+FnIPvfJlv1zJD81nLWdptTLKO2V6KO2RatUtqk7/L8t8ehYUY9exg+fS
    w/B72Va7BoncSU4w
    =a9IT
    -----END PGP MESSAGE-----
  "BROKER_PASSWORD": |-
    -----BEGIN PGP MESSAGE-----
    Version: GnuPG v1

    hQEMA3hX3TDeS0RrAQf+Lt6iPuiFbREQq0DxP30VJQ+su9H2aY592Ygi5tXXR7xT
    J8AIwyMMc1eAulpXRCgmtyPWmR92I8CzJ5sDdmMd+6eSUGUQCQzFsH/L2lxPVmY3
    ZBTJ/ZDJL+qehoSjOCnLdakdsT3U+gEDlNmrvoE91Y4q8cLlyQ5FU1In+LAS68LC
    aF0L0bGbrIEQdHIWpScaO/dS9wPpgxKwN91xKLzJl7w5udDUqpK5BEWsLrSrgZtJ
    3QyIVvSB4wZThMA3LEq44HpNzaPxCQP0P2PKhXARsbwPtFhcpiX3CLCwtrIPGhAO
    qfANmtYvE7fcZufe6H/4TmLObHm7zE6MxEA+0jCWptJbATEsVwYHrK3o8N+SpDbn
    oPzahHRzUNouEqK5obFcwF8fxzpDPFWXqCnjL8xT7HQfS3b3r10JceY0KD7sNtcR
    QW1IK6YUSwGN84YKQjDFY14H8sciVYSQ20f1tg==
    =pv8r
    -----END PGP MESSAGE-----
  "NEW_RELIC_LICENSE_KEY": |-
    -----BEGIN PGP MESSAGE-----
    Version: GnuPG v1

    hQEMA3hX3TDeS0RrAQgAkBdtcKvD/RY6VKCKSqEKz2sG3+qBZnobXdoXoY7M0WoW
    lKNq8WzypMhcToTNgin3VTkBeRICUsLCtiuwxx+/eATwvRBVPJRAMl/J9LHkD+uI
    qQ4hVQeireFZ4uOvekNbVm1hgy5tpiQZS99dGXQWIHuvvMq4xjJTvQruixqPK99n
    42XNlwYlHJhMYZVaPBAbQgcCWW7qizuID1Uf1FTikkgxF12iYGKyrSYvtRRBMNQG
    PiJlDPto+6821u0beEN3dr2Hcn9d8EpdkkiBsWb4qJjSSX14CS0Rct4XyFc1LHJ/
    JO+OmxHzWv2pyUG+kz4ZptjpjM8cHyw9RfU+L8fxZdJjAd1lgEmt2Da4WELyc5oe
    PEfFRBJsoKmjEA+wwqSFwSA5o6WaKr6Gc3ZPvDdh3c77C9PC6AI8dteKw/kJgS8Z
    7eoGhnx9ftBNvgMh730HEqEtZlacnCDJmDuetvOxJ9OMBKLJ
    =lKH7
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
  aT8KsgL5s/ndkIWZ
  =W/Y9
  -----END PGP MESSAGE-----

ssl_cert: |-
  -----BEGIN PGP MESSAGE-----
  Version: GnuPG v1

  hQEMA3hX3TDeS0RrAQf+Kkz/ax7WZaW8svMwV7dL3x9TAEKaK0h6baM+x28BFKNi
  liC19qixGApwNlPGms4MUP+CL9yqMH6X+PQrmIgVmPaoBqFq4n+h8lrnDnsVbD8X
  yWmHmKr8TWQTrkMaOnRorpmtjkRlljecCMrs01qvcfGBKsgLzfiA0idpUlL2Ucdk
  RGVtWz21ixmBYqrbjgYxcsn+nP+SEbBgP5c1hBgkdzptz/z6MAc0bwsZvgpbHoCU
  xsEFRTf4dZ2LOD2DQMX3qStRABPD3ek15yHGZQuaOd+ZO6eh0DtwXqoWwP7oBPFP
  FqNoun/U60FG3yrrxBdGJPqvJcuhnnhlQVRi1I6rE9LsAdv+pzodZYErWQ6q3y45
  2oCNjBwb+QeBS+DdMhtASQk1y1jtipKCrjmWZNu2L5KJMco9zZm2VEyTP5qruSTP
  IGHo/r3/u8uaiym5P8MZdurIajIz+RH5mYk4qjSpgYlDYGjMDyB3JLHlfCjfEasN
  McloXhel8AUwL/nVJkhIPd6X918A4avfJd7U0TXwn+LJi3wIA8/4EqXbxRL/GHxd
  JLnRnsID/CEewoygv0J62tF7JuGhZ3lukfkPxXG7wQrA+jAeYlMnbTyfLieeVA4x
  KhefyeQRcp7BLs4A2FZe/HErzRjqYRDIjcSxm7kNgVGwS6udxN4EvY1MfXGK9yj2
  P296vDkDM+J6lb7ZixHw/TBm6i2lEjuaC/9fDBSVslVtmF2BkarY8oNXoy3pY5Rc
  ZRMbY+eHxYOIf87OTp17T6JqDt6+BnO8yLedbqrNnTXo0wy4HZkUJJA3Vl2P2cvY
  AFxu70dsvffpi3rCvWrUa0YD+vZJDQNsahP42BlZ3zOdU3PfcvTu4Ju0gyTVK18V
  9TaqvcrPxaFaal6suFd1Ym53XB2zu84TOCryvPjGHIwvRUBSFd3lpP2CWP0cCxTG
  d2/UyxhXZmS6RW+QepQZddSIXt24Gur/PTU0DXzvINaFjxW/uLgO+JJvnKtPJozI
  EQ8padQ6RAsrOi9n7o0B+MJ/fkMvCy+VmkljbVaLiTB365Zrk7RDVEUmlEfPbzhq
  rmtBr/HH5pCgMRXi5tlE9RZ6TAKuKqXfo157nv8fiYkRZM0dx4zBWuFIPFN+hrIs
  bfAjeUyOGXFlHUGSLf8jyPLXOfwZD/rGx5pdd7yfcrPskPEC/KaXj9vv2NbdHCdO
  Wk8T5z/932RqpPkTJGI7CZI5GMBVetNEOuvBZJk0kMHRYbW3TpoufjWI8mQly+zd
  41W13VWKJoYp0iimrUGJKfbbOaL24GPNjJ09/SijQSfcDzLMM95aUGNI6r0lDjIq
  zqOY/CJoG91RQ5wP8RqRbUnyyLKUetaRmrldEwKSnmCCLGQlROH1DYbbIz4bDeZt
  q+BWTnuJT3eDYr7WUihmcn/AZVkNYVEQsZHola06lTM8StNR8PigfuPb+Le/ZNmF
  tZRLShmx/Q+YHkJ82EJ1NQV9nE50CZ/Ms2/4X8XlHJStGkq5KJc4kZbktCvCIyrH
  ILxMwCmnO8Ew7hs/NKXpwP0RXCG8gZXsb3+EfsC32VqY0zV4NZ7A/Xa88E2WBBP1
  6wPXixChpM/mruwvNiVmaFf3hrZxh8JCsqA38zGWISthuJuQi1JvzucLTKytgDFW
  5qfrHbHvPpx6v3fnApGJ8FbpEl75N47idobNuVYaAA50H30BeaJ2kHquUNCmmpfq
  INhk7WXXPC7TdxJwXV4RK7Ng5Ulk3bhk6f2EIjmvW361DQMCxNMWX567MvkF/AWO
  MWzjB08wa8JUNq4xQqUR2C1nZ0p4Y5DW/P0KlEPIIN3yYdHWcjMBv0SmdfL2KpGL
  0k8fH2uetolSLKsS3aqwC1BrxajEgAl8+77BKHpdVjxS6TuCbibx30wcPrIZrILx
  1W6oRxYSfNrEQIaiMsl9RHat8wKGSIUDwH3b1D4nl+3tKryVjwzprGk+B9lbu83F
  xmFEd6w7Wn7ihWQx7LT+YD1EgtVDcH46BZuwxhWJ3/Ln0mjG1oxr307dXGVFABLb
  sepTd3bZa+um/o5tAYA0Hd/zyZ6pWkOdsE/0BXFYgI8UMtn/5ffi/l6UUkDDGe6k
  PDJjbfVwZfVWQb2eVNj88qno8M1Mjulp3UzyMhiZ/lzYF6jRfyfnjVB6R/XO+0tl
  6lBycvKzBIM+JHANkEdfrp1RDaiIyKRBc+/T5VgvJtlM6leNhGPIS6597q/7j+DP
  AUXaMXsXmQsMdgLf2TVeIsPegNwb+9051JOqo+wZ9KkeQxnfNdAqyT2vPA3Krq0/
  1lkagPMMWfpjemBfIro3hoTan+jR3xD3UItOrePEE13LOcgDq+YDIdE9uu4y0wbv
  u71gKjT3+zvVl4mT/Ip1CMErzFqgFM5LHHKpPGaaQWQegw4nUq6D3qXgu3n/k9JG
  t7aatZW2pm7im91GIottOklxpCzKb843SaeZaQBWHbY28OS/lYMFm2bCptOzIr+l
  s6wKDMLlL12qKqb8cYnbzOOuzeMBtSXhZsgs3rNZbwasf5hkXp0cUw41EA5kZqCd
  8MpXG34MeZY1NElovXwDcEKKnirSpA4nFoG6JxxrGC+guxl9D4PUT1JonsFfxivY
  hFhNMJoUXG0OZQQgSyz67of8Sxcqx2RCQwyb1HRTevABSQTotMLRsGPqtJb7w+W0
  oGlHQiis6mGTRjxUJfRwZMBmaqZ2/fTDx6Ow8Y4v6/5ras8Y2wPnFSTVGYtMaxGF
  M5ub0LMU2XmNyBiAHzN/XQqWQIU3HwDFXcmHdjW3USRXUhmhlN6hpgLOtZfFYVv2
  jDTz7ihG99pV//qVX6djBv53mpQWMIrQcX9I3R6bDBt6VRgfd72wTw3KpSvMUp7C
  CxquWuAWzWT1HaRju3wreX1uHfZDHiVL24Ap3QiypI1LmVi0O5x0Ba/THHbeUwvr
  t2rzTmu244Xf1mzP/d7h/w733NrLTCV4oNVnniRPvRtPm1gaxZNnDcOSPJyu3hki
  P0zKz0aOnCa/zDU9VUKFFgn+3j212hIFjiYyYimITcp6I2r5Qxxy+qJHxtPPUIOf
  E31MrLcxn0cqdx+z42Hc9GK9ubbsfU1OD6zkWWsRGEIP9TswLV9zksiiFgGsaJC5
  R5kGr03Ve5Kj6rJX+7qN+MADJ5cBRJUneRbQUq1MASA/pf6TQ3e/kJqG6HGZt0HW
  wOxGBC9ngqRQrEYALJD0NGqp5Z4OKt5QSafCkYuxO0git0S+iOHw++MjhluDsgyg
  xjRgyH4HWWaRear0taFO1pb3aCY9NJp+8qDNQBc12Ft5P922elYafRHems23EWoS
  17w90lcDdlrGW+aUHppcfgkkJ/IC6H5I/rqCknse9C6INdwzZ5zBk3txV4b29gCV
  ign5CPA+yHv/eRAlS09fkxSHboKmHn66q88UdyRBd6IDiS7/68jVBsz8xTwXzBZ7
  iSqbZCnnZ7iqrOP0mumaJ9hzIx5O/A5opXafwCj/4wNdSvJB4mMcHyRGrDuqNF2M
  dIuR6+CLGxWa/DLyafCsTADISp5HAJRWi+Z7wNHda6kBchPg9TteYGqiUngj2nbj
  3umcaYVkYybH98Y/LFvkDurOY3bcSqyGgADukWTRiOBBeQJdkCCav+KUSBGHOemF
  rHw8qE3ot/1NIUrNdbzRvOAjh8tBX3WhaUn7hdnC5A8zcFk5790bVyc5PERiK2pV
  uneXsYkKZhVhrrtw1EblEemHD3BkbRdzlrinnq9VWcQFrrL72Utxs7b5QJilIw/s
  Cuig7EM+d6kgteV71j062cu+UQsLeM8i35Wk+QdMxB9t2NtTdBsnH/fcOBT7Objj
  0irECsc+9/yVqeyIwfuhXvFWO3cHGz7rzwi8EhT2p3l38hSxhWEz986MKgMPljmI
  rtNvWLHCVKmBVMWil3JoEvI06K9O5CLj/Q33/nn0/yZkuBdGfYqS9W3jrUZqppbv
  aoi2OX4mYAdQ5jAFBmOhodrs+VxvAeHnkYo9/LRzH5Y2CAEMaTLKl5qSKxEBvYFo
  dIa/W9dQ2fp26zPxjMLVz8QrwzeESblP/ciaKENVfosvBaBxLqPS0sRvZcYgwMX8
  f3iBdXVVIj/fMDprxfJRnJ8WDfDHkP5hjW1a5z36YpK7KH8OFzJ7v/JzhLpltVjA
  ZBzV+LICGJY3qdD4a8yGjU23mIkH5v3bpViDkOiD2BExVQxjIh5WA7VB3kD+X/dv
  M3Hb9ZO7A6KEKhTvvFK/xuYnjIgRzFrBslJKJ/1uWgYfr09St+PMhxR01F17fB8Q
  My0kLJJuo694V22MtqeDGZj7sQvU2OpSFKZWDmL8dR/t75le6K8noP296Hu/UDrU
  D5J9Gh3weB+6Em5sAQmntLxxlziMYVPkt0aAzs2xuoan8K8POdi4NwhFqlJDiREb
  2GFrO2FlbiTwaUtQlqLgN1r5c0y+w1l2DFx4hT8Z1t6mm9XtqK44WvK+bRGUq64s
  GtW6C/uL22kYcQhP+8Gy3TGrnGAH2LH8NsJM6gm4FidJo5QcM6DXsPBt+7hIMqJ8
  C/6cVSIPffcTO5VS05lXfiKfHszh13/1GM1seBpNlC3Z5E6q1iFIhTO1/lkIdG3X
  tzbEi91LF8M6xN8PGAnpmTKmvDPLsDqIOiboTy6MQjwj6SKnYRxVvsfDy8T/Bhc/
  wwGenLDLy8iA74qva8ThW5J0arluoaPxXqJe/StSvQ8FZU3fc7ocDyj5slOO1ImG
  /7pMdhxbuCo7xX2XWWuFXf8vOHqQE13O72IerFKIJLxk5lM3AxKVpuaZk10zkF+q
  sqpAyNR9h6ZOTdZ2iqsQgohQq5q/dNg140jl9eUzM9uxwgZvE4CNsORdLshomurF
  9I9rb+aQ1w9lpKpe2zhm82U/BJKwufz2SdTb72Z4luVh5Bx6XJ2n8rBSwuEQkN8Z
  ceFyDLkMp51Uvow2La5iVCSNRNDcnh7G9BVHKFbxfz5XV1FVpIcNtwCOW+tpPMoM
  NP1ElMEdvXrrXoJrEG8/XXZ6h/tWzi3guxS4bdycfgoBsQQQZdQwFoCBbWN7UWyI
  DFdlIRNSM1EP41tNjguhWVOkwgY9uP3DZmH2T6a2cGWB3+msI0q2+GRU9lcxet+R
  N9U4dKit5+DBsxvb4AxIOVSZ0Rch2wv1pjqb0tt5eMk1JmLjbvWHYa/e+nFIu1EU
  JbFc8JXIuKYES9lzIGwHnONvR32uSRxQR0oU+yrjtNOtd6BdLT4miQrXQRr9y5Xb
  jQh5uIzo9zuUJp0rpjpykH96eliTGQUbu47MTnlQ+z1Zj7Mq8kifP1BHO6q3tQXK
  eBNG5EdRW4jkq3b82qxXPWt3XeT448OMZd6zGjaXYXbKVBzPkxZAKCCAHq+SMbzo
  DOqsWiXLdP7x6dB/o30OZkqFVlcUyEawyeHgU88Mu9+GIyWB8X/KX6yOM9Dgxr9W
  ACWZtZPYvMgaLb0mPjE7Lr0NsqZMoAY72Gm0WvMl8npyTpsM2ehliEWwWJ1m3BIo
  cJGNcMiNXhjeatCzPyb+dZaPjIN0jUaxR7a9VUXo9bPk+ufK7hi+blz4pTXj4d0R
  PW6V1M7U5k1UKps3XdSHl5E50Gp7/BoBHoJbU5LpbnxNxPQNoVUnmNX1aMfTeJRP
  V3ZqJ3Ht41RryE5exH0mikYfneJvPsCIECMLj6FjdRwYuvDiL7PlVrxFJvo23vT1
  tMThboyj1o+UbcrCEGLc8BsCA3pXiZm9iabJnSIFr9KhcJ/Ynf+lVuEmaovtpHlQ
  dVwkDw/JTXPtPQsq38BHG/XL+L/SbizhsQ8DoRomp81puK0A3QNp+bX/8fTyD7Gl
  jsB+OuFkGHAWnUqt1aVrwtgIWxIYkBinrOdljhQQ+ppWoLy2BxhdF4C/QAaW+k2p
  HEnYrYg64bNlEPBaPt9+/FZr90TNlQBL7z2LQmKLgySowB8HWhX/DyzYZwCR3Yr2
  W7uVQLeueckel6tLiwKe/mzH2bRMWO3q3jp5shqtNu7EYpbJ8cXTHfgEXsuxE0R7
  FtZdlTLJ1FWZl9pYvbGFbztYz3PQLr/bHd1AprfckBf2LlLNjbJRH8oIINdUzcGf
  u24oqpFzMNF+mBnseC8T5dLomww/uJ9w4VAlm7afz4jdnvac1d7Y2yvl5GJnoCPr
  2flFZJJCekBynAUo4gy9ydxgwc6c1TuKH8mwqI0yc+AYYxTzQf68LrPk9MVonuCO
  rIvC1V+xSeWTQC7//0e/qSlPJCfTgLNIyGNQ015eK0bg
  =ZG1o
  -----END PGP MESSAGE-----
