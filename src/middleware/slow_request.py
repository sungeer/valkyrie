import time

from loguru import logger

from src import settings


class SlowRequestMiddleware:

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope['type'] != 'http':
            await self.app(scope, receive, send)
            return

        start = time.perf_counter()
        status = None

        async def send_with_status(message):
            nonlocal status
            if message['type'] == 'http.response.start':
                status = message['status']
            await send(message)

        try:
            await self.app(scope, receive, send_with_status)
        except Exception:
            status = 500
            raise
        finally:
            cost_ms = (time.perf_counter() - start) * 1000

            if cost_ms >= settings.SLOW_REQUEST_MS:
                logger.warning(
                    '[slow request] method={}, path={}, status={}, cost={:.0f}ms',
                    scope['method'], scope['path'], status, cost_ms,
                )
