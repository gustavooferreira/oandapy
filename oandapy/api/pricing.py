# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Pricing endpoint
"""


class Pricing(object):
    """Class holding pricing functions

    Pricing
        Docs: http://developer.oanda.com/rest-live-v20/pricing-ep/
    """

    def __init__(self, api):
        self._api = api

    def get_pricing(self, account_id, instruments, since=None):
        """Get pricing information for a specified list of Instruments within
        an Account.

        Args:
            account_id: A string providing an account ID.
            instruments: A list with the instruments to get pricing for.
            since: Aa optional string with the date/time to apply to the
            returned prices.

        Returns:
            A dict with pricing information.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        """ Get pricing information for a specified list of Instruments within
        an Account."""
        endpoint = 'accounts/{0}/pricing'.format(account_id)
        inst = "%2C".join(instruments)
        params = {}
        params["instruments"] = inst

        if since is not None:
            params["since"] = since

        return self._api.request(endpoint, params=params)
