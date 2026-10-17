import sqlite3

# Run the app from the project folder, so these short paths point at the right files.
DB_PATH = "database/emlakhub.db"
SCHEMA_PATH = "database/schema.sql"
SEED_PATH = "database/seed.sql"


def connect():
    connection = sqlite3.connect(DB_PATH)
    # This lets us read a column by its name, like row["price"].
    connection.row_factory = sqlite3.Row
    return connection


def read_text_file(path):
    with open(path, encoding="utf-8") as text_file:
        return text_file.read()


def create_tables():
    connection = connect()
    connection.executescript(read_text_file(SCHEMA_PATH))

    # The very first time the app starts the gallery is empty, so we fill it with the starter listings.
    count = connection.execute("SELECT COUNT(*) FROM property").fetchone()[0]
    if count == 0:
        connection.executescript(read_text_file(SEED_PATH))

    connection.commit()
    connection.close()
