from sqlalchemy import text


async def query_one(conn, user_id: int) -> dict | None:
    sql = text('''
        SELECT
            id, username, display_name, email
        FROM
            app.users
        WHERE
            id = :id
    ''')

    params = {
        'id': user_id
    }

    result = await conn.execute(sql, params)

    row = result.mappings().first()  # RowMapping | None
    # row = result.mappings().one()  # 没有或多于一条都会抛异常

    return dict(row) if row else None


async def query_many(conn, limit: int) -> list[dict]:
    sql = text('''
        SELECT
            id, username, display_name, email
        FROM
            app.users
        ORDER BY id
        LIMIT :limit
    ''')

    params = {
        'limit': limit
    }

    result = await conn.execute(sql, params)
    rows = result.mappings().all()  # list[RowMapping]

    return [dict(r) for r in rows]


async def insert_user(conn, username: str, display_name: str | None, email: str) -> int:
    sql = text('''
        INSERT INTO app.users(username, display_name, email)
        VALUES (:username, :display_name, :email)
        RETURNING id
    ''')

    params = {
        'username': username,
        'display_name': display_name,
        'email': email,
    }

    result = await conn.execute(sql, params)

    return result.scalar_one()


async def update_display_name(conn, user_id: int, display_name: str) -> int:
    sql = text('''
        UPDATE
            app.users
        SET
            display_name = :display_name
        WHERE
            id = :id
    ''')

    params = {
        'display_name': display_name,
        'id': user_id
    }

    result = await conn.execute(sql, params)

    return result.rowcount


async def username_exists(conn, username: str) -> bool:
    sql = text('''
        SELECT 1
        FROM
            app.users
        WHERE
            username = :username
    ''')

    params = {
        'username': username
    }

    row = (await conn.execute(sql, params)).mappings().first()

    return row is not None


async def email_exists(conn, email: str) -> bool:
    sql = text('''
        SELECT 1
        FROM
            app.users
        WHERE
            email = :email
    ''')

    params = {
        'email': email
    }

    row = (await conn.execute(sql, params)).mappings().first()

    return row is not None


async def delete_user(conn, user_id: int) -> int:
    sql = text('''
        DELETE FROM
            app.users
        WHERE
            id = :id
    ''')

    params = {
        'id': user_id
    }

    result = await conn.execute(sql, params)

    return result.rowcount
