from odoo import models, fields

class accrNutritionRequirements(models.Model):
    _name = 'accr.nutrition.requirements'

    name = fields.Char(string=u'Requirements', required=True, )