from operator import ge
import os
import sqlite3
from webbrowser import get
from pathlib import Path

import streamlit as st
from PIL import Image

ROOT_DIR = Path(__file__).resolve().parents[1]
DB_PATH = ROOT_DIR / "database" / "datebase.db"
DEFAULT_IMAGE = ROOT_DIR / "download.jpg"



st.set_page_config(page_title="EmlakHub - Contract", page_icon="📝", layout="wide")
st.title("📄 Contract")
st.divider()


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
        
def get_property_image(row):
    img_url = row.get("img_url")
    if img_url and isinstance(img_url, str):
        candidate = Path(img_url)
        if candidate.exists():
            return candidate

    if DEFAULT_IMAGE.exists():
        return DEFAULT_IMAGE

    return "https://via.placeholder.com/600x400?text=Property"



def get_property_value(data, *keys, default="Not specified"):
    for key in keys:
        value = data.get(key) if data else None
        if value is not None and value != "":
            return value
    return default


def save_contract_to_db(payload):
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS contracts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                phone TEXT,
                email TEXT,
                card_number TEXT,
                contract_type TEXT,
                property_id INTEGER,
                property_type TEXT,
                property_price TEXT,
                property_address TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.execute(
            """
            INSERT INTO contracts(
                name, phone, email, card_number, contract_type,
                property_id, property_type, property_price, property_address
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                payload["name"],
                payload["phone"],
                payload["email"],
                payload["card_number"],
                payload["contract_type"],
                payload["property_id"],
                payload["property_type"],
                payload["property_price"],
                payload["property_address"],
            ),
        )
        conn.commit()
    finally:
        conn.close()


if (
    "selected_property" not in st.session_state
    or st.session_state.selected_property is None
    or not st.session_state.selected_property
):
    st.warning("⚠️ No property selected. Please go back to the home page and choose a property.")
    if st.button("Back to Gallery", key="back_to_gallery", use_container_width=True):
        st.switch_page("pages/gallery.py")
    st.stop()

property_id = st.session_state.selected_property
property_data = get_property_by_id(property_id)
if property_data is None:
    st.error("⚠️ Property data is not available.")
    st.stop()


col1, col2 = st.columns(2)

with col1:
    st.subheader("Client Information")

    col1_form, col2_form = st.columns(2)

    with col1_form:
        name = st.text_input("👤 Full name")
        phone_input = st.text_input("📞 Phone number (start with +20 for Egypt)")
        email = st.text_input("📧 Email address")

    with col2_form:
        card_number = st.text_input("💳 Card number")
        contract_type = st.selectbox(
            "📑 Select contract type:", ["ownership", "tenant"], index=0
        )

    st.info("📢 Contract confirmation will be sent by email")


with col2:
    st.subheader("Property Information")
    property_type = get_property_value(property_data, "type")
    st.write(f"Type: {property_type}")
    st.write(f"Price: {get_property_value(property_data, 'price')}")
    st.write(f"Address: {get_property_value(property_data, 'address', 'Adress')}")
    st.divider()

    try:
        st.image(get_property_image(property_data), width=600)
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")


st.divider()


def load_contract_file(contract_type):
    if contract_type == "ownership":
        filename = "ownership_contract.pdf"
        label = "📃 Download sale contract"
    else:
        filename = "tenant_contract.pdf"
        label = "🏠 Download rental contract"

    try:
        path = f"assets/documents/{filename}"
        with open(path, "rb") as f:
            return f.read(), filename, label
    except FileNotFoundError:
        st.error(f"File {filename} was not found in the assets/documents folder.")
        return None, None, None


contract_data, contract_filename, contract_label = load_contract_file(contract_type)

if contract_data:
    st.download_button(
        label=contract_label,
        data=contract_data,
        file_name=contract_filename,
        mime="application/pdf",
        use_container_width=True,
        key="download_contract",
    )


uploaded_file = st.file_uploader("📤 Upload the signed contract (PDF only)", type=["pdf"])

if uploaded_file:
    os.makedirs("data/uploads", exist_ok=True)
    expected_file = (
        "ownership_contract.pdf"
        if contract_type == "ownership"
        else "tenant_contract.pdf"
    )

    if uploaded_file.name == expected_file:
        with open(f"data/uploads/{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("✅ Contract uploaded successfully!")

    else:
        st.error(f"❌ Error! Please upload the correct file: {expected_file}")

if st.button("Send contract details", key="send_contract_details", use_container_width=True):
    if not name or not phone_input or not email or not card_number:
        st.error("❌ Please fill in all the required fields before sending.")
    else:
        contract_payload = {
            "name": name,
            "phone": phone_input,
            "email": email,
            "card_number": card_number,
            "contract_type": contract_type,
            "property_id": property_id,
            "property_type": property_type,
            "property_price": get_property_value(property_data, "price"),
            "property_address": get_property_value(property_data, "address", "Adress"),
        }

        st.session_state["contract_payload"] = contract_payload
        save_contract_to_db(contract_payload)

        if contract_type == "tenant":
            st.session_state["tenant_contract_details"] = contract_payload
            st.switch_page("pages/view_tennet.py")

        st.success("✅ Contract details sent successfully!")
        st.success("📧 Contract details sent to the client via email.")
        st.success("📤 Contract uploaded to the server successfully.")

