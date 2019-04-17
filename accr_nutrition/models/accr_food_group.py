from odoo import models, fields

class accrFoodGroup(models.Model):
    _name = 'accr.food.group'

    name = fields.Char(string=u'Food Group')
    foods = fields.One2many('accr.food', 'food_group', string=u'foods')