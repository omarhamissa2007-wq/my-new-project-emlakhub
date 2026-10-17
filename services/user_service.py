from services.database import connect


def find_user_by_email(email):
    connection = connect()
    user = connection.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    connection.close()
    return user


def find_user_by_ssn(ssn):
    connection = connect()
    user = connection.execute("SELECT * FROM users WHERE ssn = ?", (ssn,)).fetchone()
    connection.close()
    return user


def add_user(name, email, phone, ssn, password):
    connection = connect()

    # The very first person who signs up becomes the admin.
    count = connection.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    is_admin = 0
    if count == 0:
        is_admin = 1

    connection.execute(
        "INSERT INTO users (name, email, phone, ssn, password, is_admin) VALUES (?, ?, ?, ?, ?, ?)",
        (name, email, phone, ssn, password, is_admin),
    )
    connection.commit()
    connection.close()


def log_in(email, password):
    connection = connect()
    user = connection.execute(
        "SELECT * FROM users WHERE email = ? AND password = ?", (email, password)
    ).fetchone()
    connection.close()

    if user is None:
        return None
    # We keep the user as a plain dictionary in the session, so every screen can read user["name"].
    return dict(user)


def get_users():
    connection = connect()
    users = connection.execute(
        "SELECT name, email, phone, ssn, is_admin, created_at FROM users ORDER BY id"
    ).fetchall()
    connection.close()
    return users
