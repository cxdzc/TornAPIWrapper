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

from .type_hints import SortOptions, FacCatScopeOptions, AttackFiltersOptions, FacContributorsStatOptions, \
    FacCrimesCatOptions, FacCrimesFiltersOptions, FacNewsCatOptions, ReportCatOptions, FacWarfareCatOptions

if TYPE_CHECKING:
    from .torn_api_wrapper import TornAPIWrapper

class Faction:
    def __init__(self, api: TornAPIWrapper):
        self.api = api

    def get_applications(self, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/applications", self.api.build_params(self.get_applications, locals()))

    def get_attacks(self, attack_filters: list[AttackFiltersOptions] = None, limit: int = 100, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/attacks", self.api.build_params(self.get_attacks, locals()))

    def get_attacksfull(self, attack_filters: list[AttackFiltersOptions] = None, limit: int = 1000, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/attacksfull", self.api.build_params(self.get_attacksfull, locals()))

    def get_balance(self, balance_category: FacCatScopeOptions = "current", timestamp: int = None, comment: str = None):
        return self.api.request("/faction/balance", self.api.build_params(self.get_balance, locals()))

    def get_basic(self, faction_id: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/basic", self.api.build_params(self.get_basic, locals()))

    def get_chain(self, faction_id: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/chain", self.api.build_params(self.get_chain, locals()))

    def get_chains(self, faction_id: int = None, limit: int = 100, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/chains", self.api.build_params(self.get_chains, locals()))

    def get_chainreport(self, chain_id: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/chainreport", self.api.build_params(self.get_chainreport, locals()))

    def get_contributors(self, stat_key: FacContributorsStatOptions, contributors_category: FacCatScopeOptions = "current", timestamp: int = None, comment: str = None):
        return self.api.request("/faction/contributors", self.api.build_params(self.get_contributors, locals()))

    def get_crimes(self, crimes_category: FacCrimesCatOptions = "all", crimes_filter: FacCrimesFiltersOptions = None, offset: int = 0, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/crimes", self.api.build_params(self.get_crimes, locals()))

    def get_crime(self, crime_id: int, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/crime", self.api.build_params(self.get_crime, locals()))

    def get_hof(self, faction_id: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/hof", self.api.build_params(self.get_hof, locals()))

    def get_members(self, faction_id: int = None, striptags: bool = True, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/members", self.api.build_params(self.get_members, locals()))

    def get_news(self, news_category: FacNewsCatOptions, striptags: bool = False, limit: int = 100, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/news", self.api.build_params(self.get_news, locals()))

    def get_positions(self, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/positions", self.api.build_params(self.get_positions, locals()))

    def get_rackets(self, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/rackets", self.api.build_params(self.get_rackets, locals()))

    def get_raidreport(self, raid_war_id: int, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/raidreport", self.api.build_params(self.get_raidreport, locals()))

    def get_raids(self, faction_id: int = None, limit: int = 20, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/raids", self.api.build_params(self.get_raids, locals()))

    def get_rankedwars(self, faction_id: int = None, limit: int = 20, offset: int = 0, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/rankedwars", self.api.build_params(self.get_rankedwars, locals()))

    def get_rankedwarreport(self, ranked_war_id: int, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/rankedwarreport", self.api.build_params(self.get_rankedwarreport, locals()))

    def get_reports(self, report_category: ReportCatOptions = None, target_id: int = None, limit: int = 20, offset: int = 0, sort: SortOptions = "DESC", timestamp: int = None, comment: str = None):
        return self.api.request("/faction/reports", self.api.build_params(self.get_reports, locals()))

    def get_revives(self, attack_filters: list[AttackFiltersOptions] = None, striptags: bool = True, limit: int = 100, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/revives", self.api.build_params(self.get_revives, locals()))

    def get_revivesfull(self, attack_filters: list[AttackFiltersOptions] = None, striptags: bool = True, limit: int = 1000, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/revivesFull", self.api.build_params(self.get_revivesfull, locals()))

    def get_search(self, faction_name: str = None, filters: list[str] = None, limit: int = 20, offset: int = 0, timestamp: int = None, comment: str = None): #1F4A9 endpoint
        return self.api.request("/faction/search", self.api.build_params(self.get_search, locals()))

    def get_stats(self, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/stats", self.api.build_params(self.get_stats, locals()))

    def get_territory(self, faction_id: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/territory", self.api.build_params(self.get_territory, locals()))

    def get_territoryownership(self, limit: int = 20, offset: int = 0, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/territoryownership", self.api.build_params(self.get_territoryownership, locals()))

    def get_territorywars(self, faction_id: int = None, limit: int = 100, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/territorywars", self.api.build_params(self.get_territorywars, locals()))

    def get_territorywarreport(self, territory_war_id: int, limit: int = 100, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/territorywarreport", self.api.build_params(self.get_territorywarreport, locals()))

    def get_upgrades(self, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/upgrades", self.api.build_params(self.get_upgrades, locals()))

    def get_warfare(self, warfare_category: FacWarfareCatOptions, limit: int = 100, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/warfare", self.api.build_params(self.get_warfare, locals()))

    def get_wars(self, faction_id: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/wars", self.api.build_params(self.get_wars, locals()))

    def get_lookup(self, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/lookup", self.api.build_params(self.get_lookup, locals()))

    def get_timestamp(self, timestamp: int = None, comment: str = None):
        return self.api.request("/faction/timestamp", self.api.build_params(self.get_timestamp, locals()))