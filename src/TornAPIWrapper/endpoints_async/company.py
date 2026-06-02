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
from ..type_hints import CpnyNewsCatOptions, SortOptions

if TYPE_CHECKING:
    from ..client_async import TornAPIWrapperAsync

class Company:
    """
    Company API endpoints.
    """

    def __init__(self, api: TornAPIWrapperAsync):
        self.api = api

    async def get_applications(self, timestamp: int = None, comment: str = None):
        """
        Get your company's applications.
        API key (Limited).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/company/applications", build_params(self.get_applications, locals()))

    async def get_employees(self, company_id: int = None, striptags: bool = True, timestamp: int = None, comment: str = None):
        """
        Get my company's employees.
        API key (Public).
        When using Limited, Custom or Full access API keys, the response will be of type CompanyEmployeeExtended, otherwise it will be of type CompanyEmployee.
        :param company_id: Company id.
        :param striptags: Determines if fields include HTML or not ('Hospitalized by user' vs 'Hospitalized by user').
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/company/employees", build_params(self.get_employees, locals()))

    async def get_news(self, news_category: CpnyNewsCatOptions, striptags: bool = False, limit: int = 100, sort: SortOptions = "DESC", to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        """
        Get your company's news details.
        API key (Minimal).
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
        return await self.api.request("/company/news", build_params(self.get_news, locals()))

    async def get_companies(self, company_type_id: int, striptags: bool = True, limit: int = 20, offset: int = None, timestamp: int = None, comment: str = None):
        """
        Get a list of companies for a specific company type.
        API key (Public).
        :param company_type_id: Company type id.
        :param limit: Number of results to return.
        :param offset: Number of rows to skip before returning results.
        :param striptags: Determines if fields include HTML or not ('Hospitalized by user' vs 'Hospitalized by user').
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/company/companies", build_params(self.get_companies, locals()))

    async def get_profile(self, company_id: int = None, striptags: bool = True, timestamp: int = None, comment: str = None):
        """
        Get a company's profile.
        API key (Public).
        When using Limited, Custom or Full access API keys, the response will be of type CompanyEmployeeExtended, otherwise it will be of type CompanyEmployee.
        :param company_id: Company id.
        :param striptags: Determines if fields include HTML or not ('Hospitalized by user' vs 'Hospitalized by user').
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/company/profile", build_params(self.get_profile, locals()))

    async def get_search(self, company_name: str = None, filters: list[str] = None, limit: int = 20, offset: int = 0, timestamp: int = None, comment: str = None) -> dict: #1F4A9 endpoint
        """
        Search companies by name or other criteria.
        API key (Public).
        This selection is standalone and cannot be used together with other selections.
        :param company_name: Name to search for.
        :param filters: A filtering query parameter allowing a comma-separated list of filters.
        :param limit: Number of results to return.
        :param offset: Number of rows to skip before returning results.
        :param timestamp: Timestamp to bypass cache or get the data in specific point in time.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/company/search", build_params(self.get_search, locals()))

    async def get_snapshot(self, timestamp: int = None, comment: str = None):
        """
        Get daily companies snapshot CSV.
        API key (Public).
        Returns a CSV daily snapshot of companies.
        This selection is standalone and cannot be used together with other selections.
        CSV columns: id, name, created_at, days_old, image, type, rating, director_id, employees_hired, employees_capacity, daily_income, daily_customers, weekly_income, weekly_customers, applications_allowed
        :param timestamp: Timestamp to bypass cache or get the data in specific point in time.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/company/snapshot", build_params(self.get_snapshot, locals()))

    async def get_stock(self, timestamp: int = None, comment: str = None):
        """
        Get your company's stock.
        API key (Limited).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/company/stock", build_params(self.get_stock, locals()))

    async def get_lookup(self, timestamp: int = None, comment: str = None):
        """
        API key (Public).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/company/lookup", build_params(self.get_lookup, locals()))

    async def get_timestamp(self, timestamp: int = None, comment: str = None):
        """
        Get current server time.
        API key (Public).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return await self.api.request("/company/timestamp", build_params(self.get_timestamp, locals()))