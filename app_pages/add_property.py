import streamlit as st

from services.photo_service import add_photo
from services.property_service import add_property

# Bigger photos make the gallery slow to load.
MAX_IMAGE_MB = 5
# Enough to show a place well without making the page long.
MAX_PHOTOS = 5

st.title("➕ Add property")

with st.form("add_property"):
    title = st.text_input("Title", placeholder="3-room apartment in New Cairo")
    description = st.text_area("Description", placeholder="What makes this place nice? Floor, view, garden, finishing...")
    offer_choice = st.radio("Offer", ["For sale", "For rent"], horizontal=True)
    property_type = st.selectbox("Type", ["apartment", "villa"])
    area = st.number_input("Area (m²)", min_value=1, value=100, step=1)
    address = st.text_input("Address", placeholder="Fifth Settlement, New Cairo")
    # The price box starts empty, so nobody saves a made-up price by accident.
    price = st.number_input("Price in EGP (the total for sale, or per month for rent)", min_value=1, value=None, step=1000)
    rooms = st.number_input("Rooms", min_value=1, value=3, step=1)
    image_files = st.file_uploader(
        "Photos (1 to " + str(MAX_PHOTOS) + ", up to " + str(MAX_IMAGE_MB) + " MB each). The first one is the cover.",
        type=["png", "jpg", "jpeg", "webp"],
        accept_multiple_files=True,
        max_upload_size=MAX_IMAGE_MB,
    )
    pressed = st.form_submit_button("Add property", type="primary")

if pressed:
    offer = "sale"
    if offer_choice == "For rent":
        offer = "rent"

    if title.strip() == "" or description.strip() == "" or address.strip() == "":
        st.error("Please fill in the title, the description and the address.")
    elif price is None:
        st.error("Please type the price.")
    elif len(image_files) == 0:
        st.error("Please add at least one photo, so the property shows up nicely in the gallery.")
    elif len(image_files) > MAX_PHOTOS:
        st.error("Please pick at most " + str(MAX_PHOTOS) + " photos.")
    else:
        property_id = add_property(
            title.strip(), description.strip(), offer, property_type, area, address.strip(), price, rooms
        )
        for image_file in image_files:
            add_photo(property_id, image_file)
        # Open the new listing, so you can see it. Leaving this page also empties the form,
        # so the same listing can't be added twice by accident.
        st.session_state.selected_property = property_id
        st.switch_page("app_pages/property_details.py")
