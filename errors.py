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

#Torn Wrapper Errors
class WrapperError(Exception):
    """
    Base class for all TornAPIWrapper errors.
    """
    pass

class UnhandledAPIError(WrapperError):
    """
    An API error code was received that is not yet implemented by TornAPIWrapper.
    Please open an issue at https://github.com/cxdzc/TornAPIWrapper/issues or
    contact AfricanChild [3157295], including details on how you encountered this error.
    """
    pass

#Torn API Errors
class APIError(Exception):
    """
    Base class for all API-related errors.
    """
    def __init__(self, message: str, code: int):
        super().__init__(message)
        self.code = code

class UnknownError(APIError):
    """
    0
    Unknown error
    Unhandled error, should not occur.
    """
    pass

class EmptyKey(APIError):
    """
    1
    Key is empty
    Private key is empty in current request.
    """
    pass

class InvalidKey(APIError):
    """
    2
    Incorrect Key
    Private key is wrong/incorrect format.
    """
    pass

class WrongType(APIError):
    """
    3
    Wrong type
    Requesting an incorrect basic type.
    """
    pass

class WrongFields(APIError):
    """
    4
    Wrong fields
    Requesting incorrect selection fields.
    """
    pass

class RateLimit(APIError):
    """
    5
    Too many requests
    Requests are blocked for a small period of time because of too many requests per user (max 100 per minute).
    """
    pass

class InvalidId(APIError):
    """
    6
    Incorrect ID
    Wrong ID value.
    """
    pass

class InvalidRelation(APIError):
    """
    7
    Incorrect ID-entity relation
    A requested selection is private (For example, personal data of another user / faction).
    """
    pass

class IpBlocked(APIError):
    """
    8
    IP block
    Current IP is banned for a small period of time because of abuse.
    """
    pass

class ApiDisabled(APIError):
    """
    9
    API disabled
    Api system is currently disabled.
    """
    pass

class KeyOwnerJailed(APIError):
    """
    10
    Key owner is in federal jail
    Current key can't be used because owner is in federal jail.
    """
    pass

class KeyChangeLimit(APIError):
    """
    11
    Key change error
    You can only change your API key once every 60 seconds.
    """
    pass

class KeyReadFailed(APIError):
    """
    12
    Key read error
    Error reading key from Database.
    """
    pass

class KeyInactive(APIError):
    """
    13
    The key is temporarily disabled due to owner inactivity
    The key owner hasn't been online for more than 7 days.
    """
    pass

class DailyLimit(APIError):
    """
    14
    Daily read limit reached
    Too many records have been pulled today by this user from our cloud services.
    """
    pass

class TemporaryFailure(APIError):
    """
    15
    Temporary error
    An error code specifically for testing purposes that has no dedicated meaning.
    """
    pass

class PermissionDenied(APIError):
    """
    16
    Access level of this key is not high enough
    A selection is being called of which this key does not have permission to access.
    """
    pass

class BackendFailure(APIError):
    """
    17
    Backend error occurred, please try again.
    """
    pass

class KeyPaused(APIError):
    """
    18
    API key has been paused by the owner.
    """
    pass

class MigrationRequired(APIError):
    """
    19
    Must be migrated to crimes 2.0.
    """
    pass

class RaceNotFinished(APIError):
    """
    20
    Race not yet finished.
    """
    pass

class InvalidCategory(APIError):
    """
    21
    Incorrect category
    Wrong cat value.
    """
    pass

class ApiV1Only(APIError):
    """
    22
    This selection is only available in API v1.
    """
    pass

class ApiV2Only(APIError):
    """
    23
    This selection is only available in API v2.
    """
    pass

class TemporarilyClosed(APIError):
    """
    24
    Closed temporarily.
    """
    pass

class InvalidStat(APIError):
    """
    25
    Invalid stat requested.
    """
    pass

class InvalidParameterCombination(APIError):
    """
    26
    Only category or stats can be requested
    """
    pass

class MigrationRequiredOC2(APIError):
    """
    27
    Must be migrated to organized crimes 2.0.
    """
    pass


class InvalidLogId(APIError):
    """
    28
    Incorrect log ID.
    """
    pass


class InvalidInteractionLogCategory(APIError):
    """
    29
    Category selection is not available for interaction logs.
    """
    pass

class TornAPIErrorHandler:
    api_error_codes = {
        0: (UnknownError, "Unknown error - Unhandled error, should not occur."),
        1: (EmptyKey, "Key is empty - Private key is empty in current request."),
        2: (InvalidKey, "Incorrect Key - Private key is wrong/incorrect format."),
        3: (WrongType, "Wrong type - Requesting an incorrect basic type."),
        4: (WrongFields, "Wrong fields - Requesting incorrect selection fields."),
        5: (RateLimit, "Too many requests - Requests are blocked for a small period of time because of too many requests per user (max 100 per minute)."),
        6: (InvalidId, "Incorrect ID - Wrong ID value."),
        7: (InvalidRelation, "Incorrect ID-entity relation - A requested selection is private (For example, personal data of another user / faction)."),
        8: (IpBlocked, "IP block - Current IP is banned for a small period of time because of abuse."),
        9: (ApiDisabled, "API disabled - Api system is currently disabled."),
        10: (KeyOwnerJailed, "Key owner is in federal jail - Current key can't be used because owner is in federal jail."),
        11: (KeyChangeLimit, "Key change error - You can only change your API key once every 60 seconds."),
        12: (KeyReadFailed, "Key read error - Error reading key from Database."),
        13: (KeyInactive, "The key is temporarily disabled due to owner inactivity - The key owner hasn't been online for more than 7 days."),
        14: (DailyLimit, "Daily read limit reached - Too many records have been pulled today by this user from our cloud services."),
        15: (TemporaryFailure, "Temporary error - An error code specifically for testing purposes that has no dedicated meaning."),
        16: (PermissionDenied, "Access level of this key is not high enough - A selection is being called of which this key does not have permission to access."),
        17: (BackendFailure, "Backend error occurred, please try again."),
        18: (KeyPaused, "API key has been paused by the owner."),
        19: (MigrationRequired, "Must be migrated to crimes 2.0."),
        20: (RaceNotFinished, "Race not yet finished."),
        21: (InvalidCategory, "Incorrect category - Wrong cat value."),
        22: (ApiV1Only, "This selection is only available in API v1."),
        23: (ApiV2Only, "This selection is only available in API v2."),
        24: (TemporarilyClosed, "Closed temporarily."),
        25: (InvalidStat, "Invalid stat requested."),
        26: (InvalidParameterCombination, "Only category or stats can be requested"),
        27: (MigrationRequiredOC2, "Must be migrated to organized crimes 2.0."),
        28: (InvalidLogId, "Incorrect log ID."),
        29: (InvalidInteractionLogCategory, "Category selection is not available for interaction logs."),
    }

    def raise_code(self, error_code: int):
        error = self.api_error_codes.get(error_code)
        if error is None:
            raise UnhandledAPIError("An API error code was received that is not yet implemented by TornAPIWrapper.\nPlease open an issue at https://github.com/cxdzc/TornAPIWrapper/issues or contact AfricanChild [3157295], including details on how you encountered this error.")
        api_error_class, message = error
        raise api_error_class(message=message, code=error_code)