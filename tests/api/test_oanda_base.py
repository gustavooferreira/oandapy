# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""

"""

import unittest
from unittest import mock
from oandapy.api.oanda_base import Core


class TestCore(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        obj = Core(environment="practice", access_token="token")

    def tearDown(self):
        pass

    def test_name(self):
        pass
