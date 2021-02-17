# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from time import time

class venta_model(models.Model):
    _name = 'videoclub_app.venta_model'
    _description = 'videoclub_app.venta_model'
    _sql_constraints = [('venta_name_uniq','UNIQUE (name)','No puede haber dos facturas con el mismo identificador'),]

    name = fields.Char(string="Referencia", required=True, index=True,readonly=True, default=str(int(time())))
    fecha = fields.Datetime(string="Fecha Venta", required=True, default=lambda self: datetime.today())

    cliente = fields.Many2one("videoclub_app.clientes_model", string="Cliente")
    empleado = fields.Many2one("videoclub_app.empleados_model", string="Empleado")
    pelicula = fields.Many2many("videoclub_app.peliculas_model", string="Pelicula")


    base = fields.Float(string="Base")
    iva = fields.Char(string="IVA", default="21%",readonly=True)
    total = fields.Float(string="Total", compute="_calc_iva", store=True)
    

    @api.depends('base')
    def _calc_iva(self):
        self.ensure_one()
        self.total = (float(self.base*21/100)+self.base)