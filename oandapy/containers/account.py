# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""Account Containers"""

from oandapy.entities.account import AccountProperties
from oandapy.entities.account import Account


class GetAccountsContainer(object):

    """Container for function get_accounts."""

    def __init__(self):
        self._accounts = None

    def serialize(self):
        """Serialize container object to dict.

        Returns:
            str: Representation of container state.

        """

        result = dict()
        if self._accounts is not None:
            result['accounts'] = []
            for account in self._accounts:
                result['accounts'].append(account.serialize())

        return result

    def deserialize(self, jsonObj):
        """Deserialize dict to container object."""

        if "accounts" in jsonObj:
            self._accounts = []
            for account in jsonObj['accounts']:
                temp = AccountProperties()
                temp.deserialize(account)
                self._accounts.append(temp)

    @property
    def accounts(self):
        """list: The list of Accounts the client is authorized to access and
        their associated properties.

        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        self._accounts = accounts

    def __str__(self):
        return "GetAccountsContainer : [ accounts = {} ]".format(self._accounts)


class GetAccountContainer(object):

    """Container for function get_account."""

    def __init__(self):
        self._account = None
        self._lastTransactionID = None

    def serialize(self):
        """Serialize container object to dict.

        Returns:
            str: Representation of container state.

        """

        result = dict()
        if self._account is not None:
            result['account'] = self._account.serialize()

        if self._lastTransactionID is not None:
            result['lastTransactionID'] = self._lastTransactionID

        return result

    def deserialize(self, jsonObj):
        """Deserialize dict to container object."""

        if "account" in jsonObj:
            self._account = Account()
            self._account.deserialize(jsonObj['account'])

        if "lastTransactionID" in jsonObj:
            self._lastTransactionID = jsonObj['lastTransactionID']

    @property
    def account(self):
        """Account: The full details of the requested Account."""
        return self._account

    @account.setter
    def account(self, account):
        self._account = account

    @property
    def lastTransactionID(self):
        """str: The unique Transaction identifier within each Account."""
        return self._lastTransactionID

    @lastTransactionID.setter
    def lastTransactionID(self, lastTransactionID):
        self._lastTransactionID = lastTransactionID
