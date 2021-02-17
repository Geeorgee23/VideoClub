# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class alquiler_model(models.Model):
    _name = 'videoclub_app.alquiler_model'
    _description = 'videoclub_app.alquiler_model'

    cliente = fields.Many2one("videoclub_app.clientes_model", string="Cliente",required=True)
    empleado = fields.Many2one("videoclub_app.empleados_model", string="Empleado", required=True)
    pelicula = fields.Many2many("videoclub_app.peliculas_model", string="Lista peliculas",required=True)
    fechaAlq = fields.Date(string="Fecha de Alquiler",help="Añade la fecha de alquiler del socio",readonly=True,default=lambda self: datetime.today())

    entregada = fields.Boolean(string="Entregada", default=False)

    base = fields.Float(string="Base")
    iva = fields.Char(string="IVA", default="21%",readonly=True)
    total = fields.Float(string="Total", compute='_calc_total', store=True)
    
    descuento = fields.Selection(string="Descuento", selection=[('0','0%'),('5', '5%'),('10', '10%'),('15', '15%')], default='0')
    

    @api.depends('base','descuento')
    def _calc_total(self):
        self.ensure_one()
        #base+iva-descuento
        self.total = self.base + (float(self.base*21/100) - ((self.base*float(self.descuento))/100))

    def peliculaEntregada(self):
        self.ensure_one()
        self.entregada = not self.entregada
        return True