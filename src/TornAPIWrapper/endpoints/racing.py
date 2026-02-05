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

from ..type_hints import SortOptions, RaceCatOptions, RaceCarCatOptions

if TYPE_CHECKING:
    from ..torn_api_wrapper import TornAPIWrapper

class Racing:
    """
    Racing API endpoints.
    """

    def __init__(self, api: TornAPIWrapper):
        self.api = api

    def get_cars(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get cars and their racing stats.
        API key (Public).
        Returns the stat details about racing cars.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/racing/cars", self.api.build_params(self.get_cars, locals()))

    def get_carupgrades(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get all possible car upgrades.
        API key (Public).
        Returns the details about all possible car upgrades.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/racing/carupgrades", self.api.build_params(self.get_carupgrades, locals()))

    def get_races(self, race_category: RaceCatOptions = None, limit: int = 100, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None) -> dict:
        """
        Get races.
        API key (Public).
        Returns a list of races, ordered by race start timestamp.
        :param race_category: Category of races returned.
        :param limit: Number of results to return.
        :param sort: Sorted by the greatest timestamps.
        :param to: Timestamp that sets the upper limit for the data returned.
        :param from_: Timestamp that sets the lower limit for the data returned.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/racing/races", self.api.build_params(self.get_races, locals()))

    def get_race(self, race_id: int, timestamp: int = None, comment: str = None) -> dict:
        """
        Get specific race details.
        API key (Public).
        Returns the details of a race.
        :param race_id: Race id.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/racing/race", self.api.build_params(self.get_race, locals()))

    def get_records(self, track_id: int, car_category: RaceCarCatOptions, timestamp: int = None, comment: str = None) -> dict:
        """
        Get track records.
        API key (Public).
        Returns a list of 5 best lap records for the chosen track and car class.
        :param track_id: Track id.
        :param car_category: Car class.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/racing/records", self.api.build_params(self.get_records, locals()))

    def get_tracks(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get race tracks and descriptions.
        API key (Public).
        Returns the details about racing tracks.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/racing/tracks", self.api.build_params(self.get_tracks, locals()))

    def get_lookup(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get all available racing selections.
        API key (Public).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/racing/lookup", self.api.build_params(self.get_lookup, locals()))

    def get_timestamp(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get current server time.
        API key (Public).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/racing/timestamp", self.api.build_params(self.get_timestamp, locals()))
