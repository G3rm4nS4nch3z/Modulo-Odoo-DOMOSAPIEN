# -*- coding: utf-8 -*- 
from odoo import models, fields, api 
class CrearFlota(models.Model):
     _name = 'crear.flota'
     _description = 'Creación de Flotas'
     matricula = fields.Char('Matricula Furgoneta', required=True)
     conductor = fields.Char('Conductor', required=True)
     acompaniante = fields.Char('Acompañante', required=True)
     ruta = fields.Char('Ruta', required=True)
     set_ids = fields.One2many('crear.flota.set','set_id')

     def reset_matricula(self):
        self.matricula = '' 
        return True


class DevSet(models.Model):
   _name = 'crear.flota.set'
   set = fields.Many2one('personalizacion.set', required=True)
   cantidad = fields.Integer('Cantidad del Set', required=True)
   set_id = fields.Many2one('crear.flota', 'Sets', ondelete='cascade')
     
