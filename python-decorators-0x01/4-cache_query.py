import time
import sqlite3
import functools

query_cache = {}

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            result = func(conn, *args, **kwargs)
            return result
        finally:
            conn.close()
    return wrapper

def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        # Use query as cache key
        cache_key = query

        # Check if result is cached
        if cache_key in query_cache:
            print(f"Using cached result for query: {query}")
            return query_cache[cache_key]

        # If not cached, execute query and cache result
        print(f"Cache miss -- executing query: {query}")
        result = func(conn, query, *args, **kwargs)
        query_cache[cache_key] = result
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# Test the function
if __name__ == "__main__":
    # First call will cache the result
    print("First call:")
    users = fetch_users_with_cache(query="SELECT * FROM users")
    print(f"Found {len(users)} users")


    # Second call will use the cached result
    print("\nSecond call:")
    users_again = fetch_users_with_cache(query="SELECT * FROM users")
    print(f"Found {len(users_again)} users (from cache)")
