from odoo.addons.theme_common.legacy_assets import delete_assets


def migrate(cr, version):
    if not version:
        return
    delete_assets(cr, r"^/?theme_common/static/")
