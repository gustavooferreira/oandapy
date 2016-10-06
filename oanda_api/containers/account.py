# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Account Containers
"""

from ..entities.account import AccountProperties


class GetAccountsContainer(object):

    """TODO
    """

    def __init__(self):
        """Constructor:"""
        """The list of Accounts the client is authorized to access and their
        associated properties.
        """
        self._accounts = None

    def serialize(self):
        """TODO: Docstring for serialize.
        Returns: TODO

        """
        result = dict()
        if self._accounts is not None:
            result['accounts'] = []
            for account in self._accounts:
                result['accounts'].append(account.serialize())

        return result

    def deserialize(self, jsonObj):
        """TODO: Docstring for deserialize.

        It still applies the properties constrains if needed!
        When resolving an object, call it deserialize method!
        """
        if "accounts" in jsonObj:
            self._accounts = []
            for account in jsonObj["accounts"]:
                temp = AccountProperties()
                temp.deserialize(account)
                self._accounts.append(temp)

    @property
    def accounts(self):
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        self._accounts = accounts

    def __str__(self):
        return "GetAccountsContainer : [ accounts = {} ]".format(self._accounts)
