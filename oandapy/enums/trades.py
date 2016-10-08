# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Trades Definitions
"""

from enum import Enum


class TradeState(Enum):
    """TradeState - The current state of the Trade.

    OPEN                    The Trade is currently open.
    CLOSED                  The Trade has been fully closed.
    CLOSE_WHEN_TRADEABLE    The Trade will be closed as soon as the trade’s
                            instrument becomes tradeable.
    """

    OPEN = 1
    CLOSED = 2
    CLOSE_WHEN_TRADEABLE = 3
