import sqlite3
from contextlib import contextmanager
DB_NAME = "tasks.db"

def init_db():
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT CHECK(status IN ('todo','in-progress','done')) NOT NULL DEFAULT 'todo',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        connection.commit()

@contextmanager
def get_db_connection():
    connection = sqlite3.connect(DB_NAME)
    try:
        yield connection
    finally:
        connection.close