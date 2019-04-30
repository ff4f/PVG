from odoo import models, fields

class accrStudent(models.Model):
    _inherit = ['x_student']
    _name = 'accr.student'

    student_notifications = fields.One2many('accr.medical.unit.medication', 'student', string=u'Medicines', )