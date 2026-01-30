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

from .type_hints import SortOptions, MrktBazaarCatOptions, MrktItemBonusOptions

if TYPE_CHECKING:
    from .torn_api_wrapper import TornAPIWrapper

class Market:
    def __init__(self, api: TornAPIWrapper):
        self.api = api

    def get_auctionhouselisting(self, listing_id: int, timestamp: int = None, comment: str = None):
        return self.api.request("/market/auctionhouselisting", self.api.build_params(self.get_auctionhouselisting, locals()))

    def get_auctionhouse(self, item_id: int = None, limit: int = 20, sort: SortOptions = None, to: int = None, from_: int = None, timestamp: int = None, comment: str = None):
        return self.api.request("/market/auctionhouse", self.api.build_params(self.get_auctionhouse, locals()))

    def get_bazaar(self, item_id: int = None, bazaar_category: MrktBazaarCatOptions = None, timestamp: int = None, comment: str = None):
        return self.api.request("/market/bazaar", self.api.build_params(self.get_bazaar, locals()))

    def get_itemmarket(self, item_id: int, bonus: MrktItemBonusOptions = None, limit: int = 20, offset: int = 0, timestamp: int = None, comment: str = None):
        return self.api.request("/market/itemmarket", self.api.build_params(self.get_itemmarket, locals()))

    def get_properties(self, property_type_id: int, limit: int = 20, offset: int = 0, sort: SortOptions = None, timestamp: int = None, comment: str = None):
        return self.api.request("/market/properties", self.api.build_params(self.get_properties, locals()))

    def get_rentals(self, property_type_id: int, limit: int = 20, offset: int = 0, sort: SortOptions = None, timestamp: int = None, comment: str = None):
        return self.api.request("/market/rentals", self.api.build_params(self.get_rentals, locals()))

    def get_lookup(self, timestamp: int = None, comment: str = None):
        return self.api.request("/market/lookup", self.api.build_params(self.get_lookup, locals()))

    def get_timestamp(self, timestamp: int = None, comment: str = None):
        return self.api.request("/market/timestamp", self.api.build_params(self.get_timestamp, locals()))
