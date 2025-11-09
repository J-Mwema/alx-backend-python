import sqlite3
import functools


#### decorator to log SQL queries
def log_queries():
    """Decorator factory that returns a decorator which logs the SQL query.

    The wrapped function is expected to accept a `query` argument (either as
    a positional or keyword argument).
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Extract the query from kwargs or from first positional arg
            query = kwargs.get('query') if 'query' in kwargs else (args[0] if args else None)
            print(f"Executing query: {query}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log_queries()
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


#### fetch users while logging the query
if __name__ == "__main__":
    users = fetch_all_users(query="SELECT * FROM users")
    print(users)
