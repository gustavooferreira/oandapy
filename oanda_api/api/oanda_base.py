# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

"""
Base module
"""

import json
import requests
from ..exceptions.exceptions import OandaError


class Core(object):
    """Core Abstract Class

    This class is not meant to be called on its own!
    """

    def __init__(self, environment, access_token=None, headers=None):
        """Instantiates an instance of Core Abstract object.

        Args:
            environment: A string providing de environment for OANDA's API.
            access_token: An optional string variable that specifies the access
                token.
            headers: An optional dict of parameters (Default: None)
        """
        envs = {"practice": "https://api-fxpractice.oanda.com",
                "live": "https://api-fxtrade.oanda.com"}

        assert environment in envs, "Environment '{0}' does not " \
            "exist".format(environment)
        self._api_url = envs[environment]

        self._version = ""

        self._client = requests.Session()
        self._client.headers['Content-Type'] = "application/json"

        self._access_token = access_token
        if access_token:
            self._client.headers['Authorization'] = 'Bearer ' + access_token
        else:
            # TODO: raise ERROR!!
            pass

        if headers:
            self._client.headers.update(headers)

    def _request(self, endpoint, method='GET', params=None):
        """Returns OANDA's response as a dictionary.

        Args:
            endpoint: A string with the url for OANDA API.
            method: An optional string variable that specifies the method to be
            used for accessing data (default: GET).
            params: An optional dict of parameters (Default: None).

        Returns:
            A dict with the response.

        Raises:
            OandaError: An error occurred while requesting the OANDA API.

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

        try:
            response = func(url, **request_args)
        except requests.RequestException as exc:
            print(str(exc))

        try:
            content = response.json()
        except ValueError as exc:
            raise OandaError(response.status_code, None) from exc

        if response.status_code >= 400:
            raise OandaError(response.status_code, content)

        return content

    def __str__(self):
        msg = 'Core = ["api_url" = {0}; "version" = {1}; "access_token" = {2}]'
        return msg.format(self._api_url, self._version or None,
                          self._access_token)
