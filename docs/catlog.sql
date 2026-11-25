

-- ----------------------------------------
-- [step-1] 获取追踪链
-- ----------------------------------------

-- 获取追踪链
grep -n -F "received request" valkyrie_2026-11-25.log | grep "14:29"

-- 日志示例
[14:23:05.857 INFO] src.domains.users.views:23
    [7fad5d8cde054f2793] list users limit=5 count=3

-- 追踪链
`7fad5d8cde054f2793`


-- ----------------------------------------
-- [step-2] 根据追踪链获取全链路
-- ----------------------------------------

-- 全链路 带行号
grep -n "7fad5d8cde054f2793" valkyrie_2026-11-25.log

-- 查看指定行 详情
less -N +29 valkyrie_2026-11-25.log


-- ----------------------------------------
-- [step-3] 特殊查询
-- ----------------------------------------

-- 或
grep -n -F -e "received request" -e "less" -e "14:29" valkyrie_2026-11-25.log

-- 且
grep -n -F -e "received request" valkyrie_2026-11-25.log | grep "less"
