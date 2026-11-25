

-- dev
uvicorn app:app --host 0.0.0.0 --port 8848 --no-access-log

-- pg win
uvicorn app:app --host 0.0.0.0 --port 8848 --no-access-log --loop asyncio:SelectorEventLoop

-- env file
uvicorn app:app --host 0.0.0.0 --port 8848 --env-file /home/user/valkyrie-testing.env

-- prod start
nohup /srv/venvs/valkyrie/bin/python /srv/valkyrie/serve.py > /srv/logs/uvicorn.out 2>&1 &

-- prod stop
kill $(cat /srv/run/uvicorn.pid)


-- 性能查看
top -p $(pgrep -d',' uvicorn)


-- 删除
rm -f /srv/valkyrie.tar
rm -rf /srv/valkyrie


-- 进程查看
ps -ef | grep uvicorn | grep -v grep
