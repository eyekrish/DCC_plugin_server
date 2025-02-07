import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# Create the inventory table
cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    quantity INTEGER NOT NULL
)
""")

conn.commit()
conn.close()
