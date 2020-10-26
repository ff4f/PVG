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
    registry_no = fields.Char(string=u'No. civil registry', )
    gander = fields.Selection(related='student.x_studio_gander', string=u'Gander', )

    school_year = fields.Char(string='School Year')
    report_date = fields.Date(string='Report Date')

    plan = fields.Many2one('x_se_long_term_plan', string=u'Plan', readonly=False, required=True, )
    plan_date = fields.Datetime(string=u'Plan Create Date')

    def _cron_plan_date(self):
        rep = self.env['accr.student.se.report'].search([])
        for rec in rep:
            if rec.plan:
                rec.plan_date = rec.plan.create_date



#     plan_categories = fields.One2many(related='plan.x_studio_categories', string=u'Plan Categories', )
#     plan_response_forms = fields.One2many(related='plan.x_studio_response_forms', string=u'Plan Response Forms', )

    desc = fields.Text(string=u'Description', )
    
    report_categories = fields.One2many('accr.student.se.report.category', 'report', string=u'Categories', readonly=False, )




    @api.multi
    @api.depends('student', 'create_date')
    def _compute_name(self):
        for record in self:
            if record.student and record.create_date:
                record.name = record.student.display_name + ' - ' + record.create_date.strftime("%Y-%m-%d")
            elif record.diet:
                record.name = record.student.display_name

    
class accrStudentSEReportCategories(models.Model):
    _name = 'accr.student.se.report.category'
    
    name = fields.Char(string=u'Name',)
    sequence = fields.Integer(string=u'Sequence',)
    report = fields.Many2one('accr.student.se.report', string=u'Report_plan',)
    plan = fields.Many2one(related='report.plan', string=u'Plan')
    plan_categories = fields.One2many(related='plan.x_studio_categories', string=u'Plan Categories', )
    report_category = fields.Many2one('x_se_plan_categories', string=u'Categories', required=True, )
    report_l_goals = fields.One2many('accr.student.se.report.l.goal', 'report_category', string=u'Long Term Goals', )
    
class accrStudentSEReportLGoals(models.Model):
    _name = 'accr.student.se.report.l.goal'
    
    name = fields.Char(string=u'Name', )
    sequence = fields.Integer(string=u'Sequence',)
    report_category = fields.Many2one('accr.student.se.report.category', name='ReportCategory', )
    report_category_category = fields.Many2one(related='report_category.report_category', string=u'Category', )
    educational_plan = fields.Many2one('x_se_plan_long_term_goals', string='Long Term Goal', )
    short_term_goals = fields.One2many('accr.student.se.report.s.goal', 'report_l_goal', string=u'Short Term Goals', readonly=False )
    notes = fields.Text(string=u'Notes')
    
class accrStudentSEReportSGoals(models.Model):
    _name = 'accr.student.se.report.s.goal'
    
    report_l_goal = fields.Many2one('accr.student.se.report.l.goal', string='Long Term Goal', )
    sequence = fields.Integer(string=u'Sequence',)
    educational_plan = fields.Many2one(related='report_l_goal.educational_plan', string=u'Educational Plan', )
    short_term_goal = fields.Many2one('x_se_plan_short_term_goals', string=u'Short Term Goal', )
    response_forms = fields.Many2many('x_se_response_form', 'accr_student_se_report_s_goal_response_forms', 'report_s_goal_id', 'response_form_id', string=u'Resposen Forms', compute='_compute_response_forms', readonly=True, )
    
    goal_achieved =  fields.Selection([('Achieved', 'Achieved'), ('Achieved With Help', 'Achieved With Help'), ('Not Achieved', 'Not Achieved'), ], string=u'Goal Achieved ?', default='Achieved')
    notes = fields.Text(string=u'Notes')
    
    @api.multi
    @api.depends('short_term_goal')
    def _compute_response_forms(self):
        for record in self:
            if record['short_term_goal']:
                plan_response_forms = self.env['x_se_response_form'].search([('x_studio_plan_short_term_goals','=',record.short_term_goal.id)])
                for plan_response_form in plan_response_forms:
                    record.response_forms = [(4, plan_response_form.id)]