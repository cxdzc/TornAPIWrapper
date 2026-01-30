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

from .type_hints import SortOptions, RaceCatOptions, UserListCatOptions, AttackFiltersOptions, \
    UserPropertiesFiltersOptions, ReportCatOptions, UserPrsnlStatsCatOptions, UserPrsnlStatsStatOptions

if TYPE_CHECKING:
    from .torn_api_wrapper import TornAPIWrapper

class User:
    def __init__(self, api: TornAPIWrapper):
        self.api = api

    def get_ammo(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/ammo", self.api.build_params(self.get_ammo, locals()))

    def get_attacks(self, attack_filters: list[AttackFiltersOptions] = None, limit: int = 100, sort: SortOptions = None, to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/user/attacks", self.api.build_params(self.get_attacks, locals()))

    def get_attacksfull(self, attack_filters: list[AttackFiltersOptions] = None, limit: int = 1000, sort: SortOptions = None, to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/user/attacksfull", self.api.build_params(self.get_attacksfull, locals()))

    def get_bars(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/bars", self.api.build_params(self.get_bars, locals()))

    def get_basic(self, user_id: int = None, striptags: bool = True, timestamp: int = None, comment: str = None):
        return self.api.request("/user/basic", self.api.build_params(self.get_basic, locals()))

    def get_battlestats(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/battlestats", self.api.build_params(self.get_battlestats, locals()))

    def get_bounties(self, user_id: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/user/bounties", self.api.build_params(self.get_bounties, locals()))

    def get_calendar(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/calendar", self.api.build_params(self.get_calendar, locals()))

    def get_competition(self, user_id: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/user/competition", self.api.build_params(self.get_competition, locals()))

    def get_cooldowns(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/cooldowns", self.api.build_params(self.get_cooldowns, locals()))

    def get_crimes(self, crime_id: int, timestamp: int = None, comment: str = None):
        return self.api.request(f"/user/crimes", self.api.build_params(self.get_crimes, locals()))

    def get_discord(self, user_id: int = None, timestamp: int = None, comment: str = None):
        return self.api.request(f"/user/discord", self.api.build_params(self.get_discord, locals()))

    def get_education(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/education", self.api.build_params(self.get_education, locals()))

    def get_enlistedcars(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/enlistedcars", self.api.build_params(self.get_enlistedcars, locals()))

    def get_equipment(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/equipment", self.api.build_params(self.get_equipment, locals()))

    def get_events(self, striptags: bool = False, limit: int = 20, to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/user/events", self.api.build_params(self.get_events, locals()))

    def get_faction(self, user_id: int = None, timestamp: int = None, comment: str = None):
        return self.api.request(f"/user/faction", self.api.build_params(self.get_faction, locals()))

    def get_forumfeed(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/forumfeed", self.api.build_params(self.get_forumfeed, locals()))

    def get_forumfriends(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/forumfriends", self.api.build_params(self.get_forumfriends, locals()))

    def get_forumposts(self, user_id: int = None, striptags: bool = True, limit: int = 20, sort: SortOptions = None, to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/user/forumposts", self.api.build_params(self.get_forumposts, locals()))

    def get_forumsubscribedthreads(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/forumsubscribedthreads", self.api.build_params(self.get_forumsubscribedthreads, locals()))

    def get_forumthreads(self, user_id: int = None, limit: int = 20, sort: SortOptions = None, to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/user/forumthreads", self.api.build_params(self.get_forumthreads, locals()))

    def get_hof(self, user_id: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/user/hof", self.api.build_params(self.get_hof, locals()))

    def get_honors(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/honors", self.api.build_params(self.get_honors, locals()))

    def get_icons(self, user_id: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/user/icons", self.api.build_params(self.get_icons, locals()))

    def get_itemmarket(self, offset: int = 0, timestamp: int = None, comment: str = None):
        return self.api.request("/user/itemmarket", self.api.build_params(self.get_itemmarket, locals()))

    def get_job(self, user_id: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/user/job", self.api.build_params(self.get_job, locals()))

    def get_jobpoints(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/jobpoints", self.api.build_params(self.get_jobpoints, locals()))

    def get_jobranks(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/jobranks", self.api.build_params(self.get_jobranks, locals()))

    def get_list(self, list_category: UserListCatOptions, striptags: bool = True, limit: int = 50, offset: int = None, sort: SortOptions = "ASC", timestamp: int = None, comment: str = None):
        return self.api.request("/user/list", self.api.build_params(self.get_list, locals()))

    def get_log(self, log_id: list[int] = None, log_category_id: int = None, target_id: int = None, limit: int = 20, to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/user/log", self.api.build_params(self.get_log, locals()))

    def get_medals(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/medals", self.api.build_params(self.get_medals, locals()))

    def get_merits(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/merits", self.api.build_params(self.get_merits, locals()))

    def get_messages(self, limit: int = 20, sort: SortOptions = None, to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/user/messages", self.api.build_params(self.get_messages, locals()))

    def get_missions(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/missions", self.api.build_params(self.get_missions, locals()))

    def get_money(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/money", self.api.build_params(self.get_money, locals()))

    def get_newevents(self, striptags: bool = False, timestamp: int = None, comment: str = None):
        return self.api.request("/user/newevents", self.api.build_params(self.get_newevents, locals()))

    def get_newmessages(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/newmessages", self.api.build_params(self.get_newmessages, locals()))

    def get_notifications(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/notifications", self.api.build_params(self.get_notifications, locals()))

    def get_organizedcrime(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/organizedcrime", self.api.build_params(self.get_organizedcrime, locals()))

    def get_personalstats(self, user_id: int = None, stat_category: UserPrsnlStatsCatOptions = None, stat_keys: list[UserPrsnlStatsStatOptions] = None, timestamp: int = None, comment: str = None):
        return self.api.request("/user/personalstats", self.api.build_params(self.get_personalstats, locals()))

    def get_profile(self, user_id: int = None, striptags: bool = True, timestamp: int = None, comment: str = None):
        return self.api.request("/user/profile", self.api.build_params(self.get_profile, locals()))

    def get_properties(self, user_id: int = None, property_filters: UserPropertiesFiltersOptions = None, limit: int = 20, offset: int = 0, timestamp: int = None, comment: str = None):
        return self.api.request("/user/properties", self.api.build_params(self.get_properties, locals()))

    def get_property(self, user_id: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/user/property", self.api.build_params(self.get_property, locals()))

    def get_races(self, race_category: RaceCatOptions = None, limit: int = 20, sort: SortOptions = None, to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/user/races", self.api.build_params(self.get_races, locals()))

    def get_racingrecords(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/racingrecords", self.api.build_params(self.get_racingrecords, locals()))

    def get_refills(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/refills", self.api.build_params(self.get_refills, locals()))

    def get_reports(self, report_category: ReportCatOptions = None, target_id: int = None, limit: int = 20, offset: int = 0, sort: SortOptions = "DESC", timestamp: int = None, comment: str = None):
        return self.api.request("/user/reports", self.api.build_params(self.get_reports, locals()))

    def get_revives(self, attack_filters: list[AttackFiltersOptions] = None, striptags: bool = True, limit: int = 20, sort: SortOptions = None, to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/user/revives", self.api.build_params(self.get_revives, locals()))

    def get_revivesfull(self, attack_filters: list[AttackFiltersOptions] = None, striptags: bool = True, limit: int = 20, sort: SortOptions = None, to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/user/revivesFull", self.api.build_params(self.get_revivesfull, locals()))

    def get_skills(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/skills", self.api.build_params(self.get_skills, locals()))

    def get_travel(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/travel", self.api.build_params(self.get_travel, locals()))

    def get_virus(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/virus", self.api.build_params(self.get_virus, locals()))

    def get_weaponexp(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/weaponexp", self.api.build_params(self.get_weaponexp, locals()))

    def get_workstats(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/workstats", self.api.build_params(self.get_workstats, locals()))

    def get_lookup(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/lookup", self.api.build_params(self.get_lookup, locals()))

    def get_timestamp(self, timestamp: int = None, comment: str = None):
        return self.api.request("/user/timestamp", self.api.build_params(self.get_timestamp, locals()))