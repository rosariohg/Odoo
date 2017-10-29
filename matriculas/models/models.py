# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class matriculas(models.Model):
#     _name = 'matriculas.matriculas'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Alumno(models.Model):
    _name = 'matriculas.alumno'

    name = fields.Char(string="Nombre y Apellidos")
    direccion = fields.Char(string="Direccion")
    telefono = fields.Integer(string="Telefono")
    dni = fields.Integer(string="DNI")

class Area(models.Model):
    _name = 'matriculas.area'

    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripción")