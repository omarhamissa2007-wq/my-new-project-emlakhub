import sqlite3
from pathlib import Path
from uuid import uuid4
import streamlit as st


ROOT_DIR = Path(__file__).resolve().parents[1]
UPLOAD_DIR = ROOT_DIR / "data" / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

st.title("Add Property")

name = st.text_input("name")
area = st.text_input("area")
type = st.text_input("type")
adress = st.text_input("adress")
price = st.text_input("price")
Number_of_rooms = st.text_input("Number_of_rooms ")
img_file = st.file_uploader("Property image", type=["png", "jpg", "jpeg", "webp"])

if st.button("submit"):
    img_url = ""
    if img_file is not None:
        file_ext = Path(img_file.name).suffix or ".jpg"
        safe_name = f"property_{uuid4().hex}{file_ext}"
        save_path = UPLOAD_DIR / safe_name
        save_path.write_bytes(img_file.getvalue())
        img_url = str(save_path)

    conn = sqlite3.connect("database/datebase.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO property(name, area, type,adress,price,Number_of_rooms, img_url)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (name, area, type, adress, price, Number_of_rooms, img_url)
    )
    conn.commit()
    conn.close()
    
    st.success("Property added successfully!")

if not all([name, area, type, adress, price, Number_of_rooms]):
    st.error("Please fill in all required fields.")
