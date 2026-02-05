import inspect
from typing import Callable

from ..params.map import parameter_map

def build_local_params(method_request: Callable, local_vars: dict) -> dict | None:
    """
    Extracts the arguments passed to `method_request` and returns them as a clean dictionary ready for further processing.
    :param method_request: The `TornAPIWrapper` method.
    :param local_vars: A dictionary containing the `method_request` scope's local variables.
    :return: A sterilized dictionary for further processing or None.
    :rtype: dict | None
    """
    return {param: local_vars[param] for param in inspect.signature(method_request).parameters if local_vars[param] is not None and param != "self"} or None

def build_params(method_request: Callable, local_vars: dict) -> dict | None:
    """
    Builds Torn API compatible query parameters from wrapper method arguments.
    :param method_request: The `TornAPIWrapper` method.
    :param local_vars: A dictionary containing the `method_request` scope's local variables.
    :return: A formatted dictionary of API query parameters | None.
    :rtype: dict | None
    """
    local_params = build_local_params(method_request, local_vars)
    if local_params is None:
        return None
    api_params = {}
    for param, value in local_params.items():
        if isinstance(value, list) and value: #Format `array[string]` or `array[int]` query for the API e.g. `get_attacks()`.
            value = ",".join(map(str, value))
        elif param == "timestamp" and isinstance(value, int): #Format Python timestamp[int] to API friendly timestamp[str].
            value = str(value)
        elif param == "striptags" and isinstance(value, bool): #Format Python striptags[bool] to API friendly striptags[str].
            value = str(value).lower()
        api_param_var = parameter_map.get(param, param) #Replace param such as `stat_category` with `cat` for the API. The wrapper param is not `cat` since type hinting is not clear to the user.
        api_params[api_param_var] = value
    return api_params or None