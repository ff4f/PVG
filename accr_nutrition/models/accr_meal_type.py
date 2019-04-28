from odoo import models, fields

class accrMealType(models.Model):
    _name = 'accr.meal.type'

    name = fields.Char(string=u'Meal Type', required=True, )
    food = fields.One2many('accr.food', 'meal_type', string=u'foods', required=True, )