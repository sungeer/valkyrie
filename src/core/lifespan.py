from contextlib import asynccontextmanager

from src.core.logging import setup_logger
from src.core.db import db
from src.core.http import http


@asynccontextmanager
async def lifespan(app):
    setup_logger()

    http.init()

    db.init()

    yield

    await http.aclose()

    await db.dispose()
