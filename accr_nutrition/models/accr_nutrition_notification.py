from odoo import models, fields, _

class accrNutritiontNotification(models.Model):
    _name="accr.nutrition.notification"
    _description = 'Nutrition Notifications'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    student = fields.Many2one('accr.nutrition.student', string=u'student', required=True, readonly=True, )
    color = fields.Integer(string=u'Color')
    message = fields.Text(string=u'Message', readonly=True, )
    notification_domain = fields.Selection(string=u'field_name', selection=[('leave_request', 'Leave Request'), ('hospital_visit', 'Hospital Visit'), ('medical_assessment', 'Medical Assessment')], )
    