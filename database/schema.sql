-- The four tables EmlakHub needs. app.py runs this file every time it starts.
-- "IF NOT EXISTS" means a table that is already there is left alone.

-- Everyone who signs up. The first person gets is_admin = 1.
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    ssn TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    is_admin INTEGER NOT NULL DEFAULT 0,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- Every apartment and villa in the gallery.
-- offer is 'sale' (price is the total) or 'rent' (price is per month), both in Egyptian pounds.
-- status is 'available', 'sold' or 'rented'. Area is in square metres.
CREATE TABLE IF NOT EXISTS property (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL DEFAULT '',
    offer TEXT NOT NULL DEFAULT 'sale',
    type TEXT NOT NULL,
    area INTEGER NOT NULL,
    address TEXT NOT NULL,
    price INTEGER NOT NULL,
    rooms INTEGER NOT NULL,
    status TEXT NOT NULL DEFAULT 'available',
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- The photos of each property (1 to 5). The one added first is the cover photo.
CREATE TABLE IF NOT EXISTS photos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    path TEXT NOT NULL
);

-- A signed contract: who signed it, for which property, where the signed PDF is, and what the admin decided.
-- contract_type is 'ownership' (buying) or 'tenant' (renting). status is 'pending', 'approved' or 'rejected'.
CREATE TABLE IF NOT EXISTS contracts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    property_id INTEGER NOT NULL,
    contract_type TEXT NOT NULL,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL,
    card_number TEXT NOT NULL,
    signed_pdf TEXT NOT NULL DEFAULT '',
    status TEXT NOT NULL DEFAULT 'pending',
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
