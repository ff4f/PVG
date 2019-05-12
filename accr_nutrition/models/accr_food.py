from odoo import models, fields

class accrFood(models.Model):
    _name = 'accr.food'

    name = fields.Char(string=u'Food', required=True, )
    food_group = fields.Many2one('accr.food.group', string=u'Food Group', required=False, )
    food_ingredients = fields.Many2one('accr.food.ingredients', string=u'Food Ingredients', required=False, )
    meal_type = fields.Many2one('accr.meal.type', string=u"Meal Type", required=False, )

    measure = fields.Integer(string=u'Measure', )
    uom = fields.Many2one('uom.uom', string=u'Unit of Measure', )
    calories = fields.Integer(string=u'Calories', )