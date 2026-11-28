import time

from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware

from src import settings


class SlowRequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.perf_counter()
        response = None

        try:
            response = await call_next(request)
            return response
        finally:
            cost_ms = (time.perf_counter() - start) * 1000

            if cost_ms >= settings.SLOW_REQUEST_MS:
                logger.warning(
                    '[slow request] method={}, path={}, status={}, cost={:.0f}ms',
                    request.method, request.url.path,
                    response.status_code if response else 500,
                    cost_ms,
                )
