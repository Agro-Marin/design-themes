import logging

from odoo.tests import TransactionCase, tagged

_logger = logging.getLogger(__name__)


@tagged("post_install", "-at_install")
class TestThemeScope(TransactionCase):
    def test_scope(self):
        websites_themes = self.env["website"].get_test_themes_websites()
        assets_count = 0
        attachments_count = 0
        fails = []
        for website in websites_themes:
            prefix = f"{website.theme_id.name}/"
            slash_prefix = f"/{website.theme_id.name}/"
            theme_module = self.env["ir.module.module"].search(
                [
                    ("name", "=", website.theme_id.name),
                ]
            )
            assets = theme_module._get_module_data("ir.asset")
            fails.extend(
                f"Asset {asset.id} {asset.key} references outside of theme {website.theme_id.name}: {asset.path}"
                for asset in assets
                if not asset.path.startswith((prefix, slash_prefix))
            )
            assets_count += len(assets)
            attachments = theme_module._get_module_data("ir.attachment")
            fails.extend(
                f"Attachment {attachment.id} {attachment.key} references outside of theme {website.theme_id.name}: {attachment.url}"
                for attachment in attachments
                if not attachment.url.startswith(slash_prefix)
            )
            attachments_count += len(attachments)
        _logger.info(
            "Verified %s assets and %s attachments", assets_count, attachments_count
        )
        self.assertFalse(fails, "\n".join(fails))
