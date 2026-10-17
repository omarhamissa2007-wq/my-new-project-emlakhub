import streamlit as st

from services.contract_service import has_pending_contract
from services.photo_service import get_photos
from services.property_service import delete_property, format_price, get_property, set_property_status

# Small photos under the big cover photo, this many in a row.
THUMB_COLUMNS = 4

st.title("🏘️ Property details")

user = st.session_state.user

# You get here from a card in the gallery. Without one picked, there's nothing to show.
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

is_admin = user is not None and user["is_admin"] == 1
photos = get_photos(listing["id"])

left, right = st.columns(2)

with left:
    # The first photo is the cover, shown big. The rest go in a row underneath.
    st.image(photos[0]["path"], width="stretch")
    thumbs = st.columns(THUMB_COLUMNS)
    index = 0
    for photo in photos[1:]:
        with thumbs[index % THUMB_COLUMNS]:
            st.image(photo["path"], width="stretch")
        index = index + 1

with right:
    if listing["status"] == "sold":
        st.badge("SOLD", color="red")
    elif listing["status"] == "rented":
        st.badge("RENTED", color="orange")
    elif listing["offer"] == "rent":
        st.badge("For rent", color="blue")
    else:
        st.badge("For sale", color="green")

    st.subheader(listing["title"])
    if listing["description"] != "":
        st.write(listing["description"])
    st.write("**Price:** " + format_price(listing["price"], listing["offer"]))
    st.write("**Type:** " + listing["type"])
    st.write("**Address:** " + listing["address"])
    st.write("**Rooms:** " + str(listing["rooms"]))
    st.write("**Area:** " + str(listing["area"]) + " m²")
    st.divider()

    # Who sees which button:
    # a taken place can't be signed for, guests must log in, the admin doesn't sign,
    # and a user who already applied waits for the admin.
    if listing["status"] != "available":
        st.info("This property is already " + listing["status"] + ".")
    elif user is None:
        st.info("Log in or sign up to buy or rent this property.")
    elif not is_admin:
        if has_pending_contract(user["id"], listing["id"]):
            st.info("You already applied for this property. You'll see the answer in **My contracts**.")
        elif st.button("✍️ Sign a contract", type="primary", width="stretch"):
            st.switch_page("app_pages/contract.py")

    if st.button("Back to gallery", width="stretch"):
        st.switch_page("app_pages/gallery.py")

    if is_admin:
        st.divider()
        st.write("**Admin**")
        if st.button("✏️ Edit property", width="stretch"):
            st.switch_page("app_pages/edit_property.py")

        if listing["status"] != "available":
            if st.button("🔓 Mark available again", width="stretch"):
                set_property_status(listing["id"], "available")
                st.rerun()

        # The tick box stops a delete by accident.
        sure = st.checkbox("Yes, delete this property for good")
        if st.button("🗑️ Delete property", disabled=not sure, width="stretch"):
            delete_property(listing["id"])
            del st.session_state.selected_property
            st.switch_page("app_pages/gallery.py")
