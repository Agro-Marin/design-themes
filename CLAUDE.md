# Design Themes — Fork Checkout

30 website/design theme modules, forked from upstream `odoo/design-themes` 19.0.
Fork work **has** started here: this file used to say "no local work has landed",
which was already untrue when it was written, and the local commits sat on `19.0`
where the same file forbade them.

> This repo is deployed as one checkout inside a larger workspace. Environment
> setup, launch commands, and addons_path priority live in that workspace's
> root `CLAUDE.md` — wherever the checkouts are assembled.

## Branch model

The sibling `odoo`/`enterprise` model, now actually adopted rather than deferred:

- **`19.0`** — pristine mirror of Odoo's `19.0`, tracking the fork's copy of it
  (`origin/19.0`), which is what the siblings do. Read-only. **Never commit
  here**; a local commit breaks the next sync and hides itself, because nothing
  in this repository gates a branch.
- **`19.0-marin`** — the active line. All local work lands here.

## Upstream sync is possible here, unlike odoo/ and enterprise/

The workspace posture "there is no upstream merge — a useful upstream fix is
re-implemented by hand" is about repositories that have diverged past the point
of replay. This one has not: the divergence is a handful of commits against a
history that is otherwise upstream's, and upstream's own traffic is almost
entirely Weblate translation refreshes. So sync by rebasing, and keep the
mirror honest:

```bash
git fetch upstream                   # Odoo's
git branch -f 19.0 upstream/19.0     # pointer only; does not touch a checked-out HEAD
git push origin 19.0                 # keep the fork's mirror honest too
git rebase 19.0                      # from 19.0-marin
```

## Two remotes, both branches on the fork

Matching the siblings, `origin` is the AgroMarin fork; `upstream` is Odoo's:

    origin     github.com/Agro-Marin/design-themes    ← push here
    upstream   github.com/odoo/design-themes          ← sync from here

The fork carries `19.0` and `19.0-marin`, and both local branches track it. That
is new as of 2026-08-15: until then the fork held `19.0` alone and the active
line had never been pushed at all, which is not a theoretical exposure. The
`theme_common` snippet port that `odoo`'s `6a7e4c38dd8` recorded in its JS
surface pins (design-themes `b76c148db`) is in this repository's history, its
reflog, `git fsck` and the fork — in none of them. It was lost precisely because
the branch holding it lived on one disk. **Push `19.0-marin` as you go**; nothing
here is generated or recoverable from another checkout.

## This checkout is an input to the odoo repo's gates

`odoo`'s `tooling/architecture/js_public_surface.py` and `js_extension_surface.py`
pin, per consumer scope, which `@web` specifiers and override points each sibling
repository reaches — and one of those scopes is this one. Changing JS here can
therefore make a gate fail *in the `odoo` repo*, and the pins are regenerated
there, from a full workspace:

```bash
python tooling/architecture/js_public_surface.py --update      # in odoo/
python tooling/architecture/js_extension_surface.py --update
```

Those gates are green from `odoo` alone whatever this repo contains — the scope
is simply absent — and red only in a workspace. A drift here is caught by nobody
but the person running Tier 1 from the workspace.

Coding standards are the canonical `doc/coding_guidelines.rst` in the `odoo` repo.
