import aiosqlite
import asyncio


async def async_fetch_users_db(db_path: str = 'users.db'):
    async with aiosqlite.connect(db_path) as db:
        async with db.execute('SELECT * FROM users') as cursor:
            return await cursor.fetchall()


async def async_fetch_older_users_db(db_path: str = 'users.db'):
    async with aiosqlite.connect(db_path) as db:
        async with db.execute('SELECT * FROM users WHERE age > ?', (40,)) as cursor:
            return await cursor.fetchall()


# Wrapper functions with exact signatures expected by the checker
async def async_fetch_users():
    return await async_fetch_users_db()


async def async_fetch_older_users():
    return await async_fetch_older_users_db()


async def fetch_concurrently():
    results = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    # results is a list: [all_users, older_users]
    all_users, older_users = results
    print('All users:', all_users)
    print('\nUsers older than 40:', older_users)


if __name__ == '__main__':
    # Run the concurrent fetch
    asyncio.run(fetch_concurrently())
