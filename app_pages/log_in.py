import streamlit as st

from services.user_service import log_in

st.title("🔑 Log in")

# A form sends both boxes together when you press the button, so the password never gets lost.
with st.form("log_in"):
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    pressed = st.form_submit_button("Log in", type="primary")

if pressed:
    if email.strip() == "" or password == "":
        st.error("Please type your email and password.")
    else:
        user = log_in(email.strip().lower(), password)
        if user is None:
            st.error("That email and password don't match an account.")
        else:
            st.session_state.user = user
            # Rerun so app.py rebuilds the menu for the logged-in user.
            st.rerun()

st.write("No account yet? Pick **Sign up** in the menu.")
