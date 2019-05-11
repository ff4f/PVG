from odoo import models, fields, api, _

class accrNutritiontNotification(models.Model):
    _name="accr.nutrition.notification"
    _description = 'Nutrition Notifications'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(sting=u'Name', )
    student = fields.Many2one('accr.nutrition.student', string=u'student', required=True, readonly=True, )
    color = fields.Integer(string=u'Color')
    message = fields.Text(string=u'Message', readonly=True, )
    notification_domain = fields.Selection(string=u'Notification Type', selection=[('leave_request', 'Leave Request'), ('hospital_visit', 'Hospital Visit'), ('medical_assessment', 'Medical Assessment')], readonly=True, )
    

    @api.multi
    @api.depends('student', 'create_date')
    def _compute_name(self):
        for record in self:
            if record.student:
                record.name = record.student.display_name + ' - ' + record.create_date.strftime("%Y-%m-%d")