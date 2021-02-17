# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError
import re


class empleados_model(models.Model):
    _name = 'videoclub_app.empleados_model'
    _description = 'videoclub_app.empleados_model'
    _sql_constraints = [("sql_cons_check_dni_empleados","UNIQUE(dni)","El dni del cliente ya existe!"),]

    foto=fields.Binary()
    name = fields.Char(string="Nombre", help="Añade el nombre del socio",required=True)
    apellidos = fields.Char(string="Apellidos", help="Añade los apellidos del socio",required=True)
    dni = fields.Char(string="DNI", help="Añade el dni del socio",required=True, index=True, size=9)
    telf= fields.Char(string="Telefono", help="Añade el telefono del socio", required=True, size=9)
    email = fields.Char(string="email",help="Añade el email del socio")

    
    #sueldo

    encargado = fields.Many2one("videoclub_app.encargados_model", string="Encargado",required=True)


    
    @api.constrains("dni")
    def _validarDni(self):
        letras="TRWAGMYFDPXBNJZSQVHLCKE"

        letra =self.dni[-1]
        num=int(self.dni[:-1])
        if letras[num%23]!=letra:
            raise ValidationError ("DNI Invalido!")


    @api.constrains("telf")
    def _validarTelefono(self):
        if len(self.telf)!=9:
            raise ValidationError ("Telefono Invalido!")


    @api.constrains("email")
    def is_valid_email(self):
        expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        if re.match(expresion_regular, self.email) is None:
            raise ValidationError ("Email Invalido!")