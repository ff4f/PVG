from odoo import models, fields

class accrVIT(models.Model):
    _name = 'accr.nutrition.vit'

    name = fields.Char(string=u"VIT", required=True)