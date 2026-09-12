import streamlit as st
import sqlite3

st.title("login page")

email = st.text_input("email")
password = st.text_input("password")



if st.button("submit"):

    conn = sqlite3.connect("datebase.db")
    cursor=conn.cursor()
    cursor.execute("""
                    select * from users
                    where email=? and  password = ?
                """,
            (email,password)
    )
    
    user = cursor.fetchone()
    
    conn.close()

    if user :
        st.success("loged in succesfully")
    else:
        st.error("invaild email or password")
