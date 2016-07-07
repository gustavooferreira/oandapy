# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

"""
Functions for Oanda REST API v20
"""


class Account(object):
    """Class holding account functions

    Account
        Docs: http://developer.oanda.com/rest-live-v20/account-ep/
    """

    def __init__(self, api):
        self._api = api

    def get_accounts(self):
        """Get a list of all Accounts authorized for the provided token.

        Args:
            This function takes no arguments.

        Returns:
            A dict with all accounts ids and tags.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        endpoint = 'accounts'
        return self._api._request(endpoint)

    def get_account(self, account_id):
        """ Get account information"""
        endpoint = 'accounts/{0}'.format(account_id)
        return self._api._request(endpoint)

    def get_account_summary(self, account_id):
        """ Get account summary"""
        endpoint = 'accounts/{0}/summary'.format(account_id)
        return self._api._request(endpoint)

    def get_instruments(self, account_id, instruments):
        """ Get instruments"""
        endpoint = 'accounts/{0}/instruments'.format(account_id)
        inst = "%2C".join(instruments)
        params = {}
        params["instruments"] = inst
        return self._api._request(endpoint, params=params)

    def set_account_settings(self, account_id, alias=None, margin_rate=None):
        """ Set account settings"""
        endpoint = 'accounts/{0}/configuration'.format(account_id)
        params = {}
        if alias:
            params["alias"] = alias

        if margin_rate:
            params["marginRate"] = margin_rate

        return self._api._request(endpoint, "PATCH", params=params)

    def get_account_changes(self, account_id, since_transaction_id):
        """ Get account current state"""
        endpoint = 'accounts/{0}/changes'.format(account_id)
        params = {}
        params["sinceTransactionID"] = since_transaction_id
        return self._api._request(endpoint, params=params)


class Orders(object):
    """Orders functions

    Orders
        Docs: http://developer.oanda.com/rest-live-v20/orders-ep/
    """

    def __init__(self, api):
        self._api = api

    def create_order(self, account_id, order):
        """Create an order for an Account"""
        endpoint = 'accounts/{0}/orders'.format(account_id)
        params = {}
        if order:
            params["order"] = order

        return self._api._request(endpoint, "POST", params=params)

    def get_orders_list(self, account_id, ids, state=None, instrument=None,
                        count=None, before_id=None):
        """Get a list of Orders for an Account"""
        endpoint = 'accounts/{0}/orders'.format(account_id)

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

        return self._api._request(endpoint, params=params)

    def get_pending_orders(self, account_id):
        """List all pending Orders in an Account"""
        endpoint = 'accounts/{0}/pendingOrders'.format(account_id)
        return self._api._request(endpoint)

    def get_order_details(self, account_id, order_id):
        """Get details for a single Order in an Account"""
        endpoint = 'accounts/{0}/orders/{1}'.format(account_id, order_id)
        return self._api._request(endpoint)

    def replace_order(self, account_id, order_id, order):
        """Replace an Order in an Account by simultaneously cancelling it and
        creating a replacement Order
        """
        endpoint = 'accounts/{0}/orders/{1}'.format(account_id, order_id)

        params = {}
        params["order"] = order

        return self._api._request(endpoint, "PUT", params=params)

    def cancel_pending_order(self, account_id, order_id):
        """Cancel a pending Order in an Account"""
        endpoint = 'accounts/{0}/orders/{1}/cancel'.format(account_id, order_id)
        return self._api._request(endpoint, "PUT")

    def update_client_extensions(self, account_id, order_id, client_extensions,
                                 trade_client_extensions):
        """Update the Client Extensions for an Order in an Account"""
        endpoint = 'accounts/{0}/orders/{1}/clientExtensions'.format(account_id,
                                                                     order_id)

        params = {}
        params["clientExtensions"] = client_extensions
        params["tradeClientExtensions"] = trade_client_extensions

        return self._api._request(endpoint, "PUT", params=params)


class Trades(object):
    """Trades functions

    Trades
        Docs: http://developer.oanda.com/rest-live-v20/trades-ep/
    """

    def __init__(self, api):
        self._api = api

    def get_trades(self, account_id, ids, state=None, instrument=None,
                   count=None, before_id=None):
        """Get a list of Trades for an Account"""
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

        return self._api._request(endpoint, params=params)

    def get_open_trades_list(self, account_id):
        """Get the list of open Trades for an Account"""
        endpoint = 'accounts/{0}/openTrades'.format(account_id)
        return self._api._request(endpoint)

    def get_trade_details(self, account_id, trade_id):
        """Get the details of a specific Trade in an Account"""
        endpoint = 'accounts/{0}/trades/{1}'.format(account_id, trade_id)
        return self._api._request(endpoint)

    def close_trade(self, account_id, trade_id, units):
        """Close (partially or fully) a specific open Trade in an Account"""
        endpoint = 'accounts/{0}/trades/{1}/close'.format(account_id, trade_id)

        params = {}
        params["units"] = units

        return self._api._request(endpoint, "PUT", params=params)

    def update_client_extensions(self, account_id, trade_id, client_extensions):
        """Update the Client Extensions for a Trade"""
        endpoint = 'accounts/{0}/trades/{1}/clientExtensions'.format(account_id,
                                                                     trade_id)

        params = {}
        params["clientExtensions"] = client_extensions

        return self._api._request(endpoint, "PUT", params=params)

    def update_trade(self, account_id, trade_id, take_profit=None,
                     stop_loss=None, trailing_stop_loss=None):
        """Create, replace and cancel a Trade’s dependent Orders (Take Profit,
        Stop Loss and Trailing Stop Loss) through the Trade itself"""
        endpoint = 'accounts/{0}/trades/{1}/orders'.format(account_id,
                                                           trade_id)

        params = {}

        if take_profit:
            params["takeProfit"] = take_profit

        if stop_loss:
            params["stopLoss"] = stop_loss

        if trailing_stop_loss:
            params["trailingStopLoss"] = trailing_stop_loss

        return self._api._request(endpoint, "PUT", params=params)


class Positions(object):
    """Positions functions

    Positions
        Docs: http://developer.oanda.com/rest-live-v20/positions-ep/
    """

    def __init__(self, api):
        self._api = api

    def get_positions(self, account_id):
        """List all Positions for an Account. The Positions returned are for
        every instrument that has had a position during the lifetime of an a
        Account."""
        endpoint = 'accounts/{0}/positions'.format(account_id)

        return self._api._request(endpoint)

    def get_open_positions(self, account_id):
        """List all open Positions for an Account. An open Position is a
        Position in an Account that currently has a Trade opened for it."""
        endpoint = 'accounts/{0}/openPositions'.format(account_id)

        return self._api._request(endpoint)

    def get_position_details(self, account_id, instrument):
        """Get the details of a single Instrument’s Position in an Account.
        The Position may by open or not."""
        endpoint = 'accounts/{0}/positions/{1}'.format(account_id, instrument)

        return self._api._request(endpoint)

    def close_position(self, account_id, instrument, long_units,
                       long_client_extensions, short_units,
                       short_client_extensions):
        """Closeout the open Position for a specific instrument in an
        Account."""
        endpoint = 'accounts/{0}/positions/{1}/close'.format(account_id,
                                                             instrument)

        params = {}

        if long_units:
            params["longUnits"] = long_units

        if short_client_extensions:
            params["longClientExtensions"] = long_client_extensions

        if short_units:
            params["shortUnits"] = short_units

        if long_client_extensions:
            params["longClientExtensions"] = long_client_extensions

        return self._api._request(endpoint, "PUT", params=params)


class Transactions(object):
    """Transactions functions

    Transactions
        Docs: http://developer.oanda.com/rest-live-v20/transactions-ep/
    """

    def __init__(self, api):
        self._api = api

    def get_transactions(self, account_id, from_date=None, to_date=None,
                         page_size=None, type_list=None):
        """Get a list of Transactions pages that satisfy a time-based
        Transaction query."""
        endpoint = 'accounts/{0}/transactions'.format(account_id)

        params = {}

        if from_date:
            params["from"] = from_date

        if to_date:
            params["to"] = to_date

        if page_size:
            params["pageSize"] = page_size

        if type_list:
            type_list = "%2C".join(type_list)
            params["type"] = type_list

        return self._api._request(endpoint, params=params)

    def get_transition_details(self, account_id, transaction_id):
        """Get the details of a single Account Transaction."""
        endpoint = 'accounts/{0}/transactions{1}'.format(account_id,
                                                         transaction_id)

        return self._api._request(endpoint)

    def get_transaction_list(self, account_id, from_date, to_date,
                             type_list=None):
        """Get a range of Transactions for an Account based on the Transaction
        IDs."""
        endpoint = 'accounts/{0}/transactions/idrange'.format(account_id)

        params = {}

        params["from"] = from_date
        params["to"] = to_date

        if type_list:
            type_list = "%2C".join(type_list)
            params["type"] = type_list

        return self._api._request(endpoint, params=params)

    def get_transaction_list2(self, account_id, id):
        """Get a range of Transactions for an Account starting at (but not
        including) a provided Transaction ID."""
        endpoint = 'accounts/{0}/transactions/sinceid'.format(account_id)

        params = {}
        params["id"] = id

        return self._api._request(endpoint, params=params)


class Pricing(object):
    """Pricing functions

    Pricing
        Docs: http://developer.oanda.com/rest-live-v20/pricing-ep/
    """

    def __init__(self, api):
        self._api = api

    def get_pricing(self, account_id, instruments, since=None):
        """ Get pricing information for a specified list of Instruments within
        an Account."""
        endpoint = 'accounts/{0}/pricing'.format(account_id)
        inst = "%2C".join(instruments)
        params = {}
        params["instruments"] = inst

        if since is not None:
            params["since"] = since

        return self._api._request(endpoint, params=params)
