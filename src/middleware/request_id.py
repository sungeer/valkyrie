import uuid

from starlette.datastructures import MutableHeaders

from src.core.ctx import request_id_var


class RequestIDMiddleware:

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope['type'] != 'http':
            await self.app(scope, receive, send)
            return

        request_id: str = uuid.uuid4().hex[:18]

        token = request_id_var.set(request_id)
        scope.setdefault('state', {})['request_id'] = request_id

        async def send_with_request_id(message):
            if message['type'] == 'http.response.start':
                MutableHeaders(scope=message)['X-Request-ID'] = request_id
            await send(message)

        try:
            await self.app(scope, receive, send_with_request_id)
        finally:
            request_id_var.reset(token)
