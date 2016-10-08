# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Account endpoint
"""

from ..containers.account import GetAccountsContainer


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
        response = self._api.request(endpoint)
        obj = GetAccountsContainer()
        obj.deserialize(response)
        return obj

    def get_account(self, account_id):
        """Get the full details for a single Account that a client has access
        to. Full pending Order, open Trade and open Position representations
        are provided.

        Args:
            account_id: A string providing an account ID.

        Returns:
            A dict with full account details.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        endpoint = 'accounts/{0}'.format(account_id)
        return self._api.request(endpoint)

    def get_account_summary(self, account_id):
        """Get a summary for a single Account that a client has access to.

        Args:
            account_id: A string providing an account ID.

        Returns:
            A dict with an account summary.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        endpoint = 'accounts/{0}/summary'.format(account_id)
        return self._api.request(endpoint)

    def get_instruments(self, account_id, instruments=None):
        """Get the list of tradeable instruments for the given Account.

        Args:
            account_id: A string providing an account ID.
            instruments: An optional list of instruments to query specifically.

        Returns:
            A dict with a list of tradeable instruments for the account ID that
            has been provided.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        endpoint = 'accounts/{0}/instruments'.format(account_id)
        params = {}

        if instruments is not None:
            inst = "%2C".join(instruments)
            params["instruments"] = inst
        return self._api.request(endpoint, params=params)

    def set_account_settings(self, account_id, alias=None, margin_rate=None):
        """Set the client-configurable portions of an Account.

        Args:
            account_id: A string providing an account ID.
            alias: An optional string defining the name for the account.
            margin_rate: An optional string defining the margin rate for the
            account.

        Returns:
            A dict with operation response.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        endpoint = 'accounts/{0}/configuration'.format(account_id)
        params = {}
        if alias:
            params["alias"] = alias

        if margin_rate:
            params["marginRate"] = margin_rate

        return self._api.request(endpoint, "PATCH", params=params)

    def get_account_changes(self, account_id, since_transaction_id):
        """Endpoint used to poll an Account for its current state and changes
        since a specified TransactionID.

        Args:
            account_id: A string providing an account ID.
            since_transaction_id: A string providing an account ID.

        Returns:
            A dict with the account state and changes.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        endpoint = 'accounts/{0}/changes'.format(account_id)
        params = {}
        params["sinceTransactionID"] = since_transaction_id
        return self._api.request(endpoint, params=params)
