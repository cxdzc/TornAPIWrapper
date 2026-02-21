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

__author__ = "cxdzc"
__copyright__ = "Copyright 2023-Present cxdzc"
__license__ = "MIT"
__title__ = "TornAPIWrapper"
__version__ = "2.1.1"
__patch__ = "19.02.2026"

from .errors import (
    WrapperError,
    UnhandledAPIError,
    APIError,
    UnknownError,
    EmptyKey,
    InvalidKey,
    WrongType,
    WrongFields,
    RateLimit,
    InvalidId,
    InvalidRelation,
    IpBlocked,
    ApiDisabled,
    KeyOwnerJailed,
    KeyChangeLimit,
    KeyReadFailed,
    KeyInactive,
    DailyLimit,
    TemporaryFailure,
    PermissionDenied,
    BackendFailure,
    KeyPaused,
    MigrationRequired,
    RaceNotFinished,
    InvalidCategory,
    ApiV1Only,
    ApiV2Only,
    TemporarilyClosed,
    InvalidStat,
    InvalidParameterCombination,
    MigrationRequiredOC2,
    InvalidLogId,
    InvalidInteractionLogCategory,
)
from .client import TornAPIWrapper
from .client_async import TornAPIWrapperAsync

__all__ = [
    "TornAPIWrapper",
    "TornAPIWrapperAsync",

    "WrapperError",
    "UnhandledAPIError",

    "APIError",
    "UnknownError",
    "EmptyKey",
    "InvalidKey",
    "WrongType",
    "WrongFields",
    "RateLimit",
    "InvalidId",
    "InvalidRelation",
    "IpBlocked",
    "ApiDisabled",
    "KeyOwnerJailed",
    "KeyChangeLimit",
    "KeyReadFailed",
    "KeyInactive",
    "DailyLimit",
    "TemporaryFailure",
    "PermissionDenied",
    "BackendFailure",
    "KeyPaused",
    "MigrationRequired",
    "RaceNotFinished",
    "InvalidCategory",
    "ApiV1Only",
    "ApiV2Only",
    "TemporarilyClosed",
    "InvalidStat",
    "InvalidParameterCombination",
    "MigrationRequiredOC2",
    "InvalidLogId",
    "InvalidInteractionLogCategory",
]
