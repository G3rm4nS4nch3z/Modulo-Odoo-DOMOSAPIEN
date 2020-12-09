# -*- coding: utf-8 -*- 
from odoo import models, fields, api 
class CrearFlota(models.Model):
     _name = 'crear.flota'
     _description = 'Creación de Flotas'
     
     matricula = fields.Char('Matricula Furgoneta', required=True)
     conductor = fields.Char('Conductor', required=True)
     acompaniante = fields.Char('Acompañante', required=True)
     set = fields.Integer('Número del Set', required=True)
     cantidad = fields.Integer('Cantidad de Sets', required=True)
     ruta = fields.Char('Ruta', required=True)
     def reset_matricula(self):
        self.matricula = '' 
        return True
     
