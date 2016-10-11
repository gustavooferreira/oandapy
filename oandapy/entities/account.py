# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Account Entities
"""


class Account(object):

    """The full details of a client’s Account. This includes full open Trade,
    open Position and pending Order representation."""

    def __init__(self):
        self._id = None
        self._alias = None
        self._currency = None
        self._balance = None
        self._createdByUserID = None
        self._createdTime = None
        self._pl = None
        self._resettabledPL = None
        self._resettabledPLTime = None
        self._marginRate = None
        self._marginCallEnterTime = None
        self._marginCallExtensionCount = None
        self._lastMarginCallExtensionTime = None
        self._openTradeCount = None
        self._openPositionCount = None
        self._pendingOrderCount = None
        self._hedgingEnabled = None
        self._unrealizedPL = None
        self._nav = None
        self._marginUsed = None
        self._marginAvailable = None
        self._positionValue = None
        self._marginCloseoutUnrealizedPL = None
        self._marginCloseoutNAV = None
        self._marginCloseoutMarginUsed = None
        self._marginCloseoutPercent = None
        self._withdrawalLimit = None
        self._marginCallMarginUsed = None
        self._marginCallPercent = None
        self._lastTransactionID = None
        self._trades = None
        self._positions = None
        self._orders = None

    def serialize(self):
        """Serialize entity object to dict.

        Returns:
            str: Representation of entity state.

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
        """Deserialize dict to entity object."""

        if "id" in jsonObj:
            self._id = jsonObj['id']

        if "mt4AccountID" in jsonObj:
            self._mt4AccountID = jsonObj['mt4AccountID']

        if "tags" in jsonObj:
            self._tags = jsonObj['tags']


class AccountProperties(object):

    """Properties related to an Account."""

    def __init__(self):
        self._id = None
        self._mt4AccountID = None
        self._tags = None

    def serialize(self):
        """Serialize entity object to dict.

        Returns:
            str: Representation of entity state.

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
        """Deserialize dict to entity object."""

        if "id" in jsonObj:
            self._id = jsonObj['id']

        if "mt4AccountID" in jsonObj:
            self._mt4AccountID = int(jsonObj['mt4AccountID'])

        if "tags" in jsonObj:
            self._tags = jsonObj['tags']

    @property
    def aid(self):
        """str: The string representation of an Account Identifier.
                Format: "-"-delimited string with format
                "{siteID}-{divisionID}-{userID}-{accountNumber}"
                The name aid was chosen because of naming conflicts in python.
        """
        return self._id

    @aid.setter
    def aid(self, aid):
        self._id = aid

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
