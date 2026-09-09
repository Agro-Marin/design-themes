{
    'name': 'Custom Theme (Testing suite)',
    # Remove the `/Hidden` part to make it selectable for tests purpose
    'category': 'Hidden/Tests',
    'depends': ['website'],
    'data': [
        'data/images.xml',
        'data/ir_asset.xml',
        'data/menu.xml',
        'data/pages.xml',
        'data/shapes.xml',
        'views/footer.xml',
        'views/header.xml',
    ],
    'assets': {
        'web.assets_tests': [
            'theme_test_custo/static/tests/tours/**/*',
        ],
        'html_builder.assets': [
            'theme_test_custo/static/src/builder/**/*',
        ],
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
}
