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

from ..type_hints import SortOptions

if TYPE_CHECKING:
    from ..torn_api_wrapper import TornAPIWrapper

class Forum:
    """
    Forum API endpoints.
    """

    def __init__(self, api: TornAPIWrapper):
        self.api = api

    def get_categories(self, timestamp: int = None, comment: str = None):
        """
        Get publicly available forum categories.
        API key (Public).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/forum/categories", self.api.build_params(self.get_categories, locals()))

    def get_posts(self, thread_id: int, striptags: bool = True, offset: int = None, sort: SortOptions = None, to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        """
        Get specific forum thread posts.
        API key (Public).
        Returns 20 posts per page for a specific thread.
        By default, it uses 'offset', but it's possible to filter posts with 'from' & 'to' parameters.
        :param thread_id: Thread id.
        :param striptags: Determines if fields include HTML or not ('Hospitalized by user' vs 'Hospitalized by user').
        :param offset: Offset used for paging.
        :param sort: Sorted by the greatest timestamps.
        :param to: Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
        :param from_: Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/forum/posts", self.api.build_params(self.get_posts, locals()))

    def get_thread(self, thread_id: int, timestamp: int = None, comment: str = None):
        """
        Get specific thread details.
        API key (Public).
        Contains details of a thread including topic content and poll (if any).
        :param thread_id: Thread id.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/forum/thread", self.api.build_params(self.get_thread, locals()))

    def get_threads(self, category_ids: list[int] = None, limit : int = 100, sort: SortOptions = None, to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        """
        Get threads across all forum categories or for specific public forum category or categories.
        API key (Public).
        :param category_ids: Category id or a list of category ids.
        :param limit: Number of results to return.
        :param sort: Sorted by the greatest timestamps.
        :param to: Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time.
        :param from_: Timestamp that sets the lower limit for the data returned. Data returned will be after this time.
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/forum/threads", self.api.build_params(self.get_threads, locals()))

    def get_lookup(self, timestamp: int = None, comment: str = None):
        """
        Get all available forum selections.
        API key (Public).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/forum/lookup", self.api.build_params(self.get_lookup, locals()))

    def get_timestamp(self, timestamp: int = None, comment: str = None) -> dict:
        """
        Get current server time.
        API key (Public).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/forum/timestamp", self.api.build_params(self.get_timestamp, locals()))
