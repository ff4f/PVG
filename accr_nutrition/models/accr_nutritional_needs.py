from odoo import models, fields

class accrNutritionalNeeds(models.Model):
    _name = 'accr.nutritional.needs'

    name = fields.Char(string=u'Nutritional Needs', required=True, )