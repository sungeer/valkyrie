from json import JSONDecodeError

from src.utils.api_errors import ParamError


async def require_body(request):
    try:
        data = await request.json()
    except JSONDecodeError:
        raise ParamError('request body is not valid JSON')
    if not isinstance(data, dict):
        raise ParamError('request body must be a JSON object')
    return data


# 该字段必须存在
def require_int(data, key):
    value = data.get(key)
    if value is None:
        raise ParamError(f'{key} is required')
    if not isinstance(value, int) or isinstance(value, bool):
        raise ParamError(f'{key} must be an integer')
    return value


def require_str(data, key):
    value = data.get(key)
    if value is None:
        raise ParamError(f'{key} is required')
    if not isinstance(value, str):
        raise ParamError(f'{key} must be a string')
    if not value.strip():
        raise ParamError(f'{key} cannot be empty')
    return value


# 该字段可以不存在
def optional_int(data, key, default=None):
    value = data.get(key)
    if value is None:
        return default
    if not isinstance(value, int) or isinstance(value, bool):
        raise ParamError(f'{key} must be an integer')
    return value


def optional_str(data, key, default=None):
    value = data.get(key)
    if value is None:
        return default
    if not isinstance(value, str):
        raise ParamError(f'{key} must be a string')
    if not value.strip():
        raise ParamError(f'{key} cannot be empty')
    return value
