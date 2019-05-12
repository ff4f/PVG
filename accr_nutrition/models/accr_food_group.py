from odoo import models, fields

class accrFoodGroup(models.Model):
    _name = 'accr.food.group'

    name = fields.Char(string=u'Food Group', required=True, )
    food = fields.Many2many('accr.food', 'food_group', 'accr_food_group_food_rel', 'food_id', 'food_group_id', string=u'foods', required=True, )