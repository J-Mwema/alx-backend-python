"""Task 0: Class-based context manager for sqlite3 connection.

This module provides DatabaseConnection which opens `users.db` when used
with the `with` statement and ensures the connection is closed afterwards.
"""
import sqlite3


class DatabaseConnection:
    """Context manager that opens and closes a sqlite3 connection.

    Example:
        with DatabaseConnection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')
            print(cursor.fetchall())
    """

    def __init__(self, db_path: str = 'users.db'):
        self.db_path = db_path
        self.conn = None

    def __enter__(self):
        # Open database connection and return it
        self.conn = sqlite3.connect(self.db_path)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        # If an exception occurred, optionally roll back
        try:
            if exc_type is not None:
                # If a transaction was started, rollback changes
                try:
                    self.conn.rollback()
                except Exception:
                    pass
            else:
                # No exception — commit any changes
                try:
                    self.conn.commit()
                except Exception:
                    pass
        finally:
            # Always close the connection
            if self.conn:
                self.conn.close()


if __name__ == "__main__":
    with DatabaseConnection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        results = cursor.fetchall()
        print(results)
