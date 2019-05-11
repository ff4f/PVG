from odoo import fields, models, api
class accrStudentSEReport(models.Model):

    _name = 'accr.student.se.report'
    _description = u'Student Special Education Report'

    name = fields.Char(string=u'Name', compute='_compute_name', )

    sudent = fields.Many2one('x_student', string=u'Student', )
    name = fields.Char(related='student.x_name', string=u'Name', )
    arabic_name = fields.Char(related='student.x_studio_name_ar', string=u'Arabic Name', )
    joining_date = fields.Date(related='student.x_studio_joining_date', string=u'Joining Date', )
    birth_date = fields.Date(related='student.x_studio_birth_date', string=u'Birth Date')
    diagnosis = fields.Text(related='student.x_studio_diagnosis', string=u'Diagnosis', )
    file_no = fields.Char(related='student.x_studio_file_no', string=u'File No', )
    gander = fields.Selection(related='student.x_studio_gander', string=u'Gander', )
    plans = fields.One2many(related='student.x_studio_se_long_term_plan', string=u'Plans', )
    
    last_plan = fields.Many2one('x_se_long_term_plan', string=u'Last Plan', compute='_compute_plan', readonly=True, required=True, )




    @api.multi
    @api.depends('sudent', 'create_date')
    def _compute_name(self):
        for record in self:
            if record.student and record.create_date:
                record.name = record.student.display_name + ' - ' + record.create_date.strftime("%Y-%m-%d")
            elif record.diet:
                record.name = record.student.display_name

    @api.multi
    @api.depends('sudent', 'create_date')
    def _compute_plan(self):
        _last_plan = self.env['x_se_long_term_plan'].search([('x_studio_student','=',self.env['x_student'].id)], order='id desc', limit=1)[1]
        self.last_plan = _last_plan

    
