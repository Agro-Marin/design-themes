from odoo.fields import Domain

from . import models


def post_init_hook(env):
    """Create a new website for each theme and install the theme on it."""
    IrModule = env["ir.module.module"]
    # The themes this module lists, not every theme on the addons path: a
    # theme from another repository (agromarin ships two) is not this
    # module's to install, and asserting it away made the module
    # uninstallable on any tree that carries one.
    names = env.ref("base.module_test_themes").dependencies_id.mapped("name")
    themes = IrModule.search(
        Domain(IrModule.get_domain_themes()) & Domain("name", "in", names),
        order="name",
    )
    assert len(themes) == len(names), "a listed theme is not a theme module"

    xmlids = []
    for theme in themes:
        website = env["website"].create(
            {
                "name": theme.display_name,
                "theme_id": theme.id,
            }
        )
        xmlids.append(
            {
                "xml_id": "test_themes.%s" % theme.display_name.replace(" ", "_"),
                "record": website,
                "noupdate": True,  # Avoid unlink on -u
            }
        )
        theme.with_context(apply_new_theme=True)._theme_get_stream_themes()._theme_load(
            website
        )
    env["ir.model.data"]._update_xmlids(xmlids)
