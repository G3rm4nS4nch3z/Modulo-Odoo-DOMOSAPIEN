#-*- coding: utf-8 -*-
from odoo import models, fields, api
#from datetime import datetime


class CrearFlota(models.Model):
   _name = 'crear.flota'
   _inherit = ['crear.flota','mail.thread','crear.flota.set']
   usuario_encargado = fields.Many2one('res.users', 'Responsable')
   inicio_alquiler = fields.Date('InicioAlquiler')
   final_alquiler = fields.Date('FinalAlquiler')
   matricula = fields.Char(help="Matricula del vehiculo alquilado.")
   litros_gasofa = fields.Integer('Litros de gasolina')
   #total_dias = fields.Integer(string="total de dias", compute='difference_date', store=True)

   #@api.multi
   #@api.depends('inicio_alquiler','final_alquiler')
   #def difference_date(self):
      #fmt = '%Y-%m-%d'
      #inicio_alquiler = self.inicio_alquiler
      #final_alquiler = self.final_alquiler
      #d1 = datetime.strptime(inicio_alquiler, fmt)
      #d2 = datetime.strptime(final_alquiler, fmt)
      #if (d2 > d1):
         #self.total_dias = (d2 - d1).days
      #else:
         #raise Exception('la fecha de inicio no puede ser posterior a la fecha final') 

   def reset_matricula(self):
        if self.user_id != self.env.user:
            raise Exception('Solo el responsable puede cambiar la matricula')
        else:
           self.matricula = ''
        return True
   

 



