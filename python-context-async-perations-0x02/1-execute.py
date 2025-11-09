"""Task 1: Reusable ExecuteQuery context manager.

This context manager accepts a SQL query and parameters, executes the query
against `users.db`, returns the fetched results from __enter__, and ensures
the connection is closed in __exit__.
"""
import sqlite3


class ExecuteQuery:
    def __init__(self, query, params=()):
        self.query = query
        self.params = params
        self.conn = None
        self.results = None

    def __enter__(self):
        # Open connection, execute query and fetch results
        self.conn = sqlite3.connect('users.db')
        cursor = self.conn.cursor()
        cursor.execute(self.query, self.params)
        self.results = cursor.fetchall()
        return self.results

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close the connection; commit or rollback depending on exception
        try:
            if exc_type is not None:
                try:
                    self.conn.rollback()
                except Exception:
                    pass
            else:
                try:
                    self.conn.commit()
                except Exception:
                    pass
        finally:
            if self.conn:
                self.conn.close()


if __name__ == "__main__":
    # Example usage: select users older than 25
    query = "SELECT * FROM users WHERE age > ?"
    with ExecuteQuery(query, (25,)) as results:
        print(results)
