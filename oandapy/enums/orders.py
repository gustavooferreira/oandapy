# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Orders Definitions
"""

from enum import Enum


class OrderType(Enum):
    """OrderType - The type of the Order

    MARKET              A Market Order
    LIMIT               A Limit Order
    STOP                A Stop Order
    MARKET_IF_TOUCHED   A Market-if-touched Order
    TAKE_PROFIT         A Take Profit Order
    STOP_LOSS           A Stop Loss Order
    TRAILING_STOP_LOSS  A Trailing Stop Loss Order
    """

    MARKET = 1
    LIMIT = 2
    STOP = 3
    MARKET_IF_TOUCHED = 4
    TAKE_PROFIT = 5
    STOP_LOSS = 6
    TRAILING_STOP_LOSS = 7


class OrderState(Enum):
    """OrderState - The current state of the Order

    PENDING     The Order is currently pending execution.
    FILLED      The Order has been filled.
    TRIGGERED   The Order has been triggered.
    CANCELLED   The Order has been cancelled.
    """

    PENDING = 1
    FILLED = 2
    TRIGGERED = 3
    CANCELLED = 4


class TimeInForce(Enum):
    """TimeInForce - The current state of the Order

    GTC     The Order is "Good unTil Cancelled".
    GTD     The Order is "Good unTil Date" and will be cancelled at the provided
            time.
    GFD     The Order is "Good For Day” and will be cancelled at 5pm New York
            time.
    FOK     The Order must be immediately "Filled Or Killed".
    IOC     The Order must be "Immediatedly paritally filled Or Cancelled".
    """

    GTC = 1
    GTD = 2
    GFD = 3
    FOK = 4
    IOC = 5


class OrderPositionFill(Enum):
    """OrderPositionFill - Specification of how Positions in the Account are
                           modified when the Order is filled.

    OPEN_ONLY       When the Order is filled, only allow Positions to be opened
                    or extended.
    REDUCE_FIRST    When the Order is filled, always fully reduce an existing
                    Position before opening a new Position.
    REDUCE_ONLY     When the Order is filled, only reduce an existing Position.
    DEFAULT         When the Order is filled, use REDUCE_FIRST behaviour for
                    non-client hedging Accounts, and OPEN_ONLY behaviour for
                    client hedging Accounts.
    """

    OPEN_ONLY = 1
    REDUCE_FIRST = 2
    REDUCE_ONLY = 3
    DEFAULT = 4
