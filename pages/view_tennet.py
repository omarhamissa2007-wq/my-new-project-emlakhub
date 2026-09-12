import sqlite3
from pathlib import Path

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_IMAGE = ROOT_DIR / "images" / "villa1.jpg"


def get_property_image(image_ref):
    candidate_paths = []

    if image_ref:
        value = str(image_ref).strip()
        if value:
            candidate_paths.extend(
                [
                    Path(value),
                    ROOT_DIR / value,
                    ROOT_DIR / "images" / value,
                    ROOT_DIR / "images" / Path(value).name,
                ]
            )

    for candidate in candidate_paths:
        if candidate.exists():
            return candidate

    if DEFAULT_IMAGE.exists():
        return DEFAULT_IMAGE

    return "https://placehold.co/600x400?text=No+Image"


st.set_page_config(page_title="View Properties", layout="wide")
st.title("View tennet")

tenant_data = st.session_state.get("tenant_contract_details")
if not tenant_data:
    conn = sqlite3.connect("database/datebase.db")
    conn.row_factory = sqlite3.Row
    try:
     conn.execute(
            "SELECT * FROM tenant_contract WHERE contract_type = 'tenant' ORDER BY id DESC LIMIT 1"
        ).fetchone()
    finally:
        conn.close()

if tenant_data:
    st.success("✅ Tenant contract details received.")
    st.subheader("Tenant Contract Information")
    st.write(f"Name: {tenant_data.get('name')}")
    st.write(f"Phone: {tenant_data.get('phone')}")
    st.write(f"Email: {tenant_data.get('email')}")
    st.write(f"Card Number: {tenant_data.get('card_number')}")
    st.write(f"Property Type: {tenant_data.get('property_type')}")
    st.write(f"Property Price: {tenant_data.get('property_price')}")
    st.write(f"Property Address: {tenant_data.get('property_address')}")
    st.divider()

conn = sqlite3.connect("database/datebase.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM tenants_contract")
properties = cursor.fetchall()
conn.close()
num_cols = 3

for row_start in range(0, len(properties), num_cols):
    row_props = properties[row_start:row_start + num_cols]
    cols = st.columns(len(row_props))

    for col_idx, prop in enumerate(row_props):
        with cols[col_idx]:
            with st.container():
                st.header(prop[1])
                image_path = get_property_image(prop[3]) if len(prop) > 3 else DEFAULT_IMAGE
                st.image(image_path, use_container_width=True)
                st.text(prop[2] if len(prop) > 2 else "")
                st.button(
                    "view datiles",
                    use_container_width=True,
                    key=f"view-details-{row_start + col_idx}",
                )

