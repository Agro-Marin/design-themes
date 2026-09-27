{
    "name": "Website Theme Customization Tests",
    "category": "Hidden/Tests",
    "summary": "Test website theme customization with sample pages, menus and shapes",
    "description": "Install a test theme with sample pages, menu hierarchies, header and footer templates, and editor shape options. Its tests exercise theme creation and menu customization.",
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
