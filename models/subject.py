from odoo import models, fields

class CourseSubject(models.Model):
    _name = 'course.subject'
    _description = 'Materias del Curso'

    name = fields.Char(string='Nombre de la materia', required=True)
    description = fields.Text(string='Descripción')
    credits = fields.Integer(string='Créditos')
