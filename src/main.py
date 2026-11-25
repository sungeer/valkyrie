from starlette.applications import Starlette

from src.core.lifespan import lifespan
from src.core.errors import exception_handlers
from src.middleware.stack import middlewares
from src.routes import routes


def create_app():
    app = Starlette(
        routes=routes,
        middleware=middlewares,
        exception_handlers=exception_handlers,
        lifespan=lifespan
    )
    return app
