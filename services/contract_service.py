import os

from services.database import connect

# The empty contracts people download and print.
BLANK_CONTRACTS_FOLDER = "assets/documents"
# The signed contracts people upload. Each one is saved under its contract number.
SIGNED_CONTRACTS_FOLDER = "data/contracts"


def read_blank_contract(contract_type):
    # There is one blank PDF for buying (ownership) and one for renting (tenant).
    with open(BLANK_CONTRACTS_FOLDER + "/" + contract_type + "_contract.pdf", "rb") as pdf_file:
        return pdf_file.read()


def add_contract(user_id, property_id, contract_type, name, phone, email, card_number, signed_pdf_file):
    connection = connect()
    cursor = connection.execute(
        "INSERT INTO contracts (user_id, property_id, contract_type, name, phone, email, card_number) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (user_id, property_id, contract_type, name, phone, email, card_number),
    )
    contract_id = cursor.lastrowid

    # The signed PDF is saved with the contract's number in its name, so two customers never overwrite each other.
    os.makedirs(SIGNED_CONTRACTS_FOLDER, exist_ok=True)
    path = SIGNED_CONTRACTS_FOLDER + "/contract_" + str(contract_id) + ".pdf"
    with open(path, "wb") as saved_file:
        saved_file.write(signed_pdf_file.getvalue())

    connection.execute("UPDATE contracts SET signed_pdf = ? WHERE id = ?", (path, contract_id))
    connection.commit()
    connection.close()


def has_pending_contract(user_id, property_id):
    connection = connect()
    found = connection.execute(
        "SELECT id FROM contracts WHERE user_id = ? AND property_id = ? AND status = 'pending'",
        (user_id, property_id),
    ).fetchone()
    connection.close()
    return found is not None


def has_waiting_contracts(property_id):
    connection = connect()
    found = connection.execute(
        "SELECT id FROM contracts WHERE property_id = ? AND status = 'pending'", (property_id,)
    ).fetchone()
    connection.close()
    return found is not None


def reject_waiting_contracts(property_id):
    connection = connect()
    connection.execute(
        "UPDATE contracts SET status = 'rejected' WHERE property_id = ? AND status = 'pending'", (property_id,)
    )
    connection.commit()
    connection.close()


def approve_contract(contract_id):
    connection = connect()
    contract = connection.execute("SELECT * FROM contracts WHERE id = ?", (contract_id,)).fetchone()

    # If the page was old and someone already decided this contract, we leave it alone.
    if contract is None or contract["status"] != "pending":
        connection.close()
        return

    connection.execute("UPDATE contracts SET status = 'approved' WHERE id = ?", (contract_id,))

    # Buying makes the place sold. Renting makes it rented.
    new_status = "sold"
    if contract["contract_type"] == "tenant":
        new_status = "rented"
    connection.execute("UPDATE property SET status = ? WHERE id = ?", (new_status, contract["property_id"]))

    connection.commit()
    connection.close()

    # Only one person can buy or rent a place, so everyone else still waiting for it is turned down.
    reject_waiting_contracts(contract["property_id"])


def reject_contract(contract_id):
    connection = connect()
    # Only a contract that is still waiting can be rejected.
    connection.execute("UPDATE contracts SET status = 'rejected' WHERE id = ? AND status = 'pending'", (contract_id,))
    connection.commit()
    connection.close()


def get_contracts():
    connection = connect()
    # LEFT JOIN keeps a contract on the list even after its property was deleted (the title is then empty).
    contracts = connection.execute(
        "SELECT contracts.*, property.title AS property_title FROM contracts "
        "LEFT JOIN property ON property.id = contracts.property_id ORDER BY contracts.id DESC"
    ).fetchall()
    connection.close()
    return contracts


def get_user_contracts(user_id):
    connection = connect()
    contracts = connection.execute(
        "SELECT contracts.*, property.title AS property_title FROM contracts "
        "LEFT JOIN property ON property.id = contracts.property_id "
        "WHERE contracts.user_id = ? ORDER BY contracts.id DESC",
        (user_id,),
    ).fetchall()
    connection.close()
    return contracts


def read_signed_contract(path):
    # Someone may have removed the file by hand, so we check it is still there.
    if not os.path.exists(path):
        return None
    with open(path, "rb") as pdf_file:
        return pdf_file.read()
