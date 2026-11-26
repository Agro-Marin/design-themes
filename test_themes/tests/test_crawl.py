from odoo.tests import HttpCase, tagged


@tagged("post_install", "-at_install")
class Crawler(HttpCase):
    def test_01_crawl_every_themes(self):
        """Crawl every website (and so every themes) to ensure all themes can
        be rendered and do not crash.
        """
        Website = self.env["website"]
        websites_themes = Website.get_test_themes_websites()
        assert len(websites_themes) == len(
            self.env.ref("base.module_test_themes").dependencies_id
        )
        websites_themes_names = websites_themes.mapped("name")

        def test_crawling():
            for website in websites_themes.filtered(
                lambda w: w.theme_id.name != "theme_default"
            ):
                r = self.url_open("/?fw=%s&debug=assets" % website.id)
                self.assertEqual(
                    r.status_code, 200, "Ensure theme is rendering without crashing"
                )
                theme_asset_url = self.env["ir.asset"]._get_asset_bundle_url(
                    "web.assets_frontend.css", "debug", {"website_id": website.id}
                )
                self.assertTrue(theme_asset_url in r.text)
                r = self.url_open(theme_asset_url)
                self.assertTrue(
                    "/%s/static/src" % website.theme_id.name in r.text,
                    "Ensure theme is actually loaded",
                )
                for name in websites_themes_names:
                    if name != website.theme_id.name:
                        self.assertFalse(
                            "/%s/static/src" % name in r.text,
                            "Ensure other themes do not pollute current one",
                        )

        test_crawling()

        self.authenticate("admin", "admin")
        test_crawling()

    def test_02_homepage_tour_every_theme(self):
        Website = self.env["website"]
        websites_themes = Website.get_test_themes_websites()
        for website in websites_themes:
            self.env.registry.clear_cache("templates")

            self.start_tour(f"/web?fw={website.id}", "homepage", login="admin")
