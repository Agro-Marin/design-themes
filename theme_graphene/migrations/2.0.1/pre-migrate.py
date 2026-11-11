from odoo.addons.theme_common.legacy_assets import remove_legacy_theme_assets


def migrate(cr, version):
    if not version:
        return
    remove_legacy_theme_assets(cr, "theme_graphene")
