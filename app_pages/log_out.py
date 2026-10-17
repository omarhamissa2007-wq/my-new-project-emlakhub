import streamlit as st

# Forget everything about this visit, then rerun so the menu goes back to the guest menu.
st.session_state.clear()
st.rerun()
