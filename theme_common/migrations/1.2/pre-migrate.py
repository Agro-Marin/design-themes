from odoo.addons.theme_common.legacy_assets import remove_assets


def migrate(cr, version):
    if not version:
        return
    remove_assets(cr, r"^/?theme_common/static/")
