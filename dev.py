import uvicorn

uvicorn.run(
    'app:app',
    port=8848,
    access_log=False,
    loop='asyncio:SelectorEventLoop',
)
