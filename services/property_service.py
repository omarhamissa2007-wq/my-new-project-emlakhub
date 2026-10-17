from services.contract_service import reject_waiting_contracts
from services.database import connect
from services.photo_service import delete_all_photos


def get_properties(search, offer, property_type, min_rooms, max_price):
    # We start with a question that matches every listing, then add one rule for each filter that is set.
    # An empty search makes the pattern "%%", which matches everything.
    pattern = "%" + search + "%"
    sql = "SELECT * FROM property WHERE (title LIKE ? OR address LIKE ?)"
    values = [pattern, pattern]

    if offer != "all":
        sql = sql + " AND offer = ?"
        values.append(offer)
    if property_type != "all":
        sql = sql + " AND type = ?"
        values.append(property_type)
    if min_rooms > 0:
        sql = sql + " AND rooms >= ?"
        values.append(min_rooms)
    if max_price > 0:
        sql = sql + " AND price <= ?"
        values.append(max_price)

    # Newest listings first.
    sql = sql + " ORDER BY id DESC"

    connection = connect()
    properties = connection.execute(sql, values).fetchall()
    connection.close()
    return properties


def get_property(property_id):
    connection = connect()
    found = connection.execute("SELECT * FROM property WHERE id = ?", (property_id,)).fetchone()
    connection.close()
    return found


def add_property(title, description, offer, property_type, area, address, price, rooms):
    connection = connect()
    cursor = connection.execute(
        "INSERT INTO property (title, description, offer, type, area, address, price, rooms) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (title, description, offer, property_type, area, address, price, rooms),
    )
    property_id = cursor.lastrowid
    connection.commit()
    connection.close()
    # The new listing's number, so its photos can be saved under it.
    return property_id


def update_property(property_id, title, description, offer, property_type, area, address, price, rooms):
    connection = connect()
    connection.execute(
        "UPDATE property SET title = ?, description = ?, offer = ?, type = ?, area = ?, address = ?, price = ?, rooms = ? WHERE id = ?",
        (title, description, offer, property_type, area, address, price, rooms, property_id),
    )
    connection.commit()
    connection.close()


def set_property_status(property_id, status):
    connection = connect()
    connection.execute("UPDATE property SET status = ? WHERE id = ?", (status, property_id))
    connection.commit()
    connection.close()


def delete_property(property_id):
    # The photos go too, so old photos don't pile up in the uploads folder.
    delete_all_photos(property_id)

    # Anyone still waiting for this place can't get it any more.
    reject_waiting_contracts(property_id)

    connection = connect()
    connection.execute("DELETE FROM property WHERE id = ?", (property_id,))
    connection.commit()
    connection.close()


def format_price(price, offer):
    # The :, puts commas in big numbers, so 8300000 shows as 8,300,000.
    text = f"{price:,} EGP"
    # A rent price is paid every month, so we say so.
    if offer == "rent":
        text = text + " / month"
    return text
