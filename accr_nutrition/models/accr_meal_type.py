from odoo import models, fields

class accrMealType(models.Model):
    _name = 'accr.meal.type'

    name = fields.Char(string=u'Meal Type', required=True, )
    food = fields.Many2many('accr.food', 'accr_meal_type_food_rel', 'food_id', 'meal_type_id', string=u'foods', required=True, )