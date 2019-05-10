from odoo import models, fields, api, _

class accrStudentOrientation(models.Model):
    _name = 'accr.student.orientation'

    name = fields.Char(string=u'Name', compute='_compute_name', )
    desc = fields.Text(string=u'Descreption', )
    individual_awareness = fields.Boolean(string=u'Individual Awareness', )
    nutrition_student = fields.Many2one('accr.nutrition.student', string=u"Student")
    student_name = fields.Char(related='nutrition_student.student_name', string='Student Name')

    @api.multi
    @api.depends('nutrition_student', 'create_date')
    def _compute_name(self):
        for record in self:
            if record.nutrition_student and record.create_date:
                record.name = record.nutrition_student.student_name + ' - ' + record.create_date.strftime("%Y-%m-%d")
            elif record.diet:
                record.name = record.nutrition_student.student_name