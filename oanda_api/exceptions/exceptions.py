# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

"""
Exceptions
"""


class OandaError(Exception):
    """Oanda Error Exception Class"""

    def __init__(self, status_code, error_response):
        """
        These checks are necessary because right now, Oanda API is buggy

        """
        if error_response:
            if "errorCode" in error_response:
                code = error_response["errorCode"]
            else:
                code = ""

            if "errorMessage" in error_response:
                message = error_response["errorMessage"]
            else:
                message = ""

            msg = "OANDA server returned [{0}] error code, and API returned " \
                "[{1}] error code ({2})".format(status_code, code, message)
        else:
            msg = \
                "OANDA server returned [{0}] error code, and no API " \
                "response".format(status_code)

        super(OandaError, self).__init__(msg)
