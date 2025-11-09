import sqlite3


def setup_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()


    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    # Insert sample data
    sample_users = [
        ('James Gathuri', 'Gathuri@gmail.com'),
        ('Andrew Ndegwa', 'Ndegwa@yahoo.com'),
        ('Bob Waigwa', 'Waigwa@gmail.com')
    ]

    # Only insert sample data if table is empty (avoids duplicate inserts)
    cursor.execute('SELECT COUNT(*) FROM users')
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.executemany('INSERT INTO users (name, email) VALUES (?, ?)', sample_users)
        conn.commit()
    else:
        print("Table already contains data; skipping sample inserts.")
    conn.close()
    print("Database setup completed!")

if __name__ == "__main__":
    setup_database()
