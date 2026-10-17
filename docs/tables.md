# tables

The real definitions live in `database/schema.sql`.

### users
- id
- name
- email (unique)
- phone
- ssn (national ID, unique)
- password (plain text, see README Limits)
- is_admin (1 for the first person who signs up)
- created_at

### property
- id
- title
- description
- offer (sale or rent)
- type (apartment or villa)
- area (m²)
- address
- price (EGP: the total for sale, per month for rent)
- rooms
- status (available, sold or rented)
- created_at

### photos
- id
- property_id
- path (a file in data/uploads; the first photo is the cover)

### contracts
- id
- user_id
- property_id
- contract_type (ownership or tenant)
- name, phone, email
- card_number
- signed_pdf (a path in data/contracts)
- status (pending, approved or rejected)
- created_at
