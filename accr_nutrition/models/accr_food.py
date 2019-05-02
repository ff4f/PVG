from odoo import models, fields

class accrFood(models.Model):
    _name = 'accr.food'

    name = fields.Char(string=u'Food', required=True, )
    food_group = fields.Many2one('accr.food.group', string=u'Food Group', required=True, )
    food_type = fields.Many2one('accr.food.type', string=u'Food Type', required=True, )
    meal_type = fields.Many2one('accr.meal.type', string=u"Meal Type", required=True, )