import streamlit as st
import sqlite3




st.set_page_config(page_title="View users", layout="wide")

st.title("view users")

conn = sqlite3.connect("database/datebase.db")
cursor=conn.cursor()
cursor.execute(
            """
                select * from users

            """
        )        
properties = cursor.fetchall()
num_cols = 3

for row_start in range(0, len(properties), num_cols):

    row_props = properties[row_start:row_start + num_cols]
    cols = st.columns(len(row_props))

    for col_idx, prop in enumerate(row_props):

        with cols[col_idx]:

            with st.container():

                st.header(prop[1])
                st.text(prop[2])
                st.button(
                    "view datiles",
                    use_container_width=True,
                    key=f"view-details-{row_start + col_idx}",
                )