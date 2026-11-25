"""应用层 HTTP 异常
用于"请求-响应"流程
"""

from src.utils.error_codes import ErrCode


class ApiError(Exception):
    """所有应用异常的基类"""
    code = ErrCode.UNKNOWN
    http_code = 200

    def __init__(self, msg: str, code: str | None = None):
        self.msg = msg
        if code is not None:
            self.code = code
        super().__init__(self.msg)


class BizError(ApiError):
    """业务失败
    HTTP 200 + success=false
    比如 库存不足 用户状态异常 资源不存在
    """
    code = ErrCode.BIZ_ERROR


class ParamError(ApiError):
    """400
    入参错误
    请求本身不合法
    服务端未执行业务逻辑
    """
    code = ErrCode.PARAM_ERROR
    http_code = 400


class UnavailableError(ApiError):
    """503
    上游依赖不可用
    """
    code = ErrCode.UPSTREAM_UNAVAILABLE
    http_code = 503


class UnauthorizedError(ApiError):
    """401
    用户认证
    """
    code = ErrCode.UNAUTHORIZED
    http_code = 401


class ForbiddenError(ApiError):
    """403
    用户权鉴
    """
    code = ErrCode.FORBIDDEN
    http_code = 403
