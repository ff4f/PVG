from odoo import models, fields

class accrDiet(models.Model):
    _name = 'accr.Diet'

    name = fields.Char(string=u'Diet')