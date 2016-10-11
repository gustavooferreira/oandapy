# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Trades endpoint
"""


class Trades(object):
    """Class holding trades functions

    Trades
        Docs: http://developer.oanda.com/rest-live-v20/trades-ep/
    """

    def __init__(self, api):
        self._api = api

    def get_trades(self, account_id, ids, state=None, instrument=None,
                   count=None, before_id=None):
        """Get a list of all Accounts authorized for the provided token.
        Get a list of Trades for an Account

        Args:
            This function takes no arguments.

        Returns:
            A dict with all accounts ids and tags.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        endpoint = 'accounts/{0}/trades'.format(account_id)

        params = {}

        ids = "%2C".join(ids)
        params["ids"] = ids

        if state:
            params["state"] = state

        if instrument:
            params["instrument"] = instrument

        if count:
            params["count"] = count

        if before_id:
            params["beforeID"] = before_id

        return self._api.request(endpoint, params=params)

    def get_open_trades_list(self, account_id):
        """Get a list of all Accounts authorized for the provided token.
        Get the list of open Trades for an Account

        Args:
            This function takes no arguments.

        Returns:
            A dict with all accounts ids and tags.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        endpoint = 'accounts/{0}/openTrades'.format(account_id)
        return self._api.request(endpoint)

    def get_trade_details(self, account_id, trade_id):
        """Get a list of all Accounts authorized for the provided token.

        Args:
            This function takes no arguments.

        Returns:
            A dict with all accounts ids and tags.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        """Get the details of a specific Trade in an Account"""
        endpoint = 'accounts/{0}/trades/{1}'.format(account_id, trade_id)
        return self._api.request(endpoint)

    def close_trade(self, account_id, trade_id, units):
        """Get a list of all Accounts authorized for the provided token.
        Close (partially or fully) a specific open Trade in an Account

        Args:
            This function takes no arguments.

        Returns:
            A dict with all accounts ids and tags.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        endpoint = 'accounts/{0}/trades/{1}/close'.format(account_id, trade_id)

        params = {}
        params["units"] = units

        return self._api.request(endpoint, "PUT", params=params)

    def update_client_extensions(self, account_id, trade_id, client_extensions):
        """Get a list of all Accounts authorized for the provided token.
        Update the Client Extensions for a Trade

        Args:
            This function takes no arguments.

        Returns:
            A dict with all accounts ids and tags.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        endpoint = 'accounts/{0}/trades/{1}/clientExtensions'.format(account_id,
                                                                     trade_id)

        params = {}
        params["clientExtensions"] = client_extensions

        return self._api.request(endpoint, "PUT", params=params)

    def update_trade(self, account_id, trade_id, take_profit=None,
                     stop_loss=None, trailing_stop_loss=None):
        """Get a list of all Accounts authorized for the provided token.
        Create, replace and cancel a Trade’s dependent Orders (Take Profit,
        Stop Loss and Trailing Stop Loss) through the Trade itself

        Args:
            This function takes no arguments.

        Returns:
            A dict with all accounts ids and tags.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        endpoint = 'accounts/{0}/trades/{1}/orders'.format(account_id,
                                                           trade_id)

        params = {}

        if take_profit:
            params["takeProfit"] = take_profit

        if stop_loss:
            params["stopLoss"] = stop_loss

        if trailing_stop_loss:
            params["trailingStopLoss"] = trailing_stop_loss

        return self._api.request(endpoint, "PUT", params=params)
