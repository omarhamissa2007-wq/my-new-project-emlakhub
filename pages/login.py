import streamlit as st
import sqlite3
from pathlib import Path

st.title(" welcome to emlakhub thelogin page")

DB_PATH = Path(__file__).parents[1] / "database" / "datebase.db"


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    return conn


def ensure_schema(conn: sqlite3.Connection):
    cursor = conn.cursor()
    # create users table if it doesn't exist (matches database/datebase.sql)
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            dob DATE,
            phone VARCHAR(255),
            ssn VARCHAR(255) UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()


email = st.text_input("email")
password = st.text_input("password", type="password")


if st.button("submit"):
    conn = get_connection()
    ensure_schema(conn)
    cursor = conn.cursor()
    cursor.execute(
        "select * from users where email=? and password=?",
        (email, password),
    )

    user = cursor.fetchone()

    conn.close()



    if user:
        st.success("logged in successfully")
        st.switch_page("pages/gallery.py")
    else:
        st.error("invalid email or password")
