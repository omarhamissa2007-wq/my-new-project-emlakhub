import streamlit as st

from services.contract_service import add_contract, has_pending_contract, read_blank_contract
from services.photo_service import get_cover_photo
from services.property_service import format_price, get_property

# A signed PDF bigger than this is almost always a phone photo saved wrongly.
MAX_PDF_MB = 5
# Bank cards in Egypt have 16 digits.
CARD_DIGITS = 16

st.title("✍️ Contract")

user = st.session_state.user

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

# The admin runs the shop, so the admin doesn't sign contracts.
if user["is_admin"] == 1:
    st.info("The admin can't sign contracts.")
    st.stop()

# Someone else may have bought it, or you may have applied already, since you opened the listing.
if listing["status"] != "available":
    st.info("This property is already " + listing["status"] + ".")
    st.stop()

if has_pending_contract(user["id"], listing["id"]):
    st.success("Your contract is saved and waiting for the admin. You'll see the answer in **My contracts**.")
    st.stop()

# Buying needs an ownership contract. Renting needs a tenant contract.
contract_type = "ownership"
if listing["offer"] == "rent":
    contract_type = "tenant"

left, right = st.columns(2)

with right:
    st.subheader(listing["title"])
    st.image(get_cover_photo(listing["id"]), width="stretch")
    st.write("**Price:** " + format_price(listing["price"], listing["offer"]))
    st.write("**Address:** " + listing["address"])

with left:
    st.subheader("1. Your details")
    # We fill these in from your account. You can change them for this contract.
    name = st.text_input("Full name", value=user["name"])
    phone = st.text_input("Phone number", value=user["phone"])
    email = st.text_input("Email", value=user["email"])
    card_number = st.text_input("Card number (" + str(CARD_DIGITS) + " digits)")
    if contract_type == "ownership":
        st.write("You are **buying** this property, so you sign an **ownership** contract.")
    else:
        st.write("You are **renting** this property, so you sign a **tenant** contract.")

    st.subheader("2. Download, print and sign")
    st.download_button(
        "📃 Download the blank " + contract_type + " contract",
        data=read_blank_contract(contract_type),
        file_name=contract_type + "_contract.pdf",
        mime="application/pdf",
    )

    st.subheader("3. Upload the signed contract")
    signed_pdf = st.file_uploader(
        "Signed contract (PDF, up to " + str(MAX_PDF_MB) + " MB)",
        type=["pdf"],
        max_upload_size=MAX_PDF_MB,
    )

    if st.button("Save contract", type="primary", width="stretch"):
        card_number = card_number.replace(" ", "")
        if name.strip() == "" or phone.strip() == "" or email.strip() == "":
            st.error("Please fill in your name, phone and email.")
        elif "@" not in email:
            st.error("That email doesn't look right. It needs an @.")
        # isascii makes sure the digits are the 0-9 kind a bank card uses.
        elif not card_number.isascii() or not card_number.isdigit() or len(card_number) != CARD_DIGITS:
            st.error("The card number should be " + str(CARD_DIGITS) + " digits.")
        elif signed_pdf is None:
            st.error("Please upload the signed contract first.")
        else:
            add_contract(
                user["id"],
                listing["id"],
                contract_type,
                name.strip(),
                phone.strip(),
                email.strip(),
                card_number,
                signed_pdf,
            )
            # Rerun, so the page shows the "waiting for the admin" message from the top.
            st.rerun()
