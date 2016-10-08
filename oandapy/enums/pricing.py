# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Pricing Definitions
"""

from enum import Enum


class PriceStatus(Enum):
    """PriceStatus - The status of the Price

    tradeable       The Instrument’s price is tradeable.
    non-tradeable   The Instrument’s price is not tradeable.
    invalid         The Instrument of the price is invalid or there is no valid
                    Price for the Instrument.

    """

    # TODO: Contact Oanda to report this inconsistency!
    # The lower case names are defined like that in the Oanda API.
    # And the dash instead of the underscore. (inconsistency)

    tradeable = 1
    non_tradeable = 2
    invalid = 3
