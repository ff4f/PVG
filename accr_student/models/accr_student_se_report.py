from odoo import fields, models, api, _
class accrStudentSEReport(models.Model):

    _name = 'accr.student.se.report'
    _description = u'Student Special Education Report'

    name = fields.Char(string=u'Name', compute='_compute_name', )

    student = fields.Many2one('x_student', string=u'Student', required=True, )
    name = fields.Char(related='student.x_name', string=u'Name', )
    arabic_name = fields.Char(related='student.x_studio_name_ar', string=u'Arabic Name', )
    joining_date = fields.Date(related='student.x_studio_joining_date', string=u'Joining Date', )
    birth_date = fields.Date(related='student.x_studio_birthdate', string=u'Birth Date')
    diagnosis = fields.Text(related='student.x_studio_diagnosis', string=u'Diagnosis', )
    file_no = fields.Char(related='student.x_studio_file_no', string=u'File No', )
    gander = fields.Selection(related='student.x_studio_gander', string=u'Gander', )
    
    plan = fields.Many2one('x_se_long_term_plan', string=u'Plan', readonly=False, required=True, )
    plan_date = fields.Datetime(related='plan.create_date', string=u'Plan Create Date', )

    plan_categories = fields.One2many(related='plan.x_studio_categories', string=u'Plan Categories', )
    plan_response_forms = fields.One2many(related='plan.x_studio_response_forms', string=u'Plan Response Forms', )

    desc = fields.Text(string=u'Description', )




    @api.multi
    @api.depends('student', 'create_date')
    def _compute_name(self):
        for record in self:
            if record.student and record.create_date:
                record.name = record.student.display_name + ' - ' + record.create_date.strftime("%Y-%m-%d")
            elif record.diet:
                record.name = record.student.display_name

    
