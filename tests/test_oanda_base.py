#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 gustavoferreira

"""

"""

import unittest
from oandapy.api import oanda_base


class TestClass(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        a = oanda_base.Core("practice")
        pass

    def tearDown(self):
        pass

    def test_name(self):
        pass
