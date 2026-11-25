import uvicorn

log_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'generic': {
            'format': '%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
            'datefmt': '[%Y-%m-%d %H:%M:%S %z]',
        },
    },
    'handlers': {
        'error_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'generic',
            'filename': '/srv/logs/uvicorn.log',
            'when': 'midnight',
            'backupCount': 7,
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'uvicorn.error': {
            'level': 'INFO',
            'handlers': ['error_file'],
            'propagate': False,
        },
    },
}

config = {
    'host': '0.0.0.0',
    'port': 8848,
    'access_log': False,
    'log_config': log_config
}

uvicorn.run('app:app', **config)
