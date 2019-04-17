from odoo import models, fields

class accrDiet(models.Model):
    _name = 'accr.diet'

    name = fields.Char(string=u'Diet')