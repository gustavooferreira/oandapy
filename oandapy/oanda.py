# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""Oanda API Library"""

from oandapy.api.oanda_base import Core
from oandapy.api.account import Account
from oandapy.api.orders import Orders
from oandapy.api.positions import Positions
from oandapy.api.pricing import Pricing
from oandapy.api.trades import Trades
from oandapy.api.transactions import Transactions


class APIv20(Core):
    """Oanda REST API v20 Class

    This class instanciates all endpoint classes

    """

    def __init__(self, environment="practice", access_token=None):
        """APIv20 object to communicate with Oanda REST API.

        Args:
            environment (str, optional): Provides the environment for
                OANDA's API. Defaults to 'practice'.
            access_token (str): Specifies the access token.

        """
        super(APIv20, self).__init__(environment, access_token)
        self._version = "v3"

        self.account = Account(self)
        self.orders = Orders(self)
        self.positions = Positions(self)
        self.pricing = Pricing(self)
        self.trades = Trades(self)
        self.transactions = Transactions(self)
