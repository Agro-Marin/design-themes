{
    "name": "Graphene Theme",
    "version": "2.0.0",
    "category": "Theme/Corporate",
    "sequence": 110,
    "summary": "Service, Corporate, Design, Technology, Robotics, Computers, IT, Blogs",
    "description": "Light colours, thin text, clean and sharp design.",
    "author": "Odoo S.A.",
    "images": [
        "static/description/graphene_poster.webp",
        "static/description/graphene_screenshot.webp",
    ],
    "images_preview_theme": {
        "website.s_cover_default_image": "/theme_graphene/static/src/img/pictures/bg_image_08.webp",
    },
    "license": "LGPL-3",
    "depends": [
        "theme_common",
    ],
    "data": [
        "data/generate_primary_template.xml",
        "data/ir_asset.xml",
        "views/images_library.xml",
        "views/customizations.xml",
        "views/new_page_template.xml",
    ],
    "assets": {
        "website.assets_editor": [
            "theme_graphene/static/src/js/tour.js",
        ],
    },
    "configurator_snippets": {
        "homepage": [
            "s_cover",
            "s_text_image",
            "s_numbers_grid",
            "s_mockup_image",
            "s_comparisons",
            "s_references",
        ],
    },
    "configurator_snippets_addons": {
        "website_sale": {
            "homepage": [
                (
                    "website_sale.s_dynamic_snippet_category_list",
                    "after",
                    "s_mockup_image",
                ),
            ],
        },
    },
    "new_page_templates": {
        "about": {
            "personal": [
                "s_text_cover",
                "s_image_text",
                "s_text_block_h2",
                "s_numbers",
                "s_features",
                "s_call_to_action",
            ],
        },
    },
    "theme_customizations": {
        "website_sale.s_dynamic_snippet_category_list": {
            "data_attributes": {
                "alignment": "left",
            },
            "template_key": "website_sale.dynamic_filter_template_product_public_category_default",
            "background": {
                "color": "o_cc2",
            },
            "add_classes": [
                "pt96",
                "pb96",
                {
                    "s_dynamic_snippet_title": "d-none",
                },
            ],
            "remove_classes": [
                "s_dynamic_category_clickable_items",
                "pt64",
                "pb64",
            ],
        },
    },
}
