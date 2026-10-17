import streamlit as st

from services.contract_service import approve_contract, get_contracts, read_signed_contract, reject_contract

st.title("📑 All contracts")

contracts = get_contracts()

if len(contracts) == 0:
    st.info("No one has signed a contract yet.")
    st.stop()

# Contracts waiting for an answer go first, so the admin sees the work to do.
pending = []
decided = []
for contract in contracts:
    if contract["status"] == "pending":
        pending.append(contract)
    else:
        decided.append(contract)

st.write(str(len(pending)) + " waiting for your answer · " + str(len(decided)) + " decided")

for contract in pending + decided:
    with st.container(border=True):
        # The property title is empty when the property was deleted after the contract was signed.
        property_title = contract["property_title"]
        if property_title is None:
            property_title = "(deleted property)"

        if contract["status"] == "pending":
            st.badge("Waiting", icon="⏳", color="orange")
        elif contract["status"] == "approved":
            st.badge("Approved", icon="✅", color="green")
        else:
            st.badge("Rejected", icon="❌", color="red")

        st.subheader("Contract " + str(contract["id"]) + " · " + contract["contract_type"])
        st.write("**Property:** " + property_title)
        st.write("**Customer:** " + contract["name"] + " · " + contract["phone"] + " · " + contract["email"])
        st.write("**Card:** " + contract["card_number"])
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

        # Approving one contract marks the place sold or rented and turns down everyone else waiting for it.
        if contract["status"] == "pending" and contract["property_title"] is not None:
            approve_box, reject_box = st.columns(2)
            with approve_box:
                if st.button("✅ Approve", key="approve_" + str(contract["id"]), width="stretch"):
                    approve_contract(contract["id"])
                    st.rerun()
            with reject_box:
                if st.button("❌ Reject", key="reject_" + str(contract["id"]), width="stretch"):
                    reject_contract(contract["id"])
                    st.rerun()
