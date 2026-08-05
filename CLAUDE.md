# Design Themes — Upstream Checkout

This repository is currently a **pristine checkout of upstream
`odoo/design-themes` 19.0** (~30 website/design theme modules). There is no
fork branch: no local work has landed here.

> This repo is deployed as one checkout inside a larger workspace. Environment
> setup, launch commands, and addons_path priority live in that workspace's
> root `CLAUDE.md` — wherever the checkouts are assembled.

- Treat it as read-mostly: it participates in the addons_path but carries no
  local changes.
- **Never commit to `19.0`** — it must stay in sync with upstream, and local
  commits would break the next pull.
- If fork work ever starts here, adopt the branch model of the sibling
  `odoo`/`enterprise` repos (`19.0` = pristine upstream mirror, `19.0-marin` =
  active line, per-task feature branches via PR) and the canonical
  `doc/coding_guidelines.rst` in the `odoo` repo.
