oandaApi
=======

oandaApi is a python3 wrapper for OANDA's REST API v20.

INSTALL
=======

Right now, this library has not yet been pushed to pypi, so as of now you can't use pip to install it. (But will be soon in pypi)

For now you will have to clone this repository and put it on your __PYTHONPATH__.
```
export PYTHONPATH="${PYTHONPATH}:/path/to/oandaApi/oanda_api"
```

oandaApi depend on _python-requests_, which you can install using pip and the requirements.txt file like this:
```
pip install -r requirements.txt
```

or:
```
pip install requests
```

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
* Use it at your own risk.
* If you want to contribute feel free to do so, I appreciate it!
* Happy hunting on the markets!!
