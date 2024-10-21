from odoo import models, fields, api
from datetime import date

class Student(models.Model):
    _inherit = 'res.partner'

    is_student = fields.Boolean(string='Es estudiante', default=False)
    date_of_birth = fields.Date(string='Fecha de nacimiento')
    age = fields.Integer(string='Edad', compute='_compute_age', store=True)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for student in self:
            if student.date_of_birth:
                today = date.today()
                student.age = today.year - student.date_of_birth.year - (
                    (today.month, today.day) < (student.date_of_birth.month, student.date_of_birth.day)
                )
            else:
                student.age = 0
