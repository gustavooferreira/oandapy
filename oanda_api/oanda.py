#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Oanda API Library
"""

from .oanda_base import Core
from .exceptions import OandaError
from . import api_v20
import sys


class APIv20(Core):
    """ REST-V20"""

    def __init__(self, environment="practice", access_token=None, headers=None):
        super(APIv20, self).__init__(environment, access_token, headers)
        self._version = "v3"

        self.account = api_v20.Account(self)
        self.orders = api_v20.Orders(self)
        self.positions = api_v20.Positions(self)
        self.pricing = api_v20.Pricing(self)
        self.trades = api_v20.Trades(self)
        self.transactions = api_v20.Transactions(self)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + " environment access_token")
    else:
        environment = sys.argv[1]
        access_token = sys.argv[2]
        con = APIv20(environment=environment, access_token=access_token)

        try:
            result = con.account.get_accounts()
            print("Result: " + str(result))
        except OandaError as exc:
            print(str(exc))
