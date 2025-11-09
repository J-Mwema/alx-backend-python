import sqlite3
import functools


# Copy the with_db_connection decorator from previous task
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()

    return wrapper


def transactional(func):
    """Decorator that wraps a DB operation in a transaction.

    The wrapped function is expected to accept a `conn` as its first
    argument.
    """
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            print(f"Transaction rolled back due to error: {e}")
            raise

    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
    print(f"Updated user {user_id} email to {new_email}")


# Test the function
if __name__ == "__main__":
    update_user_email(user_id=1, new_email='Gituiki@gmail.com')

    # Verify the update
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = 1")
    updated_user = cursor.fetchone()
    conn.close()
    print("Updated user:", updated_user)







