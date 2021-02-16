# -*- coding: utf-8 -*-
from odoo import models, fields
class PersonalizacionSet(models.Model):
        _name = 'personalizacion.set'
        _description = 'personalizar set'
        name = fields.Char('Nombre', required=True)
        name_code = fields.Char('Codigo', required=True)
        cantidad = fields.Integer('Cantidad en Stock')
        is_done = fields.Boolean('Se puede vender?')
	#seleccionar = fields.selection((('hogar','hogar'), ('oficina','oficina'), ('colegios','colegios'), ('ocio','centros de ocio')),'lugar donde colocar el set')

        def do_prueba(self):
#		self.name = 'el set de prueba'
#		self.name_code = '1152077'
#		self.cantidad = 2
#		self.is_done = True
                return True
        

