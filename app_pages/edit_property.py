import streamlit as st

from services.contract_service import has_waiting_contracts
from services.photo_service import add_photo, delete_photo, get_photos
from services.property_service import get_property, update_property

# The same limits as on the Add property screen.
MAX_IMAGE_MB = 5
MAX_PHOTOS = 5
# All five photos fit in one row.
PHOTO_COLUMNS = 5

st.title("✏️ Edit property")

if "selected_property" not in st.session_state:
    st.info("Pick a property in the gallery first.")
    if st.button("Back to gallery", type="primary"):
        st.switch_page("app_pages/gallery.py")
    st.stop()

listing = get_property(st.session_state.selected_property)

if listing is None:
    st.info("This property isn't listed any more.")
    if st.button("Back to gallery", type="primary"):
        st.switch_page("app_pages/gallery.py")
    st.stop()

# The photos are changed right away, one button per photo.
st.subheader("Photos")
photos = get_photos(listing["id"])
columns = st.columns(PHOTO_COLUMNS)
index = 0
for photo in photos:
    with columns[index % PHOTO_COLUMNS]:
        st.image(photo["path"], width="stretch")
        if index == 0:
            st.caption("Cover photo")
        # Every listing needs at least one photo, so the last one can't be removed.
        if st.button("Remove", key="remove_" + str(photo["id"]), disabled=len(photos) == 1):
            delete_photo(photo["id"])
            st.rerun()
    index = index + 1

# Pick the old offer and type in the boxes, so nothing changes unless you change it.
offer_index = 0
if listing["offer"] == "rent":
    offer_index = 1
type_index = 0
if listing["type"] == "villa":
    type_index = 1

st.subheader("Details")
with st.form("edit_property"):
    title = st.text_input("Title", value=listing["title"])
    description = st.text_area("Description", value=listing["description"])
    offer_choice = st.radio("Offer", ["For sale", "For rent"], index=offer_index, horizontal=True)
    property_type = st.selectbox("Type", ["apartment", "villa"], index=type_index)
    area = st.number_input("Area (m²)", min_value=1, value=listing["area"], step=1)
    address = st.text_input("Address", value=listing["address"])
    price = st.number_input("Price in EGP (the total for sale, or per month for rent)", min_value=1, value=listing["price"], step=1000)
    rooms = st.number_input("Rooms", min_value=1, value=listing["rooms"], step=1)
    image_files = st.file_uploader(
        "Add photos (up to " + str(MAX_PHOTOS) + " in total, " + str(MAX_IMAGE_MB) + " MB each)",
        type=["png", "jpg", "jpeg", "webp"],
        accept_multiple_files=True,
        max_upload_size=MAX_IMAGE_MB,
    )
    pressed = st.form_submit_button("Save changes", type="primary")

if pressed:
    offer = "sale"
    if offer_choice == "For rent":
        offer = "rent"

    if title.strip() == "" or description.strip() == "" or address.strip() == "":
        st.error("Please fill in the title, the description and the address.")
    # People signed for "buy" or "rent", so that can't change under them.
    elif offer != listing["offer"] and (listing["status"] != "available" or has_waiting_contracts(listing["id"])):
        st.error("You can't switch between sale and rent while the place is taken or contracts are waiting.")
    elif len(photos) + len(image_files) > MAX_PHOTOS:
        st.error("A listing can have at most " + str(MAX_PHOTOS) + " photos. Remove some first.")
    else:
        update_property(
            listing["id"], title.strip(), description.strip(), offer, property_type, area, address.strip(), price, rooms
        )
        for image_file in image_files:
            add_photo(listing["id"], image_file)
        # Go back to the listing, so you can see your changes.
        st.switch_page("app_pages/property_details.py")

if st.button("Cancel"):
    st.switch_page("app_pages/property_details.py")
