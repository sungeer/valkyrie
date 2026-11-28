from sqlalchemy.exc import IntegrityError

from src.utils.error_codes import ErrCode
from src.utils.api_errors import BizError
from src.core.db import db
from src.domains.users import repository


async def get_user(user_id: int) -> dict:
    async with db.connect() as conn:
        user = await repository.query_one(conn, user_id)
    if user is None:
        raise BizError('user not found', code=ErrCode.USER_NOT_FOUND)
    return user


async def list_users(limit: int) -> list[dict]:
    async with db.connect() as conn:
        users = await repository.query_many(conn, limit)
    return users


async def create_user(username: str, display_name: str | None, email: str) -> int:
    try:
        async with db.begin() as conn:
            if await repository.username_exists(conn, username):
                raise BizError('username already exists', code=ErrCode.USERNAME_EXISTS)
            if await repository.email_exists(conn, email):
                raise BizError('email already exists', code=ErrCode.EMAIL_EXISTS)
            user_id = await repository.insert_user(conn, username, display_name, email)
    except IntegrityError as exc:
        # 预检漏网的竞态：唯一键是权威判据，翻成业务错误
        raise BizError(
            'username or email already exists',
            code=ErrCode.USER_EXISTS
        ) from exc
    return user_id


async def update_display_name(user_id: int, display_name: str) -> int:
    async with db.begin() as conn:
        row_count = await repository.update_display_name(conn, user_id, display_name)
    if row_count == 0:
        raise BizError('user not found', code=ErrCode.USER_NOT_FOUND)
    return row_count


async def delete_user(user_id: int) -> int:
    async with db.begin() as conn:
        row_count = await repository.delete_user(conn, user_id)
    if row_count == 0:
        raise BizError('user not found', code=ErrCode.USER_NOT_FOUND)
    return row_count
