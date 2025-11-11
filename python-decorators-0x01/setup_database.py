import sqlite3


def setup_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()


    # Create users table (include age column for other exercises)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER
        )
    ''')

    # Sample data with ages
    sample_users = [
        ('James Gathuri', 'Gathuri@gmail.com', 45),
        ('Andrew Ndegwa', 'Ndegwa@yahoo.com', 30),
        ('Bob Waigwa', 'Waigwa@gmail.com', 50)
    ]

    # Only insert sample data if table is empty (avoids duplicate inserts)
    cursor.execute('SELECT COUNT(*) FROM users')
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.executemany('INSERT INTO users (name, email, age) VALUES (?, ?, ?)', sample_users)
        conn.commit()
    else:
        # If table exists but age column might be NULL for old rows, try to fill ages
        cursor.execute("PRAGMA table_info('users')")
        cols = [row[1] for row in cursor.fetchall()]
        if 'age' not in cols:
            # Add the column and set ages for known users
            cursor.execute('ALTER TABLE users ADD COLUMN age INTEGER')
            # Update known users by name (best effort)
            updates = [
                (45, 'James Gathuri'),
                (30, 'Andrew Ndegwa'),
                (50, 'Bob Waigwa'),
            ]
            for age, name in updates:
                cursor.execute('UPDATE users SET age = ? WHERE name = ?', (age, name))
            conn.commit()
        else:
            # If age column exists but rows may have NULL age, fill known users
            cursor.execute('SELECT COUNT(*) FROM users WHERE age IS NULL')
            null_ages = cursor.fetchone()[0]
            if null_ages > 0:
                updates = [
                    (45, 'James Gathuri'),
                    (30, 'Andrew Ndegwa'),
                    (50, 'Bob Waigwa'),
                ]
                for age, name in updates:
                    cursor.execute('UPDATE users SET age = ? WHERE name = ? AND (age IS NULL OR age = 0)', (age, name))
                conn.commit()
    conn.close()
    print("Database setup completed!")

if __name__ == "__main__":
    setup_database()
