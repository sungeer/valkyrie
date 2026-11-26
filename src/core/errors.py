from loguru import logger
from starlette.exceptions import HTTPException
from starlette.requests import ClientDisconnect

from src.utils.error_codes import ErrCode
from src.utils.api_errors import ApiError
from src.core.response import fail


# 业务失败
async def api_error(request, exc):
    err_msg = exc.msg
    http_code = exc.http_code
    code = exc.code

    logger.info(
        '[app error] method={}, path={}, http_code={}, code={}, msg={}',
        request.method, request.url.path, http_code, code, err_msg,
    )
    return fail(err_msg, http_code, code)


# 客户端断开
async def client_disconnect(request, exc):  # noqa
    err_msg = 'client closed request'
    http_code = 499
    code = ErrCode.CLIENT_CLOSED

    logger.info('[client closed] path={}', request.url.path)
    return fail(err_msg, http_code, code)


# 所有未显式注册的 400 413 416 等
async def http_error(request, exc):
    err_msg = exc.detail
    http_code = exc.status_code
    code = f'HTTP_{http_code}'

    logger.info(
        '[http error] method={}, path={}, http_code={}, msg={}',
        request.method, request.url.path, http_code, err_msg,
    )
    return fail(err_msg, http_code, code)


# 内部错误 500
async def server_error(request, exc):  # noqa
    err_msg = 'server error'
    http_code = 500
    code = ErrCode.SERVER_ERROR

    logger.exception('[server error]path={}', request.url.path)

    request_id = getattr(request.state, 'request_id', None)
    headers = {'X-Request-ID': request_id} if request_id else None
    return fail(err_msg, http_code, code, headers)


exception_handlers = {
    ApiError: api_error,
    ClientDisconnect: client_disconnect,
    HTTPException: http_error,
    Exception: server_error,
}
