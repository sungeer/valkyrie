from sqlalchemy.ext.asyncio import create_async_engine

from src import settings


class _Engine:

    def __init__(self):
        self._engine = None

    def init(self):
        self._engine = create_async_engine(
            settings.DB_URL,
            echo=False,  # 不打印SQL语句
            pool_size=10,  # 空闲连接 上限（平时保持 10 条）
            max_overflow=10,  # 高峰额外最多再开 10 条（峰值共 20 条）
            pool_timeout=5,  # 取连接等待 5s 失败就报错
            pool_recycle=1800,  # 回收重连
            pool_pre_ping=True,  # 避免拿到失效连接
            connect_args={
                'connect_timeout': 5,  # 连不上 DB 时 5s 快速失败
                'options': '-c statement_timeout=60s',
            },
        )

    def get(self):
        if self._engine is None:
            raise RuntimeError('Engine not initialized')
        return self._engine

    def connect(self):
        return self.get().connect()

    def begin(self):
        # 退出时提交，异常时回滚
        return self.get().begin()

    async def dispose(self):
        if self._engine is not None:
            await self._engine.dispose()


db = _Engine()
