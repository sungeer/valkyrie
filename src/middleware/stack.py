from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from src import settings
from src.middleware import request_id
from src.middleware import slow_request

middlewares = [
    Middleware(request_id.RequestIDMiddleware),  # 最外层 最先执行
    Middleware(slow_request.SlowRequestMiddleware),
    Middleware(
        CORSMiddleware,
        allow_origins=settings.ORIGINS,  # allow_origins=['*']  # 允许所有来源
        allow_credentials=True,
        allow_methods=['*'],  # 允许所有方法
        allow_headers=['*'],  # 允许所有头部
        expose_headers=['X-Request-ID'],  # 跨源时允许前端 JS 读取该响应头
    ),
]
