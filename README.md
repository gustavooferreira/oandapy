OVERVIEW
========

[oandaApi](https://github.com/gustavooferreira/oandaApi) is a python3 wrapper for OANDA's REST API v20.

This library currently implements the features released under [version 3.0.1](http://developer.oanda.com/rest-live-v20/release-notes/) of OANDA's REST API.

Head over to [OANDA's REST API v20 docs](http://developer.oanda.com/rest-live-v20/introduction/) to go through their documentation.

INSTALL
=======

Right now, this library has not yet been pushed to pypi, so as of now you can't use pip to install it. (But will be soon in pypi)

For now you will have to clone this repository and put it on your __PYTHONPATH__.
```
export PYTHONPATH="${PYTHONPATH}:/path/to/oandaApi"
```

oandaApi depends on _python-requests_, which you can install using pip and the requirements.txt file like this:
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

__NOTE__: that you should use pip3 to install requests's python3 library.

TEST
====

You can do a quick test by typing

```
make run env="practice" token="you access token here"
```

You will get all of your account's IDs associated with this token.

__NOTE:__ don't use your live account's token for this test, because it will get saved in your command line history!


USAGE
=====

Import the oanda_api module and create an instance with your account token:
```
from oanda_api import oanda

access_token = ""
con = oanda.APIv20(environment="practice", access_token=access_token)

try:
    result = con.account.get_accounts()
    print("Result: " + str(result))
except oanda.OandaError as exc:
    print(str(exc))
```

NOTES
=====

This project is still in its __testing and documentation phase__, and because of that no release has yet been made.

Quick notes
-----------

* This project started with [oanda/oandapy](https://github.com/oanda/oandapy) as a base project, but then was implemented in a different way, to easily support future oanda api versions.
* Oanda API REST-v20 is still under development, some functionality have not yet been implemented (Streaming, Pricing History, Forex Labs), but I will keep an eye on it, and as soon as it gets implemented I will update this library accordingly.
* Use this library at your own risk.
* If you want to contribute feel free to do so, I appreciate it!
* Happy hunting on the markets!!

LICENSE
=======

This library is under the terms of MIT License. Have a look at [LICENSE](https://github.com/gustavooferreira/oandaApi/blob/master/LICENCE.md) for more information.
