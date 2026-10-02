import sqlite3
from pathlib import Path

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parents[1]
DB_PATH = ROOT_DIR / "database" / "datebase.db"

st.set_page_config(page_title="Delete Property", page_icon="🗑️", layout="wide")
st.title("🗑️ Delete Property")


def get_properties():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        return [dict(row) for row in conn.execute(
            "SELECT * FROM property ORDER BY id DESC"
        ).fetchall()]
    finally:
        conn.close()


def delete_property(property_id):
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM property WHERE id = ?", (property_id,))
        conn.commit()
        return cursor.rowcount
    finally:
        conn.close()


properties = get_properties()

if not properties:
    st.warning("There are no properties available to delete at the moment.")
    st.stop()

property_options = {
    f"{item.get('id')} - {item.get('name') or 'Unnamed'} - {item.get('address') or item.get('adress') or 'No address'}": item.get("id")
    for item in properties
}

selected_label = st.selectbox("Select the property you want to delete", list(property_options.keys()))
selected_id = property_options[selected_label]
selected_property = next(item for item in properties if item.get("id") == selected_id)

st.subheader("Selected Property Information")
st.write(f"ID: {selected_property.get('id')}")
st.write(f"Name: {selected_property.get('name', 'Not specified')}")
st.write(f"Price: {selected_property.get('price', 'Not specified')}")
st.write(f"Address: {selected_property.get('address', selected_property.get('adress', 'Not specified'))}")
st.write(f"Type: {selected_property.get('type', 'Not specified')}")

st.warning("⚠️ Warning: Deleting this property will permanently remove it from the database, and this action cannot be undone.")

if st.button("Delete property from database", type="primary", use_container_width=True):
    deleted_rows = delete_property(selected_id)
    if deleted_rows > 0:
        st.success(f"The property with ID {selected_id} was deleted successfully from the database.")
        st.rerun()
    else:
        st.error("Failed to delete the property. The ID may not exist or there may be an issue with the database.")

if st.button("Back to gallery", use_container_width=True):
    st.switch_page("pages/gallery.py")
