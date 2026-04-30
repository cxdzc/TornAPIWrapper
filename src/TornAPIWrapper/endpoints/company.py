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

if TYPE_CHECKING:
    from ..client import TornAPIWrapper

class Company:
    """
    Company API endpoints.
    """

    def __init__(self, api: TornAPIWrapper):
        self.api = api

    def get_applications(self, timestamp: int = None, comment: str = None):
        """
        Get your company's applications.
        API key (Limited).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/company/applications", build_params(self.get_applications, locals()))

    def get_employees(self, company_id: int = None, striptags: bool = True, timestamp: int = None, comment: str = None):
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
        return self.api.request("/company/employees", build_params(self.get_employees, locals()))

    def get_profile(self, company_id: int = None, striptags: bool = True, timestamp: int = None, comment: str = None):
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
        return self.api.request("/company/profile", build_params(self.get_profile, locals()))

    def get_stock(self, timestamp: int = None, comment: str = None):
        """
        Get your company's stock.
        API key (Limited).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/company/stock", build_params(self.get_stock, locals()))

    def get_lookup(self, timestamp: int = None, comment: str = None):
        """
        API key (Public).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/company/lookup", build_params(self.get_lookup, locals()))

    def get_timestamp(self, timestamp: int = None, comment: str = None):
        """
        Get current server time.
        API key (Public).
        :param timestamp: Timestamp to bypass cache.
        :param comment: Comment for your tool/service/bot/website to be visible in the logs.
        :return: API response data.
        :rtype: dict
        """
        return self.api.request("/company/timestamp", build_params(self.get_timestamp, locals()))