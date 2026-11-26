import contextlib

from odoo.exceptions import UserError
from odoo.tests import standalone

from odoo.addons.http_routing.tests.common import MockRequest


@standalone("theme_upgrade", "website_standalone")
def test_01_theme_upgrade_post_copy(env):
    """This test ensures the theme `_post_copy()` method is only called when a
    theme is installed for the first time on a website and not when the theme is
    updated on that website.
    """
    website = env["website"].search([], limit=1)
    Website = env["website"].with_context(website_id=website.id)

    Website.get_test_themes_websites().unlink()
    for w in Website.search([("theme_id", "!=", False), ("id", "!=", website.id)]):
        with contextlib.suppress(UserError):
            w.unlink()

    tfd_specific_view = Website._get_template_view(
        "website.template_footer_descriptive"
    )
    fls_specific_view = Website._get_template_view("portal.footer_language_selector")
    theme_nano_module = env.ref("base.module_theme_nano")

    def _simulate_user_manual_change():
        tfd_specific_view.active = False
        fls_specific_view.active = True

    _simulate_user_manual_change()

    with MockRequest(env, website=website):
        theme_nano_module.with_context(website_id=website.id).button_choose_theme()

    assert (
        Website._get_template_view("website.template_footer_descriptive").active is True
    ), "Theme Nano custo should be applied"
    assert (
        Website._get_template_view("portal.footer_language_selector").active is False
    ), "Theme Nano custo should be applied (2)"

    _simulate_user_manual_change()

    theme_nano_module.button_immediate_upgrade()
    env.transaction.reset()

    assert (
        Website._get_template_view("website.template_footer_descriptive").active
        is False
    ), "Theme Nano custo should NOT be applied"
    assert (
        Website._get_template_view("portal.footer_language_selector").active is True
    ), "Theme Nano custo should NOT be applied (2)"
