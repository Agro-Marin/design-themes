"""Delete the asset rows of the legacy stylesheets the themes no longer ship.

Dropping a theme's `<asset>` records lets `_process_end` delete the
`theme.ir.asset` templates, but not the per-website `ir.asset` copies: their
`theme_template_id` is set to NULL and they survive until the theme is next
loaded on that website. Rows the saas-11.4 upgrade converted from views never
had a template, so nothing ever sweeps them. A row left pointing at a deleted
file breaks its bundle the moment it is active, so they go by path, in both
tables, with their ir.model.data.
"""

import logging

from odoo.tools import SQL

_logger = logging.getLogger(__name__)

LEGACY_THEME_ASSETS = r"static/src/(old_snippets/|scss/compatibility-saas-)"


def delete_assets(cr, path_pattern):
    for table, model in (
        ("ir_asset", "ir.asset"),
        ("theme_ir_asset", "theme.ir.asset"),
    ):
        cr.execute(
            SQL(
                "DELETE FROM %s WHERE path ~ %s RETURNING id",
                SQL.identifier(table),
                path_pattern,
            )
        )
        ids = [row[0] for row in cr.fetchall()]
        if not ids:
            continue
        cr.execute(
            SQL(
                "DELETE FROM ir_model_data WHERE model = %s AND res_id = ANY(%s)",
                model,
                ids,
            )
        )
        _logger.info("Deleted %s %s rows matching %s", len(ids), model, path_pattern)


def delete_legacy_theme_assets(cr, module):
    delete_assets(cr, rf"^/?{module}/{LEGACY_THEME_ASSETS}")
