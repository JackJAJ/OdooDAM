# -*- coding: utf-8 -*-
{
    'name': "ProyectoDAM",
    'summary': """
        lolShort (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "Denis Ivan Jack",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'application': True,
    'installable': True,
    'auto_install': False,
    'external_dependencies': {
        'python': ['jsonrpc'],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
