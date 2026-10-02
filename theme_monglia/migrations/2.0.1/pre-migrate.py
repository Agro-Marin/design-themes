from odoo.addons.theme_common.legacy_assets import delete_legacy_theme_assets


def migrate(cr, version):
    if not version:
        return
    delete_legacy_theme_assets(cr, "theme_monglia")
