import streamlit as st
import sqlite3

st.title("register page")

name = st.text_input("name")
phone = st.text_input("phone")
password = st.text_input("password")
ssn = st.text_input("ssn")
email = st.text_input("email")



if st.button("submit"):
        conn = sqlite3.connect("database\datebase.db")
        cursor=conn.cursor()
        cursor.execute(
            """
            INSERT INTO users(name, phone, password, email, ssn)
            VALUES (?, ?, ?, ?, ?)
            """,
            (name, phone, password, email, ssn)
        )        
        conn.commit()
        conn.close()
