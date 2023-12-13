"""
MIT License

Copyright (c) 2023-Present cxdzc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

class TornApiErrorHandler:
    """
    Handle Torn API errors.

    Methods:
    - api_error_handler(response) -> dict: Handle Torn API errors.
    """
    error_codes = {0: {"Unknown error": "Unhandled error, should not occur."},
       1: {"Key is empty": "Private key is empty in current request."},
       2: {"Incorrect Key": "Private key is wrong/incorrect format."},
       3: {"Wrong type": "Requesting an incorrect basic type."},
       4: {"Wrong fields": "Requesting incorrect selection fields."},
       5: {"Too many requests": "Requests are blocked for a small period of time because of too many requests per user (max 100 per minute)."},
       6: {"Incorrect ID": "Wrong ID value."},
       7: {"Incorrect ID-entity relation": "A requested selection is private (For example, personal data of another user / faction)."},
       8: {"IP block": "Current IP is banned for a small period of time because of abuse."},
       9: {"API disabled": "Api system is currently disabled."},
       10: {"Key owner is in federal jail": "Current key can't be used because owner is in federal jail."},
       11: {"Key change error": "You can only change your API key once every 60 seconds."},
       12: {"Key read error": "Error reading key from Database."},
       13: {"The key is temporarily disabled due to owner inactivity": "The key owner hasn't been online for more than 7 days."},
       14: {"Daily read limit reached": "Too many records have been pulled today by this user from our cloud services."},
       15: {"Temporary error": "An error code specifically for testing purposes that has no dedicated meaning."},
       16: {"Access level of this key is not high enough": "A selection is being called of which this key does not have permission to access."},
       17: {"Backend error occurred": "Please try again."}}

    def api_error_handler(self, response) -> dict:
        """
        Handle Torn API errors.
        :param response: Response object from `api_request`.
        :return: Json-encoded data.
        """
        if response.status_code == 200:
            data = response.json()
            if "error" in data:
                error_code = data["error"]["code"]
                if error_code in [0, 1, 2, 5, 8, 9, 10, 11, 12, 13, 14, 16, 17]:
                    raise Exception(f"API Error Code {error_code}: {self.error_codes[error_code]}")
                else:
                    error, description = list(self.error_codes[error_code].items())[0]
                    data = {"error": {"code": error_code, "error": error, "description": description}}
            return data
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")