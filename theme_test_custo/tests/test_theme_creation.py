from odoo.tests import HttpCase, tagged


@tagged("post_install", "-at_install", "test_themes")
class Crawler(HttpCase):
    def test_01_menu_hierarchies(self):
        theme_custo = self.env.ref("base.module_theme_test_custo")
        website = self.env["website"].browse(1)
        website.theme_id = theme_custo.id
        theme_custo.with_context(load_all_views=True, apply_new_theme=True)._theme_load(
            website
        )
        self.start_tour("/@/example", "theme_menu_hierarchies", login="admin")
