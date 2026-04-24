# -*- coding: utf-8 -*-
{
    'name': 'Control de Empleados',
    'version': '19.0.1.0.0',
    'summary': 'Módulo para gestionar empleados de la empresa',
    'description': """
        Control de Empleados
        ====================
        Módulo personalizado para gestionar el registro de empleados.
        Permite añadir, editar y consultar empleados con sus datos principales.
    """,
    'author': 'Mariano',
    'category': 'Human Resources',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/empleado_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
