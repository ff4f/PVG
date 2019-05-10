from odoo import models, fields

class accrNutritionFollowUp(models.Model):
    _name = 'accr.nutrition.followup'

    name = fields.Char(string=u'Follow Up', required=True, )

