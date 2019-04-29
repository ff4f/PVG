from odoo import models, fields

class accrFoodGroup(models.Model):
    _name = 'accr.food.group'

    name = fields.Char(string=u'Food Group', required=True, )
    food = fields.One2many('accr.food', 'food_group', string=u'foods', required=True, )