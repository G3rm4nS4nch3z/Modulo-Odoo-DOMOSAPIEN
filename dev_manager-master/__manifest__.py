# -*- encoding: utf-8 -*-
{
    'name': 'Developments Manager',
    'version': '1.0',
    'author': 'EEP - Profesor',
    'description': """ Modulo gestion de solicitudes de desarrollo.""",
    'depends': ['base'],
    'application': True,
    'data' : ['views/devman_views.xml',
              'security/ir.model.access.csv',],
}
