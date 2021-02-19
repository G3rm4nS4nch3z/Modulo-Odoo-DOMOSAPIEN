#-*- coding: utf-8 -*-
from odoo import models, fields, api
class PersonalizacionSet(models.Model):
  _name = 'personalizacion.set'
  _inherit = ['personalizacion.set','mail.thread']
  user_id = fields.Many2one('res.users', 'Responsable')
  date_deadline = fields.Date('Fecha Creación')
  name = fields.Char(help="Breve descripcion de latarea.")
