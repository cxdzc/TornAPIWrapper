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

import aiohttp

from . import __version__
from .endpoints_async.faction import Faction
from .endpoints_async.forum import Forum
from .endpoints_async.key import Key
from .endpoints_async.market import Market
from .endpoints_async.property import Property
from .endpoints_async.racing import Racing
from .endpoints_async.torn import Torn
from .endpoints_async.user import User
from .errors import TornAPIErrorHandler

class TornAPIWrapperAsync:
    """
    A Python wrapper for the Torn City API, providing access to Torn City data.
    """
    BASE_URL = "https://api.torn.com/v2"
    api_error_handler: TornAPIErrorHandler = TornAPIErrorHandler()

    def __init__(self, api_key: str, request_timeout: float | tuple[float, float] = 10):
        self.api_key = api_key

        session_timeout: aiohttp.ClientTimeout | None = None
        if isinstance(request_timeout, (int, float)):
            session_timeout = aiohttp.ClientTimeout(total=float(request_timeout))
        elif isinstance(request_timeout, tuple) and len(request_timeout) == 2:
            session_timeout = aiohttp.ClientTimeout(sock_connect=float(request_timeout[0]), sock_read=float(request_timeout[1]))

        self.session = aiohttp.ClientSession(timeout=session_timeout)
        self.session.headers.update({"Authorization": f"ApiKey {self.api_key}", "User-Agent": f"TornAPIWrapper/{__version__}", "Accept": "application/json", "Accept-Encoding": "gzip, deflate"})

        self.user: User = User(self)
        self.faction: Faction = Faction(self)
        self.market: Market = Market(self)
        self.forum: Forum = Forum(self)
        self.racing: Racing = Racing(self)
        self.property: Property = Property(self)
        self.key: Key = Key(self)
        self.torn: Torn = Torn(self)

    async def request(self, endpoint: str, params: dict | None) -> dict:
        """
        Sends a request to the Torn API and returns the JSON response.
        :param endpoint: Torn API endpoint path.
        :param params: Query parameters to include in the request.
        :return: API response data.
        :rtype: dict
        """
        async with self.session.get(url=f"{self.BASE_URL}{endpoint}", params=params) as api_request:
            api_request.raise_for_status()
            api_request_json = await api_request.json()
        api_request_error = api_request_json.get("error")
        if api_request_error:
            self.api_error_handler.raise_code(api_request_error["code"])
        return api_request_json

    async def close(self) -> None:
        if self.session and not self.session.closed:
            await self.session.close()

    async def __aenter__(self) -> "TornAPIWrapperAsync":
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.close()