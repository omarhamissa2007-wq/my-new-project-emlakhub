# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

EmlakHub is a real-estate listings and contracts app built with Streamlit (pinned in `requirements.txt`) and SQLite. `README.md` explains how it works and lists the **Limits** the owner chose. Read the Limits before "fixing" anything, because those trade-offs were made on purpose. Issues are tracked in `ISSUES.md` (close them with `closes #N`).

## Running

```bash
streamlit run app.py        # serves on http://localhost:8501
```

Run it from the repo root. The DB (`database/emlakhub.db`) and file paths (`data/uploads/...`, `data/contracts/...`, `assets/documents/...`) are relative.

There is no test suite. To check a change, use `streamlit.testing.v1.AppTest.from_file("app.py")`. Set `at.session_state.user` (and `selected_property`) and call `at.run()` before `at.switch_page("app_pages/x.py")`, because the menu is built from session state. Run it against a **copy** of the project with `database/emlakhub.db` deleted, since the screens write to the DB and to `data/`. AppTest can't upload files, so check uploads (add property, signed contract) in a real browser.

## Architecture

- **`app.py` runs before every page.** It calls `create_tables()`, which runs `database/schema.sql` (all `CREATE TABLE IF NOT EXISTS`) and loads `database/seed.sql` when `property` is empty. It then builds the `st.navigation` menu from `st.session_state.user`. A page that isn't in the menu can't be opened, so the screens don't check roles themselves. `property_details.py`, `contract.py` and `edit_property.py` (admin) are registered with `visibility="hidden"` and reached with `st.switch_page`.
- **Screens live in `app_pages/`, never `pages/`.** A `pages/` folder would turn Streamlit's auto-listed sidebar back on and bypass the role menu.
- **`services/`** holds every function, one file per topic: `database.py` (`connect`, `create_tables`), `user_service.py`, `property_service.py` (listings, filters, `format_price`), `photo_service.py`, `contract_service.py` (including `approve_contract`, which also rejects the other pending contracts and marks the property sold or rented). Each function opens a connection, does one thing and closes it. Rows are `sqlite3.Row`, so they're read like `row["price"]`.
- **Session state:**
  - `user` is `None` or a dict of the `users` row (`id`, `name`, `email`, `phone`, `ssn`, `is_admin`, ...).
  - `selected_property` is the `property.id` set by a gallery card.
- **After log in, sign up or log out, call `st.rerun()`** so `app.py` rebuilds the menu. Log out is `st.session_state.clear()` then `st.rerun()`.
- **Log in, sign up, add property and edit property use `st.form`.** In Streamlit 1.64, tabbing out of a `type="password"` box onto its eye toggle and then clicking a plain button drops the password, so keep forms on any screen with a password field. Add and edit property switch to the details page after saving. Leaving the page empties the form, so a second click can't save twice, and a failed check keeps what the admin typed (don't use `clear_on_submit`). `contract.py` can't be a form, because it has a download button.
- **Data rules:**
  - `property.offer` is `sale` or `rent`, and `price` is the total or the monthly rent. Always show it with `format_price(price, offer)`.
  - `property.status` is `available`, `sold` or `rented`.
  - `contracts.contract_type` follows the offer (`sale` → `ownership`, `rent` → `tenant`).
  - `contracts.status` is `pending`, `approved` or `rejected`.
  - Photo files are named after their row (`data/uploads/photo_<id>.<ext>`). The seed photos keep their old `property_<hex>` names.
  - Approve and reject only touch `pending` contracts (an old page can't double-approve). The admin can't open `contract.py`, and the offer can't change while a listing is taken or has waiting contracts.
  - `photos` holds 1–5 rows per property. The lowest `id` is the cover (`get_cover_photo`). Every listing must keep at least one photo.
  - `price` and `area` are integers.
- The first user is admin (`is_admin = 1`, set in `add_user`).

## Kid-simple rules (keep these)

This code is kept simple enough for a curious 12-year-old to read top to bottom.

- Plain variables, `if`s and loops, and functions with verb names. No classes, decorators, type hints, comprehensions, lambdas or generators.
- One short comment, in kid words, above anything a kid would ask "why?" about. Constants go at the top of the file in CAPITALS, with a comment saying why.
- Repeating a few lines is fine if it keeps a screen readable on its own (the "pick a property first" check is in both `property_details.py` and `contract.py`).
- Use plain `if` checks with a friendly `st.error` for problems a user will actually hit (empty fields, email or national ID already used, card not 16 digits, no file). Don't add `try`/`except`. Design inside limits instead, e.g. `max_upload_size` on uploaders.
- Use the standard library first. The only installed library is `streamlit`. A new one has to do something plain code can't do in about 10 lines, and it gets pinned in `requirements.txt`.
- Hide what a user can't use (via the menu in `app.py`) instead of showing it and refusing.
- Give each screen one `type="primary"` button for its main action, and use friendly sentence-case labels with icons on menu items.
- SQL stays as readable text: the schema in `database/schema.sql`, and queries as plain strings with `?` placeholders.
- Every new shortcut that removes safety or capability goes in the README's **Limits** section.

## Docs

`docs/` holds the competition kit: `emlakhub-documentation.md` (+ PDF), the poster, the slide deck, the diagrams and real screenshots, all in the logo's navy and gold (`docs/assets/brand.css`). Rebuild with `python docs/build.py`, which needs `playwright` and `markdown-it-py`. Those are not app dependencies, so they stay out of `requirements.txt`. Yellow ✏️ boxes are for the student to fill in. `docs/tables.md` lists the tables. Keep the docs and screenshots in step with the code when screens, tables or files change.
