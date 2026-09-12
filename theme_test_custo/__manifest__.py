{
    "name": "Custom Theme (Testing suite)",
    "category": "Hidden/Tests",
    "author": "Odoo S.A.",
    "license": "LGPL-3",
    "depends": [
        "website",
    ],
    "data": [
        "data/images.xml",
        "data/ir_asset.xml",
        "data/menu.xml",
        "data/pages.xml",
        "data/shapes.xml",
        "views/footer.xml",
        "views/header.xml",
    ],
    "assets": {
        "web.assets_tests": [
            "theme_test_custo/static/tests/tours/**/*",
        ],
        "html_builder.assets": [
            "theme_test_custo/static/src/builder/**/*",
        ],
    },
}
