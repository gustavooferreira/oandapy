# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""Account Definitions"""

from enum import Enum


class AccountFinancingMode(Enum):
    """AccountFinancingMode - The financing mode of an Account.

    NO_FINANCING : No financing is paid/charged for open Trades in the Account.
    SECOND_BY_SECOND : Second-by-second financing is paid/charged for open
        Trades in the Account, both daily and when the the Trade is closed.
    DAILY : A full day’s worth of financing is paid/charged for open Trades in
        the Account daily at 5pm New York time.

    """

    NO_FINANCING = 1
    SECOND_BY_SECOND = 2
    DAILY = 3


class PositionAggregationMode(Enum):
    """PositionAggregationMode - The financing mode of an Account.

    ABSOLUTE_SUM : The Position value or margin for each side (long and short)
        of the Position are computed independently and added together.
    MAXIMAL_SIDE : The Position value or margin for each side (long and short)
        of the Position are computed independently. The Position value or margin
        chosen is the maximal absolute value of the two.
    NET_SUM : The units for each side (long and short) of the Position are
        netted together and the resulting value (long or short) is used to
        compute the Position value or margin.

    """

    ABSOLUTE_SUM = 1
    MAXIMAL_SIDE = 2
    NET_SUM = 3
