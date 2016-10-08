# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Primitives Definitions
"""

from enum import Enum


class InstrumentType(Enum):
    """InstrumentType - The type of an Instrument

    CURRENCY    Currency
    CFD         Contract For Difference
    METAL       Metal
    """

    CURRENCY = 1
    CFD = 2
    METAL = 3
