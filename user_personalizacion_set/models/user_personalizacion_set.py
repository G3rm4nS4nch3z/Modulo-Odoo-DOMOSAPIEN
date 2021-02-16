#-*- coding: utf-8 -*-
from odoo import models, fields, api
class PersonalizacionSet(models.Model):
  _name = 'personalizacion.set'
  _inherit = ['personalizacion.set','mail.thread']
  user_id = fields.Many2one('res.user', 'Responsable')
  date_deadline = fields.Date('Fecha Creación')
  name = fields.Char(help="Breve descripcion de latarea.")
  componente_ids = fields.One2many('personalizacion.set.componente','componente_id')
    

class DevComponente(models.Model):
  _name = 'personalizacion.set.componente'
  name_componente = fields.Char('Componente', required=True)
  cantidad = fields.Integer('Cantidad')
  componente_id = fields.Many2one('personalizacion.set', 'Request', ondelete='cascade')



  

