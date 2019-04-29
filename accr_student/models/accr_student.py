from odoo import models, fields, _

class accrStudent(models.Model):
    _inherit = ['studio_customization.x_student']

    student_notifications = fields.One2many('accr.student.notification', 'student', string=u'Notifications', )