from odoo import models, fields

class accrStudent(models.Model):
    _inherit = ['184']

    student_notifications = fields.One2many('accr.medical.unit.medication', 'student', string=u'Medicines', )