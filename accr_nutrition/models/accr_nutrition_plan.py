from odoo import models, fields, api, _

class accrNutritionPlan(models.Model):
    _name = 'accr.nutrition.plan'

    name = fields.Char(string=u'Nutrition Plan', required=True, compute="_compute_name", )
    nutrition_student = fields.Many2one('accr.nutrition.student', string=u"Student", copy=True, )
    plan_desc = fields.Text(string=u'Plan Description', copy=True, )
    improvement = fields.Text(string=u'Improvement', copy=True, )
    Recomendations = fields.Text(string=u'Recomendations', copy=True, )
    date = fields.Date(string=u"Date", required=True, )


    @api.multi
    @api.depends('nutrition_student', 'create_date')
    def _compute_name(self):
        for record in self:
            if record.nutrition_student and record.create_date:
                record.name = record.nutrition_student.student_name + ' - ' + record.create_date.strftime("%Y-%m-%d")
            elif record.nutrition_student:
                record.name = record.nutrition_student.student_name