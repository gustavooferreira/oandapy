# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""Base module where the Core class is created.

This module consists of a base class that is not meant to be used on its own.

"""

import json
import requests
from oandapy.exceptions import OandaError


class Core(object):
    """Core Abstract Class to be inherited.

    This class is not meant to be called on its own!

    """

    def __init__(self, environment, access_token=None):
        """Core Abstract object.

        Args:
            environment (str): Provides the environment for OANDA's API.
            access_token (str): Specifies the access token.

        """
        envs = {"practice": "https://api-fxpractice.oanda.com",
                "live": "https://api-fxtrade.oanda.com"}

        assert environment in envs, ("Environment '{0}' does not "
                                     "exist!".format(environment))
        self._api_url = envs[environment]

        self._client = requests.Session()
        self._client.headers['Content-Type'] = "application/json"

        if access_token:
            self._client.headers['Authorization'] = 'Bearer ' + access_token
        else:
            assert access_token is not None, ("Access token needs to be defined"
                                              " for authorization purpose.")

    def request(self, endpoint, method, params=None):
        """Requests data from Oanda API.

        Args:
            endpoint (str): URL for Oanda API endpoint.
            method (str): Specifies the method to be used on the request.
            params (dict, optional): Specifies parameters to be sent with the
                request. Defaults to None.

        Returns:
            dict: Data retrieved for specified endpoint.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            OandaError: An error occurred while requesting the Oanda API.

        """
        url = "/".join((self._api_url, self._version, endpoint))

        method = method.lower()
        func = getattr(self._client, method)

        params = params or {}

        request_args = {}
        if method == 'get':
            request_args['params'] = params
        else:
            request_args['data'] = json.dumps(params)

        # This function might throw a RequestException
        response = func(url, **request_args)

        # This function might throw a ValueError Exception
        content = response.json()

        if response.status_code >= 400:
            raise OandaError(response.status_code, content)

        return content
