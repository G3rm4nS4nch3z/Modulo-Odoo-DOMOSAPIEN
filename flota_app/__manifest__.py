{
     'name': 'Manejo de Flotas',
     'version': '1.0',
     'description': 'Controla las flotas que saldran de la empresa',
     'author': 'Compañia DOMO SAPIEN',
     'depends': ['base'],
     'application': True,
     'data' : ['views/flota_app_views.xml',        
               'security/ir.model.access.csv',
              ],
}
