import streamlit as st

from services.user_service import get_users

st.title("👥 Users")

users = get_users()

if len(users) == 0:
    st.info("Nobody has signed up yet.")
    st.stop()

# Build one row per person for the table. We leave the password out on purpose.
rows = []
for user in users:
    role = "user"
    if user["is_admin"] == 1:
        role = "admin"
    rows.append({
        "Name": user["name"],
        "Email": user["email"],
        "Phone": user["phone"],
        "National ID": user["ssn"],
        "Role": role,
        "Joined": user["created_at"],
    })

st.write(str(len(users)) + " people have signed up.")
st.dataframe(rows, hide_index=True)
