from odoo import models, fields, api, _

class accrDietPlan(models.Model):
    _name = 'accr.diet.plan'

    name = fields.Char(string=u'DietPlan', required=True, compute="_compute_name", )
    diet = fields.Many2one('accr.diet', string=u'Diet', )
    meal_types = fields.Many2many('accr.meal.type', 'accr_diet_plan_meal_type_rel', 'diet_plan_id', 'meal_type_id', string=u"Meal Types", )
    food = fields.Many2many('accr.food', 'accr_diet_plan_food_rel', 'diet_plan_id', 'food_id', string=u"Food", )
    students = fields.One2many(related='diet.students', string=u"Students", )

    @api.multi
    @api.depends('diet', 'create_date')
    def _compute_name(self):
        for record in self:
            if record.diet and record.create_date:
                record.name = record.diet.display_name + ' - ' + record.create_date.strftime("%Y-%m-%d")
            elif record.diet:
                record.name = record.diet.display_name