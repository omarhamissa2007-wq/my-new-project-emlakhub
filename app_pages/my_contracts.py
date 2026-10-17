import streamlit as st

from services.contract_service import get_user_contracts, read_signed_contract

st.title("📄 My contracts")

user = st.session_state.user
contracts = get_user_contracts(user["id"])

if len(contracts) == 0:
    st.info("You haven't signed a contract yet. Open a property in the gallery to sign one.")
    if st.button("Go to gallery", type="primary"):
        st.switch_page("app_pages/gallery.py")
    st.stop()

for contract in contracts:
    with st.container(border=True):
        # The property title is empty when the property was deleted after the contract was signed.
        property_title = contract["property_title"]
        if property_title is None:
            property_title = "(deleted property)"

        if contract["status"] == "pending":
            st.badge("Waiting for the admin", icon="⏳", color="orange")
        elif contract["status"] == "approved":
            st.badge("Approved", icon="✅", color="green")
        else:
            st.badge("Rejected", icon="❌", color="red")

        st.subheader("Contract " + str(contract["id"]) + " · " + contract["contract_type"])
        st.write("**Property:** " + property_title)
        st.write("**Signed on:** " + contract["created_at"])

        pdf = read_signed_contract(contract["signed_pdf"])
        if pdf is None:
            st.caption("The signed PDF is missing.")
        else:
            st.download_button(
                "Download signed PDF",
                data=pdf,
                file_name="contract_" + str(contract["id"]) + ".pdf",
                mime="application/pdf",
                key="pdf_" + str(contract["id"]),
            )
