from odoo import models, fields

class StudentEnrollment(models.Model):
    _name = 'student.enrollment'
    _description = 'Gestión de Inscripciones'

    student_id = fields.Many2one('res.partner', string='Alumno', domain=[('is_student', '=', True)])
    course_id = fields.Many2one('product.template', string='Curso')
    date_enrollment = fields.Date(string='Fecha de inscripción', default=fields.Date.today)
    state = fields.Selection([
        ('pending', 'Pendiente'),
        ('confirmed', 'Confirmada'),
        ('cancelled', 'Cancelada')
    ], string='Estado', default='pending')
