import streamlit as st

from services.user_service import add_user, find_user_by_email, find_user_by_ssn, log_in

st.title("📝 Sign up")

# A form sends all the boxes together when you press the button, so nothing you typed gets lost.
with st.form("sign_up"):
    name = st.text_input("Full name")
    email = st.text_input("Email")
    phone = st.text_input("Phone number", placeholder="+20 ...")
    ssn = st.text_input("National ID number")
    password = st.text_input("Password", type="password")
    pressed = st.form_submit_button("Create account", type="primary")

if pressed:
    name = name.strip()
    # Emails don't care about capital letters, so we save them in small letters.
    email = email.strip().lower()
    phone = phone.strip()
    ssn = ssn.strip()

    if name == "" or email == "" or phone == "" or ssn == "" or password == "":
        st.error("Please fill in every field.")
    elif "@" not in email:
        st.error("That email doesn't look right. It needs an @.")
    elif find_user_by_email(email) is not None:
        st.error("That email already has an account. Try logging in.")
    elif find_user_by_ssn(ssn) is not None:
        st.error("That national ID already has an account.")
    else:
        add_user(name, email, phone, ssn, password)
        # Log the new person straight in, so they don't have to type it all again.
        st.session_state.user = log_in(email, password)
        st.rerun()
