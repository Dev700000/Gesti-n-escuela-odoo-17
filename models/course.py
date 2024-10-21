from odoo import models, fields

class Course(models.Model):
    _inherit = 'product.template'

    is_course = fields.Boolean(string='Es curso', default=True)
    teacher_ids = fields.Many2many('res.partner', string='Profesores', domain=[('is_teacher', '=', True)])
    subject_ids = fields.Many2many('course.subject', string='Materias')
    duration = fields.Float(string='Duración (horas)')
    date_start = fields.Date(string='Fecha de inicio')
    max_students = fields.Integer(string='Capacidad máxima de alumnos')
