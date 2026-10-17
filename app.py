import streamlit as st

from services.database import create_tables

st.set_page_config(page_title="EmlakHub", page_icon="🏠", layout="wide")

# Make the tables (and the starter listings) if they aren't there yet.
create_tables()

# Nobody is logged in until they log in.
if "user" not in st.session_state:
    st.session_state.user = None

user = st.session_state.user

# Everyone can look at the gallery and open a listing.
pages = [
    st.Page("app_pages/gallery.py", title="Gallery", icon="🏠", default=True),
    st.Page("app_pages/property_details.py", title="Property details", icon="🏘️", visibility="hidden"),
]

if user is None:
    pages.append(st.Page("app_pages/log_in.py", title="Log in", icon="🔑"))
    pages.append(st.Page("app_pages/sign_up.py", title="Sign up", icon="📝"))
else:
    # The contract screen is hidden from the menu. You reach it with the button on a listing.
    pages.append(st.Page("app_pages/contract.py", title="Contract", icon="✍️", visibility="hidden"))

    if user["is_admin"] == 1:
        pages.append(st.Page("app_pages/add_property.py", title="Add property", icon="➕"))
        pages.append(st.Page("app_pages/edit_property.py", title="Edit property", icon="✏️", visibility="hidden"))
        pages.append(st.Page("app_pages/users.py", title="Users", icon="👥"))
        pages.append(st.Page("app_pages/contracts.py", title="All contracts", icon="📑"))
    else:
        pages.append(st.Page("app_pages/my_contracts.py", title="My contracts", icon="📄"))

    pages.append(st.Page("app_pages/log_out.py", title="Log out", icon="🚪"))

# Only the pages in this list show up in the menu, and only they can be opened.
page = st.navigation(pages)
page.run()
