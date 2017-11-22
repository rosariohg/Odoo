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
    matriculas_ids = fields.One2many('matriculas.matricula','alumno_id',string='Matriculas del alumno')

class Area(models.Model):
    _name = 'matriculas.area'

    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripción")

class Matricula(models.Model):
    _name = 'matriculas.matricula'

    name = fields.Char()
    anio = fields.Char(string='Anio')
    periodo = fields.Char(string='Periodo')
    nivel = fields.Char(string='Nivel')
    fecha_matricula = fields.Date(string='Fechas de matrícula')
    curso_id = fields.Many2one('matriculas.curso',string='Curso')
    alumno_id = fields.Many2one('matriculas.alumno',string='Alumno')

class Curso(models.Model):
    _name = 'matriculas.curso'

    name = fields.Char(string='Nombre')
    creditos = fields.Char(string='Creditos')
    area_id = fields.Many2one('matriculas.area',string='Area')    
        