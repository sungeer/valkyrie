import sys

from loguru import logger

from src import settings
from src.core.ctx import request_id_var


def _patch(record):
    rid = request_id_var.get()
    if rid:
        record['message'] = f'[{rid}] {record["message"]}'


def setup_logger():
    logger.remove()

    logger.configure(patcher=_patch)

    fmt = (
        '[{time:HH:mm:ss.SSS} {level}] '
        '{name}:{line}\n    {message}'
    )

    env = settings.ENVIRONMENT

    if env == 'development':
        logger.add(
            sys.stdout,
            format=fmt,
            diagnose=False,
            backtrace=False,
            colorize=False,
            enqueue=False,
            level='DEBUG',
        )

    log_file = settings.LOG_DIR / 'valkyrie_{time:YYYY-MM-DD}.log'

    logger.add(
        log_file,
        format=fmt,
        diagnose=False,
        backtrace=False,
        colorize=False,
        enqueue=True,
        level='INFO',
        encoding='utf-8',
        rotation='00:00',
        retention='14 days',
    )
