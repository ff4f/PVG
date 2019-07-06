from odoo import models, fields, api, _

class accrNutritiontNotification(models.Model):
    _name="accr.nutrition.notification"
    _description = 'Nutrition Notifications'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(sting=u'Name', compute='_compute_name', )
    student = fields.Many2one('accr.nutrition.student', string=u'student', required=False, readonly=True, )
    color = fields.Integer(string=u'Color')
    message = fields.Text(string=u'Message', readonly=True, )
    notification_domain = fields.Selection(string=u'Notification Type', selection=[('leave_request', 'Leave Request'), ('residential_notes', 'Residential Notes'), ('hospital_visit', 'Hospital Visit'), ('medical_assessment', 'Medical Assessment'), ('new_student', 'New Student')], readonly=True, )
    

    @api.multi
    @api.depends('student', 'create_date')
    def _compute_name(self):
        for record in self:
            if record.student:
                record.name = record.student.display_name + ' - ' + record.notification_domain + ' - '+ record.create_date.strftime("%Y-%m-%d")