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

import inspect
from typing import Callable

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

    param_from = {"from_"}
    param_target = {"target_id"}
    param_name = {"faction_name"}
    param_stat = {"stat_key", "stat_keys"}
    param_log = {"attack_log_id", "log_id"}
    param_ids = {"category_ids", "honor_ids", "item_ids", "medals_ids", "territory_ids"}
    param_filters = {"attack_filters", "crimes_filter", "property_filters"}
    param_id = {"chain_id", "crime_id", "faction_id", "item_id", "listing_id", "log_category_id_torn", "property_id", "property_type_id", "race_id", "raid_war_id", "ranked_war_id", "team_id", "territory_war_id", "thread_id", "track_id", "user_id"}
    param_cat = {"balance_category", "bazaar_category", "car_category", "contributors_category", "crimes_category", "item_category", "leaderboard_category", "list_category", "log_category_id", "news_category", "race_category", "report_category", "stat_category", "warfare_category"}
    param_group = {"from": param_from, "target": param_target, "name": param_name, "stat": param_stat, "log": param_log, "ids": param_ids, "filters": param_filters, "id": param_id, "cat": param_cat}
    parameter_map = {key: group for group, keys in param_group.items() for key in keys}

    api_error_handler : TornAPIErrorHandler = TornAPIErrorHandler()

    def __init__(self, api_key: str, request_timeout: float | tuple[float, float] = 10):
        self.api_key = api_key
        self.request_timeout = request_timeout
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"ApiKey {self.api_key}", "User-Agent": "TornAPIWrapper/2.0.0", "Accept": "application/json"})

        self.user : User = User(self)
        self.faction : Faction = Faction(self)
        self.market : Market = Market(self)
        self.forum : Forum = Forum(self)
        self.racing : Racing = Racing(self)
        self.property : Property = Property(self)
        self.key : Key = Key(self)
        self.torn : Torn = Torn(self)

    @staticmethod
    def build_local_params(method_request: Callable, local_vars: dict) -> dict | None:
        """
        Extracts the arguments passed to `method_request` and returns them as a clean dictionary ready for further processing.
        :param method_request: The `TornAPIWrapper` method.
        :param local_vars: A dictionary containing the `method_request` scope's local variables.
        :return: A sterilized dictionary for further processing or None.
        :rtype: dict | None
        """
        return {param: local_vars[param] for param in inspect.signature(method_request).parameters if local_vars[param] is not None and param != "self"} or None

    def build_params(self, method_request: Callable, local_vars: dict) -> dict | None:
        """
        Builds Torn API compatible query parameters from wrapper method arguments.
        :param method_request: The `TornAPIWrapper` method.
        :param local_vars: A dictionary containing the `method_request` scope's local variables.
        :return: A formatted dictionary of API query parameters | None.
        :rtype: dict | None
        """
        local_params = self.build_local_params(method_request, local_vars)
        if local_params is None:
            return None
        api_params = {}
        for param, value in local_params.items():
            if isinstance(value, list) and value: #Format `array[string]` or `array[int]` query for the API e.g. `get_attacks()`.
                value = ",".join(map(str, value))
            elif param == "timestamp" and isinstance(value, int): #Format Python timestamp[int] to API friendly timestamp[str].
                value = str(value)
            elif param == "striptags" and isinstance(value, bool): #Format Python striptags[bool] to API friendly striptags[str].
                value = str(value).lower()
            api_param_var = self.parameter_map.get(param, param) #Replace param such as `stat_category` with `cat` for the API. The wrapper param is not `cat` since type hinting is not clear to the user.
            api_params[api_param_var] = value
        return api_params or None

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