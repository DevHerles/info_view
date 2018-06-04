# -*- coding: utf-8 -*-
{
    'name': "info_view",

    'summary': """
        Custom Info view""",

    'description': """
        Custom Info view
    """,

    'author': "ArandaSF",
    'website': "http://www.arandasf.com",

    'category': 'module_category_tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/info_view_assets.xml',
        'views/info_view_views.xml',
    ],
    'qweb': [
        'static/src/xml/info_view_templates.xml',
    ]
}
