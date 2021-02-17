# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class peliculas_model(models.Model):
    _name = 'videoclub_app.peliculas_model'
    _description = 'videoclub_app.peliculas_model'
    _sql_constraints = [("sql_cons_check_nombre_pelicula","UNIQUE(name)","El titulo de la pelicula ya existe!"),]

    name = fields.Char(string="Titulo",help="Nombre de la pelicula", size=50, required=True)
    foto = fields.Binary()
    autor = fields.Char(string="Director",help="Director de la pelicula", size=50, required=True)
    fecha = fields.Date(string="Fecha Estreno", help="Añade la fecha y la hora", default=datetime.today())
    descripcion = fields.Html(string="Sinopsis",help="Descripcion de la pelicula")