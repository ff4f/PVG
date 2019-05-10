from odoo import models, fields, _

class accrNutritiontNotification(models.Model):
    _name="accr.nutrition.student.notification"
    _description = 'Student Nutrition Notification'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    student = fields.Many2one('accr.nutrition.student', string=u'student', )
    color = fields.Integer(string=u'Color')
    message = fields.Text(string=u'Message')