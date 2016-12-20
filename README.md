Oanda REST-v20 API wrapper
==========================

[![Build Status](https://travis-ci.org/gustavooferreira/oandapy.svg?branch=master)](https://travis-ci.org/gustavooferreira/oandapy)
[![Coverage Status](https://coveralls.io/repos/github/gustavooferreira/oandapy/badge.svg?branch=master)](https://coveralls.io/github/gustavooferreira/oandapy?branch=master)
[![Code Health](https://landscape.io/github/gustavooferreira/oandapy/master/landscape.svg?style=flat)](https://landscape.io/github/gustavooferreira/oandapy/master)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/gustavooferreira/oandapy/blob/master/LICENCE.md)

__NOTE__: DO NOT USE THIS LIBRARY!
It is under heavy development and still lacks testing suites. It is also partially documented.


OVERVIEW
--------

[oandapy](https://github.com/gustavooferreira/oandapy) is a python3 wrapper for Oanda's REST API v20.

This library currently implements the features released under [version 3.0.1](http://developer.oanda.com/rest-live-v20/release-notes/) of OANDA's REST API.

Head over to [OANDA's REST API v20 docs](http://developer.oanda.com/rest-live-v20/introduction/) to go through their documentation.

__NOTE__: This library requires at least python 3.4 because it uses Enum classes.


INSTALL
-------

Right now, this library has not yet been pushed to pypi, so as of now you can't use pip to install it. (But will be soon in pypi)

For now you will have to clone this repository and put it on your __PYTHONPATH__.
```
export PYTHONPATH="${PYTHONPATH}:/path/to/oandapy"
```

oandapy depends on _python-requests_, which you can install using pip and the requirements.txt file like this:
```
pip install -r requirements.txt
```
or
```
make init
```
or
```
pip install requests
```

__NOTE__: You should use pip3 to install requests's python3 library.


USAGE
-----

Import the oandapy module and create an instance with your account token:
```
from oandapy import oanda
from oandapy.exceptions import OandaError

access_token = ""
con = oanda.APIv20(environment="practice", access_token=access_token)

try:
  result = con.account.get_accounts()

  for acc in result.accounts:
    print(acc.aid)
except oanda.OandaError as exc:
  print(str(exc))
```


NOTES
-----

* Oanda API REST-v20 is still under development, some functionality have not yet been implemented (Streaming, Pricing History, Forex Labs), but I will keep an eye on it, and as soon as it gets implemented I will update this library accordingly.
* Use this library at your own risk.
* If you want to contribute feel free to do so, I appreciate it!
* Happy hunting on the markets!!
