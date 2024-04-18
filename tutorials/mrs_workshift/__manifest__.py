{
    'name': 'MRS Workshift',
    'version': '1.0',
    'author': 'Alejandro',
    'category': 'Human Resources',
    'summary': 'Manage work shifts and teams',
    'depends': ['base', 'hr', 'resource'],  # Asegúrate de incluir todas las dependencias
    'data': [
    'views/team_resource_view.xml',
    'views/hr_employee_view.xml',
    'views/menu_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
