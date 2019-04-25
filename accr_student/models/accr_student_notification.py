from odoo import models, fields, _

class accrStudentNotification(models.Model):
    _name="accr.student.notification"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    student = fields.Many2one('x_student', string=u'student', )
    passport_expiration_date = fields.Date(related='student.x_studio_passport_expiration_date', string=u'Passport Expiration Date', readonly=True)
    id_expiration_date = fields.Date(related='student.x_studio_id_expiration_date', string=u'ID Expiration Date', readonly=True)
    color = fields.Integer(string=u'Color')
    message = fields.Text(string=u'Message')