{
    "name": "Paptic Theme",
    "version": "2.1.0",
    "category": "Theme/Corporate",
    "sequence": 110,
    "summary": "Consultancy, Design, Tech, Computers, IT, Blogs",
    "description": "Clean and sharp design.",
    "author": "Odoo S.A.",
    "images": [
        "static/description/paptic_poster.webp",
        "static/description/paptic_screenshot.webp",
    ],
    "license": "LGPL-3",
    "depends": [
        "website",
    ],
    "data": [
        "data/generate_primary_template.xml",
        "data/ir_asset.xml",
        "views/images.xml",
        "views/customizations.xml",
        "views/new_page_template.xml",
    ],
    "assets": {
        "website.assets_editor": [
            "theme_paptic/static/src/js/tour.js",
        ],
    },
    "configurator_snippets": {
        "homepage": [
            "s_cover",
            "s_references",
            "s_image_text",
            "s_text_image",
            "s_masonry_block_images_template",
            "s_faq_list",
            "s_cta_box",
        ],
    },
    "configurator_snippets_addons": {
        "website_sale": {
            "homepage": [
                (
                    "website_sale.s_dynamic_snippet_category_list",
                    "after",
                    "s_image_text",
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
            "template_key": "website_sale.dynamic_filter_template_product_public_category_default",
            "data_attributes": {
                "rounded": "3",
                "gap": "3",
                "size": "small",
                "alignment": "left",
            },
            "remove_classes": [
                "s_dynamic_category_clickable_items",
            ],
        },
    },
}
