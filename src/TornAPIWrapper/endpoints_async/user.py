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

from ..params.builders import build_params
from ..type_hints import SortOptions, RaceCatOptions, UserListCatOptions, AttackFiltersOptions, \
    UserPropertiesFiltersOptions, ReportCatOptions, UserPrsnlStatsCatOptions, UserPrsnlStatsStatOptions

if TYPE_CHECKING:
    from ..client_async import TornAPIWrapperAsync

class User:
    """
    User API endpoints.
    """

    def __init__(self, api: TornAPIWrapperAsync):
        self.api = api

    async def get_ammo(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your ammo information.
        API key (Minimal).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/ammo", build_params(self.get_ammo, locals()))

    async def get_attacks(self, attack_filters: list[AttackFiltersOptions] = None, limit: int = 100, sort: SortOptions = None, to: int = None, from_: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your detailed attacks.
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
        return await self.api.request("/user/attacks", build_params(self.get_attacks, locals()))

    async def get_attacksfull(self, attack_filters: list[AttackFiltersOptions] = None, limit: int = 1000, sort: SortOptions = None, to: int = None, from_: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your simplified attacks.
        API key (Limited).
        Returns up to 1,000 rows.
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
        return await self.api.request("/user/attacksfull", build_params(self.get_attacksfull, locals()))

    async def get_bars(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your bars information.
        API key (Minimal).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/bars", build_params(self.get_bars, locals()))

    async def get_basic(self, user_id: int = None, striptags: bool = True, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your basic profile information or for a specific user.
        API key (Public).
        :param user_id: User id or user discord id.
        :param striptags: Determines if fields include HTML or not ('Hospitalized by user' vs 'Hospitalized by user').
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/basic", build_params(self.get_basic, locals()))

    async def get_battlestats(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your battlestats.
        API key (Public).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/battlestats", build_params(self.get_battlestats, locals()))

    async def get_bounties(self, user_id: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get bounties placed on you or for a specific user.
        API key (Public).
        :param user_id: User id or user discord id.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/bounties", build_params(self.get_bounties, locals()))

    async def get_calendar(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your calendar events start time.
        API key (Minimal).
        Only available to yourself.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/calendar", build_params(self.get_calendar, locals()))

    async def get_competition(self, user_id: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your competition information or for a specific player.
        API key (Public).
        :param user_id: User id or user discord id.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/competition", build_params(self.get_competition, locals()))

    async def get_cooldowns(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your cooldowns information.
        API key (Minimal).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/cooldowns", build_params(self.get_cooldowns, locals()))

    async def get_crimes(self, crime_id: int, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your crime statistics.
        API key (Minimal).
        Return the details and statistics about for a specific crime.
        :param crime_id: Crime id.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/crimes", build_params(self.get_crimes, locals()))

    async def get_discord(self, user_id: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your discord information or for a specific user.
        API key (Public).
        :param user_id: User id or user discord id.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/discord", build_params(self.get_discord, locals()))

    async def get_education(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your education information.
        API key (Public).
        The response contains a list of complete eduactions and of a current education (if any).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/education", build_params(self.get_education, locals()))

    async def get_enlistedcars(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your enlisted cars.
        API key (Minimal).
        Returns a list of all user enlisted cars.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/enlistedcars", build_params(self.get_enlistedcars, locals()))

    async def get_equipment(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your equipment & clothing.
        API key (Minimal).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/equipment", build_params(self.get_equipment, locals()))

    async def get_events(self, striptags: bool = False, limit: int = 20, to: int = None, from_: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your events.
        API key (Limited).
        :param striptags: Determines if fields include HTML or not ('Hospitalized by user' vs 'Hospitalized by user').
        :param limit: Number of results to return.
        :param to: Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
        :param from_: Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/events", build_params(self.get_events, locals()))

    async def get_faction(self, user_id: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your faction information or for a specific player.
        API key (Public).
        :param user_id: User id or user discord id.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/faction", build_params(self.get_faction, locals()))

    async def get_forumfeed(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get updates on your threads and posts.
        API key (Minimal).
        This selection returns data visible in 'Feed' section on forum page. Feed is sorted by timestamp descending. Only a maximum of 100 rows are returned.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/forumfeed", build_params(self.get_forumfeed, locals()))

    async def get_forumfriends(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get updates on your friends' activity.
        API key (Minimal).
        This selection returns data visible in 'Friends' section on forum page. Feed is sorted by timestamp descending. Only a maximum of 100 rows are returned.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/forumfriends", build_params(self.get_forumfriends, locals()))

    async def get_forumposts(self, user_id: int = None, striptags: bool = True, limit: int = 20, sort: SortOptions = None, to: int = None, from_: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your posts or for a specific player.
        API key (Public).
        Returns 20 posts per page.
        :param user_id: User id or user discord id.
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
        return await self.api.request("/user/forumposts", build_params(self.get_forumposts, locals()))

    async def get_forumsubscribedthreads(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get updates on threads you subscribed to.
        API key (Minimal).
        This selection returns data visible in 'Subscribed Threads' section on forum page. Threads are sorted in the same way as on site.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/forumsubscribedthreads", build_params(self.get_forumsubscribedthreads, locals()))

    async def get_forumthreads(self, user_id: int = None, limit: int = 20, sort: SortOptions = None, to: int = None, from_: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your threads or for a specific player.
        API key (Public).
        Returns up to 100 threads per page. The field 'new_posts' is also available, indicating the amount of unread posts with a Minimum API key (or higher).
        Specific Player - When requesting data for the key owner, a field 'new_posts' is also available, indicating the amount of unread posts. Minimum API key is required for that.
        :param user_id: User id or user discord id.
        :param limit: Number of results to return.
        :param sort: Sorted by the greatest timestamps.
        :param to: Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
        :param from_: Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/forumthreads", build_params(self.get_forumthreads, locals()))

    async def get_hof(self, user_id: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your hall of fame rankings or for a specific player.
        API key (Public).
        When requesting selection with Limited, Full or Custom key, battle_stats selection will be populated.
        Specific Player - The battle_stats selection will be populated only when requesting selection with Limited, Full or Custom key and for yourself.
        :param user_id: User id or user discord id.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/hof", build_params(self.get_hof, locals()))

    async def get_honors(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your achieved honors.
        API key (Public).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/honors", build_params(self.get_honors, locals()))

    async def get_icons(self, user_id: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your icons information or for a specific player.
        API key (Public).
        When requesting data for yourself with 'Custom', 'Limited' or 'Full' access keys, the response will be of type UserIconPrivate, otherwise UserIconPublic.
        :param user_id: User id or user discord id.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/icons", build_params(self.get_icons, locals()))

    async def get_itemmarket(self, offset: int = 0, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your item market listings for a specific item.
        API key (Limited).
        :param offset: Number of rows to skip before returning results.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/itemmarket", build_params(self.get_itemmarket, locals()))

    async def get_job(self, user_id: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your job information or for a specific player.
        API key (Public).
        :param user_id: User id or user discord id.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/job", build_params(self.get_job, locals()))

    async def get_jobpoints(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your jobpoints.
        API key (Public).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/jobpoints", build_params(self.get_jobpoints, locals()))

    async def get_jobranks(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your starter job positions.
        API key (Minimal).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/jobranks", build_params(self.get_jobranks, locals()))

    async def get_list(self, list_category: UserListCatOptions, striptags: bool = True, limit: int = 50, offset: int = None, sort: SortOptions = "ASC", timestamp: int = None, comment: str = None) -> dict:
        """
        Get your friends, enemies or targets list.
        API key (Limited).
        :param list_category: Select list type.
        :param striptags: Determines if fields include HTML or not ('Hospitalized by user' vs 'Hospitalized by user').
        :param limit: Number of results to return.
        :param offset: Number of rows to skip before returning results.
        :param sort: Sort rows from newest to oldest.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/list", build_params(self.get_list, locals()))

    async def get_log(self, log_id: list[int] = None, log_category_id: int = None, target_id: int = None, limit: int = 20, to: int = None, from_: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your logs.
        API key (Full).
        It's possible to pass a list of log ids or a log category id.
        :param log_id: Log ids.
        :param log_category_id: Log category id.
        :param target_id: Get logs where you interacted with a specific player by passing their player ID.
        :param limit: Number of results to return.
        :param to: Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
        :param from_: Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/log", build_params(self.get_log, locals()))

    async def get_medals(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your achieved medals.
        API key (Public).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/medals", build_params(self.get_medals, locals()))

    async def get_merits(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your merits.
        API key (Public).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/merits", build_params(self.get_merits, locals()))

    async def get_messages(self, limit: int = 20, sort: SortOptions = None, to: int = None, from_: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your messages.
        API key (Limited).
        :param limit: Number of results to return.
        :param sort: Sorted by the greatest timestamps.
        :param to: Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
        :param from_: Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/messages", build_params(self.get_messages, locals()))

    async def get_missions(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your current missions information.
        API key (Minimal).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/missions", build_params(self.get_missions, locals()))

    async def get_money(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your current wealth.
        API key (Public).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/money", build_params(self.get_money, locals()))

    async def get_newevents(self, striptags: bool = False, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your unseen events.
        API key (Limited).
        :param striptags: Determines if fields include HTML or not ('Hospitalized by user' vs 'Hospitalized by user').
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/newevents", build_params(self.get_newevents, locals()))

    async def get_newmessages(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your unseen messages.
        API key (Limited).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/newmessages", build_params(self.get_newmessages, locals()))

    async def get_notifications(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your notifications.
        API key (Minimal).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/notifications", build_params(self.get_notifications, locals()))

    async def get_organizedcrime(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your current ongoing organized crime.
        API key (Minimal).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/organizedcrime", build_params(self.get_organizedcrime, locals()))

    async def get_organizedcrimes(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get available slots for organized crimes with status 'Recruiting'.
        API key (Minimal).
        Unlike 'faction' -> 'crimes', this selection only shows empty slots, and only for crimes with the 'Recruiting' status.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/organizedcrimes", build_params(self.get_organizedcrimes, locals()))

    async def get_personalstats(self, user_id: int = None, stat_category: UserPrsnlStatsCatOptions = None, stat_keys: list[UserPrsnlStatsStatOptions] = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your personal stats or for a specific user.
        API key (Public).
         - UserPersonalStatsFull is returned only when this selection is requested with Limited, Full or Custom key access key.
         - UserPersonalStatsFullPublic is returned when the requested category is 'all'.
         - UserPersonalStatsPopular is returned when the requested category is 'popular'. Please try to use UserPersonalStatsPopular over UserPersonalStatsFullPublic wherever possible in order to reduce the server load.
         - Otherwise, UserPersonalStatsCategory is returned for the matched category.
         - Historical stats can be fetched via 'stat' query parameter. It's only possible to pass up to 10 historical stats at once (the rest is trimmed). When requesting historical stats the response will be of type UserPersonalStatsHistoric.
         - Use 'timestamp' query parameter to get historical stats at the certain point in time. It's possible some historical stats didn't exist at the given timestamp, and for such stats you will not receive anything back.
        Specific Player:
         - It's possible to request specific stats via 'stat' parameter. In this case the response will vary depending on the stats requested. Private stats are still available only to the key owner (with Limited or higher key).
         - Additionally, historical stats can also be fetched via 'stat' query parameter, but 'timestamp' parameter must be provided as well. It's only possible to pass up to 10 historical stats at once (the rest is trimmed). When requesting historical stats the response will be of type UserPersonalStatsHistoric.
        :param user_id: User id or user discord id.
        :param stat_category: Personal stat category.
        :param stat_keys: Stat names (10 maximum). Used to fetch historical stat values.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/personalstats", build_params(self.get_personalstats, locals()))

    async def get_profile(self, user_id: int = None, striptags: bool = True, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your profile information or for a specific player.
        API key (Public).
        :param user_id: User id or user discord id.
        :param striptags: Determines if fields include HTML or not ('Hospitalized by user' vs 'Hospitalized by user').
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/profile", build_params(self.get_profile, locals()))

    async def get_properties(self, user_id: int = None, property_filters: UserPropertiesFiltersOptions = None, limit: int = 20, offset: int = 0, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your own properties or for a specific user.
        API key (Public).
        Extended responses are available when requesting the data with Limited or higher access keys.
        Specific Player - Extended responses are available when requesting the data with Limited or higher access keys for yourself or your spouse.
        :param user_id: User id or user discord id.
        :param property_filters: It's possible to use this query parameter to filter properties by the key owner or their spouse.
        :param limit: Number of results to return.
        :param offset: Number of rows to skip before returning results.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/properties", build_params(self.get_properties, locals()))

    async def get_property(self, user_id: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your current property or for a specific user.
        API key (Public).
        :param user_id: User id or user discord id.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/property", build_params(self.get_property, locals()))

    async def get_races(self, race_category: RaceCatOptions = None, limit: int = 20, sort: SortOptions = None, to: int = None, from_: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get user races.
        API key (Minimal).
        :param race_category: Category of races returned.
        :param limit: Number of results to return.
        :param sort: Sorted by the greatest timestamps.
        :param to: Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
        :param from_: Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/races", build_params(self.get_races, locals()))

    async def get_racingrecords(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your current racing records.
        API key (Minimal).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/racingrecords", build_params(self.get_racingrecords, locals()))

    async def get_refills(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your refills information.
        API key (Minimal).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/refills", build_params(self.get_refills, locals()))

    async def get_reports(self, report_category: ReportCatOptions = None, target_id: int = None, limit: int = 20, offset: int = 0, sort: SortOptions = "DESC", timestamp: int = None, comment: str = None) -> dict:
        """
        Get your reports.
        API key (Limited).
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
        return await self.api.request("/user/reports", build_params(self.get_reports, locals()))

    async def get_revives(self, attack_filters: list[AttackFiltersOptions] = None, striptags: bool = True, limit: int = 20, sort: SortOptions = None, to: int = None, from_: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your detailed revives.
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
        return await self.api.request("/user/revives", build_params(self.get_revives, locals()))

    async def get_revivesfull(self, attack_filters: list[AttackFiltersOptions] = None, striptags: bool = True, limit: int = 20, sort: SortOptions = None, to: int = None, from_: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your simplified revives.
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
        return await self.api.request("/user/revivesFull", build_params(self.get_revivesfull, locals()))

    async def get_skills(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your skills.
        API key (Public).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/skills", build_params(self.get_skills, locals()))

    async def get_stocks(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your stocks.
        API key (Limited).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/stocks", build_params(self.get_stocks, locals()))

    async def get_travel(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your travel information.
        API key (Minimal).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/travel", build_params(self.get_travel, locals()))

    async def get_virus(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your virus information.
        API key (Minimal).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/virus", build_params(self.get_virus, locals()))

    async def get_weaponexp(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your weapon experience information.
        API key (Minimal).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/weaponexp", build_params(self.get_weaponexp, locals()))

    async def get_workstats(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get your working stats.
        API key (Public).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/workstats", build_params(self.get_workstats, locals()))

    async def get_lookup(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get all available user selections.
        API key (Public).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/lookup", build_params(self.get_lookup, locals()))

    async def get_timestamp(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get current server time.
        API key (Public).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/user/timestamp", build_params(self.get_timestamp, locals()))