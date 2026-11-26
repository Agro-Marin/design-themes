from unittest.mock import patch

from odoo.tests import standalone

from odoo.addons.http_routing.tests.common import MockRequest


@standalone("website_standalone")
def test_01_theme_install_generate_primary_templates(env):
    """This test ensures the theme `_create_primary_snippet_templates()`
    method is correctly called before xml views are generated.
    """
    theme_buzzy = env.ref("base.module_theme_clean")

    if theme_buzzy.state == "installed":
        theme_buzzy.button_immediate_uninstall()
    env["ir.ui.view"].with_context(_force_unlink=True).search(
        [("key", "=", "website.configurator_s_banner")]
    ).unlink()
    env["ir.ui.view"].with_context(_force_unlink=True).search(
        [("key", "=", "website.configurator_s_cover")]
    ).unlink()
    theme_buzzy.button_immediate_install()


@standalone("website_standalone")
def test_02_theme_default_generate_primary_templates(env):

    def fake_website_api(self, path, payload):
        assert path.startswith("/api/website/2/configurator/custom_resources")
        return {"images": {}}

    def fake_olg_api(self, path, payload):
        assert path == "/api/olg/1/generate_placeholder"
        placeholders = payload.get("placeholders", [])
        return {key: key for key in placeholders}

    theme_default = env.ref("base.module_theme_default")
    website_module = env.ref("base.module_website")

    if theme_default.state == "installed":
        theme_default.button_immediate_uninstall()
    env["ir.ui.view"].with_context(_force_unlink=True).search(
        [("key", "like", "website.configurator_")]
    ).unlink()

    with (
        patch(
            "odoo.addons.website.models.website_configurator.Website._website_api_rpc",
            autospec=True,
            side_effect=fake_website_api,
        ),
        patch(
            "odoo.addons.website.models.website_configurator.Website._OLG_api_rpc",
            autospec=True,
            side_effect=fake_olg_api,
        ),
    ):
        if website_module.state == "installed":
            website_module.button_immediate_upgrade()
        else:
            website_module.button_immediate_install()

        template_keys = (
            env["ir.ui.view"]
            .search([("key", "like", "website.configurator")])
            .mapped("key")
        )
        manifest = env["ir.module.module"].get_module_info("theme_default")
        snippets_per_page = manifest.get("configurator_snippets")
        for page in snippets_per_page:
            for snippet in snippets_per_page[page]:
                template_key = f"website.configurator_{page}_{snippet}"
                assert template_key in template_keys, f"{template_key} should exist"

        website = env["website"].search([], limit=1)
        website.check_singleton()
        with MockRequest(env, website=website):
            website.configurator_apply(
                selected_features=[1, 2, 3, 4],
                industry_id=2836,
                industry_name="private university",
                selected_palette="default-15",
                theme_name="theme_bewise",
                website_purpose="get_leads",
                website_type="business",
            )
