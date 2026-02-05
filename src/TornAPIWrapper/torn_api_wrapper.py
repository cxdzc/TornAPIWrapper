"""
The MIT License (MIT)

Copyright (c) 2023-Present cxdzc

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import requests

from .endpoints.faction import Faction
from .endpoints.forum import Forum
from .endpoints.key import Key
from .endpoints.market import Market
from .endpoints.property import Property
from .endpoints.racing import Racing
from .endpoints.torn import Torn
from .endpoints.user import User
from .errors import TornAPIErrorHandler

class TornAPIWrapper:
    """
    A Python wrapper for the Torn City API, providing access to Torn City data.
    """
    BASE_URL = "https://api.torn.com/v2"
    api_error_handler: TornAPIErrorHandler = TornAPIErrorHandler()

    def __init__(self, api_key: str, request_timeout: float | tuple[float, float] = 10):
        self.api_key = api_key
        self.request_timeout = request_timeout
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"ApiKey {self.api_key}", "User-Agent": "TornAPIWrapper/2.0.0", "Accept": "application/json"})

        self.user: User = User(self)
        self.faction: Faction = Faction(self)
        self.market: Market = Market(self)
        self.forum: Forum = Forum(self)
        self.racing: Racing = Racing(self)
        self.property: Property = Property(self)
        self.key: Key = Key(self)
        self.torn: Torn = Torn(self)

    def request(self, endpoint: str, params: dict | None) -> dict:
        """
        Sends a request to the Torn API and returns the JSON response.
        :param endpoint: Torn API endpoint path.
        :param params: Query parameters to include in the request.
        :return: API response data.
        :rtype: dict
        """
        api_request = self.session.get(url=f"{self.BASE_URL}{endpoint}", params=params, timeout=self.request_timeout)
        api_request.raise_for_status()
        api_request_json = api_request.json()
        api_request_error = api_request_json.get("error")
        if api_request_error:
            self.api_error_handler.raise_code(api_request_error["code"])
        return api_request_json