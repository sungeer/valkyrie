import json
from typing import Any

from starlette.responses import JSONResponse

from src.utils.serial import JSONExtendEncoder


class APIResponse(JSONResponse):
    def render(self, content: Any) -> bytes:
        return json.dumps(
            content,
            cls=JSONExtendEncoder,
            ensure_ascii=False,
            allow_nan=False,
            indent=None,
            separators=(',', ':'),
        ).encode('utf-8')


def ok(data=None, http_code=200) -> APIResponse:
    return APIResponse(
        {
            'success': True,
            'data': data
        },
        status_code=http_code
    )


def fail(message: str, http_code: int, code: str, headers=None) -> APIResponse:
    return APIResponse(
        {
            'success': False,
            'code': code,
            'message': message
        },
        status_code=http_code,
        headers=headers
    )
