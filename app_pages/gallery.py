import streamlit as st

from services.photo_service import get_cover_photo
from services.property_service import format_price, get_properties

# Three cards in a row leaves room for the photo and the details.
COLUMNS = 3

st.title("🏠 EmlakHub")
st.write("Apartments and villas for sale or rent. Open one to see more and sign a contract.")

search = st.text_input("Search", placeholder="Type a title or an area, like New Cairo")

offer_box, type_box, rooms_box, price_box = st.columns(4)
with offer_box:
    offer_choice = st.selectbox("For", ["All", "For sale", "For rent"])
with type_box:
    type_choice = st.selectbox("Type", ["All", "Apartment", "Villa"])
with rooms_box:
    min_rooms = st.number_input("At least this many rooms", min_value=0, value=0, step=1)

# Turn the friendly words in the boxes into the words saved in the database.
offer = "all"
if offer_choice == "For sale":
    offer = "sale"
if offer_choice == "For rent":
    offer = "rent"

property_type = "all"
if type_choice == "Apartment":
    property_type = "apartment"
if type_choice == "Villa":
    property_type = "villa"

# A sale price (millions) and a monthly rent can't be compared,
# so the price box only shows up after you pick sale or rent.
max_price = 0
with price_box:
    if offer == "sale":
        max_price = st.number_input("Max price (EGP, 0 = any)", min_value=0, value=0, step=500000)
    if offer == "rent":
        max_price = st.number_input("Max rent per month (EGP, 0 = any)", min_value=0, value=0, step=1000)

properties = get_properties(search.strip(), offer, property_type, min_rooms, max_price)

if len(properties) == 0:
    st.info("Nothing matches. Try another word or fewer filters.")
    user = st.session_state.user
    if user is not None and user["is_admin"] == 1:
        st.write("You can add a listing from **Add property** in the menu.")
    st.stop()

st.caption(str(len(properties)) + " listings")

columns = st.columns(COLUMNS)
index = 0
for listing in properties:
    # Cards fill the columns left to right, then start again on the next row.
    with columns[index % COLUMNS]:
        with st.container(border=True):
            st.image(get_cover_photo(listing["id"]), width="stretch")

            if listing["status"] == "sold":
                st.badge("SOLD", color="red")
            elif listing["status"] == "rented":
                st.badge("RENTED", color="orange")
            elif listing["offer"] == "rent":
                st.badge("For rent", color="blue")
            else:
                st.badge("For sale", color="green")

            st.subheader(listing["title"])
            st.write("**Price:** " + format_price(listing["price"], listing["offer"]))
            st.write("**Address:** " + listing["address"])
            st.write("**Rooms:** " + str(listing["rooms"]) + " · **Area:** " + str(listing["area"]) + " m²")
            if st.button("View details", key="details_" + str(listing["id"]), width="stretch"):
                st.session_state.selected_property = listing["id"]
                st.switch_page("app_pages/property_details.py")
    index = index + 1
