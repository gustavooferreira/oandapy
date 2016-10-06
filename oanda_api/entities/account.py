#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Account Entities
"""


class AccountProperties(object):

    """Docstring for AccountProperties. """

    def __init__(self):
        """Constructor:"""
        self._id = None
        self._mt4AccountID = None
        self._tags = None

    @property
    def id(self):
        """str: The string representation of an Account Identifier.
                Format: "-"-delimited string with format
                "{siteID}-{divisionID}-{userID}-{accountNumber}"
        """
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def mt4AccountID(self):
        """int: The Account’s associated MT4 Account ID. This field will not be
                present if the Account is not an MT4 account.
        """
        return self._mt4AccountID

    @mt4AccountID.setter
    def mt4AccountID(self, mt4AccountID):
        self._mt4AccountID = mt4AccountID

    @property
    def tags(self):
        """list of str: The Account’s tags
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        self._tags = tags
