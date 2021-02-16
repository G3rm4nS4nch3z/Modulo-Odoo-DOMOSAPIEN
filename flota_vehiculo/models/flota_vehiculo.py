#-*- coding: utf-8 -*-

from odoo import models, fields, api

class CrearFlota(models.Model):
   _name = 'crear.flota'
   _inherit = ['crear.flota','mail.thread','crear.flota.set']
   usuario_encargado = fields.Many2one('res.users', 'Responsable')
   inicio_alquiler = fields.Date('InicioAlquiler')
   final_alquiler = fields.Date('FinalAlquiler')
   matricula = fields.Char(help="Matricula del vehiculo alquilado.")
   

   def reset_matricula(self):
        if self.user_id != self.env.user:
            raise Exception('Solo el responsable puede cambiar la matricula')
        else:
           self.matricula = ''
        return True

 



