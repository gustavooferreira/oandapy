# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Transactions endpoint
"""


class Transactions(object):
    """Class holding transactions functions

    Transactions
        Docs: http://developer.oanda.com/rest-live-v20/transactions-ep/
    """

    def __init__(self, api):
        self._api = api

    def get_transactions(self, account_id, from_date=None, to_date=None,
                         page_size=None, type_list=None):
        """Get a list of all Accounts authorized for the provided token.
        Get a list of Transactions pages that satisfy a time-based
        Transaction query.

        Args:
            This function takes no arguments.

        Returns:
            A dict with all accounts ids and tags.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
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

        return self._api.request(endpoint, params=params)

    def get_transition_details(self, account_id, transaction_id):
        """Get a list of all Accounts authorized for the provided token.
        Get the details of a single Account Transaction.

        Args:
            This function takes no arguments.

        Returns:
            A dict with all accounts ids and tags.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        endpoint = 'accounts/{0}/transactions{1}'.format(account_id,
                                                         transaction_id)

        return self._api.request(endpoint)

    def get_transaction_list(self, account_id, from_date, to_date,
                             type_list=None):
        """Get a list of all Accounts authorized for the provided token.
        Get a range of Transactions for an Account based on the Transaction
        IDs.

        Args:
            This function takes no arguments.

        Returns:
            A dict with all accounts ids and tags.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        endpoint = 'accounts/{0}/transactions/idrange'.format(account_id)

        params = {}

        params["from"] = from_date
        params["to"] = to_date

        if type_list:
            type_list = "%2C".join(type_list)
            params["type"] = type_list

        return self._api.request(endpoint, params=params)

    def get_transaction_list2(self, account_id, aid):
        """Get a list of all Accounts authorized for the provided token.
        Get a range of Transactions for an Account starting at (but not
        including) a provided Transaction ID.

        Args:
            This function takes no arguments.

        Returns:
            A dict with all accounts ids and tags.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        endpoint = 'accounts/{0}/transactions/sinceid'.format(account_id)

        params = {}
        params["id"] = id

        return self._api.request(endpoint, params=params)
