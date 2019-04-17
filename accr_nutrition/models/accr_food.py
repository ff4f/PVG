from odoo import models, fields

class accrFood(models.Model):
    _name = 'accr.food'

    name = fields.Char(string=u'Food')
    food_group = fields.Many2one('accr.food.group', string=u'Food Group')