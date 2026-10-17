import os

from services.database import connect

# Where every property photo is saved.
UPLOAD_FOLDER = "data/uploads"


def get_photos(property_id):
    connection = connect()
    # Oldest first, so the first photo ever added is the cover.
    photos = connection.execute(
        "SELECT * FROM photos WHERE property_id = ? ORDER BY id", (property_id,)
    ).fetchall()
    connection.close()
    return photos


def get_cover_photo(property_id):
    photos = get_photos(property_id)
    return photos[0]["path"]


def add_photo(property_id, image_file):
    connection = connect()
    cursor = connection.execute("INSERT INTO photos (property_id, path) VALUES (?, '')", (property_id,))
    photo_id = cursor.lastrowid

    # Every photo gets its own row number, so naming the file after it means a new photo never replaces an old one.
    extension = os.path.splitext(image_file.name)[1]
    path = UPLOAD_FOLDER + "/photo_" + str(photo_id) + extension

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    with open(path, "wb") as saved_file:
        saved_file.write(image_file.getvalue())

    connection.execute("UPDATE photos SET path = ? WHERE id = ?", (path, photo_id))
    connection.commit()
    connection.close()


def delete_photo(photo_id):
    connection = connect()
    photo = connection.execute("SELECT * FROM photos WHERE id = ?", (photo_id,)).fetchone()
    if photo is not None and os.path.exists(photo["path"]):
        os.remove(photo["path"])
    connection.execute("DELETE FROM photos WHERE id = ?", (photo_id,))
    connection.commit()
    connection.close()


def delete_all_photos(property_id):
    for photo in get_photos(property_id):
        delete_photo(photo["id"])
