# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Positions endpoints
"""


class Positions(object):
    """Class holding positions functions

    Positions
        Docs: http://developer.oanda.com/rest-live-v20/positions-ep/
    """

    def __init__(self, api):
        self._api = api

    def get_positions(self, account_id):
        """Get a list of all Accounts authorized for the provided token.

        Args:
            This function takes no arguments.

        Returns:
            A dict with all accounts ids and tags.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        """List all Positions for an Account. The Positions returned are for
        every instrument that has had a position during the lifetime of an a
        Account."""
        endpoint = 'accounts/{0}/positions'.format(account_id)

        return self._api.request(endpoint)

    def get_open_positions(self, account_id):
        """Get a list of all Accounts authorized for the provided token.

        Args:
            This function takes no arguments.

        Returns:
            A dict with all accounts ids and tags.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        """List all open Positions for an Account. An open Position is a
        Position in an Account that currently has a Trade opened for it."""
        endpoint = 'accounts/{0}/openPositions'.format(account_id)

        return self._api.request(endpoint)

    def get_position_details(self, account_id, instrument):
        """Get a list of all Accounts authorized for the provided token.

        Args:
            This function takes no arguments.

        Returns:
            A dict with all accounts ids and tags.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        """Get the details of a single Instrument’s Position in an Account.
        The Position may by open or not."""
        endpoint = 'accounts/{0}/positions/{1}'.format(account_id, instrument)

        return self._api.request(endpoint)

    def close_position(self, account_id, instrument, long_units,
                       long_client_extensions, short_units,
                       short_client_extensions):
        """Get a list of all Accounts authorized for the provided token.

        Args:
            This function takes no arguments.

        Returns:
            A dict with all accounts ids and tags.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.
        """
        """Closeout the open Position for a specific instrument in an
        Account."""
        endpoint = 'accounts/{0}/positions/{1}/close'.format(account_id,
                                                             instrument)

        params = {}

        if long_units:
            params["longUnits"] = long_units

        if short_client_extensions:
            params["longClientExtensions"] = long_client_extensions

        if short_units:
            params["shortUnits"] = short_units

        if long_client_extensions:
            params["longClientExtensions"] = long_client_extensions

        return self._api.request(endpoint, "PUT", params=params)
