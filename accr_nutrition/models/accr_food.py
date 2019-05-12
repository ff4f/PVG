from odoo import models, fields

class accrFood(models.Model):
    _name = 'accr.food'

    name = fields.Char(string=u'Food', required=True, )
    food_group = fields.Many2many('accr.food.group', 'accr_food_group_food_rel', 'food_group_id', 'food_id', string=u'Food Group', )
    food_ingredients = fields.Many2many('accr.food.ingredients', 'accr_food_ingredients_food_rel', 'food_ingredients_id', 'food_id', string=u'Food Ingredients', )
    meal_type = fields.Many2many('accr.meal.type', 'accr_meal_type_food_rel', 'meal_type_id', 'food_id', string=u"Meal Type", )

    measure = fields.Integer(string=u'Measure', )
    uom = fields.Many2one('uom.uom', string=u'Unit of Measure', )
    calories = fields.Integer(string=u'Calories', )