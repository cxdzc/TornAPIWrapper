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
    """
    Faction API endpoints.
    """

    def __init__(self, api: TornAPIWrapper):
        self.api = api

    def get_applications(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your faction's applications.
        Requires faction API access permissions.
        API key (Minimal).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/applications", self.api.build_params(self.get_applications, locals()))

    def get_attacks(self, attack_filters: list[AttackFiltersOptions] = None, limit: int = 100, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your faction's detailed attacks.
        Requires faction API access permissions.
        API key (Limited).
        :param attack_filters: It's possible to use this query parameter to only get incoming or outgoing attacks / revives. If not specified, this selection will return both incoming and outgoing attacks / revives. It's also possible to combine this with 'idFilter'. This filter allows using from/to to filter by ids instead of timestamps.
        :param limit: Number of results to return.
        :param sort: Sorted by the greatest timestamps.
        :param to: Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
        :param from_: Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/attacks", self.api.build_params(self.get_attacks, locals()))

    def get_attacksfull(self, attack_filters: list[AttackFiltersOptions] = None, limit: int = 1000, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your faction's simplified attacks
        Requires faction API access permissions.
        API key (Limited).
        :param attack_filters: It's possible to use this query parameter to only get incoming or outgoing attacks / revives. If not specified, this selection will return both incoming and outgoing attacks / revives. It's also possible to combine this with 'idFilter'. This filter allows using from/to to filter by ids instead of timestamps.
        :param limit: Number of results to return.
        :param sort: Sorted by the greatest timestamps.
        :param to: Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
        :param from_: Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/attacksfull", self.api.build_params(self.get_attacksfull, locals()))

    def get_balance(self, balance_category: FacCatScopeOptions = "current", timestamp: int = None, comment: str = None) -> dict:
        """
        Get your faction's & member's balance details.
        Requires faction API access permissions.
        API key (Limited).
        :param balance_category: By default, this selection will return only current faction's member balances, and the option 'all' will return all current members balances + additionally those of ex-members which do have money or points on their balance.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/balance", self.api.build_params(self.get_balance, locals()))

    def get_basic(self, faction_id: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your faction's basic details or a faction's basic details.
        API key (Public).
        The 'is_enlisted' value will be populated if you have API faction permissions (with custom, limited or full access keys), otherwise it will be set as null.
        Specific Faction - The 'is_enlisted' value will be populated if you're requesting data for your faction and have faction permissions (with custom, limited or full access keys), otherwise it will be set as null.
        :param faction_id: Faction id.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/basic", self.api.build_params(self.get_basic, locals()))

    def get_chain(self, faction_id: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your faction's current chain or a specific faction.
        API key (Public).
        :param faction_id: Faction id.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/chain", self.api.build_params(self.get_chain, locals()))

    def get_chains(self, faction_id: int = None, limit: int = 100, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get a list of completed chains for your faction or a specific faction.
        API key (Public).
        :param faction_id: Faction id.
        :param limit: Number of results to return.
        :param sort: Sorted by the greatest timestamps.
        :param to: Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
        :param from_: Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/chains", self.api.build_params(self.get_chains, locals()))

    def get_chainreport(self, chain_id: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get the latest chain report for your faction or a specific faction.
        API key (Public).
        This includes currently ongoing chains.
        Specifc Faction - Chain reports for ongoing chains are available only for your own faction.
        :param chain_id: Chain id.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/chainreport", self.api.build_params(self.get_chainreport, locals()))

    def get_contributors(self, stat_key: FacContributorsStatOptions, contributors_category: FacCatScopeOptions = "current", timestamp: int = None, comment: str = None) -> dict:
        """
        Get your faction's challenge contributors.
        Requires faction API access permissions.
        API key (Public).
        :param stat_key: Get contributors for this field.
        :param contributors_category: By default, this selection will return only current faction's member contributions, and the option 'all' will return all contributors.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/contributors", self.api.build_params(self.get_contributors, locals()))

    def get_crimes(self, crimes_category: FacCrimesCatOptions = "all", crimes_filter: FacCrimesFiltersOptions = None, offset: int = 0, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your faction's organized crimes.
        Requires faction API access permissions.
        API key (Minimal).
        It's possible to get older entries either by timestamp range (from, to) or with offset.
        Crimes are ordered depending on the category chosen:
         - For categories 'all' & 'available', the ordering field is 'created_at'.
         - For categories 'successful', 'failed' & 'completed', the ordering field is 'executed_at'.
         - For categories 'recruiting' & 'expired', the ordering field is 'expired_at'.
         - For category 'planning', the ordering field is 'ready_at'.
        :param crimes_category: Category of organized crimes returned. Category 'available' includes both 'recruiting' & 'planning', and category 'completed' includes both 'successful' & 'failure'.
        :param crimes_filter: It's possible to set this parameter to specify a field used for the sort, from & to query parameters. If not specified, the field will default to the category sorting as described above.
        :param offset: Number of rows to skip before returning results.
        :param sort: Sorted by the greatest timestamps.
        :param to: Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
        :param from_: Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/crimes", self.api.build_params(self.get_crimes, locals()))

    def get_crime(self, crime_id: int, timestamp: int = None, comment: str = None) -> dict:
        """
        Get a specific organized crime.
        API key (Minimal).
        :param crime_id: Crime id.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/crime", self.api.build_params(self.get_crime, locals()))

    def get_hof(self, faction_id: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get the hall of fame rankings for your faction or a specific faction.
        API key (Public).
        :param faction_id: Faction id.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/hof", self.api.build_params(self.get_hof, locals()))

    def get_members(self, faction_id: int = None, striptags: bool = True, timestamp: int = None, comment: str = None) -> dict:
        """
        Get a list of members for your faction or a specific faction.
        API key (Public).
        The 'revive_setting' value will be populated (not Unknown) if you have faction permissions (with custom, limited or full access keys), otherwise it will be set as 'Unknown'.
        Specific Faction - The 'revive_setting' value will be populated (not Unknown) if you're requesting data for your own faction and have faction permissions (with custom, limited or full access keys), otherwise it will be set as 'Unknown'.
        :param faction_id: Faction id.
        :param striptags: Determines if fields include HTML or not ('Hospitalized by user' vs 'Hospitalized by user').
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/members", self.api.build_params(self.get_members, locals()))

    def get_news(self, news_category: FacNewsCatOptions, striptags: bool = False, limit: int = 100, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your faction's news details.
        Requires faction API access permissions.
        API key (Minimal).
        It is possible to pass up to 10 categories at the time.
        :param news_category: News category type.
        :param striptags: Determines if fields include HTML or not ('Hospitalized by user' vs 'Hospitalized by user').
        :param limit: Number of results to return.
        :param sort: Sorted by the greatest timestamps.
        :param to: Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
        :param from_: Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/news", self.api.build_params(self.get_news, locals()))

    def get_positions(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your faction's positions details.
        Requires faction API access permissions.
        API key (Minimal).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/positions", self.api.build_params(self.get_positions, locals()))

    def get_rackets(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get a list of current rackets.
        API key (Public).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/rackets", self.api.build_params(self.get_rackets, locals()))

    def get_raidreport(self, raid_war_id: int, timestamp: int = None, comment: str = None) -> dict:
        """
        Get raid war details.
        API key (Public).
        :param raid_war_id: Raid war id.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/raidreport", self.api.build_params(self.get_raidreport, locals()))

    def get_raids(self, faction_id: int = None, limit: int = 20, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get the raids history for your faction or a specific faction.
        API key (Public).
        :param faction_id: Faction id.
        :param limit: Number of results to return.
        :param sort: Sorted by the greatest timestamps.
        :param to: Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
        :param from_: Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/raids", self.api.build_params(self.get_raids, locals()))

    def get_rankedwars(self, faction_id: int = None, limit: int = 20, offset: int = 0, timestamp: int = None, comment: str = None) -> dict:
        """
        Get the ranked wars history for your faction or a specific faction.
        Requires faction API access permissions.
        API key (Public).
        Use offset to get older results which are always ordered descending.
        :param faction_id: Faction id.
        :param limit: Number of results to return.
        :param offset: Number of rows to skip before returning results.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/rankedwars", self.api.build_params(self.get_rankedwars, locals()))

    def get_rankedwarreport(self, ranked_war_id: int, timestamp: int = None, comment: str = None) -> dict:
        """
        Get ranked war details.
        API key (Public).
        :param ranked_war_id: Ranked war id.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/rankedwarreport", self.api.build_params(self.get_rankedwarreport, locals()))

    def get_reports(self, report_category: ReportCatOptions = None, target_id: int = None, limit: int = 20, offset: int = 0, sort: SortOptions = "DESC", timestamp: int = None, comment: str = None) -> dict:
        """
        Get faction reports.
        API key (Limited).
        The default limit is set to 25. However, the limit can be set to 100 for the 'stats' category.
        :param report_category: Used to filter reports with a specific type.
        :param target_id: Get reports for a specific player by passing their player ID.
        :param limit: Number of results to return.
        :param offset: Number of rows to skip before returning results.
        :param sort: Sorted by the greatest timestamps.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/reports", self.api.build_params(self.get_reports, locals()))

    def get_revives(self, attack_filters: list[AttackFiltersOptions] = None, striptags: bool = True, limit: int = 100, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your faction's detailed revives.
        Requires faction API access permissions.
        API key (Limited).
        :param attack_filters: It's possible to use this query parameter to only get incoming or outgoing attacks / revives. If not specified, this selection will return both incoming and outgoing attacks / revives. It's also possible to combine this with 'idFilter'. This filter allows using from/to to filter by ids instead of timestamps.
        :param striptags: Determines if fields include HTML or not ('Hospitalized by user' vs 'Hospitalized by user').
        :param limit: Number of results to return.
        :param sort: Sorted by the greatest timestamps.
        :param to: Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
        :param from_: Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/revives", self.api.build_params(self.get_revives, locals()))

    def get_revivesfull(self, attack_filters: list[AttackFiltersOptions] = None, striptags: bool = True, limit: int = 1000, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your faction's simplified revives.
        Requires faction API access permissions.
        API key (Limited).
        :param attack_filters: It's possible to use this query parameter to only get incoming or outgoing attacks / revives. If not specified, this selection will return both incoming and outgoing attacks / revives. It's also possible to combine this with 'idFilter'. This filter allows using from/to to filter by ids instead of timestamps.
        :param striptags: Determines if fields include HTML or not ('Hospitalized by user' vs 'Hospitalized by user').
        :param limit: Number of results to return.
        :param sort: Sorted by the greatest timestamps.
        :param to: Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
        :param from_: Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/revivesFull", self.api.build_params(self.get_revivesfull, locals()))

    def get_search(self, faction_name: str = None, filters: list[str] = None, limit: int = 20, offset: int = 0, timestamp: int = None, comment: str = None) -> dict: #1F4A9 endpoint
        """
        Search factions by name or other criteria.
        API key (Public).
        This selection is standalone and cannot be used together with other selections.
        :param faction_name: Name to search for.
        :param filters: A filtering query parameter allowing a comma-separated list of filters.
        :param limit: Number of results to return.
        :param offset: Number of rows to skip before returning results.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/search", self.api.build_params(self.get_search, locals()))

    def get_stats(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your faction's challenges stats.
        Requires faction API access permissions.
        API key (Minimal).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/stats", self.api.build_params(self.get_stats, locals()))

    def get_territory(self, faction_id: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get a list of territories for your faction or a specific faction.
        API key (Public).
        :param faction_id: Faction id.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/territory", self.api.build_params(self.get_territory, locals()))

    def get_territoryownership(self, limit: int = 20, offset: int = 0, timestamp: int = None, comment: str = None) -> dict:
        """
        Get a list territory ownership.
        API key (Public).
        :param limit: Number of results to return.
        :param offset: Number of rows to skip before returning results.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/territoryownership", self.api.build_params(self.get_territoryownership, locals()))

    def get_territorywars(self, faction_id: int = None, limit: int = 100, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get the territory wars history for your faction or a specific faction.
        API key (Public).
        :param faction_id: Faction id.
        :param limit: Number of results to return.
        :param sort: Sorted by the greatest timestamps.
        :param to: Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
        :param from_: Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/territorywars", self.api.build_params(self.get_territorywars, locals()))

    def get_territorywarreport(self, territory_war_id: int, timestamp: int = None, comment: str = None) -> dict:
        """
        Get territory war details.
        API key (Public).
        :param territory_war_id: Territory war id.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/territorywarreport", self.api.build_params(self.get_territorywarreport, locals()))

    def get_upgrades(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your faction's upgrades.
        Requires faction API access permissions.
        API key (Minimal).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/upgrades", self.api.build_params(self.get_upgrades, locals()))

    def get_warfare(self, warfare_category: FacWarfareCatOptions, limit: int = 100, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get faction warfare.
        API key (Public).
        The response depends on the selected category.
        :param warfare_category: Warefare categories.
        :param limit: Number of results to return.
        :param sort: Sorted by the greatest timestamps.
        :param to: Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
        :param from_: Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/warfare", self.api.build_params(self.get_warfare, locals()))

    def get_wars(self, faction_id: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get the wars and pacts details for your faction or a specific faction.
        API key (Public).
        :param faction_id: Faction id.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/wars", self.api.build_params(self.get_wars, locals()))

    def get_lookup(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get all available faction selections.
        API key (Public).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/lookup", self.api.build_params(self.get_lookup, locals()))

    def get_timestamp(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get current server time.
        API key (Public).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/faction/timestamp", self.api.build_params(self.get_timestamp, locals()))