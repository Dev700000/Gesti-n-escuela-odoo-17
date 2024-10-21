from odoo import models, fields

class Teacher(models.Model):
    _inherit = 'res.partner'

    is_teacher = fields.Boolean(string='Es profesor', default=False)
    subject_ids = fields.Many2many('course.subject', string='Materias impartidas')
