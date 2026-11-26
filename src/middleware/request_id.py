import time
import uuid

from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware

from src import settings
from src.core.ctx import request_id_var


class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request_id: str = uuid.uuid4().hex[:18]

        token = request_id_var.set(request_id)

        request.state.request_id = request_id

        start = time.perf_counter()
        status = None

        try:
            response = await call_next(request)
            status = response.status_code
        finally:
            cost_ms = (time.perf_counter() - start) * 1000

            if cost_ms >= settings.SLOW_REQUEST_MS:
                logger.warning(
                    '[slow request] method={}, path={}, status={}, cost={:.0f}ms',
                    request.method, request.url.path, status, cost_ms,
                )

            request_id_var.reset(token)

        response.headers['X-Request-ID'] = request_id
        return response
