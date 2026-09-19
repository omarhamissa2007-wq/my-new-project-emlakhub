CREATE TABLE property (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    area VARCHAR(255),
    type VARCHAR(255),
    address VARCHAR(255),
    price DECIMAL(10,2),
    number_of_rooms INTEGER,
    img_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- alter table property add column img_url TEXT;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    dob DATE,
    phone VARCHAR(255),
    ssn VARCHAR(255) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tenant_contract (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    card_number TEXT,
    contract_type TEXT,
    property_id INTEGER,
    property_type TEXT,
    property_price TEXT,
    property_address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

delete from property where id = 18;