from odoo import models, fields, api

class accrResidentialNMNotification(models.Model):
    _name = "accr.residential.nm.notification"
    _description = "Resdintial Notifications for Medical and Nutrition"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string=u'Subject', required=True, )
    date_time = fields.Datetime(string=u'Date & Time', default=fields.Datetime.now, required=True, )
    notes = fields.Text(string=u'Notes', required=True, ) 
    
    section = fields.Many2one(string=u'Section', comodel_name='x_student_residential_sections', ondelete='set null', required=True, )
    students = fields.Many2many(string=u'Students', comodel_name='x_student', relation='student_residential_nm_notification_rel', column1='student_id', column2='residential_nm_notification_id',)
    color = fields.Integer(string=u'Color')
    
    