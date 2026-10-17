# Issues

Close an issue from a commit message with `closes #N`.

## #1 Kid-simple refactor · refactor · closed

Rebuild EmlakHub so a curious 12-year-old can read it top to bottom.

- `app.py` + `app_pages/` + `services/`, with a role-based `st.navigation` menu (guest / user / admin, first sign-up is admin).
- Fresh `database/emlakhub.db` built from `schema.sql` + `seed.sql` (the 50 listings, image paths fixed, type typos cleaned).
- Working search, login that is remembered, contract flow that saves each signed PDF as `data/contracts/contract_<id>.pdf`.
- Only `streamlit` in `requirements.txt`.
- README with Limits, CLAUDE.md with the kid-simple rules.

## #2 Contract status and sale/rent · feature · closed

- `property.offer` is `sale` or `rent` (price = total or per month). The contract type follows the offer.
- `contracts.status` goes pending → approved / rejected. The admin approves or rejects on All contracts.
- Approving marks the listing sold or rented and rejects the other pending contracts on it. Taken listings keep a SOLD/RENTED badge, and the admin can mark them available again.
- A user can't apply twice for the same listing while a contract is pending. The admin can't sign contracts.

## #3 Better listings · feature · closed

- `name` becomes `title`, plus a required `description`. Seed titles are built from rooms, type and area.
- A `photos` table holds 1–5 photos per listing, and the first one is the cover.
- Gallery filters: sale/rent, type, min rooms, and a max price that appears after picking sale or rent.
- An admin Edit screen changes every field and adds or removes photos.
