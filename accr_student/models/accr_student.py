from odoo import models, fields, _

class accrStudent(models.Model):
    _inherit = ['x_student']

    student_notifications = fields.One2many('accr.student.notification', 'student', string=u'Notifications', )


class LongPlan(models.Model):
    _inherit = ['x_se_long_term_plan']

    write_date = fields.Datetime("Last Updated On", readonly=False)
