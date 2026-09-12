import sqlite3
from pathlib import Path

import streamlit as st
from PIL import Image

ROOT_DIR = Path(__file__).resolve().parents[1]
DB_PATH = ROOT_DIR / "database" / "datebase.db"
DEFAULT_IMAGE = ROOT_DIR / "download.jpg"

st.set_page_config(page_title="EmlakHub - Home", page_icon="🏠", layout="wide")


def get_property_value(row, *keys, default="Not specified"):
    for key in keys:
        value = row.get(key)
        if value is not None and value != "":
            return value
    return default


def get_property_image(row):
    img_url = row.get("img_url")
    if img_url and isinstance(img_url, str):
        candidate = Path(img_url)
        if candidate.exists():
            return candidate

    if DEFAULT_IMAGE.exists():
        return DEFAULT_IMAGE

    return "https://via.placeholder.com/600x400?text=Property"


def get_properties():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        rows = conn.execute(
            "SELECT * FROM property ORDER BY id DESC"
        ).fetchall()
        return [dict(row) for row in rows]
    finally:
        conn.close()


st.title("Gallery")
st.write("---")

properties = get_properties()

if properties:
    cols = st.columns(4)

    for index, property_data in enumerate(properties):
        try:
            col = cols[index % 4]
            with col:
                with st.container():
                    st.image(get_property_image(property_data), use_container_width=True)
                    st.subheader(get_property_value(property_data, "name", default="Property"))
                    st.write(f"**Price:** {get_property_value(property_data, 'price', default='Not specified')}")
                    st.write(f"**Address:** {get_property_value(property_data, 'address', 'Adress', default='Not specified')}")
                    st.write(f"**Rooms:** {get_property_value(property_data, 'number_of_rooms', 'Number_of_rooms', default='Not specified')}")
                    st.write(f"**Area:** {get_property_value(property_data, 'area', default='Not specified')}")

                    if st.button("View details", key=f"details_{property_data.get('id')}", use_container_width=True):
                        st.session_state.selected_property = property_data.get("id")
                        st.session_state.selected_property_image = str(get_property_image(property_data))
                        details_page = ROOT_DIR / "pages" / "property_details.py"
                        if details_page.exists():
                            st.switch_page("pages/property_details.py")
                        else:
                            st.info("Property details page is not available.")

        except Exception as e:
            st.error(f"Error loading property #{property_data.get('id')}: {str(e)}")
else:
    st.warning("No properties found.")
