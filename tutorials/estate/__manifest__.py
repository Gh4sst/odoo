{
    'name': 'estate',
    'version': '1.0',
    'summary': 'Breve descripción del módulo',
    'author': 'Tu nombre',
    'license': 'AGPL-3',
    'website': 'https://www.ejemplo.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}