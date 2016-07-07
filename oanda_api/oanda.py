# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Oanda API Library
"""

from .oanda_base import Core
from . import api_v20


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
