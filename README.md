# EmlakHub

EmlakHub is a small real-estate website. You can browse apartments and villas for sale or for rent, filter them, open one to see its photos and details, and sign a contract to buy it (ownership) or rent it (tenant). The admin adds, edits and deletes listings, approves or rejects contracts, and sees every user.

## What each person can do

| Who | What they see in the menu |
| --- | --- |
| Guest | Gallery (with search and filters), property details, Log in, Sign up |
| User | Gallery, My contracts (with each contract's status), Log out. On an available listing: **Sign a contract** |
| Admin | Gallery, Add property, Users, All contracts (with **Approve** and **Reject**), Log out. On a listing: **Edit property**, **Mark available again**, **Delete property** |

The very first person who signs up becomes the admin. Everyone after that is a normal user.

## How it works

- `app.py` runs first every time. It makes the database tables (and adds the 50 starter listings if the gallery is empty), then builds the menu for whoever is logged in. Pages that aren't in your menu can't be opened.
- `app_pages/` holds the screens. Each one is a plain script that runs top to bottom.
- `services/` holds every function, one file per topic. `database.py` opens the database and makes the tables. `user_service.py`, `property_service.py` and `contract_service.py` each do one job, like adding a user or saving a contract.
- `database/schema.sql` describes the four tables (`users`, `property`, `photos`, `contracts`). `database/seed.sql` holds the 50 starter listings (all for sale) and their photos.
- Each listing is either **for sale** (the price is the total) or **for rent** (the price is per month). Each one has 1 to 5 photos, and the first one is the cover.
- Property photos are saved in `data/uploads/`. Signed contracts are saved in `data/contracts/` as `contract_<number>.pdf`. The blank contracts people download are in `assets/documents/`.

Signing a contract takes three steps on one screen:

1. Check your details (they're filled in from your account) and type your card number. The contract type comes from the listing: buying means an ownership contract, renting means a tenant contract.
2. Download the blank PDF, print it and sign it.
3. Upload the signed PDF and press **Save contract**.

What happens to a contract next:

- It starts as **waiting**. While you have one waiting for a listing, you can't sign another for the same one.
- The admin **approves** or **rejects** it. Approving one marks the listing **sold** or **rented** and rejects everyone else still waiting for it.
- Sold and rented listings stay in the gallery with a badge, but nobody can sign for them. When a lease ends, the admin presses **Mark available again**.
- Deleting a listing rejects every contract still waiting for it.

## Run it

You need Python 3.10 or newer.

```bash
pip install -r requirements.txt
streamlit run app.py
```

Run it from this folder, because the database and photo paths are relative. Then open http://localhost:8501.

To start over with an empty database, delete `database/emlakhub.db` and run the app again. It makes fresh tables and adds the 50 starter listings. The next person to sign up becomes the admin.

## Deploy it

On [Streamlit Community Cloud](https://streamlit.io/cloud), point a new app at this repo with `app.py` as the main file. It needs no secrets.

The cloud's disk is wiped when the app restarts, so new users, listings and contracts disappear and the app goes back to what's committed in git.

## Limits

These were chosen on purpose to keep the code simple. Read them before "fixing" anything.

- **Passwords are stored as plain text.** Anyone who opens `database/emlakhub.db` can read them. Don't reuse a real password here.
- **National ID numbers and card numbers are stored as plain text** too. Nothing is paid and nothing is checked with a bank. The card number only has to be 16 digits.
- **The database file is committed to git.** Every account and contract you make locally ends up on GitHub when you push.
- **The first person to sign up is the admin, forever.** There's no screen to make someone else admin. To change it, edit `is_admin` in the database or start a fresh database.
- **No email is sent.** After a contract is saved, the app says it's waiting for the admin. The user sees the answer in **My contracts**.
- **Nobody checks the signed PDF.** Any PDF up to 5 MB is accepted.
- **The admin can't explain a rejection.** The user only sees "Rejected".
- **Sale or rent is locked while it matters.** The admin can't switch a listing between sale and rent while it's sold, rented or has contracts waiting.
- **Old approved contracts stay approved.** After **Mark available again**, the earlier contract still shows as approved, as history.
- **One price per listing.** A place is either for sale or for rent, never both.
- **The cover photo is always the oldest photo.** To change it, remove photos until the one you want is first.
- **Uploads are capped at 5 MB** (photos and PDFs) instead of being resized.
- **Deleting a property is permanent.** Its photos are deleted too (for a starter listing that also removes a committed file from `data/uploads/`). Contracts for it stay, but show "(deleted property)".
- **Search is a simple "contains" match** on the title and address. The max-price filter only shows up after you pick sale or rent, because a total price and a monthly rent can't be compared.
- **The 50 starter listings have no description.** Their titles were made from their rooms, type and area. Editing one means writing a description, because it's required.
- **No `try`/`except`.** If a file is missing or the disk is full, Streamlit shows its own error box.
- **Log in, Sign up, Add property and Edit property use a form** (`st.form`). In Streamlit 1.64, pressing Tab out of a password box and then clicking the button loses the password. A form sends every box at once, so this can't happen.
