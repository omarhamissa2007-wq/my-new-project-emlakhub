import sqlite3
from pathlib import Path

import streamlit as st
from PIL import Image

ROOT_DIR = Path(__file__).resolve().parents[1]
DB_PATH = ROOT_DIR / "database" / "datebase.db"
DEFAULT_IMAGE = ROOT_DIR / "download.jpg"


st.set_page_config(page_title="EmlakHub - Details", page_icon="🏠", layout="wide")
st.title("🏘️ Property Details")


def get_property_by_id(property_id):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute(
            "SELECT * FROM property WHERE id = ?",
            (property_id,),
        ).fetchone()
        return dict(row) if row else None
    finally:
        conn.close()


def get_value(data, *keys, default="Not specified"):
    for key in keys:
        if data is None:
            return default
        value = data.get(key)
        if value is not None and value != "":
            return value
    return default


if (
    "selected_property" not in st.session_state
    or st.session_state.selected_property is None
):
    st.warning("⚠️ No property selected. Please go back to the home page and choose a property.")
    if st.button("← Back to Home"):
        st.switch_page("pages/gallery.py")
else:
    property_id = st.session_state.selected_property
    property_data = get_property_by_id(property_id)

    if property_data is None:
        st.error(f"Property with ID {property_id} was not found in the database.")
        if st.button("← Back to Home"):
            st.session_state.selected_property = None
            st.switch_page("pages/gallery.py")
    else:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Property Image")

            try:
                selected_image = st.session_state.get("selected_property_image")
                image_path = Path(selected_image) if selected_image else DEFAULT_IMAGE

                if image_path.exists():
                    img = Image.open(image_path)
                    st.image(img, width=600)
                elif selected_image:
                    st.image(selected_image, width=600)
                elif DEFAULT_IMAGE.exists():
                    img = Image.open(DEFAULT_IMAGE)
                    st.image(img, width=600)
                else:
                    st.image("https://via.placeholder.com/600x400?text=Property", width=600)
            except Exception as e:
                st.error(f"Error loading image: {str(e)}")

            if st.button("📄 View Contract", use_container_width=True):
                contract_page = ROOT_DIR / "pages" / "contract.py"
                if contract_page.exists():
                    st.session_state.selected_property = property_id
                    st.switch_page("pages/contract.py")
                else:
                    st.info("Contract page is not available yet.")

        with col2:
            st.subheader("Property Information")
            st.write(f"ID: {property_id}")
            st.write(f"Name: {get_value(property_data, 'name')}")
            st.write(f"Price: {get_value(property_data, 'price')}")
            st.write(f"Address: {get_value(property_data, 'address', 'Adress')}")
            st.write(f"Type: {get_value(property_data, 'type')}")

            st.divider()

            st.subheader("Specifications")
            st.write(f"Rooms: {get_value(property_data, 'number_of_rooms', 'Number_of_rooms')}")
            st.write(f"Area: {get_value(property_data, 'area')}")

     

        col1, col2 = st.columns(2)

        with col1:
            if st.button("← Back to Home", use_container_width=True):
                st.session_state.selected_property = None
                st.switch_page("pages/gallery.py")

        with col2:
            if st.button("🔄 Choose Another Property", use_container_width=True):
                st.session_state.selected_property = None
                st.rerun()
