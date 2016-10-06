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

    def serialize(self):
        """TODO: Docstring for serialize.
        Returns: TODO

        """
        result = dict()
        if self._id is not None:
            result['id'] = self._id

        if self._mt4AccountID is not None:
            result['mt4AccountID'] = self._mt4AccountID

        if self._tags is not None:
            result['tags'] = self._tags
        return result

    def deserialize(self, jsonObj):
        """TODO: Docstring for deserialize.

        It still applies the properties constrains if needed!
        When resolving an object, call it deserialize method!

        """
        if "id" in jsonObj:
            self._id = jsonObj['id']

        if "mt4AccountID" in jsonObj:
            self._mt4AccountID = jsonObj['mt4AccountID']

        if "tags" in jsonObj:
            self._tags = jsonObj['tags']

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

    def __str__(self):
        return "AccountProperties : [ id = {}; mt4AccountID = {}; tags = '{}'"\
            " ]".format(self._id, self._mt4AccountID, self._tags)
