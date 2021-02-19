#-*- coding: utf-8 -*-

from odoo import models, fields

class TodoTask(models.Model):
    _inherit = 'crear.flota'
    priority = fields.Selection([('0','Low'),('1','Normal'),('2','High')],'Priority',default='1')
    kanban_state = fields.Selection([('normal', 'En camino'),('blocked', 'Bloqueado'), ('done', 'Listo para la siguiente entrega')],'Estado de Entregas',default='normal')