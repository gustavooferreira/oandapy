# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""Exceptions module definition"""


class OandaError(Exception):
    """Oanda Error Exception Class"""

    def __init__(self, status_code, resp_content):
        """OandaError Exception raised when server returns error.

        Args:
            status_code (str): Status code retrieved from the server.
            resp_content (dict): Response's body with more detailed info about
                the problem that has occured.

        """

        # TODO: Contact Oanda to inform about this bug
        # These checks are necessary because right now, Oanda API is buggy
        if resp_content:
            if "errorCode" in resp_content:
                code = resp_content["errorCode"]
            else:
                code = ""

            if "errorMessage" in resp_content:
                message = resp_content["errorMessage"]
            else:
                message = ""

            msg = ("OANDA server returned [{0}] error code, and API returned "
                   "[{1}] error code, with message: ({2})"
                   .format(status_code, code, message))
        else:
            msg = ("OANDA server returned [{0}] error code, and no API "
                   "response".format(status_code))

        super(OandaError, self).__init__(msg)
