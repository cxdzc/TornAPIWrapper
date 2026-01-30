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

from __future__ import annotations

from typing import TYPE_CHECKING

from .type_hints import SortOptions, TornFactionHofCatOptions, TornHofCatOptions, TornItemsCatOptions

if TYPE_CHECKING:
    from .torn_api_wrapper import TornAPIWrapper

class Torn:
    def __init__(self, api: TornAPIWrapper):
        self.api = api

    def get_attacklog(self, attack_log_id: str, striptags: bool = True, offset: int = 0, sort: SortOptions = None, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/attacklog", self.api.build_params(self.get_attacklog, locals()))

    def get_bounties(self, limit: int = 100, offset: int = 0, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/bounties", self.api.build_params(self.get_bounties, locals()))

    def get_calendar(self, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/calendar", self.api.build_params(self.get_calendar, locals()))

    def get_crimes(self, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/crimes", self.api.build_params(self.get_crimes, locals()))

    def get_education(self, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/education", self.api.build_params(self.get_education, locals()))

    def get_elimination(self, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/elimination", self.api.build_params(self.get_elimination, locals()))

    def get_eliminationteam(self, team_id: int, limit: int = 100, offset: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/eliminationteam", self.api.build_params(self.get_eliminationteam, locals()))

    def get_factionhof(self, leaderboard_category: TornFactionHofCatOptions, limit: int = 100, offset: int = 0, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/factionhof", self.api.build_params(self.get_factionhof, locals()))

    def get_factiontree(self, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/factiontree", self.api.build_params(self.get_factiontree, locals()))

    def get_honors(self, honor_ids: list[int] = None, limit: int = 20, offset: int = 0, sort: SortOptions = None, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/honors", self.api.build_params(self.get_honors, locals()))

    def get_hof(self, leaderboard_category: TornHofCatOptions, limit: int = 100, offset: int = 0, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/hof", self.api.build_params(self.get_hof, locals()))

    def get_itemammo(self, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/itemammo", self.api.build_params(self.get_itemammo, locals()))

    def get_itemdetails(self, item_id: int, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/itemdetails", self.api.build_params(self.get_itemdetails, locals()))

    def get_itemmods(self, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/itemmods", self.api.build_params(self.get_itemmods, locals()))

    def get_items(self, item_ids: list[int] = None, item_category: TornItemsCatOptions = None, sort: SortOptions = "ASC", timestamp: int = None, comment: str = None):
        return self.api.request("/torn/items", self.api.build_params(self.get_items, locals()))

    def get_logcategories(self, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/logcategories", self.api.build_params(self.get_logcategories, locals()))

    def get_logtypes(self, log_category_id_torn: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/logtypes", self.api.build_params(self.get_logtypes, locals()))

    def get_medals(self, medals_ids: list[int] = None, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/medals", self.api.build_params(self.get_medals, locals()))

    def get_merits(self, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/merits", self.api.build_params(self.get_merits, locals()))

    def get_organizedcrimes(self, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/organizedcrimes", self.api.build_params(self.get_organizedcrimes, locals()))

    def get_properties(self, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/properties", self.api.build_params(self.get_properties, locals()))

    def get_subcrimes(self, crime_id: int, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/subcrimes", self.api.build_params(self.get_subcrimes, locals()))

    def get_territory(self, territory_ids: list[str] = None, limit: int = 20, offset: int = 0, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/territory", self.api.build_params(self.get_territory, locals()))

    def get_lookup(self, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/lookup", self.api.build_params(self.get_lookup, locals()))

    def get_timestamp(self, timestamp: int = None, comment: str = None):
        return self.api.request("/torn/timestamp", self.api.build_params(self.get_timestamp, locals()))