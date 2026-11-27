import logging

from odoo.tools import SQL

_logger = logging.getLogger(__name__)

LEGACY_THEME_ASSETS = r"static/src/(old_snippets/|scss/compatibility-saas-)"


def remove_assets(cr, path_pattern):
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


def remove_legacy_theme_assets(cr, module):
    remove_assets(cr, rf"^/?{module}/{LEGACY_THEME_ASSETS}")
