from odoo import models, fields

class accrFood(models.Model):
    _name = 'accr.food'

    name = fields.Char(string=u'Food', required=True, )
    food_group = fields.Many2one('accr.food.group', string=u'Food Group', required=False, )
    food_type = fields.Many2one('accr.food.type', string=u'Food Type', required=False, )
    meal_type = fields.Many2one('accr.meal.type', string=u"Meal Type", required=False, )

    uom = fields.Many2one('uom.uom', string=u'Unit of Measure', )
    calories = fields.Integer(string=u'Calories', )
    category_id = fields.Integer(related='uom.category_id.id')