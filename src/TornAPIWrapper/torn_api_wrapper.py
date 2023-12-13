"""
MIT License

Copyright (c) 2023-Present cxdzc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import requests
from typing import Union, List, Dict
from .torn_api_error_handler import TornApiErrorHandler

class TornApiWrapper:
    """
    A Python wrapper for the Torn City API (https://www.torn.com/api.html), providing access to Torn City data.

    Parameters:
    - api_key (str): API key used to authenticate API requests.

    Methods:
    - api_request(self, endpoint: str, input_id: int = None, selections: List[str] = None, limit: int = None, sort: str = None, stat: str = None, cat: int = None, log: int = None, from_unix: int = None, to_unix: int = None, unix_timestamp: int = None) -> dict: Make a request to Torn City API.
    - get_user(user_id: int = None, selections: list = None) -> dict: Get Torn City user data.
    - get_property(property_id: int, selections: list = None) -> dict: Get Torn City property data.
    - get_faction(faction_id: int = None, selections: list = None) -> dict: Get Torn City faction data.
    - get_company(company_id: int = None, selections: list = None) -> dict: Get Torn City company data.
    - get_market(item_id: int, selections: list = None) -> dict: Get Torn City market data.
    - get_torn(torn_id: Union[str, int] = None, selections: List[str] = None) -> dict: Json-encoded Torn City data.
    - get_key_info() -> dict: Get Torn City API key data.
    """

    base_url = "https://api.torn.com"

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_comment = None
        self.api_error_handler = TornApiErrorHandler().api_error_handler

    def api_request(self, endpoint: str, input_id: int = None, selections: List[str] = None, limit: int = None, sort: str = None, stat: str = None, cat: int = None, log: int = None, from_unix: int = None, to_unix: int = None, unix_timestamp: int = None) -> dict:
        """
        Make a request to Torn City API.
        :param endpoint: API endpoint.
        :param input_id: ID input for endpoint.
        :param selections: List of selections from available fields.
        :param limit: Limit amount of results.
        :param sort: Sort results.
        :param stat: Select a stat to view.
        :param cat: Filter logs based on the Torn log categories. ^⨀ᴥ⨀^
        :param log: Filter logs based on the Torn log types.
        :param from_unix: UNIX timestamp to filter results, including entries on or after this timestamp.
        :param to_unix: UNIX timestamp to filter results, including entries on or before this timestamp.
        :param unix_timestamp: UNIX timestamp to get specific stat from date.
        :return: Json-encoded data.
        """
        endpoint = f"{endpoint}{'/' + str(input_id) if input_id else ''}"
        params: Dict[str, Union[str, int]] = {"selections": ','.join(selections)} if selections else {}
        params["key"] = self.api_key
        if limit is not None: params["limit"] = limit
        if sort is not None: params["sort"] = sort
        if stat is not None: params["stat"] = stat
        if cat is not None: params["cat"] = cat
        if log is not None: params["log"] = log
        if from_unix is not None: params["from"] = from_unix
        if to_unix is not None: params["to"] = to_unix
        if unix_timestamp is not None: params["timestamp"] = unix_timestamp
        if self.api_comment is not None: params["comment"] = self.api_comment
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        return self.api_error_handler(response)

    def get_user(self, user_id: int = None, selections: List[str] = None, limit: int = None, stat: str = None, cat: int = None, log: int = None, from_unix: int = None, to_unix: int = None, unix_timestamp: int = None) -> dict:
        """
        Get Torn City user data.
        :param user_id: Torn City user ID.
        :param selections: List of selections from available fields.
        :param limit: Limit amount of results.
        :param stat: Select a stat to view.
        :param cat: Filter based on the log categories. ^⨀ᴥ⨀^
        :param log: Filter based on the log types.
        :param from_unix: UNIX timestamp to filter results, including entries on or after this timestamp.
        :param to_unix: UNIX timestamp to filter results, including entries on or before this timestamp.
        :param unix_timestamp: UNIX timestamp to get specific stat from date.
        :return: Json-encoded Torn City user data.
        """
        return self.api_request("/user", user_id, selections, limit, stat=stat, cat=cat, log=log, from_unix=from_unix, to_unix=to_unix, unix_timestamp=unix_timestamp)

    def get_property(self, property_id: int, selections: List[str] = None) -> dict:
        """
        Get Torn City property data.
        :param property_id: Torn City property ID.
        :param selections: List of selections from available fields.
        :return: Json-encoded Torn City property data.
        """
        return self.api_request(f"/property", property_id, selections)

    def get_faction(self, faction_id: int = None, selections: List[str] = None, limit: int = None, sort: str = None, from_unix: int = None, to_unix: int = None) -> dict:
        """
        Get Torn City faction data.
        :param faction_id: Torn City faction ID.
        :param selections: List of selections from available fields.
        :param limit: Limit amount of results.
        :param sort: Sort results.
        :param from_unix: UNIX timestamps to filter results, including entries on or after this timestamp.
        :param to_unix: UNIX timestamps to filter results, including entries on or before this timestamp.
        :return: Json-encoded Torn City faction data.
        """
        return self.api_request(f"/faction", faction_id, selections, limit, sort, from_unix=from_unix, to_unix=to_unix)

    def get_company(self, company_id: int = None, selections: List[str] = None, limit: int = None, from_unix: int = None, to_unix: int = None) -> dict:
        """
        Get Torn City company data.
        :param company_id: Torn City company ID.
        :param selections: List of selections from available fields.
        :param limit: Limit amount of results.
        :param from_unix: UNIX timestamps to filter results, including entries on or after this timestamp.
        :param to_unix: UNIX timestamps to filter results, including entries on or before this timestamp.
        :return: Json-encoded Torn City company data.
        """
        return self.api_request(f"/company", company_id, selections, limit, from_unix=from_unix, to_unix=to_unix)

    def get_market(self, item_id: int, selections: List[str] = None) -> dict:
        """
        Get Torn City market data.
        :param item_id: Torn City item ID.
        :param selections: List of selections from available fields.
        :return: Json-encoded Torn City market data.
        """
        return self.api_request(f"/market", item_id, selections)

    def get_torn(self, torn_id: Union[str, int] = None, selections: List[str] = None) -> dict:
        """
        Get Torn City data.
        :param torn_id: Torn City ID.
        :param selections: List of selections from available fields.
        :return: Json-encoded Torn City data.
        """
        return self.api_request(f"/torn", torn_id, selections)

    def get_key_info(self) -> dict:
        """
        Get Torn City API key data.
        :return: Json-encoded Torn City data.
        """
        return self.api_request(f"/key", None, ["info"])